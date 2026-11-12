-- Migration 001: Initial Archive Schema
-- Created: 2026-11-12

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS sites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    key TEXT NOT NULL UNIQUE,
    name TEXT NOT NULL,
    domain TEXT NOT NULL,
    base_url TEXT NOT NULL,
    api_url TEXT NOT NULL,
    default_language TEXT NOT NULL DEFAULT 'en',
    enabled INTEGER NOT NULL DEFAULT 1,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER NOT NULL,
    wp_author_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    slug TEXT NOT NULL,
    email TEXT,
    url TEXT,
    description TEXT,
    avatar_url TEXT,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    UNIQUE (site_id, wp_author_id)
);

CREATE TABLE IF NOT EXISTS categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER NOT NULL,
    wp_category_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    slug TEXT NOT NULL,
    description TEXT,
    parent_id INTEGER DEFAULT 0,
    count INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    UNIQUE (site_id, wp_category_id)
);

CREATE TABLE IF NOT EXISTS tags (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER NOT NULL,
    wp_tag_id INTEGER NOT NULL,
    name TEXT NOT NULL,
    slug TEXT NOT NULL,
    description TEXT,
    count INTEGER DEFAULT 0,
    created_at TEXT NOT NULL,
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    UNIQUE (site_id, wp_tag_id)
);

CREATE TABLE IF NOT EXISTS media (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER NOT NULL,
    wp_media_id INTEGER,
    original_url TEXT NOT NULL,
    local_path TEXT,
    file_name TEXT,
    mime_type TEXT,
    file_size INTEGER DEFAULT 0,
    sha256_hash TEXT,
    width INTEGER,
    height INTEGER,
    alt_text TEXT,
    caption TEXT,
    download_status TEXT NOT NULL DEFAULT 'pending',
    downloaded_at TEXT,
    error_message TEXT,
    created_at TEXT NOT NULL,
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    UNIQUE (site_id, wp_media_id)
);

CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    archive_id TEXT NOT NULL UNIQUE,
    site_id INTEGER NOT NULL,
    wp_post_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    slug TEXT NOT NULL,
    language TEXT NOT NULL DEFAULT 'en',
    content_html TEXT NOT NULL,
    content_markdown TEXT NOT NULL,
    excerpt TEXT,
    status TEXT NOT NULL DEFAULT 'publish',
    post_type TEXT NOT NULL DEFAULT 'post',
    original_url TEXT NOT NULL,
    published_at TEXT NOT NULL,
    published_at_gmt TEXT,
    modified_at TEXT NOT NULL,
    modified_at_gmt TEXT,
    author_id INTEGER,
    featured_media_id INTEGER,
    content_hash TEXT NOT NULL,
    markdown_path TEXT NOT NULL,
    is_deleted INTEGER NOT NULL DEFAULT 0,
    archived_at TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES authors(id) ON DELETE SET NULL,
    FOREIGN KEY (featured_media_id) REFERENCES media(id) ON DELETE SET NULL,
    UNIQUE (site_id, wp_post_id)
);

CREATE TABLE IF NOT EXISTS post_categories (
    post_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    PRIMARY KEY (post_id, category_id),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS post_tags (
    post_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS post_media (
    post_id INTEGER NOT NULL,
    media_id INTEGER NOT NULL,
    is_featured INTEGER NOT NULL DEFAULT 0,
    PRIMARY KEY (post_id, media_id),
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE,
    FOREIGN KEY (media_id) REFERENCES media(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS post_revisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    post_id INTEGER NOT NULL,
    revision_number INTEGER NOT NULL,
    title TEXT NOT NULL,
    content_html TEXT NOT NULL,
    content_markdown TEXT NOT NULL,
    excerpt TEXT,
    modified_at TEXT NOT NULL,
    modified_at_gmt TEXT,
    content_hash TEXT NOT NULL,
    change_summary TEXT,
    recorded_at TEXT NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sync_state (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER NOT NULL UNIQUE,
    last_sync_at TEXT,
    last_post_modified_at TEXT,
    total_synced_posts INTEGER DEFAULT 0,
    sync_status TEXT NOT NULL DEFAULT 'idle',
    error_message TEXT,
    updated_at TEXT NOT NULL,
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS sync_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    site_id INTEGER,
    mode TEXT NOT NULL,
    started_at TEXT NOT NULL,
    finished_at TEXT,
    status TEXT NOT NULL,
    posts_created INTEGER DEFAULT 0,
    posts_updated INTEGER DEFAULT 0,
    posts_unchanged INTEGER DEFAULT 0,
    media_downloaded INTEGER DEFAULT 0,
    errors_count INTEGER DEFAULT 0,
    details_json TEXT,
    FOREIGN KEY (site_id) REFERENCES sites(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS schema_migrations (
    version INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    applied_at TEXT NOT NULL
);

CREATE INDEX IF NOT EXISTS idx_posts_site_id ON posts(site_id);
CREATE INDEX IF NOT EXISTS idx_posts_archive_id ON posts(archive_id);
CREATE INDEX IF NOT EXISTS idx_posts_slug ON posts(slug);
CREATE INDEX IF NOT EXISTS idx_posts_published_at ON posts(published_at);
CREATE INDEX IF NOT EXISTS idx_posts_modified_at ON posts(modified_at);
CREATE INDEX IF NOT EXISTS idx_posts_language ON posts(language);
CREATE INDEX IF NOT EXISTS idx_posts_content_hash ON posts(content_hash);
CREATE INDEX IF NOT EXISTS idx_categories_site_id ON categories(site_id);
CREATE INDEX IF NOT EXISTS idx_tags_site_id ON tags(site_id);
CREATE INDEX IF NOT EXISTS idx_media_sha256 ON media(sha256_hash);
CREATE INDEX IF NOT EXISTS idx_media_site_wp_media ON media(site_id, wp_media_id);
CREATE INDEX IF NOT EXISTS idx_post_revisions_post_id ON post_revisions(post_id);

CREATE VIRTUAL TABLE IF NOT EXISTS posts_fts USING fts5(
    archive_id UNINDEXED,
    title,
    content_markdown,
    excerpt,
    tokenize = 'unicode61'
);

CREATE TRIGGER IF NOT EXISTS trg_posts_ai AFTER INSERT ON posts BEGIN
    INSERT INTO posts_fts (rowid, archive_id, title, content_markdown, excerpt)
    VALUES (new.id, new.archive_id, new.title, new.content_markdown, coalesce(new.excerpt, ''));
END;

CREATE TRIGGER IF NOT EXISTS trg_posts_ad AFTER DELETE ON posts BEGIN
    DELETE FROM posts_fts WHERE rowid = old.id;
END;

CREATE TRIGGER IF NOT EXISTS trg_posts_au AFTER UPDATE ON posts BEGIN
    DELETE FROM posts_fts WHERE rowid = old.id;
    INSERT INTO posts_fts (rowid, archive_id, title, content_markdown, excerpt)
    VALUES (new.id, new.archive_id, new.title, new.content_markdown, coalesce(new.excerpt, ''));
END;
