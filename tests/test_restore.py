"""Unit tests for backup packaging, integrity verification, and database reconstruction."""

import json
from pathlib import Path

from scripts.backup import create_backup_package, calculate_sha256
from scripts.database import get_db, init_database
from scripts.markdown_export import save_article_markdown
from scripts.restore import (
    rebuild_database_from_markdown,
    restore_article_revision,
    verify_backup,
)


def test_rebuild_database_from_markdown_files(tmp_path: Path):
    """Test that SQLite database can be completely reconstructed from raw Markdown files."""
    articles_dir = tmp_path / "articles" / "shamokaldarpon" / "bangla" / "2026"
    articles_dir.mkdir(parents=True, exist_ok=True)
    
    meta = {
        "archive_id": "shamokaldarpon-6524",
        "source": "shamokaldarpon",
        "wordpress_id": 6524,
        "title": "বাংলাদেশের জরুরি হেল্পলাইন নম্বর",
        "slug": "toll-free-number-bangladesh",
        "language": "bn",
        "published_at": "2026-11-05T11:59:00",
        "categories": ["জরুরি সেবা"],
        "tags": ["টোল ফ্রি"],
        "original_url": "https://www.shamokaldarpon.com/6524",
        "author": "মেহেদী আকরাম",
        "content_hash": "hash123"
    }
    body = "জরুরি সেবা পাওয়ার জন্য সরকারি নম্বর তালিকা।"
    
    md_file = articles_dir / "toll-free-number-bangladesh.md"
    save_article_markdown(md_file, meta, body)
    
    target_db = tmp_path / "rebuilt.sqlite"
    
    import unittest.mock as mock
    with mock.patch("scripts.restore.ROOT_DIR", tmp_path), \
         mock.patch("scripts.restore.get_db_path", return_value=target_db):
        
        count = rebuild_database_from_markdown(target_db)
        assert count == 1
        
        with get_db(target_db) as conn:
            post = conn.execute("SELECT * FROM posts WHERE archive_id = 'shamokaldarpon-6524'").fetchone()
            assert post is not None
            assert post["title"] == "বাংলাদেশের জরুরি হেল্পলাইন নম্বর"
            assert post["language"] == "bn"


def test_backup_and_verify_package(tmp_path: Path):
    """Test creating a backup package and verifying its checksum and zip integrity."""
    backup_dir = tmp_path / "backups"
    
    import unittest.mock as mock
    with mock.patch("scripts.backup.ROOT_DIR", tmp_path), \
         mock.patch("scripts.backup.BACKUPS_DIR", backup_dir):
        
        # Initialize a test db
        db_file = tmp_path / "database" / "archive.sqlite"
        init_database(db_file)
        
        # Create package
        pkg_path = create_backup_package(output_dir=backup_dir)
        assert pkg_path.exists()
        assert pkg_path.suffix == ".zip"
        
        # Verify package
        assert verify_backup(pkg_path) is True
