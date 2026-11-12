"""Static Website Builder for Mehdi's Digital Legacy.

Compiles search indexes, article summaries, sitemap.xml, and robots.txt
for zero-backend deployment to GitHub Pages.
"""

from __future__ import annotations

import json
import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.database import checkpoint_and_clean_db, get_db, init_database
from scripts.json_export import generate_json_exports
from scripts.search_index import build_search_indexes

WEBSITE_DIR = ROOT_DIR / "website"
CONFIG_DIR = ROOT_DIR / "config"


def generate_sitemap(articles: list, base_url: str) -> None:
    """Generates valid XML sitemap for search engines."""
    clean_base = base_url.rstrip("/")
    urlset = ET.Element(
        "urlset",
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    )

    static_pages = [
        "",
        "/archive.html",
        "/search.html",
        "/categories.html",
        "/tags.html",
        "/author.html",
        "/about.html",
        "/downloads.html",
    ]

    now_date = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Static pages
    for page in static_pages:
        url_elem = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_elem, "loc")
        loc.text = f"{clean_base}{page}"
        lastmod = ET.SubElement(url_elem, "lastmod")
        lastmod.text = now_date
        changefreq = ET.SubElement(url_elem, "changefreq")
        changefreq.text = "daily" if page == "" else "weekly"
        priority = ET.SubElement(url_elem, "priority")
        priority.text = "1.0" if page == "" else "0.8"

    # Article details pages (article.html?id=royaltechbd-123)
    for art in articles:
        url_elem = ET.SubElement(urlset, "url")
        loc = ET.SubElement(url_elem, "loc")
        loc.text = f"{clean_base}/article.html?id={art['archive_id']}"
        lastmod = ET.SubElement(url_elem, "lastmod")
        lastmod.text = (art.get("modified_at") or art.get("published_at") or now_date)[:10]
        changefreq = ET.SubElement(url_elem, "changefreq")
        changefreq.text = "monthly"
        priority = ET.SubElement(url_elem, "priority")
        priority.text = "0.7"

    tree = ET.ElementTree(urlset)
    sitemap_path = WEBSITE_DIR / "sitemap.xml"
    with open(sitemap_path, "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
    print(f"  ✓ Generated: {sitemap_path.name} ({len(static_pages) + len(articles)} URLs)")


def generate_robots_txt(base_url: str) -> None:
    """Generates standard robots.txt permitting archival crawlers."""
    clean_base = base_url.rstrip("/")
    robots_path = WEBSITE_DIR / "robots.txt"
    with open(robots_path, "w", encoding="utf-8") as f:
        f.write(
            "User-agent: *\n"
            "Allow: /\n\n"
            f"Sitemap: {clean_base}/sitemap.xml\n"
        )
    print(f"  ✓ Generated: {robots_path.name}")


def build_website() -> None:
    """Runs the full website compilation workflow."""
    print("=" * 60)
    print("MEHDI'S DIGITAL LEGACY: STATIC WEBSITE BUILDER")
    print("=" * 60)

    init_database()

    settings_file = CONFIG_DIR / "settings.json"
    base_url = "https://mehdiakram.github.io/mehdi-writing-archive"
    if settings_file.exists():
        with open(settings_file, "r", encoding="utf-8") as f:
            base_url = json.load(f).get("base_website_url", base_url)

    with get_db() as conn:
        print("[1/3] Generating JSON data exports...")
        manifest = generate_json_exports(conn)

        print("[2/3] Compiling search index & article summaries...")
        idx_res = build_search_indexes(conn)

        # Load articles for sitemap
        articles_file = ROOT_DIR / "exports" / "articles.json"
        articles = []
        if articles_file.exists():
            with open(articles_file, "r", encoding="utf-8") as af:
                articles = json.load(af)

        print("[3/3] Generating sitemap.xml and robots.txt...")
        generate_sitemap(articles, base_url)
        generate_robots_txt(base_url)

    checkpoint_and_clean_db()

    print("\n" + "=" * 60)
    print(f"WEBSITE BUILD COMPLETE!")
    print(f"  - Total Articles: {manifest.get('total_articles', 0)}")
    print(f"  - Search Index: {idx_res.get('indexed_articles', 0)} articles indexed")
    print(f"  - Target URL: {base_url}")
    print("=" * 60)


if __name__ == "__main__":
    build_website()
