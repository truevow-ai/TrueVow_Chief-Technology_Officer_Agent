#!/usr/bin/env python3
"""
Codebase Memory - Python client.
Direct SQLite access to the same schema used by codebase-memory (yuga-hashimoto).
No MCP server needed. Works with any agent that can run Python.

Schema:
  memories (id, category, title, content, tags, file_paths, created_at, updated_at, access_count, importance, source)
  memories_fts (FTS5 virtual table on title, content, tags)

Usage:
  from memory import MemoryDatabase
  db = MemoryDatabase("TrueVow_Shared_Codebase_Memory/memory.db")
  db.create(category="architecture", title="Microservices", content="We use gRPC...")
  results = db.query(query="microservices", category="architecture")
  summary = db.get_summary()

CLI:
  python memory.py summarize
  python memory.py remember "architecture" "Title" "Content" --importance 8
  python memory.py recall "search terms" --category pattern --limit 5
  python memory.py forget <id>
  python memory.py update <id> --title "New Title" --importance 9
"""

import sqlite3
import json
import uuid
import sys
from pathlib import Path
from datetime import datetime, timezone
from typing import Optional


CATEGORIES = [
    "architecture", "pattern", "decision", "dependency",
    "convention", "bug", "context", "todo", "relationship",
]

SORT_MAP = {
    "recent": "updated_at DESC",
    "importance": "importance DESC",
    "accessed": "access_count DESC",
    "relevance": "updated_at DESC",
}


class MemoryDatabase:
    def __init__(self, db_path: str, wal_mode: bool = True):
        self.db = sqlite3.connect(db_path)
        self.db.row_factory = sqlite3.Row
        if wal_mode:
            self.db.execute("PRAGMA journal_mode=WAL")
        self.db.execute("PRAGMA foreign_keys=ON")
        self._initialize()

    def _initialize(self):
        self.db.executescript("""
            CREATE TABLE IF NOT EXISTS memories (
                id TEXT PRIMARY KEY,
                category TEXT NOT NULL,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                tags TEXT NOT NULL DEFAULT '[]',
                file_paths TEXT NOT NULL DEFAULT '[]',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL,
                access_count INTEGER NOT NULL DEFAULT 0,
                importance INTEGER NOT NULL DEFAULT 5,
                source TEXT NOT NULL DEFAULT 'user'
            );

            CREATE INDEX IF NOT EXISTS idx_memories_category ON memories(category);
            CREATE INDEX IF NOT EXISTS idx_memories_importance ON memories(importance DESC);
            CREATE INDEX IF NOT EXISTS idx_memories_updated ON memories(updated_at DESC);
            CREATE INDEX IF NOT EXISTS idx_memories_accessed ON memories(access_count DESC);

            CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts USING fts5(
                title, content, tags,
                content='memories',
                content_rowid='rowid'
            );

            CREATE TRIGGER IF NOT EXISTS memories_ai AFTER INSERT ON memories BEGIN
                INSERT INTO memories_fts(rowid, title, content, tags)
                VALUES (new.rowid, new.title, new.content, new.tags);
            END;

            CREATE TRIGGER IF NOT EXISTS memories_ad AFTER DELETE ON memories BEGIN
                INSERT INTO memories_fts(memories_fts, rowid, title, content, tags)
                VALUES ('delete', old.rowid, old.title, old.content, old.tags);
            END;

            CREATE TRIGGER IF NOT EXISTS memories_au AFTER UPDATE ON memories BEGIN
                INSERT INTO memories_fts(memories_fts, rowid, title, content, tags)
                VALUES ('delete', old.rowid, old.title, old.content, old.tags);
                INSERT INTO memories_fts(rowid, title, content, tags)
                VALUES (new.rowid, new.title, new.content, new.tags);
            END;
        """)
        self.db.commit()

    def create(self, category: str, title: str, content: str,
               tags: list = None, file_paths: list = None, importance: int = 5,
               source: str = "user") -> dict:
        if category not in CATEGORIES:
            raise ValueError(f"Invalid category: {category}. Must be one of {CATEGORIES}")
        mid = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()
        tags_json = json.dumps(tags or [])
        files_json = json.dumps(file_paths or [])
        importance = max(1, min(10, importance))

        self.db.execute(
            """INSERT INTO memories (id, category, title, content, tags, file_paths, created_at, updated_at, importance, source)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (mid, category, title, content, tags_json, files_json, now, now, importance, source)
        )
        self.db.commit()
        return self.get_by_id(mid)

    def get_by_id(self, mid: str, increment_access: bool = False) -> Optional[dict]:
        row = self.db.execute("SELECT * FROM memories WHERE id = ?", (mid,)).fetchone()
        if not row:
            return None
        if increment_access:
            self.db.execute("UPDATE memories SET access_count = access_count + 1 WHERE id = ?", (mid,))
            self.db.commit()
        return self._row_to_dict(row)

    def update(self, mid: str, title: str = None, content: str = None,
               category: str = None, tags: list = None, file_paths: list = None,
               importance: int = None) -> Optional[dict]:
        existing = self.db.execute("SELECT * FROM memories WHERE id = ?", (mid,)).fetchone()
        if not existing:
            return None

        updates = []
        values = []
        if title is not None:
            updates.append("title = ?"); values.append(title)
        if content is not None:
            updates.append("content = ?"); values.append(content)
        if category is not None:
            updates.append("category = ?"); values.append(category)
        if tags is not None:
            updates.append("tags = ?"); values.append(json.dumps(tags))
        if file_paths is not None:
            updates.append("file_paths = ?"); values.append(json.dumps(file_paths))
        if importance is not None:
            updates.append("importance = ?"); values.append(max(1, min(10, importance)))

        if not updates:
            return self._row_to_dict(existing)

        updates.append("updated_at = ?")
        values.append(datetime.now(timezone.utc).isoformat())
        values.append(mid)

        self.db.execute(f"UPDATE memories SET {', '.join(updates)} WHERE id = ?", values)
        self.db.commit()
        return self.get_by_id(mid)

    def delete(self, mid: str) -> bool:
        result = self.db.execute("DELETE FROM memories WHERE id = ?", (mid,))
        self.db.commit()
        return result.rowcount > 0

    def query(self, query: str = None, category: str = None, tags: list = None,
              file_path: str = None, min_importance: int = None,
              limit: int = 20, offset: int = 0, sort_by: str = "recent") -> list:
        limit = min(limit, 100)

        if query:
            fts_query = ' OR '.join(f'"{w.replace(chr(34), chr(34)+chr(34))}"' for w in query.split())
            sql = """
                SELECT m.*, rank
                FROM memories m
                JOIN memories_fts f ON m.rowid = f.rowid
                WHERE memories_fts MATCH ?
            """
            params = [fts_query]

            if category:
                sql += " AND m.category = ?"; params.append(category)
            if min_importance:
                sql += " AND m.importance >= ?"; params.append(min_importance)
            if file_path:
                sql += " AND m.file_paths LIKE ?"; params.append(f"%{file_path}%")

            sql += " ORDER BY rank"
            sql += " LIMIT ? OFFSET ?"; params.extend([limit, offset])
            rows = self.db.execute(sql, params).fetchall()
        else:
            sql = "SELECT * FROM memories WHERE 1=1"
            params = []

            if category:
                sql += " AND category = ?"; params.append(category)
            if min_importance:
                sql += " AND importance >= ?"; params.append(min_importance)
            if file_path:
                sql += " AND file_paths LIKE ?"; params.append(f"%{file_path}%")
            if tags:
                for tag in tags:
                    sql += " AND tags LIKE ?"; params.append(f'%"{tag}"%')

            sql += f" ORDER BY {SORT_MAP.get(sort_by, 'updated_at DESC')}"
            sql += " LIMIT ? OFFSET ?"; params.extend([limit, offset])
            rows = self.db.execute(sql, params).fetchall()

        return [self._row_to_dict(r) for r in rows]

    def get_summary(self) -> dict:
        total = self.db.execute("SELECT COUNT(*) as count FROM memories").fetchone()["count"]
        by_category = {}
        for cat in CATEGORIES:
            row = self.db.execute("SELECT COUNT(*) as count FROM memories WHERE category = ?", (cat,)).fetchone()
            by_category[cat] = row["count"]

        all_rows = self.db.execute("SELECT tags FROM memories").fetchall()
        tag_counts = {}
        for row in all_rows:
            for tag in json.loads(row["tags"]):
                tag_counts[tag] = tag_counts.get(tag, 0) + 1
        top_tags = sorted(tag_counts.items(), key=lambda x: -x[1])[:10]
        top_tags = [{"tag": k, "count": v} for k, v in top_tags]

        return {
            "totalMemories": total,
            "byCategory": by_category,
            "topTags": top_tags,
            "recentlyUpdated": self.query(sort_by="recent", limit=5),
            "mostAccessed": self.query(sort_by="accessed", limit=5),
            "highImportance": self.query(min_importance=8, sort_by="importance", limit=5),
        }

    def close(self):
        self.db.close()

    def _row_to_dict(self, row) -> dict:
        return {
            "id": row["id"],
            "category": row["category"],
            "title": row["title"],
            "content": row["content"],
            "tags": json.loads(row["tags"]),
            "filePaths": json.loads(row["file_paths"]),
            "createdAt": row["created_at"],
            "updatedAt": row["updated_at"],
            "accessCount": row["access_count"],
            "importance": row["importance"],
            "source": row["source"],
        }


def _get_db():
    root = Path(__file__).resolve().parent.parent
    db_path = root / "TrueVow_Shared_Codebase_Memory" / "memory.db"
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return MemoryDatabase(str(db_path))


def cli_summarize():
    db = _get_db()
    summary = db.get_summary()
    print(f"\n=== Codebase Memory Summary ===")
    print(f"Total memories: {summary['totalMemories']}")
    print(f"\nBy category:")
    for cat, count in summary["byCategory"].items():
        if count > 0:
            print(f"  {cat:20s} {count:3d}")
    if summary["topTags"]:
        print(f"\nTop tags:")
        for t in summary["topTags"][:5]:
            print(f"  #{t['tag']:20s} ({t['count']})")
    if summary["highImportance"]:
        print(f"\nHigh importance (8+):")
        for m in summary["highImportance"]:
            print(f"  [{m['category']}] {m['title']} (imp: {m['importance']})")
    db.close()


def cli_remember():
    if len(sys.argv) < 5:
        print("Usage: python memory.py remember <category> <title> <content> [--importance N] [--tags t1,t2]")
        return
    category = sys.argv[2]
    title = sys.argv[3]
    content = sys.argv[4]
    importance = 5
    tags = []
    args = sys.argv[5:]
    i = 0
    while i < len(args):
        if args[i] == "--importance" and i + 1 < len(args):
            importance = int(args[i + 1]); i += 2
        elif args[i] == "--tags" and i + 1 < len(args):
            tags = [t.strip() for t in args[i + 1].split(",")]; i += 2
        else:
            i += 1

    db = _get_db()
    entry = db.create(category=category, title=title, content=content, tags=tags, importance=importance)
    print(f"Memory created: {entry['id']}")
    print(f"  [{entry['category']}] {entry['title']} (importance: {entry['importance']})")
    db.close()


def cli_recall():
    query = None
    category = None
    limit = 20
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == "--category" and i + 1 < len(args):
            category = args[i + 1]; i += 2
        elif args[i] == "--limit" and i + 1 < len(args):
            limit = int(args[i + 1]); i += 2
        elif not args[i].startswith("--"):
            query = args[i]; i += 1
        else:
            i += 1

    db = _get_db()
    results = db.query(query=query, category=category, limit=limit)
    if not results:
        print("No memories found.")
    for m in results:
        print(f"  [{m['category']}] {m['title']}")
        print(f"    {m['content'][:120]}{'...' if len(m['content']) > 120 else ''}")
        print(f"    id={m['id']}  importance={m['importance']}  tags={m['tags']}")
        print()
    db.close()


def cli_forget():
    if len(sys.argv) < 3:
        print("Usage: python memory.py forget <id>")
        return
    mid = sys.argv[2]
    db = _get_db()
    ok = db.delete(mid)
    print(f"Deleted: {ok}" if ok else f"Not found: {mid}")
    db.close()


def cli_update():
    if len(sys.argv) < 3:
        print("Usage: python memory.py update <id> [--title T] [--content C] [--importance N]")
        return
    mid = sys.argv[2]
    kwargs = {}
    args = sys.argv[3:]
    i = 0
    while i < len(args):
        if args[i] == "--title" and i + 1 < len(args):
            kwargs["title"] = args[i + 1]; i += 2
        elif args[i] == "--content" and i + 1 < len(args):
            kwargs["content"] = args[i + 1]; i += 2
        elif args[i] == "--importance" and i + 1 < len(args):
            kwargs["importance"] = int(args[i + 1]); i += 2
        elif args[i] == "--category" and i + 1 < len(args):
            kwargs["category"] = args[i + 1]; i += 2
        elif args[i] == "--tags" and i + 1 < len(args):
            kwargs["tags"] = [t.strip() for t in args[i + 1].split(",")]; i += 2
        else:
            i += 1

    db = _get_db()
    entry = db.update(mid, **kwargs)
    if entry:
        print(f"Updated: [{entry['category']}] {entry['title']}")
    else:
        print(f"Not found: {mid}")
    db.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        print("Commands: summarize | remember | recall | forget | update")
        sys.exit(0)

    cmd = sys.argv[1]
    if cmd == "summarize":
        cli_summarize()
    elif cmd == "remember":
        cli_remember()
    elif cmd == "recall":
        cli_recall()
    elif cmd == "forget":
        cli_forget()
    elif cmd == "update":
        cli_update()
    else:
        print(f"Unknown command: {cmd}")
        print("Commands: summarize | remember | recall | forget | update")
