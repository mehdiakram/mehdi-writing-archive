"""Unit tests for SQLite database engine and FTS5 search."""

import sqlite3
import pytest
from pathlib import Path

from scripts.database import (
    create_connection,
    get_db,
    init_database,
    compute_content_hash,
    utc_now_iso
)
from scripts.migrations import run_migrations


@pytest.fixture
def temp_db(tmp_path: Path):
    """Provides a temporary test database path initialized with schema."""
    db_file = tmp_path / "test_archive.sqlite"
    init_database(db_file)
    return db_file


def test_database_initialization(temp_db: Path):
    """Test that all required archive tables and virtual tables are created."""
    with get_db(temp_db) as conn:
        tables = [
            r["name"] for r in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table'"
            ).fetchall()
        ]
        
        required_tables = [
            "sites", "authors", "posts", "categories", "tags",
            "post_categories", "post_tags", "media", "post_media",
            "post_revisions", "sync_state", "sync_logs",
            "schema_migrations", "posts_fts"
        ]
        
        for req in required_tables:
            assert req in tables, f"Missing required table: {req}"


def test_foreign_key_constraints(temp_db: Path):
    """Test that foreign key violations are rejected."""
    with get_db(temp_db) as conn:
        # Inserting a post with non-existent site_id must raise IntegrityError
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                """
                INSERT INTO posts (
                    archive_id, site_id, wp_post_id, title, slug, language,
                    content_html, content_markdown, excerpt, status, post_type,
                    original_url, published_at, modified_at, content_hash,
                    markdown_path, archived_at, created_at, updated_at
                ) VALUES (
                    'fake-999', 999999, 1, 'Fake', 'fake', 'en',
                    '', '', '', 'publish', 'post',
                    'https://fake.url', '2026-01-01', '2026-01-01', 'hash',
                    'articles/fake.md', '2026-01-01', '2026-01-01', '2026-01-01'
                )
                """
            )


def test_unique_constraint_post_deduplication(temp_db: Path):
    """Test that (site_id, wp_post_id) duplicate insertions are prevented."""
    now = utc_now_iso()
    with get_db(temp_db) as conn:
        site_id = conn.execute("SELECT id FROM sites LIMIT 1").fetchone()["id"]
        
        # First insert
        conn.execute(
            """
            INSERT INTO posts (
                archive_id, site_id, wp_post_id, title, slug, language,
                content_html, content_markdown, excerpt, status, post_type,
                original_url, published_at, modified_at, content_hash,
                markdown_path, archived_at, created_at, updated_at
            ) VALUES (
                'test-1', ?, 100, 'Test 1', 'test-1', 'en',
                '', '', '', 'publish', 'post',
                'https://test.url/1', ?, ?, 'hash1',
                'articles/test-1.md', ?, ?, ?
            )
            """,
            (site_id, now, now, now, now, now)
        )
        
        # Second insert with same site_id and wp_post_id must fail
        with pytest.raises(sqlite3.IntegrityError):
            conn.execute(
                """
                INSERT INTO posts (
                    archive_id, site_id, wp_post_id, title, slug, language,
                    content_html, content_markdown, excerpt, status, post_type,
                    original_url, published_at, modified_at, content_hash,
                    markdown_path, archived_at, created_at, updated_at
                ) VALUES (
                    'test-2', ?, 100, 'Test 2', 'test-2', 'en',
                    '', '', '', 'publish', 'post',
                    'https://test.url/2', ?, ?, 'hash2',
                    'articles/test-2.md', ?, ?, ?
                )
                """,
                (site_id, now, now, now, now, now)
            )


def test_fts5_bengali_and_english_search(temp_db: Path):
    """Test FTS5 search with both Bengali and English keywords."""
    now = utc_now_iso()
    with get_db(temp_db) as conn:
        site_id = conn.execute("SELECT id FROM sites LIMIT 1").fetchone()["id"]
        
        # Insert English post
        conn.execute(
            """
            INSERT INTO posts (
                archive_id, site_id, wp_post_id, title, slug, language,
                content_html, content_markdown, excerpt, status, post_type,
                original_url, published_at, modified_at, content_hash,
                markdown_path, archived_at, created_at, updated_at
            ) VALUES (
                'royaltechbd-1', ?, 101, 'Kubernetes Cloud Clustering', 'kubernetes', 'en',
                '<p>Docker and container orchestration.</p>',
                'Docker and container orchestration guides.',
                'Container orchestration.', 'publish', 'post',
                'https://royal.url/k8s', ?, ?, 'hash_en',
                'articles/k8s.md', ?, ?, ?
            )
            """,
            (site_id, now, now, now, now, now)
        )
        
        # Insert Bengali post
        conn.execute(
            """
            INSERT INTO posts (
                archive_id, site_id, wp_post_id, title, slug, language,
                content_html, content_markdown, excerpt, status, post_type,
                original_url, published_at, modified_at, content_hash,
                markdown_path, archived_at, created_at, updated_at
            ) VALUES (
                'shamokaldarpon-1', ?, 201, 'বাংলা ভাষার ডিজিটাল মহাফেজখানা', 'bangla-archive', 'bn',
                '<p>চিরস্থায়ী ডিজিটাল সংরক্ষণাগার নির্মাণ গাইড।</p>',
                'চিরস্থায়ী ডিজিটাল সংরক্ষণাগার নির্মাণ গাইড।',
                'ডিজিটাল সংরক্ষণ।', 'publish', 'post',
                'https://shamokal.url/archive', ?, ?, 'hash_bn',
                'articles/archive.md', ?, ?, ?
            )
            """,
            (site_id, now, now, now, now, now)
        )
        
        # Test English FTS match
        en_matches = conn.execute(
            "SELECT archive_id FROM posts_fts WHERE posts_fts MATCH 'Kubernetes'"
        ).fetchall()
        assert len(en_matches) == 1
        assert en_matches[0]["archive_id"] == "royaltechbd-1"
        
        # Test Bengali FTS match
        bn_matches = conn.execute(
            "SELECT archive_id FROM posts_fts WHERE posts_fts MATCH 'মহাফেজখানা'"
        ).fetchall()
        assert len(bn_matches) == 1
        assert bn_matches[0]["archive_id"] == "shamokaldarpon-1"


def test_migrations_runner(tmp_path: Path):
    """Test that migrations can be run idempotently."""
    db_file = tmp_path / "migration_test.sqlite"
    count1 = run_migrations(db_file)
    assert count1 >= 0
    # Second run should apply 0
    count2 = run_migrations(db_file)
    assert count2 == 0
