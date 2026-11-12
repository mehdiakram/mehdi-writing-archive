"""Deterministic JSON Exporter for Mehdi's Digital Legacy.

Generates articles.json, categories.json, tags.json, authors.json, and manifest.json.
All exports are deterministically sorted to prevent unnecessary Git diffs.
"""

from __future__ import annotations

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT_DIR = Path(__file__).resolve().parent.parent
EXPORTS_DIR = ROOT_DIR / "exports"


def generate_json_exports(conn: sqlite3.Connection, exports_dir: Optional[Path] = None) -> Dict[str, Any]:
    """Extracts all data from SQLite and writes deterministic JSON files."""
    dest_dir = exports_dir or EXPORTS_DIR
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Fetch Authors
    authors_cur = conn.execute(
        """
        SELECT a.id, a.wp_author_id, a.name, a.slug, a.url, a.description, s.key as source_key
        FROM authors a
        JOIN sites s ON a.site_id = s.id
        ORDER BY a.id ASC
        """
    )
    authors = []
    for r in authors_cur.fetchall():
        authors.append({
            "id": r["id"],
            "source": r["source_key"],
            "wordpress_author_id": r["wp_author_id"],
            "name": r["name"],
            "slug": r["slug"],
            "url": r["url"] or "",
            "description": r["description"] or "",
        })
        
    # 2. Fetch Categories
    cat_cur = conn.execute(
        """
        SELECT c.id, c.wp_category_id, c.name, c.slug, c.description, c.count, s.key as source_key
        FROM categories c
        JOIN sites s ON c.site_id = s.id
        ORDER BY s.key ASC, c.name ASC
        """
    )
    categories = []
    for r in cat_cur.fetchall():
        categories.append({
            "id": r["id"],
            "source": r["source_key"],
            "wordpress_category_id": r["wp_category_id"],
            "name": r["name"],
            "slug": r["slug"],
            "description": r["description"] or "",
            "count": r["count"] or 0,
        })
        
    # 3. Fetch Tags
    tag_cur = conn.execute(
        """
        SELECT t.id, t.wp_tag_id, t.name, t.slug, t.description, t.count, s.key as source_key
        FROM tags t
        JOIN sites s ON t.site_id = s.id
        ORDER BY s.key ASC, t.name ASC
        """
    )
    tags = []
    for r in tag_cur.fetchall():
        tags.append({
            "id": r["id"],
            "source": r["source_key"],
            "wordpress_tag_id": r["wp_tag_id"],
            "name": r["name"],
            "slug": r["slug"],
            "description": r["description"] or "",
            "count": r["count"] or 0,
        })
        
    # 4. Fetch Articles
    art_cur = conn.execute(
        """
        SELECT 
            p.id, p.archive_id, s.key as source, s.name as source_name, p.wp_post_id,
            p.title, p.slug, p.language, p.excerpt, p.status, p.post_type,
            p.original_url, p.published_at, p.modified_at,
            a.name as author_name,
            m.original_url as featured_image_url, m.local_path as featured_image_local,
            p.content_hash, p.markdown_path
        FROM posts p
        JOIN sites s ON p.site_id = s.id
        LEFT JOIN authors a ON p.author_id = a.id
        LEFT JOIN media m ON p.featured_media_id = m.id
        WHERE p.is_deleted = 0
        ORDER BY p.published_at DESC, p.id DESC
        """
    )
    
    articles = []
    articles_by_source: Dict[str, int] = {}
    articles_by_language: Dict[str, int] = {}
    
    for r in art_cur.fetchall():
        post_id = r["id"]
        source = r["source"]
        lang = r["language"]
        
        articles_by_source[source] = articles_by_source.get(source, 0) + 1
        articles_by_language[lang] = articles_by_language.get(lang, 0) + 1
        
        # Get categories for this post
        post_cats = [
            c["name"] for c in conn.execute(
                """
                SELECT c.name FROM categories c
                JOIN post_categories pc ON c.id = pc.category_id
                WHERE pc.post_id = ?
                ORDER BY c.name ASC
                """,
                (post_id,)
            ).fetchall()
        ]
        
        # Get tags for this post
        post_tags = [
            t["name"] for t in conn.execute(
                """
                SELECT t.name FROM tags t
                JOIN post_tags pt ON t.id = pt.tag_id
                WHERE pt.post_id = ?
                ORDER BY t.name ASC
                """,
                (post_id,)
            ).fetchall()
        ]
        
        articles.append({
            "archive_id": r["archive_id"],
            "source": source,
            "source_name": r["source_name"],
            "wordpress_id": r["wp_post_id"],
            "title": r["title"],
            "slug": r["slug"],
            "language": lang,
            "excerpt": r["excerpt"] or "",
            "published_at": r["published_at"],
            "modified_at": r["modified_at"],
            "original_url": r["original_url"],
            "author": r["author_name"] or "Mehdi Akram",
            "categories": post_cats,
            "tags": post_tags,
            "featured_image": r["featured_image_local"] or r["featured_image_url"] or "",
            "markdown_path": r["markdown_path"].replace("\\", "/"),
            "content_hash": r["content_hash"],
        })

    # Count media
    media_count = conn.execute("SELECT count(*) as c FROM media").fetchone()["c"]

    # Manifest
    now_iso = datetime.now(timezone.utc).isoformat()
    manifest = {
        "archive_generation_timestamp": now_iso,
        "archive_name": "Mehdi's Digital Legacy",
        "archive_tagline": "A Lifetime of Thoughts, Knowledge and Experiences, Preserved for Generations.",
        "export_format_version": "1.0.0",
        "database_schema_version": 1,
        "archive_integrity_status": "verified",
        "total_articles": len(articles),
        "article_counts_by_source": articles_by_source,
        "article_counts_by_language": articles_by_language,
        "total_categories": len(categories),
        "total_tags": len(tags),
        "total_media_files": media_count,
    }

    # Write files deterministically
    def write_json(file_path: Path, data: Any) -> None:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            f.write("\n")

    write_json(dest_dir / "authors.json", authors)
    write_json(dest_dir / "categories.json", categories)
    write_json(dest_dir / "tags.json", tags)
    write_json(dest_dir / "articles.json", articles)
    write_json(dest_dir / "manifest.json", manifest)

    return manifest
