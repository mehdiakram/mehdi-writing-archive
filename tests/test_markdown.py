"""Unit tests for Markdown generation, language detection, and parsing."""

from pathlib import Path
from scripts.markdown_export import (
    detect_language,
    html_to_clean_markdown,
    format_yaml_frontmatter,
    parse_markdown_file,
    determine_article_path,
    save_article_markdown,
    sanitize_slug
)


def test_html_to_clean_markdown():
    html = """
    <h2>Introduction</h2>
    <p>This is a <strong>test</strong> article with a <a href="https://example.com">link</a>.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
    </ul>
    <blockquote>Quote from author</blockquote>
    <script>alert('hack');</script>
    """
    md = html_to_clean_markdown(html)
    assert "## Introduction" in md
    assert "**test**" in md
    assert "[link](https://example.com)" in md
    assert "- Item 1" in md
    assert "> Quote from author" in md
    assert "alert('hack')" not in md  # Scripts stripped


def test_language_detection():
    # English title & content
    assert detect_language("How to Install Docker on Linux", "Step by step instructions") == "en"
    
    # Bengali title & content
    assert detect_language("বাংলাদেশের জরুরি হেল্পলাইন নম্বর", "জরুরি সেবা পাওয়ার জন্য সরকারি নম্বর") == "bn"
    
    # Mixed content with default fallback
    assert detect_language("Tech Update", "No bengali characters here", default_language="en") == "en"


def test_markdown_frontmatter_bidirectional(tmp_path: Path):
    meta = {
        "archive_id": "royaltechbd-4600",
        "source": "royaltechbd",
        "wordpress_id": 4600,
        "title": "Test Title",
        "slug": "test-title",
        "language": "en",
        "published_at": "2026-11-08T12:00:00",
        "categories": ["Tech", "Hosting"],
        "content_hash": "abc123hash"
    }
    body = "## Content Header\n\nThis is the markdown content body."
    
    test_file = tmp_path / "test-article.md"
    save_article_markdown(test_file, meta, body)
    
    # Read back and verify
    read_meta, read_body = parse_markdown_file(test_file)
    assert read_meta["archive_id"] == "royaltechbd-4600"
    assert read_meta["title"] == "Test Title"
    assert read_meta["categories"] == ["Tech", "Hosting"]
    assert "## Content Header" in read_body


def test_sanitize_slug():
    assert sanitize_slug("Social Media: A Manager's Guide?") == "social-media-a-managers-guide"
    assert sanitize_slug("বাংলা স্লাগ টেস্ট") == "বাংলা-স্লাগ-টেস্ট"
    assert sanitize_slug("") == "untitled"


def test_determine_article_path(tmp_path: Path):
    path = determine_article_path(
        source_key="royaltechbd",
        language="en",
        published_at="2026-11-08T12:00:00",
        slug="cloud-computing",
        wp_post_id=500,
        base_dir=tmp_path
    )
    assert "royaltechbd" in str(path)
    assert "english" in str(path)
    assert "2026" in str(path)
    assert path.name == "cloud-computing.md"
