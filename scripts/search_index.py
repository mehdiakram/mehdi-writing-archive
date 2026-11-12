"""Search Index Builder for Mehdi's Digital Legacy.

Generates an optimized client-side search index (search-index.json)
and lightweight articles summary (articles-summary.json) supporting both
Bangla and English tokenization.
"""

from __future__ import annotations

import json
import re
import sqlite3
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT_DIR = Path(__file__).resolve().parent.parent
WEBSITE_DATA_DIR = ROOT_DIR / "website" / "data"


def normalize_search_text(text: str) -> str:
    """Normalizes text for indexing across English and Bengali scripts."""
    if not text:
        return ""
    # Unicode NFC normalization
    text = unicodedata.normalize("NFC", text)
    # Remove HTML tags if any remain
    text = re.sub(r"<[^>]+>", " ", text)
    # Lowercase Latin characters
    text = text.lower()
    # Normalize excessive spaces
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def build_search_indexes(conn: sqlite3.Connection, out_dir: Optional[Path] = None) -> Dict[str, Any]:
    """Generates search-index.json and articles-summary.json for the static frontend."""
    dest_dir = out_dir or WEBSITE_DATA_DIR
    dest_dir.mkdir(parents=True, exist_ok=True)

    cursor = conn.execute(
        """
        SELECT 
            p.id, p.archive_id, s.key as source, s.name as source_name, p.wp_post_id,
            p.title, p.slug, p.language, p.excerpt, p.content_markdown,
            p.original_url, p.published_at, p.modified_at,
            a.name as author_name,
            m.original_url as featured_image_url, m.local_path as featured_image_local,
            p.markdown_path
        FROM posts p
        JOIN sites s ON p.site_id = s.id
        LEFT JOIN authors a ON p.author_id = a.id
        LEFT JOIN media m ON p.featured_media_id = m.id
        WHERE p.is_deleted = 0
        ORDER BY p.published_at DESC
        """
    )

    search_items: List[Dict[str, Any]] = []
    summary_items: List[Dict[str, Any]] = []

    for r in cursor.fetchall():
        post_id = r["id"]
        
        # Get categories
        cats = [
            c["name"] for c in conn.execute(
                """
                SELECT c.name FROM categories c
                JOIN post_categories pc ON c.id = pc.category_id
                WHERE pc.post_id = ?
                """,
                (post_id,)
            ).fetchall()
        ]
        
        # Get tags
        tags = [
            t["name"] for t in conn.execute(
                """
                SELECT t.name FROM tags t
                JOIN post_tags pt ON t.id = pt.tag_id
                WHERE pt.post_id = ?
                """,
                (post_id,)
            ).fetchall()
        ]

        pub_date = r["published_at"] or ""
        year = "Unknown"
        if pub_date:
            try:
                year = str(datetime.fromisoformat(pub_date.replace("Z", "+00:00")).year)
            except Exception:
                match = re.match(r"^(\d{4})", pub_date)
                if match:
                    year = match.group(1)

        # Lightweight summary for article listing / cards
        summary_items.append({
            "archive_id": r["archive_id"],
            "title": r["title"],
            "slug": r["slug"],
            "source": r["source"],
            "source_name": r["source_name"],
            "language": r["language"],
            "published_at": pub_date,
            "year": year,
            "excerpt": r["excerpt"] or "",
            "author": r["author_name"] or "Mehdi Akram",
            "categories": cats,
            "tags": tags,
            "featured_image": r["featured_image_local"] or r["featured_image_url"] or "",
            "original_url": r["original_url"],
            "markdown_path": r["markdown_path"].replace("\\", "/"),
        })

        # Search index item (optimized for client-side search)
        # We index title, categories, tags, excerpt, and the first 3000 chars of body
        body_sample = (r["content_markdown"] or "")[:3000]
        searchable_content = f"{r['title']} {' '.join(cats)} {' '.join(tags)} {r['excerpt'] or ''} {body_sample}"
        normalized = normalize_search_text(searchable_content)

        search_items.append({
            "id": r["archive_id"],
            "t": r["title"],
            "s": r["slug"],
            "src": r["source"],
            "src_n": r["source_name"],
            "lang": r["language"],
            "yr": year,
            "dt": pub_date[:10] if pub_date else "",
            "c": cats,
            "tg": tags,
            "a": r["author_name"] or "Mehdi Akram",
            "ex": r["excerpt"] or "",
            "txt": normalized,
            "img": r["featured_image_local"] or r["featured_image_url"] or "",
        })

    # Write search-index.json and articles-summary.json
    with open(dest_dir / "search-index.json", "w", encoding="utf-8") as f:
        json.dump(search_items, f, ensure_ascii=False)

    with open(dest_dir / "articles-summary.json", "w", encoding="utf-8") as f:
        json.dump(summary_items, f, ensure_ascii=False, indent=2)

    return {
        "indexed_articles": len(search_items),
        "search_index_path": str(dest_dir / "search-index.json"),
        "articles_summary_path": str(dest_dir / "articles-summary.json"),
    }
