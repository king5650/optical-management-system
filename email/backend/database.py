# backend/database.py
import sqlite3
import os
from datetime import datetime

DB_NAME = "mail_system.db"


def get_connection():
    """Return a database connection with row factory enabled."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_database():
    """Create database tables if they do not exist."""
    conn = get_connection()
    cursor = conn.cursor()

    # ---- TABLE: people ----
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS people (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            group_name TEXT,
            created_at TEXT NOT NULL
        )
    """)

    # ---- TABLE: mail_history ----
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mail_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject TEXT NOT NULL,
            message TEXT NOT NULL,
            recipients TEXT NOT NULL,
            attachments TEXT,
            sent_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def reset_database():
    """Delete all tables and recreate them (for debugging/testing)."""
    if os.path.exists(DB_NAME):
        os.remove(DB_NAME)
    init_database()


# Initialize database automatically when module is imported
init_database()
