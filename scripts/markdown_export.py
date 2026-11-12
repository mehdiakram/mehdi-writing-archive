"""Markdown Exporter & Parser for Mehdi's Digital Legacy.

Converts WordPress HTML content to clean Markdown, generates YAML frontmatter,
and supports bidirectional parsing to rebuild the database from Markdown.
"""

from __future__ import annotations

import os
import re
import unicodedata
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import markdownify
import yaml
from bs4 import BeautifulSoup

ROOT_DIR = Path(__file__).resolve().parent.parent
ARTICLES_DIR = ROOT_DIR / "articles"

# Regex to detect Bengali Unicode characters
BENGALI_CHAR_PATTERN = re.compile(r"[\u0980-\u09FF]")


def detect_language(title: str, text: str, default_language: str = "en") -> str:
    """Detects whether text is primarily Bengali ('bn') or English ('en')."""
    sample = f"{title} {text[:1000]}"
    bengali_chars = len(BENGALI_CHAR_PATTERN.findall(sample))
    # If there are 10 or more Bengali characters, it's Bengali
    if bengali_chars >= 10:
        return "bn"
    # If the default is Bengali and there are any Bengali characters
    if default_language == "bn" and bengali_chars > 0:
        return "bn"
    return default_language


def sanitize_slug(slug: str) -> str:
    """Normalizes and cleans a slug for cross-platform filesystem safety."""
    if not slug:
        return "untitled"
    # Unquote URL encodings if present
    import urllib.parse
    slug = urllib.parse.unquote(slug)
    # Remove filesystem prohibited characters and quotes
    cleaned = re.sub(r'[\'\"`’‘<>:"/\\|?*\x00-\x1f]', "", slug)
    cleaned = re.sub(r"\s+", "-", cleaned).strip("-.")
    return cleaned.lower() if cleaned else "untitled"


def html_to_clean_markdown(html_content: str) -> str:
    """Converts WordPress HTML into standardized Markdown while preserving structure."""
    if not html_content:
        return ""
        
    soup = BeautifulSoup(html_content, "html.parser")
    
    # Convert iframes to visible archival reference links rather than silently dropping
    for iframe in soup.find_all("iframe"):
        src = iframe.get("src", "")
        if src:
            iframe.replace_with(f"\n\n[Embedded External Content: {src}]\n\n")
        else:
            iframe.decompose()

    # Remove script, style, and noscript tags for safety
    for element in soup(["script", "style", "noscript"]):
        element.decompose()
        
    cleaned_html = str(soup)
    
    # Convert HTML to Markdown
    md = markdownify.markdownify(
        cleaned_html,
        heading_style=markdownify.ATX,
        bullets="-",
        strip=["script", "style"]
    )
    
    # Clean up excessive blank lines
    md = re.sub(r"\n{3,}", "\n\n", md)
    return md.strip()


def format_yaml_frontmatter(metadata: Dict[str, Any]) -> str:
    """Serializes metadata dict into valid YAML frontmatter."""
    yaml_text = yaml.safe_dump(
        metadata,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False
    )
    return f"---\n{yaml_text}---\n\n"


def parse_markdown_file(file_path: Path | str) -> Tuple[Dict[str, Any], str]:
    """Parses a Markdown file into frontmatter metadata and body text."""
    path = Path(file_path)
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()
        
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            raw_frontmatter = parts[1]
            body = parts[2].lstrip()
            metadata = yaml.safe_load(raw_frontmatter) or {}
            return metadata, body
            
    return {}, content


def determine_article_path(
    source_key: str,
    language: str,
    published_at: str,
    slug: str,
    wp_post_id: int,
    base_dir: Optional[Path] = None
) -> Path:
    """Determines the canonical file path: articles/{source}/{language}/{year}/{slug}.md."""
    base = base_dir or ARTICLES_DIR
    lang_folder = "bangla" if language == "bn" else "english"
    
    # Parse year from published_at (e.g. 2026-11-08)
    year = "unknown"
    if published_at:
        try:
            year = str(datetime.fromisoformat(published_at.replace("Z", "+00:00")).year)
        except Exception:
            match = re.match(r"^(\d{4})", published_at)
            if match:
                year = match.group(1)
                
    clean_slug = sanitize_slug(slug)
    
    dir_path = base / source_key / lang_folder / year
    dir_path.mkdir(parents=True, exist_ok=True)
    
    candidate = dir_path / f"{clean_slug}.md"
    
    # If collision occurs with an article of a different ID, append post ID
    if candidate.exists():
        try:
            meta, _ = parse_markdown_file(candidate)
            existing_wp_id = meta.get("wordpress_id")
            if existing_wp_id and existing_wp_id != wp_post_id:
                candidate = dir_path / f"{clean_slug}-{wp_post_id}.md"
        except Exception:
            candidate = dir_path / f"{clean_slug}-{wp_post_id}.md"
            
    return candidate


def save_article_markdown(
    file_path: Path,
    metadata: Dict[str, Any],
    markdown_body: str
) -> None:
    """Atomically writes article metadata and Markdown body to disk in UTF-8."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    frontmatter = format_yaml_frontmatter(metadata)
    full_content = frontmatter + markdown_body + "\n"
    
    tmp_path = file_path.with_suffix(".tmp")
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(full_content)
        
    tmp_path.replace(file_path)
