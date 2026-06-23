import sqlite3
from typing import List, Tuple, Optional, Dict


class ContactsManager:
    def __init__(self, db_path: str = "contacts.db"):
        self.db_path = db_path
        self._create_table()

    def _connect(self):
        """Create a new DB connection each time (safe for multi-thread)."""
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        """Ensure the contacts table exists."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL UNIQUE,
                    department TEXT,
                    tag TEXT
                )
                """
            )
            conn.commit()

    # ---------------- CRUD Operations ---------------- #

    def add_contact(self, name: str, phone: str, department: Optional[str] = None, tag: Optional[str] = None) -> int:
        """Insert new contact. Returns the new contact ID."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO contacts (name, phone, department, tag) VALUES (?, ?, ?, ?)",
                (name, phone, department, tag),
            )
            conn.commit()
            return cursor.lastrowid

    def edit_contact(self, contact_id: int, name: str, phone: str, department: Optional[str] = None, tag: Optional[str] = None) -> bool:
        """Update an existing contact. Returns True if updated."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "UPDATE contacts SET name=?, phone=?, department=?, tag=? WHERE id=?",
                (name, phone, department, tag, contact_id),
            )
            conn.commit()
            return cursor.rowcount > 0

    def delete_contact(self, contact_id: int) -> bool:
        """Delete a contact. Returns True if deleted."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM contacts WHERE id=?", (contact_id,))
            conn.commit()
            return cursor.rowcount > 0

    def list_contacts(self) -> List[Dict]:
        """Fetch all contacts as list of dicts."""
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, phone, department, tag FROM contacts ORDER BY name")
            rows = cursor.fetchall()
            return [
                {"id": row[0], "name": row[1], "phone": row[2], "department": row[3], "tag": row[4]}
                for row in rows
            ]

    def search_contacts(self, query: str) -> List[Dict]:
        """Search by name, phone, department, or tag."""
        with self._connect() as conn:
            cursor = conn.cursor()
            like_query = f"%{query}%"
            cursor.execute(
                """
                SELECT id, name, phone, department, tag
                FROM contacts
                WHERE name LIKE ? OR phone LIKE ? OR department LIKE ? OR tag LIKE ?
                ORDER BY name
                """,
                (like_query, like_query, like_query, like_query),
            )
            rows = cursor.fetchall()
            return [
                {"id": row[0], "name": row[1], "phone": row[2], "department": row[3], "tag": row[4]}
                for row in rows
            ]


# ---------------- Example Usage ---------------- #
if __name__ == "__main__":
    cm = ContactsManager()

    # Add contacts
    cm.add_contact("Alice Johnson", "+123456789", "HR", "Manager")
    cm.add_contact("Bob Smith", "+987654321", "IT", "Developer")

    # List contacts
    print("All contacts:", cm.list_contacts())

    # Search
    print("Search 'IT':", cm.search_contacts("IT"))

    # Edit contact
    cm.edit_contact(1, "Alice J.", "+123456789", "HR", "Director")

    # Delete
    cm.delete_contact(2)

    print("Final contacts:", cm.list_contacts())
