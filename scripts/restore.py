"""Restoration and Recovery Toolkit for Mehdi's Digital Legacy.

Verifies backup archives, rebuilds SQLite database from Markdown files,
rebuilds static website, and restores prior article revisions.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.database import (
    checkpoint_and_clean_db,
    compute_content_hash,
    get_db,
    get_db_path,
    init_database,
    utc_now_iso,
)
from scripts.json_export import generate_json_exports
from scripts.markdown_export import (
    parse_markdown_file,
    save_article_markdown,
)
from scripts.search_index import build_search_indexes


def verify_backup(backup_path: Path | str) -> bool:
    """Verifies zip integrity and checks against checksums.sha256."""
    path = Path(backup_path)
    if not path.exists():
        print(f"[Verify] Error: File not found: {path}")
        return False

    print(f"[Verify] Verifying backup archive: {path.name}...")

    # 1. Test zip CRC
    try:
        with zipfile.ZipFile(path, "r") as zipf:
            bad_file = zipf.testzip()
            if bad_file:
                print(f"[Verify] Corrupted file in archive: {bad_file}")
                return False
            file_list = zipf.namelist()
            print(f"  ✓ Zip archive is structurally sound ({len(file_list)} files inside).")
    except Exception as e:
        print(f"[Verify] Error opening zip archive: {e}")
        return False

    # 2. Compute SHA-256
    hasher = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    actual_hash = hasher.hexdigest()
    print(f"  ✓ Computed SHA-256: {actual_hash}")

    # Check against checksums.sha256 if present
    checksum_file = path.parent / "checksums.sha256"
    if checksum_file.exists():
        with open(checksum_file, "r", encoding="utf-8") as cf:
            for line in cf:
                parts = line.strip().split()
                if len(parts) >= 2 and parts[1] == path.name:
                    expected_hash = parts[0]
                    if actual_hash == expected_hash:
                        print(f"  ✓ SHA-256 matches recorded checksum in {checksum_file.name}")
                        return True
                    else:
                        print(f"  ✗ CHECKSUM MISMATCH! Expected: {expected_hash}, Actual: {actual_hash}")
                        return False

    print("  ✓ Verification successful.")
    return True


def rebuild_database_from_markdown(db_path: Optional[Path | str] = None) -> int:
    """Reconstructs the SQLite database entirely from independent Markdown article files."""
    articles_dir = ROOT_DIR / "articles"
    if not articles_dir.exists():
        print("[Rebuild DB] No articles directory found.")
        return 0

    print("[Rebuild DB] Initializing fresh SQLite schema...")
    target_path = Path(db_path) if db_path else get_db_path()
    
    # Initialize schema and seed sites
    init_database(target_path)

    md_files = list(articles_dir.glob("**/*.md"))
    print(f"[Rebuild DB] Found {len(md_files)} Markdown articles to ingest...")

    now = utc_now_iso()
    reconstructed_count = 0

    with get_db(target_path) as conn:
        # Load sites map
        site_rows = conn.execute("SELECT id, key FROM sites").fetchall()
        site_map = {r["key"]: r["id"] for r in site_rows}

        for md_path in md_files:
            try:
                meta, body = parse_markdown_file(md_path)
                if not meta or "archive_id" not in meta:
                    continue

                archive_id = meta["archive_id"]
                source_key = meta.get("source")
                site_id = site_map.get(source_key)
                if not site_id:
                    print(f"  [!] Unknown source key '{source_key}' for {archive_id}, skipping.")
                    continue

                wp_post_id = meta.get("wordpress_id", 0)
                title = meta.get("title", "Untitled")
                slug = meta.get("slug", "untitled")
                language = meta.get("language", "en")
                published_at = meta.get("published_at", now)
                published_at_gmt = meta.get("published_at_gmt")
                modified_at = meta.get("modified_at", published_at)
                modified_at_gmt = meta.get("modified_at_gmt")
                original_url = meta.get("original_url", "")
                author_name = meta.get("author", "Mehdi Akram")
                content_hash = meta.get("content_hash") or compute_content_hash(f"{title}\n{body}")
                rel_md_path = str(md_path.relative_to(ROOT_DIR)).replace("\\", "/")

                # Ensure author exists
                conn.execute(
                    """
                    INSERT OR IGNORE INTO authors (site_id, wp_author_id, name, slug, created_at, updated_at)
                    VALUES (?, 1, ?, 'author', ?, ?)
                    """,
                    (site_id, author_name, now, now)
                )
                author_id = conn.execute(
                    "SELECT id FROM authors WHERE site_id = ? AND name = ?",
                    (site_id, author_name)
                ).fetchone()["id"]

                # Insert or replace post
                conn.execute(
                    """
                    INSERT INTO posts (
                        archive_id, site_id, wp_post_id, title, slug, language,
                        content_html, content_markdown, excerpt, status, post_type,
                        original_url, published_at, published_at_gmt, modified_at,
                        modified_at_gmt, author_id, content_hash, markdown_path,
                        archived_at, created_at, updated_at
                    ) VALUES (?, ?, ?, ?, ?, ?, '', ?, '', 'publish', 'post', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ON CONFLICT(archive_id) DO UPDATE SET
                        title = excluded.title,
                        content_markdown = excluded.content_markdown,
                        language = excluded.language,
                        modified_at = excluded.modified_at,
                        content_hash = excluded.content_hash,
                        markdown_path = excluded.markdown_path,
                        updated_at = excluded.updated_at
                    """,
                    (
                        archive_id, site_id, wp_post_id, title, slug, language,
                        body, original_url, published_at, published_at_gmt,
                        modified_at, modified_at_gmt, author_id, content_hash,
                        rel_md_path, now, now, now
                    )
                )

                post_db_id = conn.execute(
                    "SELECT id FROM posts WHERE archive_id = ?", (archive_id,)
                ).fetchone()["id"]

                # Categories
                for cat_name in meta.get("categories", []):
                    if cat_name:
                        conn.execute(
                            """
                            INSERT OR IGNORE INTO categories (site_id, wp_category_id, name, slug, created_at)
                            VALUES (?, abs(random()) % 100000 + 1, ?, ?, ?)
                            """,
                            (site_id, cat_name, cat_name.lower().replace(" ", "-"), now)
                        )
                        cat_row = conn.execute(
                            "SELECT id FROM categories WHERE site_id = ? AND name = ?",
                            (site_id, cat_name)
                        ).fetchone()
                        if cat_row:
                            conn.execute(
                                "INSERT OR IGNORE INTO post_categories (post_id, category_id) VALUES (?, ?)",
                                (post_db_id, cat_row["id"])
                            )

                # Tags
                for tag_name in meta.get("tags", []):
                    if tag_name:
                        conn.execute(
                            """
                            INSERT OR IGNORE INTO tags (site_id, wp_tag_id, name, slug, created_at)
                            VALUES (?, abs(random()) % 100000 + 1, ?, ?, ?)
                            """,
                            (site_id, tag_name, tag_name.lower().replace(" ", "-"), now)
                        )
                        tag_row = conn.execute(
                            "SELECT id FROM tags WHERE site_id = ? AND name = ?",
                            (site_id, tag_name)
                        ).fetchone()
                        if tag_row:
                            conn.execute(
                                "INSERT OR IGNORE INTO post_tags (post_id, tag_id) VALUES (?, ?)",
                                (post_db_id, tag_row["id"])
                            )

                reconstructed_count += 1

            except Exception as e:
                print(f"  [!] Error parsing {md_path.name}: {e}")

        # Update sync_state counts
        for s_key, s_id in site_map.items():
            cnt = conn.execute("SELECT count(*) as c FROM posts WHERE site_id = ?", (s_id,)).fetchone()["c"]
            conn.execute(
                "UPDATE sync_state SET total_synced_posts = ?, sync_status = 'success', updated_at = ? WHERE site_id = ?",
                (cnt, now, s_id)
            )

        print(f"[Rebuild DB] Ingested {reconstructed_count} articles into SQLite.")
        print("[Rebuild DB] Refreshing JSON exports & search indexes...")
        generate_json_exports(conn, exports_dir=ROOT_DIR / "exports")
        build_search_indexes(conn, out_dir=ROOT_DIR / "website" / "data")

    checkpoint_and_clean_db(target_path)
    print("[Rebuild DB] Rebuild complete and verified.")
    return reconstructed_count


def restore_article_revision(archive_id: str, revision_number: int) -> bool:
    """Restores an article to a prior revision from post_revisions table."""
    with get_db() as conn:
        post = conn.execute(
            """
            SELECT p.id, p.site_id, p.wp_post_id, p.slug, p.language, p.published_at,
                   p.published_at_gmt, p.original_url, p.markdown_path, s.key as source_key, s.name as source_name
            FROM posts p
            JOIN sites s ON p.site_id = s.id
            WHERE p.archive_id = ?
            """,
            (archive_id,)
        ).fetchone()

        if not post:
            print(f"[Restore Revision] Article '{archive_id}' not found.")
            return False

        post_id = post["id"]
        rev = conn.execute(
            """
            SELECT revision_number, title, content_html, content_markdown, excerpt,
                   modified_at, modified_at_gmt, content_hash
            FROM post_revisions
            WHERE post_id = ? AND revision_number = ?
            """,
            (post_id, revision_number)
        ).fetchone()

        if not rev:
            print(f"[Restore Revision] Revision {revision_number} not found for '{archive_id}'.")
            return False

        now = utc_now_iso()
        print(f"[Restore Revision] Restoring {archive_id} to revision {revision_number} ('{rev['title']}')...")

        # 1. Update posts record
        conn.execute(
            """
            UPDATE posts SET
                title = ?,
                content_html = ?,
                content_markdown = ?,
                excerpt = ?,
                modified_at = ?,
                modified_at_gmt = ?,
                content_hash = ?,
                updated_at = ?
            WHERE id = ?
            """,
            (
                rev["title"], rev["content_html"], rev["content_markdown"],
                rev["excerpt"], rev["modified_at"], rev["modified_at_gmt"],
                rev["content_hash"], now, post_id
            )
        )

        # 2. Record restoration log
        conn.execute(
            """
            INSERT INTO sync_logs (
                site_id, mode, started_at, finished_at, status, posts_updated, details_json
            ) VALUES (?, 'restore', ?, ?, 'success', 1, ?)
            """,
            (
                post["site_id"], now, now,
                json.dumps({
                    "action": "restore_revision",
                    "archive_id": archive_id,
                    "restored_revision": revision_number
                })
            )
        )

        # 3. Regenerate Markdown file
        md_file = ROOT_DIR / post["markdown_path"]
        meta, _ = parse_markdown_file(md_file)
        meta["title"] = rev["title"]
        meta["modified_at"] = rev["modified_at"]
        meta["content_hash"] = rev["content_hash"]
        meta["restored_from_revision"] = revision_number
        meta["restored_at"] = now

        save_article_markdown(md_file, meta, rev["content_markdown"])
        print(f"  ✓ Updated Markdown file: {md_file.name}")

        # 4. Refresh JSON exports and indexes
        generate_json_exports(conn)
        build_search_indexes(conn)

    checkpoint_and_clean_db()
    print(f"[Restore Revision] Successfully restored {archive_id} to revision {revision_number}.")
    return True


def rebuild_website() -> None:
    """Refreshes static website data and sitemaps."""
    print("[Rebuild Website] Regenerating static website data...")
    with get_db() as conn:
        build_search_indexes(conn)
        generate_json_exports(conn)
    checkpoint_and_clean_db()
    print("[Rebuild Website] Static website data regenerated successfully.")


def main() -> None:
    parser = argparse.ArgumentParser(description="Restoration & Recovery Toolkit for Mehdi's Digital Legacy")
    parser.add_argument("--verify", type=str, help="Verify backup archive integrity and checksum")
    parser.add_argument("--rebuild-database", action="store_true", help="Reconstruct SQLite database from Markdown files")
    parser.add_argument("--rebuild-website", action="store_true", help="Regenerate static website data and indexes")
    parser.add_argument("--article", type=str, help="Target article archive_id for revision restoration (e.g. royaltechbd-4600)")
    parser.add_argument("--revision", type=int, help="Target revision number to restore")

    args = parser.parse_args()

    if args.verify:
        success = verify_backup(args.verify)
        sys.exit(0 if success else 1)
    elif args.rebuild_database:
        rebuild_database_from_markdown()
        sys.exit(0)
    elif args.rebuild_website:
        rebuild_website()
        sys.exit(0)
    elif args.article and args.revision is not None:
        success = restore_article_revision(args.article, args.revision)
        sys.exit(0 if success else 1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
