# Mehdi's Digital Legacy
### *A Lifetime of Thoughts, Knowledge and Experiences, Preserved for Generations.*

[![Daily Sync](https://github.com/mehdiakram/mehdi-writing-archive/actions/workflows/daily-sync.yml/badge.svg)](https://github.com/mehdiakram/mehdi-writing-archive/actions/workflows/daily-sync.yml)
[![Validation Suite](https://github.com/mehdiakram/mehdi-writing-archive/actions/workflows/validate.yml/badge.svg)](https://github.com/mehdiakram/mehdi-writing-archive/actions/workflows/validate.yml)
[![Pages Deployment](https://github.com/mehdiakram/mehdi-writing-archive/actions/workflows/deploy-pages.yml/badge.svg)](https://github.com/mehdiakram/mehdi-writing-archive/actions/workflows/deploy-pages.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python: 3.12+](https://img.shields.io/badge/Python-3.12%2B-green.svg)](pyproject.toml)

---

## 1. Overview & Preservation Mission

**Mehdi's Digital Legacy** is an independent, production-ready, long-term personal digital preservation platform designed to preserve the published writings, technical research, tutorials, and essays authored by **Mehdi Akram (এস এম মেহেদী আকরাম)**.

The archive ingests and archives content from two active WordPress websites:
1. **Royal Technologies** (`https://www.royaltechbd.com/`) - Technology, hosting, systems, web solutions, and software engineering.
2. **সমকাল দর্পণ (Shamokal Darpon)** (`https://www.shamokaldarpon.com/`) - Personal essays, Bengali technology guides, open-source discussions, civic tech, and reflections.

### Why This Exists (The Digital Preservation Imperative)
Digital publishing on the web is notoriously fragile. Domain names expire, hosting bills lapse, Content Management Systems (CMS) evolve into incompatibility, and server environments shut down. 

This platform operates on the principle of **radical digital independence**:
- **Zero Server Overhead**: The public archive runs entirely as static HTML/CSS/JS hosted on GitHub Pages. No PHP, MySQL, or cloud database servers are required to view the archive.
- **Durable Formats**: Every single article is preserved simultaneously in three formats:
  - An **ACID SQLite 3** relational database with full-text search (FTS5).
  - Clean, human-readable **Markdown (.md)** files with YAML frontmatter.
  - Machine-readable, deterministic **JSON exports**.
- **Self-Healing Reconstruction**: If the database is lost, it can be 100% reconstructed solely from the Markdown files. If the Markdown files are lost, they can be regenerated from SQLite.
- **Multilingual Support**: First-class handling of Bengali (বাংলা) and English text, including character encoding, slugification, and search tokenization.

---

## 2. Architecture & Repository Structure

```
mehdi-writing-archive/
├── README.md                   # Complete architectural guide & setup manual
├── LICENSE                     # MIT Software License + CC BY 4.0 Content Notice
├── CONTRIBUTING.md              # Community contribution guidelines
├── DIGITAL-LEGACY.md           # Master English legacy preservation manual
├── DIGITAL-LEGACY-BN.md        # Master Bengali legacy preservation manual (ডিজিটাল লিগ্যাসি গাইড)
├── CHANGELOG.md                # Version history
├── requirements.txt            # Python dependencies
├── pyproject.toml              # Build & project configuration
│
├── .github/workflows/          # Automated GitHub Actions
│   ├── daily-sync.yml          # Daily synchronization at 06:00 AM BST (00:00 UTC)
│   ├── deploy-pages.yml        # Continuous deployment to GitHub Pages
│   ├── validate.yml            # CI test runner & integrity validator
│   └── backup.yml              # 3-2-1 backup archive generator
│
├── config/                     # Configuration files
│   ├── sources.json            # WordPress REST API source endpoints & languages
│   ├── settings.json           # Archive engine runtime parameters
│   └── media-policy.json       # SSRF protection & image download rules
│
├── database/                   # Relational storage
│   ├── archive.sqlite          # Primary SQLite 3 archive database (with FTS5)
│   ├── schema.sql              # Normalized schema definition
│   └── migrations/             # Timestamped migration scripts
│
├── articles/                   # Human-readable Markdown repository
│   ├── royaltechbd/            # Articles from Royal Technologies
│   │   ├── bangla/             # Bengali articles categorized by year
│   │   └── english/            # English articles categorized by year
│   └── shamokaldarpon/         # Articles from সমকাল দর্পণ
│       ├── bangla/
│       └── english/
│
├── authors/                    # Author biographical profiles
│   └── mehdi-akram.md
│
├── media/                      # Locally archived media & images
│   ├── royaltechbd/
│   └── shamokaldarpon/
│
├── exports/                    # Deterministic, machine-readable exports
│   ├── articles.json
│   ├── categories.json
│   ├── tags.json
│   ├── authors.json
│   └── manifest.json
│
├── scripts/                    # Preservation & automation engine
│   ├── sync.py                 # Full and incremental synchronizer
│   ├── wordpress.py            # Resilient WordPress REST API client
│   ├── database.py             # Database connection, transactions, & WAL handling
│   ├── migrations.py           # Database migration runner
│   ├── markdown_export.py      # HTML to Markdown converter & frontmatter generator
│   ├── json_export.py          # Deterministic JSON export generator
│   ├── media.py                # Safe media downloader & deduplicator
│   ├── search_index.py         # Static full-text search index builder
│   ├── validate.py             # Data integrity & validation suite
│   ├── build.py                # Static website builder
│   ├── backup.py               # 3-2-1 disaster recovery backup packager
│   ├── restore.py              # Database & website recovery toolkit
│   └── report.py               # Archive status & audit reporter
│
├── tests/                      # Automated pytest test suite
│   ├── test_database.py
│   ├── test_sync.py
│   ├── test_markdown.py
│   ├── test_media.py
│   ├── test_restore.py
│   └── fixtures/               # Mock data fixtures for tests
│
└── website/                    # Static archive website (GitHub Pages root)
    ├── index.html              # Archive homepage
    ├── article.html            # Article reading experience
    ├── archive.html            # Timeline & chronological archive
    ├── categories.html         # Categories browser
    ├── tags.html               # Tag cloud & lists
    ├── search.html             # Client-side full-text search
    ├── author.html             # Author biography
    ├── about.html              # Preservation philosophy & project information
    ├── downloads.html          # Bulk download portal (SQLite, JSON, Markdown)
    ├── 404.html                # Friendly fallback page
    ├── sitemap.xml             # Search engine sitemap
    ├── robots.txt              # Crawler permissions
    └── assets/                 # Lightweight CSS and Vanilla JS
```

---

## 3. Quick Start & CLI Usage

### Prerequisites
- Python 3.12 or higher
- Git

### Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/mehdiakram/mehdi-writing-archive.git
cd mehdi-writing-archive
pip install -r requirements.txt
```

### Command Line Interface

| Task | Command | Description |
| :--- | :--- | :--- |
| **Initial Migration** | `python scripts/migrations.py` | Applies database schema & creates tables |
| **Full Historical Import** | `python scripts/sync.py --mode full` | Discovers & downloads all articles from both sites |
| **Single Source Import** | `python scripts/sync.py --source royaltechbd` | Imports articles exclusively from Royal Technologies |
| **Incremental Sync** | `python scripts/sync.py --mode incremental` | Checks for updates with a 48h overlap window |
| **Validate Archive** | `python scripts/validate.py` | Verifies SQLite integrity, JSON schemas, & Markdown |
| **Build Website** | `python scripts/build.py` | Compiles static search indexes & ready-to-host website |
| **Create Backup** | `python scripts/backup.py` | Packages SQLite, Markdown, JSON & Media into a dated zip |
| **Rebuild Database** | `python scripts/restore.py --rebuild-database` | Rebuilds SQLite entirely from Markdown files |
| **Rebuild Website** | `python scripts/restore.py --rebuild-website` | Regenerates all website data from the SQLite database |
| **Restore Revision** | `python scripts/restore.py --article royaltechbd-4600 --revision 1` | Rolls back an article to a prior revision |
| **Status Report** | `python scripts/report.py` | Displays live summary of archive stats & health |

---

## 4. Source Websites & Live Status

| Website | Domain | Language | Total Posts | API Endpoint |
| :--- | :--- | :--- | :--- | :--- |
| **Royal Technologies** | `www.royaltechbd.com` | English (`en`) / Bangla | 162 | `https://www.royaltechbd.com/wp-json/wp/v2` |
| **সমকাল দর্পণ** | `www.shamokaldarpon.com` | Bangla (`bn`) | 1,110 | `https://www.shamokaldarpon.com/wp-json/wp/v2` |

---

## 5. 3-2-1 Backup Strategy

Preservation relies on geographic and infrastructural redundancy:
1. **Copy 1 (Active Production)**: Public GitHub repository (`mehdiakram/mehdi-writing-archive`).
2. **Copy 2 (Automated Cloud Artifacts)**: GitHub Releases & encrypted remote object store triggered by `.github/workflows/backup.yml`.
3. **Copy 3 (Cold Storage)**: Offline hard drive or USB drive updated periodically using `python scripts/backup.py`.

---

## 6. Documentation Links

- **English Digital Legacy Guide**: [DIGITAL-LEGACY.md](DIGITAL-LEGACY.md)
- **Bengali Digital Legacy Guide**: [DIGITAL-LEGACY-BN.md](DIGITAL-LEGACY-BN.md)
- **Author Profile**: [authors/mehdi-akram.md](authors/mehdi-akram.md)

---

## 7. License

- Software & Tools: [MIT License](LICENSE)
- Articles & Content: [Creative Commons Attribution 4.0 International (CC BY 4.0)](LICENSE)
