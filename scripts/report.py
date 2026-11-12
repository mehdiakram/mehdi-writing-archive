"""Status and Audit Reporter for Mehdi's Digital Legacy.

Outputs human-readable CLI summary and persists machine-readable
JSON reports in reports/ directory.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.database import get_db, get_db_path, init_database

REPORTS_DIR = ROOT_DIR / "reports"


def generate_status_report() -> Dict[str, Any]:
    """Generates detailed archive health and statistics report."""
    REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    init_database()

    db_path = get_db_path()
    now_iso = datetime.now(timezone.utc).isoformat()

    with get_db(db_path, wal_mode=False) as conn:
        # Total counts
        total_posts = conn.execute("SELECT count(*) as c FROM posts WHERE is_deleted = 0").fetchone()["c"]
        total_media = conn.execute("SELECT count(*) as c FROM media").fetchone()["c"]
        total_categories = conn.execute("SELECT count(*) as c FROM categories").fetchone()["c"]
        total_tags = conn.execute("SELECT count(*) as c FROM tags").fetchone()["c"]
        total_revisions = conn.execute("SELECT count(*) as c FROM post_revisions").fetchone()["c"]

        # Counts by source
        sources_cur = conn.execute(
            """
            SELECT s.key, s.name, s.domain, s.default_language,
                   st.last_sync_at, st.sync_status, st.total_synced_posts, st.error_message,
                   count(p.id) as current_posts
            FROM sites s
            LEFT JOIN sync_state st ON s.id = st.site_id
            LEFT JOIN posts p ON s.id = p.site_id AND p.is_deleted = 0
            GROUP BY s.id
            """
        )
        sources_data = []
        for r in sources_cur.fetchall():
            sources_data.append({
                "key": r["key"],
                "name": r["name"],
                "domain": r["domain"],
                "default_language": r["default_language"],
                "last_sync_at": r["last_sync_at"],
                "sync_status": r["sync_status"] or "never",
                "total_synced_posts": r["current_posts"],
                "last_error": r["error_message"],
            })

        # Counts by language
        lang_cur = conn.execute(
            "SELECT language, count(*) as c FROM posts WHERE is_deleted = 0 GROUP BY language"
        )
        language_counts = {r["language"]: r["c"] for r in lang_cur.fetchall()}

        # Integrity status
        integrity_ok = True
        try:
            row = conn.execute("PRAGMA integrity_check;").fetchone()
            if row[0].lower() != "ok":
                integrity_ok = False
        except Exception:
            integrity_ok = False

    report = {
        "report_generated_at": now_iso,
        "archive_name": "Mehdi's Digital Legacy",
        "archive_health": "healthy" if integrity_ok else "corrupted",
        "total_articles": total_posts,
        "total_media": total_media,
        "total_categories": total_categories,
        "total_tags": total_tags,
        "total_revisions": total_revisions,
        "articles_by_language": language_counts,
        "sources": sources_data,
    }

    # Print human-readable report
    print("=" * 65)
    print("MEHDI'S DIGITAL LEGACY: ARCHIVE STATUS REPORT")
    print("=" * 65)
    print(f"Report Timestamp:    {now_iso}")
    print(f"Archive Health:      {'✓ HEALTHY' if integrity_ok else '✗ CORRUPTED'}")
    print(f"Total Articles:      {total_posts}")
    print(f"Total Media Files:   {total_media}")
    print(f"Total Categories:    {total_categories}")
    print(f"Total Tags:          {total_tags}")
    print(f"Article Revisions:   {total_revisions}")
    print("-" * 65)
    print("Articles by Language:")
    for lang, count in language_counts.items():
        lang_label = "Bengali (বাংলা)" if lang == "bn" else "English (en)"
        print(f"  - {lang_label}: {count}")
    print("-" * 65)
    print("Source Status:")
    for s in sources_data:
        print(f"  • {s['name']} ({s['key']})")
        print(f"      Articles Preserved: {s['total_synced_posts']}")
        print(f"      Last Sync:          {s['last_sync_at'] or 'Never'}")
        print(f"      Status:             {s['sync_status'].upper()}")
        if s['last_error']:
            print(f"      Error:              {s['last_error']}")
    print("=" * 65)

    # Save to reports/
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    report_file = REPORTS_DIR / f"archive_status_{timestamp}.json"
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    print(f"Machine-readable report saved to: {report_file.name}")

    return report


if __name__ == "__main__":
    generate_status_report()
