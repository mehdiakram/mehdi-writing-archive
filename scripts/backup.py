"""3-2-1 Disaster Recovery Backup Packager for Mehdi's Digital Legacy.

Performs consistent SQLite hot-backup, packages articles, media, exports,
and documentation into a dated archive with SHA-256 checksums.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import sqlite3
import sys
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.database import get_db_path, checkpoint_and_clean_db

BACKUPS_DIR = ROOT_DIR / "backups"


def create_sqlite_consistent_backup(src_path: Path, dest_path: Path) -> None:
    """Uses SQLite's native backup API to create a bit-consistent copy of the database."""
    dest_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Checkpoint any WAL entries first
    checkpoint_and_clean_db(src_path)
    
    src_conn = sqlite3.connect(str(src_path), timeout=30.0)
    dest_conn = sqlite3.connect(str(dest_path), timeout=30.0)
    try:
        with dest_conn:
            src_conn.backup(dest_conn, pages=100)
    finally:
        dest_conn.close()
        src_conn.close()


def calculate_sha256(file_path: Path) -> str:
    """Computes SHA-256 checksum for a file."""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            hasher.update(chunk)
    return hasher.hexdigest()


def create_backup_package(output_dir: Optional[Path] = None) -> Path:
    """Creates a comprehensive, self-contained zip backup package."""
    dest_dir = output_dir or BACKUPS_DIR
    dest_dir.mkdir(parents=True, exist_ok=True)
    
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
    pkg_name = f"mehdi_legacy_backup_{timestamp}"
    zip_path = dest_dir / f"{pkg_name}.zip"
    
    temp_dir = dest_dir / f"tmp_{timestamp}"
    temp_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"[Backup] Initiating 3-2-1 backup creation: {zip_path.name}")
    
    try:
        # 1. Consistent SQLite backup
        db_src = get_db_path()
        if db_src.exists():
            temp_db = temp_dir / "database" / "archive.sqlite"
            print(f"  -> Creating consistent SQLite backup from {db_src.name}...")
            create_sqlite_consistent_backup(db_src, temp_db)
            
        # 2. Prepare recovery instructions inside the package
        recovery_readme = temp_dir / "RECOVERY-INSTRUCTIONS.txt"
        with open(recovery_readme, "w", encoding="utf-8") as f:
            f.write(
                f"MEHDI'S DIGITAL LEGACY - DISASTER RECOVERY ARCHIVE\n"
                f"Generated at: {datetime.now(timezone.utc).isoformat()}\n"
                f"Package: {pkg_name}\n"
                f"====================================================\n\n"
                f"This package contains a complete, self-contained preservation copy of:\n"
                f"1. archive.sqlite: Complete relational database with full-text search.\n"
                f"2. articles/: All articles in human-readable Markdown (.md) with YAML frontmatter.\n"
                f"3. exports/: Deterministic JSON data files.\n"
                f"4. media/: Downloaded article imagery and media files.\n"
                f"5. authors/: Author biographical profiles.\n"
                f"6. config/: Source endpoints and preservation policies.\n"
                f"7. DIGITAL-LEGACY.md & DIGITAL-LEGACY-BN.md: Bilingual preservation manuals.\n\n"
                f"HOW TO RESTORE:\n"
                f"- To extract: Unzip this file.\n"
                f"- To inspect database: Open database/archive.sqlite in DB Browser for SQLite.\n"
                f"- To read articles: Open any .md file in articles/ in any text editor.\n"
                f"- To rebuild database from Markdown: Run 'python scripts/restore.py --rebuild-database'\n"
                f"- To rebuild website: Run 'python scripts/restore.py --rebuild-website'\n"
            )
            
        # 3. Create Zip file
        print("  -> Bundling files into compressed archive...")
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
            # Add recovery readme
            zipf.write(recovery_readme, "RECOVERY-INSTRUCTIONS.txt")
            
            # Add backup SQLite DB
            if (temp_dir / "database" / "archive.sqlite").exists():
                zipf.write(temp_dir / "database" / "archive.sqlite", "database/archive.sqlite")
                
            # Add schema.sql
            schema_file = ROOT_DIR / "database" / "schema.sql"
            if schema_file.exists():
                zipf.write(schema_file, "database/schema.sql")
                
            # Add documentation files
            for doc_name in ["README.md", "LICENSE", "DIGITAL-LEGACY.md", "DIGITAL-LEGACY-BN.md", "CHANGELOG.md"]:
                doc_file = ROOT_DIR / doc_name
                if doc_file.exists():
                    zipf.write(doc_file, doc_name)
                    
            # Add config files
            config_dir = ROOT_DIR / "config"
            if config_dir.exists():
                for cf in config_dir.glob("*.json"):
                    zipf.write(cf, f"config/{cf.name}")
                    
            # Add authors
            authors_dir = ROOT_DIR / "authors"
            if authors_dir.exists():
                for af in authors_dir.glob("*.md"):
                    zipf.write(af, f"authors/{af.name}")
                    
            # Add exports
            exports_dir = ROOT_DIR / "exports"
            if exports_dir.exists():
                for ef in exports_dir.glob("*.json"):
                    zipf.write(ef, f"exports/{ef.name}")
                    
            # Add articles
            articles_dir = ROOT_DIR / "articles"
            if articles_dir.exists():
                for af in articles_dir.glob("**/*.md"):
                    rel = af.relative_to(ROOT_DIR)
                    zipf.write(af, str(rel))
                    
            # Add media
            media_dir = ROOT_DIR / "media"
            if media_dir.exists():
                for mf in media_dir.glob("**/*"):
                    if mf.is_file():
                        rel = mf.relative_to(ROOT_DIR)
                        zipf.write(mf, str(rel))

        # 4. Compute SHA-256 checksum
        checksum = calculate_sha256(zip_path)
        checksum_file = dest_dir / "checksums.sha256"
        with open(checksum_file, "a", encoding="utf-8") as cf:
            cf.write(f"{checksum}  {zip_path.name}\n")
            
        print(f"[Backup] Successfully generated: {zip_path.name}")
        print(f"  -> File Size: {zip_path.stat().st_size:,} bytes")
        print(f"  -> SHA-256: {checksum}")
        print(f"  -> Checksum recorded in: {checksum_file.name}")
        
        return zip_path
        
    finally:
        # Clean up temporary directory
        if temp_dir.exists():
            shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == "__main__":
    create_backup_package()
