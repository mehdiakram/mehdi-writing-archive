"""Master Synchronization Engine for Mehdi's Digital Legacy.

Supports both full historical import and daily incremental synchronization
with revision history tracking, media downloading, Markdown generation,
and JSON export pipelines.
"""

from __future__ import annotations

import argparse
import html
import json
import logging
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from bs4 import BeautifulSoup

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.database import (
    checkpoint_and_clean_db,
    compute_content_hash,
    get_db,
    init_database,
    utc_now_iso,
)
from scripts.json_export import generate_json_exports
from scripts.markdown_export import (
    determine_article_path,
    detect_language,
    html_to_clean_markdown,
    save_article_markdown,
)
from scripts.media import MediaArchiver
from scripts.search_index import build_search_indexes
from scripts.wordpress import WordPressAPIClient, WordPressClientError

# Setup logging
LOGS_DIR = ROOT_DIR / "logs"
LOGS_DIR.mkdir(parents=True, exist_ok=True)
REPORTS_DIR = ROOT_DIR / "reports"
REPORTS_DIR.mkdir(parents=True, exist_ok=True)

log_file = LOGS_DIR / f"sync_{datetime.now(timezone.utc).strftime('%Y%m%d')}.log"

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(str(log_file), encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger("archive.sync")


def load_sources_config() -> List[Dict[str, Any]]:
    """Loads sources from config/sources.json."""
    config_file = ROOT_DIR / "config" / "sources.json"
    with open(config_file, "r", encoding="utf-8") as f:
        return json.load(f).get("sources", [])


def load_settings() -> Dict[str, Any]:
    """Loads runtime settings from config/settings.json."""
    settings_file = ROOT_DIR / "config" / "settings.json"
    if settings_file.exists():
        with open(settings_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


class ArchiveSynchronizer:
    """Orchestrates ingestion, persistence, and exports for one or all sources."""

    def __init__(self, mode: str = "incremental", target_source: Optional[str] = None) -> None:
        self.mode = mode
        self.target_source = target_source
        self.settings = load_settings()
        self.media_archiver = MediaArchiver()
        
        # Ensure DB tables exist
        init_database()

    def sync_taxonomies_and_authors(
        self,
        conn: Any,
        client: WordPressAPIClient,
        site_id: int,
        source_key: str
    ) -> Tuple[Dict[int, int], Dict[int, int], Dict[int, int]]:
        """Syncs authors, categories, and tags from WordPress into SQLite.
        
        Returns mapping dictionaries: (author_map, category_map, tag_map).
        """
        logger.info(f"[{source_key}] Syncing authors, categories, and tags...")
        now = utc_now_iso()

        # 1. Sync Authors
        author_map: Dict[int, int] = {}
        users = client.get_users()
        for u in users:
            wp_author_id = u["id"]
            name = u.get("name") or "Mehdi Akram"
            slug = u.get("slug") or "author"
            url = u.get("url") or ""
            desc = u.get("description") or ""
            avatar = u.get("avatar_urls", {}).get("96") or ""
            
            conn.execute(
                """
                INSERT INTO authors (site_id, wp_author_id, name, slug, url, description, avatar_url, created_at, updated_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(site_id, wp_author_id) DO UPDATE SET
                    name = excluded.name,
                    slug = excluded.slug,
                    url = excluded.url,
                    description = excluded.description,
                    avatar_url = excluded.avatar_url,
                    updated_at = excluded.updated_at
                """,
                (site_id, wp_author_id, name, slug, url, desc, avatar, now, now)
            )
            row = conn.execute(
                "SELECT id FROM authors WHERE site_id = ? AND wp_author_id = ?",
                (site_id, wp_author_id)
            ).fetchone()
            if row:
                author_map[wp_author_id] = row["id"]

        # Default fallback author if none returned
        if not author_map:
            conn.execute(
                """
                INSERT OR IGNORE INTO authors (site_id, wp_author_id, name, slug, created_at, updated_at)
                VALUES (?, 1, 'Mehdi Akram', 'mehdi-akram', ?, ?)
                """,
                (site_id, now, now)
            )
            row = conn.execute(
                "SELECT id FROM authors WHERE site_id = ? AND wp_author_id = 1",
                (site_id,)
            ).fetchone()
            if row:
                author_map[1] = row["id"]

        # 2. Sync Categories
        category_map: Dict[int, int] = {}
        categories = client.get_categories()
        for c in categories:
            wp_cat_id = c["id"]
            name = html.unescape(c.get("name") or "Uncategorized")
            slug = c.get("slug") or "uncategorized"
            desc = c.get("description") or ""
            parent = c.get("parent") or 0
            count = c.get("count") or 0

            conn.execute(
                """
                INSERT INTO categories (site_id, wp_category_id, name, slug, description, parent_id, count, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(site_id, wp_category_id) DO UPDATE SET
                    name = excluded.name,
                    slug = excluded.slug,
                    description = excluded.description,
                    parent_id = excluded.parent_id,
                    count = excluded.count
                """,
                (site_id, wp_cat_id, name, slug, desc, parent, count, now)
            )
            row = conn.execute(
                "SELECT id FROM categories WHERE site_id = ? AND wp_category_id = ?",
                (site_id, wp_cat_id)
            ).fetchone()
            if row:
                category_map[wp_cat_id] = row["id"]

        # 3. Sync Tags
        tag_map: Dict[int, int] = {}
        tags = client.get_tags()
        for t in tags:
            wp_tag_id = t["id"]
            name = html.unescape(t.get("name") or "Tag")
            slug = t.get("slug") or "tag"
            desc = t.get("description") or ""
            count = t.get("count") or 0

            conn.execute(
                """
                INSERT INTO tags (site_id, wp_tag_id, name, slug, description, count, created_at)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(site_id, wp_tag_id) DO UPDATE SET
                    name = excluded.name,
                    slug = excluded.slug,
                    description = excluded.description,
                    count = excluded.count
                """,
                (site_id, wp_tag_id, name, slug, desc, count, now)
            )
            row = conn.execute(
                "SELECT id FROM tags WHERE site_id = ? AND wp_tag_id = ?",
                (site_id, wp_tag_id)
            ).fetchone()
            if row:
                tag_map[wp_tag_id] = row["id"]

        cat_name_map = {c["id"]: html.unescape(c.get("name") or "Uncategorized") for c in categories}
        tag_name_map = {t["id"]: html.unescape(t.get("name") or "Tag") for t in tags}
        author_name_map = {u["id"]: html.unescape(u.get("name") or "Mehdi Akram") for u in users}

        return author_map, category_map, tag_map, cat_name_map, tag_name_map, author_name_map

    def process_featured_media(
        self,
        conn: Any,
        client: WordPressAPIClient,
        site_id: int,
        source_key: str,
        post_data: Dict[str, Any]
    ) -> Optional[int]:
        """Archives featured image for a post if present."""
        featured_media_id = post_data.get("featured_media")
        if not featured_media_id or featured_media_id == 0:
            return None

        # Check if already in media table
        existing = conn.execute(
            "SELECT id FROM media WHERE site_id = ? AND wp_media_id = ?",
            (site_id, featured_media_id)
        ).fetchone()
        if existing:
            return existing["id"]

        # Try to extract URL from embedded media object first
        image_url = None
        alt_text = ""
        caption = ""

        embedded = post_data.get("_embedded", {})
        featured_list = embedded.get("wp:featuredmedia", [])
        if featured_list and isinstance(featured_list, list) and len(featured_list) > 0:
            fm = featured_list[0]
            image_url = fm.get("source_url")
            alt_text = fm.get("alt_text", "")
            caption = fm.get("caption", {}).get("rendered", "")

        # If not embedded, fetch via client
        if not image_url:
            media_item = client.get_media_item(featured_media_id)
            if media_item:
                image_url = media_item.get("source_url")
                alt_text = media_item.get("alt_text", "")
                caption = media_item.get("caption", {}).get("rendered", "")

        if not image_url:
            return None

        # Download safely
        download_res = self.media_archiver.download_image(image_url, source_key)
        now = utc_now_iso()

        conn.execute(
            """
            INSERT INTO media (
                site_id, wp_media_id, original_url, local_path, file_name,
                mime_type, file_size, sha256_hash, alt_text, caption,
                download_status, downloaded_at, error_message, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            ON CONFLICT(site_id, wp_media_id) DO UPDATE SET
                local_path = excluded.local_path,
                download_status = excluded.download_status,
                downloaded_at = excluded.downloaded_at,
                error_message = excluded.error_message
            """,
            (
                site_id,
                featured_media_id,
                image_url,
                download_res.get("local_path"),
                Path(download_res.get("local_path", "")).name if download_res.get("local_path") else None,
                download_res.get("mime_type"),
                download_res.get("file_size", 0),
                download_res.get("sha256_hash"),
                alt_text,
                caption,
                download_res.get("status", "failed"),
                now if download_res.get("status") == "completed" else None,
                download_res.get("error_message"),
                now
            )
        )

        row = conn.execute(
            "SELECT id FROM media WHERE site_id = ? AND wp_media_id = ?",
            (site_id, featured_media_id)
        ).fetchone()
        return row["id"] if row else None

    def sync_single_source(self, source_conf: Dict[str, Any]) -> Dict[str, Any]:
        """Performs full or incremental sync for one specific source."""
        source_key = source_conf["key"]
        source_name = source_conf["name"]
        default_lang = source_conf.get("default_language", "en")
        
        sync_stats = {
            "source_key": source_key,
            "source_name": source_name,
            "mode": self.mode,
            "status": "success",
            "posts_created": 0,
            "posts_updated": 0,
            "posts_unchanged": 0,
            "media_downloaded": 0,
            "errors_count": 0,
            "error_details": [],
            "started_at": utc_now_iso(),
            "finished_at": None,
        }

        logger.info(f"[{source_key}] Starting sync (mode: {self.mode})...")

        client = WordPressAPIClient(
            base_url=source_conf["base_url"],
            api_url=source_conf["api_url"],
            source_key=source_key,
            timeout=self.settings.get("sync", {}).get("request_timeout_seconds", 30),
            max_retries=self.settings.get("sync", {}).get("max_retries", 3),
            retry_backoff=self.settings.get("sync", {}).get("retry_backoff_factor", 1.5),
            delay_ms=self.settings.get("sync", {}).get("delay_between_requests_ms", 250),
        )

        with get_db() as conn:
            site_row = conn.execute("SELECT id FROM sites WHERE key = ?", (source_key,)).fetchone()
            if not site_row:
                raise ValueError(f"Site key {source_key} not registered in database.")
            site_id = site_row["id"]

            # Update sync state to running
            conn.execute(
                "UPDATE sync_state SET sync_status = 'running', updated_at = ? WHERE site_id = ?",
                (utc_now_iso(), site_id)
            )

            try:
                # 1. Sync Taxonomies & Authors
                author_map, category_map, tag_map, cat_name_map, tag_name_map, author_name_map = self.sync_taxonomies_and_authors(
                    conn, client, site_id, source_key
                )

                # 2. Determine modified_after filter if incremental
                modified_after = None
                if self.mode == "incremental":
                    state_row = conn.execute(
                        "SELECT last_post_modified_at FROM sync_state WHERE site_id = ?",
                        (site_id,)
                    ).fetchone()
                    if state_row and state_row["last_post_modified_at"]:
                        overlap_hours = self.settings.get("sync", {}).get("overlap_hours", 48)
                        try:
                            last_mod = datetime.fromisoformat(
                                state_row["last_post_modified_at"].replace("Z", "+00:00")
                            )
                            cutoff = last_mod - timedelta(hours=overlap_hours)
                            modified_after = cutoff.isoformat()
                            logger.info(f"[{source_key}] Incremental cutoff window: {modified_after}")
                        except Exception as e:
                            logger.warning(f"[{source_key}] Could not parse last modified date: {e}")

                # 3. Stream posts from WordPress REST API
                batch_size = self.settings.get("sync", {}).get("batch_size", 50)
                latest_post_modified = None

                for post in client.iterate_all_posts(per_page=batch_size, modified_after=modified_after):
                    wp_post_id = post["id"]
                    archive_id = f"{source_key}-{wp_post_id}"
                    
                    title = html.unescape(post.get("title", {}).get("rendered", "Untitled")).strip()
                    raw_html = post.get("content", {}).get("rendered", "")
                    raw_excerpt = post.get("excerpt", {}).get("rendered", "")
                    slug = post.get("slug") or str(wp_post_id)
                    original_url = post.get("link") or f"{source_conf['base_url']}/?p={wp_post_id}"
                    published_at = post.get("date") or utc_now_iso()
                    published_at_gmt = post.get("date_gmt")
                    modified_at = post.get("modified") or published_at
                    modified_at_gmt = post.get("modified_gmt")
                    
                    # Track latest modified date
                    if not latest_post_modified or modified_at > latest_post_modified:
                        latest_post_modified = modified_at

                    # Clean excerpt
                    clean_excerpt = ""
                    if raw_excerpt:
                        clean_excerpt = BeautifulSoup(raw_excerpt, "html.parser").get_text().strip()

                    # Convert HTML to clean Markdown
                    markdown_body = html_to_clean_markdown(raw_html)
                    if not markdown_body:
                        if clean_excerpt:
                            markdown_body = clean_excerpt
                        else:
                            markdown_body = (
                                "*(No textual body content was exposed by the source WordPress API "
                                "for this entry; it may be an interactive tool or template-rendered page.)*"
                            )
                    
                    # Language detection
                    language = detect_language(title, markdown_body, default_language=default_lang)
                    
                    # Content hash for revision detection
                    content_hash = compute_content_hash(f"{title}\n{markdown_body}")

                    # Author mapping
                    wp_author_id = post.get("author")
                    db_author_id = author_map.get(wp_author_id) or list(author_map.values())[0]

                    # Featured media
                    db_media_id = self.process_featured_media(conn, client, site_id, source_key, post)
                    if db_media_id:
                        sync_stats["media_downloaded"] += 1

                    # Check if post already exists in database
                    existing = conn.execute(
                        "SELECT id, title, content_html, content_markdown, excerpt, modified_at, modified_at_gmt, content_hash, markdown_path "
                        "FROM posts WHERE site_id = ? AND wp_post_id = ?",
                        (site_id, wp_post_id)
                    ).fetchone()

                    now = utc_now_iso()

                    if existing is None:
                        # NEW POST
                        # Determine canonical Markdown path
                        md_path = determine_article_path(
                            source_key=source_key,
                            language=language,
                            published_at=published_at,
                            slug=slug,
                            wp_post_id=wp_post_id
                        )
                        rel_md_path = str(md_path.relative_to(ROOT_DIR)).replace("\\", "/")

                        conn.execute(
                            """
                            INSERT INTO posts (
                                archive_id, site_id, wp_post_id, title, slug, language,
                                content_html, content_markdown, excerpt, status, post_type,
                                original_url, published_at, published_at_gmt, modified_at,
                                modified_at_gmt, author_id, featured_media_id, content_hash,
                                markdown_path, archived_at, created_at, updated_at
                            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'publish', 'post', ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                            """,
                            (
                                archive_id, site_id, wp_post_id, title, slug, language,
                                raw_html, markdown_body, clean_excerpt, original_url,
                                published_at, published_at_gmt, modified_at, modified_at_gmt,
                                db_author_id, db_media_id, content_hash, rel_md_path,
                                now, now, now
                            )
                        )
                        post_row = conn.execute(
                            "SELECT id FROM posts WHERE archive_id = ?", (archive_id,)
                        ).fetchone()
                        post_db_id = post_row["id"]

                        # Link categories
                        for wp_cat in post.get("categories", []):
                            if wp_cat in category_map:
                                conn.execute(
                                    "INSERT OR IGNORE INTO post_categories (post_id, category_id) VALUES (?, ?)",
                                    (post_db_id, category_map[wp_cat])
                                )

                        # Link tags
                        for wp_tag in post.get("tags", []):
                            if wp_tag in tag_map:
                                conn.execute(
                                    "INSERT OR IGNORE INTO post_tags (post_id, tag_id) VALUES (?, ?)",
                                    (post_db_id, tag_map[wp_tag])
                                )

                        # Save Markdown file
                        meta = {
                            "archive_id": archive_id,
                            "source": source_key,
                            "source_name": source_name,
                            "wordpress_id": wp_post_id,
                            "title": title,
                            "slug": slug,
                            "language": language,
                            "status": "publish",
                            "published_at": published_at,
                            "published_at_gmt": published_at_gmt,
                            "modified_at": modified_at,
                            "modified_at_gmt": modified_at_gmt,
                            "original_url": original_url,
                            "author": author_name_map.get(wp_author_id, "Mehdi Akram"),
                            "categories": [cat_name_map[cid] for cid in post.get("categories", []) if cid in cat_name_map],
                            "tags": [tag_name_map[tid] for tid in post.get("tags", []) if tid in tag_name_map],
                            "content_hash": content_hash,
                            "archived_at": now,
                        }
                        save_article_markdown(md_path, meta, markdown_body)

                        sync_stats["posts_created"] += 1
                        logger.info(f"[{source_key}] [+] Created: {archive_id} - {title[:50]}")

                    else:
                        # EXISTING POST: Check if modified
                        post_db_id = existing["id"]
                        old_hash = existing["content_hash"]

                        if old_hash != content_hash:
                            # Content has changed: record revision and update
                            rev_count = conn.execute(
                                "SELECT count(*) as c FROM post_revisions WHERE post_id = ?",
                                (post_db_id,)
                            ).fetchone()["c"]
                            next_rev = rev_count + 1

                            conn.execute(
                                """
                                INSERT INTO post_revisions (
                                    post_id, revision_number, title, content_html,
                                    content_markdown, excerpt, modified_at, modified_at_gmt,
                                    content_hash, change_summary, recorded_at
                                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 'Synchronized update from WordPress', ?)
                                """,
                                (
                                    post_db_id, next_rev, existing["title"],
                                    existing["content_html"], existing["content_markdown"],
                                    existing["excerpt"], existing["modified_at"],
                                    existing["modified_at_gmt"], old_hash, now
                                )
                            )

                            # Update active record
                            conn.execute(
                                """
                                UPDATE posts SET
                                    title = ?,
                                    content_html = ?,
                                    content_markdown = ?,
                                    excerpt = ?,
                                    language = ?,
                                    modified_at = ?,
                                    modified_at_gmt = ?,
                                    content_hash = ?,
                                    author_id = ?,
                                    featured_media_id = ?,
                                    updated_at = ?
                                WHERE id = ?
                                """,
                                (
                                    title, raw_html, markdown_body, clean_excerpt,
                                    language, modified_at, modified_at_gmt, content_hash,
                                    db_author_id, db_media_id, now, post_db_id
                                )
                            )

                            # Regenerate Markdown file
                            md_full_path = ROOT_DIR / existing["markdown_path"]
                            meta = {
                                "archive_id": archive_id,
                                "source": source_key,
                                "source_name": source_name,
                                "wordpress_id": wp_post_id,
                                "title": title,
                                "slug": slug,
                                "language": language,
                                "status": "publish",
                                "published_at": published_at,
                                "published_at_gmt": published_at_gmt,
                                "modified_at": modified_at,
                                "modified_at_gmt": modified_at_gmt,
                                "original_url": original_url,
                                "author": author_name_map.get(wp_author_id, "Mehdi Akram"),
                                "categories": [cat_name_map[cid] for cid in post.get("categories", []) if cid in cat_name_map],
                                "tags": [tag_name_map[tid] for tid in post.get("tags", []) if tid in tag_name_map],
                                "content_hash": content_hash,
                                "archived_at": now,
                            }
                            save_article_markdown(md_full_path, meta, markdown_body)

                            sync_stats["posts_updated"] += 1
                            logger.info(f"[{source_key}] [*] Updated (rev {next_rev}): {archive_id} - {title[:50]}")

                        else:
                            sync_stats["posts_unchanged"] += 1

                # Update sync_state on success
                finish_time = utc_now_iso()
                sync_stats["finished_at"] = finish_time

                total_synced = conn.execute(
                    "SELECT count(*) as c FROM posts WHERE site_id = ?", (site_id,)
                ).fetchone()["c"]

                conn.execute(
                    """
                    UPDATE sync_state SET
                        last_sync_at = ?,
                        last_post_modified_at = coalesce(?, last_post_modified_at),
                        total_synced_posts = ?,
                        sync_status = 'success',
                        error_message = NULL,
                        updated_at = ?
                    WHERE site_id = ?
                    """,
                    (finish_time, latest_post_modified, total_synced, finish_time, site_id)
                )

                # Record in sync_logs
                conn.execute(
                    """
                    INSERT INTO sync_logs (
                        site_id, mode, started_at, finished_at, status,
                        posts_created, posts_updated, posts_unchanged,
                        media_downloaded, errors_count, details_json
                    ) VALUES (?, ?, ?, ?, 'success', ?, ?, ?, ?, 0, ?)
                    """,
                    (
                        site_id, self.mode, sync_stats["started_at"], finish_time,
                        sync_stats["posts_created"], sync_stats["posts_updated"],
                        sync_stats["posts_unchanged"], sync_stats["media_downloaded"],
                        json.dumps(sync_stats)
                    )
                )

            except Exception as e:
                err_time = utc_now_iso()
                sync_stats["status"] = "error"
                sync_stats["finished_at"] = err_time
                sync_stats["errors_count"] += 1
                sync_stats["error_details"].append(str(e))
                logger.error(f"[{source_key}] Sync error: {e}", exc_info=True)

                conn.execute(
                    """
                    UPDATE sync_state SET
                        sync_status = 'error',
                        error_message = ?,
                        updated_at = ?
                    WHERE site_id = ?
                    """,
                    (str(e), err_time, site_id)
                )

                conn.execute(
                    """
                    INSERT INTO sync_logs (
                        site_id, mode, started_at, finished_at, status,
                        posts_created, posts_updated, posts_unchanged,
                        media_downloaded, errors_count, details_json
                    ) VALUES (?, ?, ?, ?, 'error', ?, ?, ?, ?, 1, ?)
                    """,
                    (
                        site_id, self.mode, sync_stats["started_at"], err_time,
                        sync_stats["posts_created"], sync_stats["posts_updated"],
                        sync_stats["posts_unchanged"], sync_stats["media_downloaded"],
                        json.dumps(sync_stats)
                    )
                )

        return sync_stats

    def run(self) -> List[Dict[str, Any]]:
        """Executes synchronization according to configuration and arguments."""
        sources = load_sources_config()
        all_stats = []

        for src in sources:
            if not src.get("enabled", True):
                continue
            if self.target_source and src["key"] != self.target_source:
                continue

            stats = self.sync_single_source(src)
            all_stats.append(stats)

        # After syncing sources, refresh JSON exports and search indexes
        with get_db() as conn:
            logger.info("Generating deterministic JSON exports...")
            generate_json_exports(conn)
            logger.info("Building static search indexes...")
            build_search_indexes(conn)

        # Checkpoint WAL cleanly
        checkpoint_and_clean_db()

        # Write audit report
        report_file = REPORTS_DIR / f"sync_report_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, "w", encoding="utf-8") as rf:
            json.dump(all_stats, rf, ensure_ascii=False, indent=2)

        logger.info(f"Sync complete. Report saved to {report_file}")
        return all_stats


def main() -> None:
    parser = argparse.ArgumentParser(description="Synchronize Mehdi's Digital Legacy Archive")
    parser.add_argument(
        "--mode",
        choices=["full", "incremental"],
        default="incremental",
        help="Synchronization mode: full historical or incremental"
    )
    parser.add_argument(
        "--source",
        choices=["royaltechbd", "shamokaldarpon"],
        default=None,
        help="Restrict sync to a specific source"
    )
    args = parser.parse_args()

    syncer = ArchiveSynchronizer(mode=args.mode, target_source=args.source)
    results = syncer.run()

    has_errors = any(r["status"] == "error" for r in results)
    sys.exit(1 if has_errors else 0)


if __name__ == "__main__":
    main()
