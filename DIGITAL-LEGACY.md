# Mehdi's Digital Legacy: Master Preservation Manual
### *A Lifetime of Thoughts, Knowledge and Experiences, Preserved for Generations.*

---

## 1. Introduction: What Is This Project?

This repository is **Mehdi's Digital Legacy**, a permanent, autonomous, long-term personal digital archive created to preserve the lifetime writings, essays, tutorials, and research of **Mehdi Akram (এস এম মেহেদী আকরাম)**.

This is not a temporary backup or an ordinary dynamic blog. It is an independent digital monument designed to survive indefinitely. Even if:
- The author is no longer alive,
- The original hosting providers shut down,
- The domain registrations expire or are auctioned off,
- Content Management Systems (like WordPress) become obsolete,

This archive ensures that every single article, guide, and essay remains accessible, readable, searchable, and verifiable for future generations.

---

## 2. Who Created This Archive?

This archive was created by and for **Mehdi Akram** (also known online and professionally as **S M Mehdi Akram**, বাংলা: **এস এম মেহেদী আকরাম**).
- **Author Identity**: Technologist, Web Systems Engineer, Writer, and Founder from Bangladesh.
- **Biographical Profile**: Detailed in [authors/mehdi-akram.md](authors/mehdi-akram.md).
- **Primary Email**: `mehdi@shamokaldarpon.com`

---

## 3. Which Websites Are Preserved?

The archive aggregates and continuously preserves content from two distinct web publications:

1. **Royal Technologies**
   - **Primary Website**: [https://www.royaltechbd.com/](https://www.royaltechbd.com/)
   - **Focus**: Web hosting, server administration, domain name systems, internet infrastructure, business software, and enterprise solutions.
   - **Primary Language**: English (`en`) with occasional Bengali publications.

2. **সমকাল দর্পণ (Shamokal Darpon)**
   - **Primary Website**: [https://www.shamokaldarpon.com/](https://www.shamokaldarpon.com/)
   - **Focus**: Personal blog, Bengali technology tutorials, open-source advocacy, civil liberties in computing, automation, and reflections.
   - **Primary Language**: Bengali (`bn`).

Both websites remain logically separate in this archive. Every article retains its original website identity, original URL, WordPress post identifier, publication date, and author attribution.

---

## 4. How the Repository Is Structured

This repository is strictly organized to decouple storage, data, presentation, and automation:

- `articles/`: Individual Markdown files for every article. This is the **primary readable text asset**. Each article lives at `articles/{source}/{language}/{year}/{slug}.md`.
- `database/`: Contains `archive.sqlite`, the complete normalized relational database with full-text search capability.
- `exports/`: Machine-readable JSON files (`articles.json`, `categories.json`, `tags.json`, `manifest.json`).
- `media/`: Archived images downloaded from the source websites according to safe download policies.
- `website/`: A static website (HTML, CSS, JavaScript) that requires zero server software and can be viewed directly in any web browser or hosted via GitHub Pages.
- `scripts/`: Python command-line tools to sync, build, validate, back up, and restore the archive.
- `.github/workflows/`: Automated daily synchronization workflows that pull new posts every morning at 06:00 AM Bangladesh Time (00:00 UTC).

---

## 5. Non-Programmer Guide: How to Read the Content

You do not need to be a software developer or computer programmer to read the writings in this archive.

### Option A: Read Directly in Any Web Browser
1. Visit the published static website on GitHub Pages:
   `https://mehdiakram.github.io/mehdi-writing-archive/`
2. Or open the file `website/index.html` directly from your local computer into Google Chrome, Mozilla Firefox, Safari, or Microsoft Edge.
3. You can browse by site, search in English or Bengali, filter by categories, or view yearly timelines.

### Option B: Read the Plain Markdown Files
1. Navigate to the `articles/` directory on your computer or on GitHub.
2. Open any folder (for example, `articles/shamokaldarpon/bangla/2026/`).
3. Click on any `.md` file. It is plain human-readable text.
4. You can open and read these files with Notepad, TextEdit, VS Code, Obsidian, or any simple text editor.

### Option C: Inspect the SQLite Database
If you wish to run SQL queries or view the structured database:
1. Download a free program called **DB Browser for SQLite** (available at [https://sqlitebrowser.org/](https://sqlitebrowser.org/)).
2. Open `database/archive.sqlite`.
3. Click "Browse Data" and choose the `posts` table.
4. You can search, filter, and export the entire collection to Excel, CSV, or PDF.

---

## 6. How to Rebuild the Database and Website

If either the database or the website files ever become corrupted or lost, they can be regenerated automatically from the independent Markdown text files:

### Rebuilding the SQLite Database from Markdown Files:
Run this single command:
```bash
python scripts/restore.py --rebuild-database
```
This reads all Markdown files, extracts their YAML frontmatter, validates content integrity, and populates a brand-new `database/archive.sqlite` with full-text search indexes.

### Rebuilding the Website from the Database:
Run this command:
```bash
python scripts/build.py
```
This updates the static website data, generates the client-side search index (`website/data/search-index.json`), and refreshes the manifest.

---

## 7. How to Restore an Older Revision of an Article

The platform preserves historical revisions whenever an article is edited on the original WordPress sites.

1. To inspect revision history or restore an article:
```bash
python scripts/restore.py --article royaltechbd-4600 --revision 1
```
2. Restoring an older revision creates an auditable historical event and updates the active Markdown file and database entry without deleting historical records.

---

## 8. Automated Daily Synchronization

The repository is configured with a GitHub Actions workflow (`.github/workflows/daily-sync.yml`) that runs daily at **06:00 AM Bangladesh Time (UTC+6)**:
- Checks both source sites for newly published or modified articles.
- Calculates SHA-256 hashes of content to detect changes.
- Records revisions if existing articles were updated.
- Downloads new media safely.
- Updates Markdown files, SQLite database, JSON exports, and search index.
- Automatically commits and pushes changes back to the repository.

You can also trigger a sync manually anytime from the **GitHub Actions** tab by clicking "Run workflow".

---

## 9. 3-2-1 Disaster Recovery Strategy

To guarantee survival over decades, the archive adopts the industry-standard 3-2-1 backup principle:

- **Copy 1**: The primary GitHub repository (`mehdiakram/mehdi-writing-archive`).
- **Copy 2 (Cloud Backup)**: Automated zip backups created by `.github/workflows/backup.yml` stored as GitHub Releases and off-site cloud storage.
- **Copy 3 (Physical Cold Storage)**: An offline copy stored on an external hard drive, USB flash drive, or M-DISC optical media.

### Creating an Offline Backup Archive:
Run:
```bash
python scripts/backup.py
```
This produces a dated, self-contained zip file (e.g. `backups/mehdi_legacy_backup_20261112.zip`) accompanied by SHA-256 checksums and recovery instructions.

---

## 10. Handing Over to a Future Maintainer / Family Member

If the original creator is unable to maintain this repository, guardianship of this digital legacy should be transitioned as follows:

1. **Fork or Transfer Repository**:
   - A trusted family member, collaborator, or archivist can fork this repository on GitHub or request a repository transfer.
2. **Configure GitHub Pages**:
   - In GitHub Settings > Pages, select "Deploy from a branch" > `main` > `/website` (or root depending on setup).
3. **Updating Configuration**:
   - If new source domains or mirror sites are created, update `config/sources.json`.
4. **Offline Preservation**:
   - Keep a copy of the repository and the latest backup zip on an external storage drive.
   - The archive will continue to be readable offline even without the internet or GitHub.

---

## 11. Recovering Access to the GitHub Account

If access to the original GitHub account (`mehdiakram`) is lost:
1. GitHub accounts can be recovered via the official GitHub Account Recovery procedure using verified secondary email addresses and account recovery keys.
2. Because this repository is public, anyone may clone the entire repository (`git clone https://github.com/mehdiakram/mehdi-writing-archive.git`) at any time to preserve an exact, bit-for-bit mirror.
3. No secrets or private passwords are stored in this archive. Everything required to keep the archive running is completely self-contained within this codebase.

---

*Preserved with dedication for knowledge, truth, and future generations.*
