"""Database Engine for Mehdi's Digital Legacy.

Manages SQLite connection, foreign keys, WAL mode, migrations,
transactions, and WAL checkpoints.
"""

from __future__ import annotations

import contextlib
import hashlib
import json
import os
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Tuple

ROOT_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = ROOT_DIR / "config"
DATABASE_DIR = ROOT_DIR / "database"
DEFAULT_DB_PATH = DATABASE_DIR / "archive.sqlite"
SCHEMA_PATH = DATABASE_DIR / "schema.sql"


def utc_now_iso() -> str:
    """Returns current UTC timestamp in ISO 8601 format."""
    return datetime.now(timezone.utc).isoformat()


def get_db_path() -> Path:
    """Resolves the database path from settings or defaults."""
    settings_file = CONFIG_DIR / "settings.json"
    if settings_file.exists():
        try:
            with open(settings_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                configured = data.get("database", {}).get("path")
                if configured:
                    return ROOT_DIR / configured
        except Exception:
            pass
    return DEFAULT_DB_PATH


def create_connection(db_path: Optional[Path | str] = None, wal_mode: bool = True) -> sqlite3.Connection:
    """Creates a configured SQLite connection with foreign keys and row factory."""
    path = Path(db_path) if db_path else get_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(str(path), timeout=30.0)
    conn.row_factory = sqlite3.Row
    
    # Always enforce foreign keys
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.execute("PRAGMA busy_timeout = 5000;")
    
    if wal_mode:
        conn.execute("PRAGMA journal_mode = WAL;")
        conn.execute("PRAGMA synchronous = NORMAL;")
        
    return conn


@contextlib.contextmanager
def get_db(db_path: Optional[Path | str] = None, wal_mode: bool = True) -> Generator[sqlite3.Connection, None, None]:
    """Context manager for SQLite database transactions."""
    conn = create_connection(db_path, wal_mode=wal_mode)
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def checkpoint_and_clean_db(db_path: Optional[Path | str] = None) -> None:
    """Safely checkpoints WAL, truncates the WAL file, and switches back to standard journal.
    
    This ensures no temporary WAL/SHM files are left behind when committing to Git.
    """
    path = Path(db_path) if db_path else get_db_path()
    if not path.exists():
        return
        
    conn = sqlite3.connect(str(path), timeout=30.0)
    try:
        conn.execute("PRAGMA wal_checkpoint(TRUNCATE);")
        conn.execute("PRAGMA journal_mode = DELETE;")
        conn.commit()
    finally:
        conn.close()


def init_database(db_path: Optional[Path | str] = None) -> None:
    """Initializes the database using schema.sql and registers initial migration."""
    path = Path(db_path) if db_path else get_db_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with get_db(path) as conn:
        if SCHEMA_PATH.exists():
            with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
                schema_sql = f.read()
            conn.executescript(schema_sql)
            
            # Register initial migration if not exists
            now = utc_now_iso()
            conn.execute(
                """
                INSERT OR IGNORE INTO schema_migrations (version, name, applied_at)
                VALUES (1, '001_initial_schema.sql', ?)
                """,
                (now,)
            )
            
            # Register sources from sources.json
            sources_file = CONFIG_DIR / "sources.json"
            if sources_file.exists():
                with open(sources_file, "r", encoding="utf-8") as sf:
                    sources_data = json.load(sf).get("sources", [])
                for s in sources_data:
                    conn.execute(
                        """
                        INSERT INTO sites (key, name, domain, base_url, api_url, default_language, enabled, created_at, updated_at)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        ON CONFLICT(key) DO UPDATE SET
                            name = excluded.name,
                            domain = excluded.domain,
                            base_url = excluded.base_url,
                            api_url = excluded.api_url,
                            default_language = excluded.default_language,
                            enabled = excluded.enabled,
                            updated_at = excluded.updated_at
                        """,
                        (
                            s["key"],
                            s["name"],
                            s["domain"],
                            s["base_url"],
                            s["api_url"],
                            s.get("default_language", "en"),
                            1 if s.get("enabled", True) else 0,
                            now,
                            now,
                        )
                    )
                    
                    # Ensure sync_state record exists
                    site_row = conn.execute("SELECT id FROM sites WHERE key = ?", (s["key"],)).fetchone()
                    if site_row:
                        conn.execute(
                            """
                            INSERT OR IGNORE INTO sync_state (site_id, sync_status, updated_at)
                            VALUES (?, 'idle', ?)
                            """,
                            (site_row["id"], now)
                        )


def compute_content_hash(text: str) -> str:
    """Computes deterministic SHA-256 hash of content."""
    normalized = (text or "").strip().encode("utf-8")
    return hashlib.sha256(normalized).hexdigest()
