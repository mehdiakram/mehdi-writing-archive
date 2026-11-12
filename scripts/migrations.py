"""Database Migrations Runner for Mehdi's Digital Legacy."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import List, Tuple

# Adjust sys.path to allow running from any working directory
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from scripts.database import get_db, utc_now_iso, init_database, get_db_path


def get_migration_files() -> List[Tuple[int, str, Path]]:
    """Discovers and sorts all SQL migration files."""
    migrations_dir = ROOT_DIR / "database" / "migrations"
    migrations_dir.mkdir(parents=True, exist_ok=True)
    
    files = []
    pattern = re.compile(r"^(\d+)_(.+)\.sql$")
    for p in migrations_dir.glob("*.sql"):
        match = pattern.match(p.name)
        if match:
            version = int(match.group(1))
            files.append((version, p.name, p))
            
    files.sort(key=lambda x: x[0])
    return files


def run_migrations(db_path: Path | str | None = None) -> int:
    """Applies all pending migrations."""
    init_database(db_path)
    
    with get_db(db_path) as conn:
        applied_rows = conn.execute("SELECT version FROM schema_migrations").fetchall()
        applied_versions = {row["version"] for row in applied_rows}
        
        migration_files = get_migration_files()
        applied_count = 0
        
        for version, name, path in migration_files:
            if version not in applied_versions:
                print(f"[Migration] Applying {name} (v{version})...")
                with open(path, "r", encoding="utf-8") as f:
                    sql_script = f.read()
                conn.executescript(sql_script)
                conn.execute(
                    "INSERT INTO schema_migrations (version, name, applied_at) VALUES (?, ?, ?)",
                    (version, name, utc_now_iso())
                )
                applied_count += 1
                print(f"[Migration] Successfully applied {name}")
                
        if applied_count == 0:
            print("[Migration] Database is already up to date.")
        else:
            print(f"[Migration] Total migrations applied: {applied_count}")
            
    return applied_count


if __name__ == "__main__":
    count = run_migrations()
    sys.exit(0)
