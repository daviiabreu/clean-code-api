import sqlite3
from contextlib import contextmanager

SCHEMA = """
CREATE TABLE IF NOT EXISTS figurinha (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    numero     TEXT NOT NULL,
    tipo       TEXT NOT NULL,
    posicao    TEXT NOT NULL,
    created_at TEXT NOT NULL,
    updated_at TEXT NOT NULL
);
"""


@contextmanager
def connection():
    conn = sqlite3.connect("figurinhas.db")
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()


def init_db():
    with connection() as conn:
        conn.executescript(SCHEMA)
