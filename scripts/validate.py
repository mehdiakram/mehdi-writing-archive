"""Integrity Validation Suite for Mehdi's Digital Legacy.

Validates SQLite integrity, foreign keys, Markdown frontmatter, JSON exports,
and required repository structure.
"""

from __future__ import annotations

import json
import sqlite3
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.database import get_db, get_db_path
from scripts.markdown_export import parse_markdown_file


def validate_required_files() -> Tuple[bool, List[str]]:
    """Checks that all mandatory core files and directories exist."""
    required = [
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "CHANGELOG.md",
        "DIGITAL-LEGACY.md",
        "DIGITAL-LEGACY-BN.md",
        "requirements.txt",
        "pyproject.toml",
        "config/sources.json",
        "config/settings.json",
        "config/media-policy.json",
        "database/schema.sql",
        ".github/workflows/daily-sync.yml",
        ".github/workflows/deploy-pages.yml",
        ".github/workflows/validate.yml",
        ".github/workflows/backup.yml",
        "website/index.html",
        "authors/mehdi-akram.md",
    ]
    
    missing = []
    for rel_path in required:
        full_path = ROOT_DIR / rel_path
        if not full_path.exists():
            missing.append(rel_path)
            
    return (len(missing) == 0), missing


def validate_sqlite_integrity() -> Tuple[bool, List[str]]:
    """Runs PRAGMA integrity_check and PRAGMA foreign_key_check on archive.sqlite."""
    db_path = get_db_path()
    errors = []
    
    if not db_path.exists():
        return False, [f"Database file not found: {db_path}"]
        
    try:
        with get_db(db_path, wal_mode=False) as conn:
            # Integrity check
            rows = conn.execute("PRAGMA integrity_check;").fetchall()
            for r in rows:
                val = r[0]
                if val.lower() != "ok":
                    errors.append(f"Integrity check issue: {val}")
                    
            # Foreign key check
            fk_violations = conn.execute("PRAGMA foreign_key_check;").fetchall()
            for fk in fk_violations:
                errors.append(f"Foreign key violation: table={fk[0]}, rowid={fk[1]}, parent={fk[2]}")
                
            # Check FTS index integrity
            try:
                conn.execute("INSERT INTO posts_fts(posts_fts) VALUES('integrity-check');")
            except Exception as e:
                errors.append(f"FTS5 integrity error: {e}")
                
    except Exception as e:
        errors.append(f"Database error during validation: {e}")
        
    return (len(errors) == 0), errors


def validate_markdown_articles() -> Tuple[bool, List[str]]:
    """Validates that all Markdown articles have valid YAML frontmatter and content."""
    articles_dir = ROOT_DIR / "articles"
    errors = []
    
    if not articles_dir.exists():
        return True, []
        
    md_files = list(articles_dir.glob("**/*.md"))
    required_frontmatter_keys = [
        "archive_id", "source", "wordpress_id", "title", "published_at", "content_hash"
    ]
    
    for file_path in md_files:
        rel = file_path.relative_to(ROOT_DIR)
        try:
            meta, body = parse_markdown_file(file_path)
            if not meta:
                errors.append(f"{rel}: Missing or malformed YAML frontmatter")
                continue
                
            for key in required_frontmatter_keys:
                if key not in meta or meta[key] is None:
                    errors.append(f"{rel}: Missing required frontmatter key '{key}'")
                    
            if not body or len(body.strip()) == 0:
                errors.append(f"{rel}: Article body is completely empty")
                
        except Exception as e:
            errors.append(f"{rel}: Failed to parse Markdown file ({e})")
            
    return (len(errors) == 0), errors


def validate_json_exports() -> Tuple[bool, List[str]]:
    """Validates structure and consistency of exported JSON files."""
    exports_dir = ROOT_DIR / "exports"
    errors = []
    
    if not exports_dir.exists():
        return True, []
        
    manifest_path = exports_dir / "manifest.json"
    articles_path = exports_dir / "articles.json"
    
    if not manifest_path.exists() and not articles_path.exists():
        return True, []
        
    try:
        if manifest_path.exists():
            with open(manifest_path, "r", encoding="utf-8") as f:
                manifest = json.load(f)
                
            if "total_articles" not in manifest:
                errors.append("manifest.json: Missing 'total_articles' field")
                
        if articles_path.exists():
            with open(articles_path, "r", encoding="utf-8") as f:
                articles = json.load(f)
                
            if not isinstance(articles, list):
                errors.append("articles.json: Expected JSON array")
            elif manifest_path.exists():
                if manifest.get("total_articles") != len(articles):
                    errors.append(
                        f"Count mismatch: manifest says {manifest.get('total_articles')} but articles.json has {len(articles)}"
                    )
    except Exception as e:
        errors.append(f"JSON validation error: {e}")
        
    return (len(errors) == 0), errors


def run_all_validations() -> bool:
    """Runs all archive validation checks and prints detailed diagnostic report."""
    print("=" * 60)
    print("MEHDI'S DIGITAL LEGACY: ARCHIVE INTEGRITY VALIDATION")
    print("=" * 60)
    
    all_passed = True
    
    # 1. Required Files
    print("[1/4] Checking required repository files...")
    ok, missing = validate_required_files()
    if ok:
        print("  ✓ All required repository files present.")
    else:
        print(f"  ✗ Missing {len(missing)} required files:")
        for m in missing:
            print(f"    - {m}")
        all_passed = False
        
    # 2. SQLite Integrity
    print("\n[2/4] Validating SQLite database integrity & foreign keys...")
    ok, db_errors = validate_sqlite_integrity()
    if ok:
        print("  ✓ SQLite database integrity check passed (PRAGMA integrity_check = ok, 0 foreign key violations).")
    else:
        print(f"  ✗ SQLite integrity errors ({len(db_errors)}):")
        for e in db_errors:
            print(f"    - {e}")
        all_passed = False
        
    # 3. Markdown Validation
    print("\n[3/4] Validating Markdown articles and YAML frontmatter...")
    ok, md_errors = validate_markdown_articles()
    if ok:
        print("  ✓ All Markdown articles validated successfully.")
    else:
        print(f"  ✗ Markdown validation issues ({len(md_errors)}):")
        for e in md_errors[:10]:
            print(f"    - {e}")
        if len(md_errors) > 10:
            print(f"    ... and {len(md_errors) - 10} more")
        all_passed = False
        
    # 4. JSON Exports
    print("\n[4/4] Validating JSON exports and manifest consistency...")
    ok, json_errors = validate_json_exports()
    if ok:
        print("  ✓ JSON exports and manifest validated successfully.")
    else:
        print(f"  ✗ JSON export validation errors ({len(json_errors)}):")
        for e in json_errors:
            print(f"    - {e}")
        all_passed = False
        
    print("\n" + "=" * 60)
    if all_passed:
        print("RESULT: ALL VALIDATION CHECKS PASSED (STATUS: HEALTHY)")
        print("=" * 60)
        return True
    else:
        print("RESULT: VALIDATION FAILED WITH ERRORS (STATUS: ATTENTION REQUIRED)")
        print("=" * 60)
        return False


if __name__ == "__main__":
    success = run_all_validations()
    sys.exit(0 if success else 1)
