# Changelog

All notable changes to **Mehdi's Digital Legacy** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-11-12

### Added
- **Preservation Architecture**: Complete digital preservation framework for Royal Technologies and সমকাল দর্পণ (Shamokal Darpon).
- **SQLite 3 Engine**: Normalized schema with FTS5 unicode61 full-text search, WAL mode support, foreign keys, and migration tracking.
- **REST API Synchronizer**: Robust WordPress REST API collector with retry backoff, pagination handling, and incremental sync overlap window.
- **Markdown Archive**: Individual UTF-8 Markdown export for every article with YAML frontmatter located at `articles/{source}/{language}/{year}/{slug}.md`.
- **Media Preservation**: Safety-controlled image archiver with SSRF protection, MIME validation, and SHA-256 deduplication.
- **Article Revision Tracking**: Independent versioning of modified articles with rollback CLI support (`python scripts/restore.py --article <id> --revision <rev>`).
- **Deterministic JSON Exports**: `articles.json`, `categories.json`, `tags.json`, `authors.json`, and `manifest.json`.
- **Static Reader Website**: Serverless editorial website for reading, browsing, and searching articles on GitHub Pages.
- **Multilingual Search**: Client-side full-text search supporting both Bengali (বাংলা) and English content.
- **3-2-1 Backup Strategy**: Comprehensive backup generator and disaster recovery toolkit to rebuild the database and website from raw text.
- **GitHub Actions Automation**: Workflows for daily synchronization (06:00 AM BST), GitHub Pages deployment, integrity validation, and backup generation.
- **Bilingual Legacy Guides**: Comprehensive documentation in English (`DIGITAL-LEGACY.md`) and Bengali (`DIGITAL-LEGACY-BN.md`).
