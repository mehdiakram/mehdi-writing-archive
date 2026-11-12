"""Unit tests for WordPress synchronization engine and revision tracking."""

import json
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest
from scripts.database import get_db, init_database
from scripts.sync import ArchiveSynchronizer

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


@pytest.fixture
def mock_fixtures():
    with open(FIXTURES_DIR / "royaltechbd_posts.json", "r", encoding="utf-8") as f:
        royal_posts = json.load(f)
    with open(FIXTURES_DIR / "shamokaldarpon_posts.json", "r", encoding="utf-8") as f:
        shamokal_posts = json.load(f)
    with open(FIXTURES_DIR / "categories.json", "r", encoding="utf-8") as f:
        cats = json.load(f)
    with open(FIXTURES_DIR / "tags.json", "r", encoding="utf-8") as f:
        tags = json.load(f)
    return {
        "royal": royal_posts,
        "shamokal": shamokal_posts,
        "categories": cats,
        "tags": tags,
    }


def test_mocked_sync_and_revision_generation(tmp_path: Path, mock_fixtures):
    """Tests full synchronization and subsequent incremental revision creation."""
    db_file = tmp_path / "test_sync.sqlite"
    articles_dir = tmp_path / "articles"
    exports_dir = tmp_path / "exports"
    
    with patch("scripts.database.get_db_path", return_value=db_file), \
         patch("scripts.sync.ROOT_DIR", tmp_path), \
         patch("scripts.markdown_export.ARTICLES_DIR", articles_dir), \
         patch("scripts.json_export.EXPORTS_DIR", exports_dir):
        
        init_database(db_file)
        syncer = ArchiveSynchronizer(mode="full")
        
        # Mock WordPress API methods
        with patch("scripts.sync.WordPressAPIClient.get_users", return_value=[{"id": 2, "name": "Mehdi Akram", "slug": "mehdi"}]), \
             patch("scripts.sync.WordPressAPIClient.get_categories", return_value=mock_fixtures["categories"]), \
             patch("scripts.sync.WordPressAPIClient.get_tags", return_value=mock_fixtures["tags"]), \
             patch("scripts.sync.WordPressAPIClient.iterate_all_posts", return_value=iter(mock_fixtures["royal"])):
            
            # 1. Run initial sync for royaltechbd
            source_conf = {
                "key": "royaltechbd",
                "name": "Royal Technologies",
                "domain": "www.royaltechbd.com",
                "base_url": "https://www.royaltechbd.com",
                "api_url": "https://www.royaltechbd.com/wp-json/wp/v2",
                "default_language": "en"
            }
            stats = syncer.sync_single_source(source_conf)
            assert stats["posts_created"] == 2
            assert stats["posts_updated"] == 0
            
            with get_db(db_file) as conn:
                posts_count = conn.execute("SELECT count(*) as c FROM posts").fetchone()["c"]
                assert posts_count == 2
                
            # 2. Modify one post in the fixture and run incremental sync
            modified_fixture = [dict(mock_fixtures["royal"][0])]
            modified_fixture[0]["title"] = {"rendered": "Updated Title for Social Media Manager"}
            modified_fixture[0]["modified"] = "2026-11-10T15:00:00"
            
            syncer.mode = "incremental"
            with patch("scripts.sync.WordPressAPIClient.iterate_all_posts", return_value=iter(modified_fixture)):
                stats_inc = syncer.sync_single_source(source_conf)
                assert stats_inc["posts_updated"] == 1
                assert stats_inc["posts_created"] == 0
                
            # Verify revision recorded in post_revisions
            with get_db(db_file) as conn:
                rev_row = conn.execute("SELECT count(*) as c FROM post_revisions").fetchone()
                assert rev_row["c"] == 1
                
                updated_post = conn.execute(
                    "SELECT title FROM posts WHERE archive_id = 'royaltechbd-4600'"
                ).fetchone()
                assert updated_post["title"] == "Updated Title for Social Media Manager"
