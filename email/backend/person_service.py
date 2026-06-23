# backend/person_service.py

import sqlite3
import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import re
from datetime import datetime
from backend.database import get_connection


class PersonService:
    def __init__(self):
        self.db = get_connection()
    # -----------------------------------------------------------
    # EMAIL VALIDATION
    # -----------------------------------------------------------
    @staticmethod
    def is_valid_email(email: str) -> bool:
        """Basic email format validation using regex."""
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return re.match(pattern, email) is not None

    @staticmethod
    def email_exists(email: str, exclude_id: int = None) -> bool:
        """Check if an email is already in the database."""
        conn = get_connection()
        cursor = conn.cursor()

        if exclude_id:
            cursor.execute("SELECT id FROM people WHERE email = ? AND id != ?", (email, exclude_id))
        else:
            cursor.execute("SELECT id FROM people WHERE email = ?", (email,))

        exists = cursor.fetchone() is not None

        conn.close()
        return exists

    # -----------------------------------------------------------
    # CRUD OPERATIONS
    # -----------------------------------------------------------
    @staticmethod
    def add_person(name: str, email: str, group_name: str = None) -> bool:
        """Add a new person. Returns True if successful."""

        if not PersonService.is_valid_email(email):
            raise ValueError("Invalid email format.")

        if PersonService.email_exists(email):
            raise ValueError("Email already registered.")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO people (name, email, group_name, created_at)
            VALUES (?, ?, ?, ?)
        """, (name, email, group_name, datetime.now().isoformat()))

        conn.commit()
        conn.close()
        return True
    @staticmethod
    def update_person(person_id: int, name: str, email: str, group_name: str) -> bool:

        if not PersonService.is_valid_email(email):
            raise ValueError("Invalid email format.")

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE people 
            SET name = ?, email = ?, group_name = ?
            WHERE id = ?
        """, (name, email, group_name, person_id))

        conn.commit()
        conn.close()
        return True


    @staticmethod
    def delete_person(person_id: int) -> bool:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM people WHERE id = ?", (person_id,))
        conn.commit()
        conn.close()
        return True

    # @staticmethod
    # def update_person(person_id: int, name: str, email: str, group_name: str = None):
    #     """Update a person's details."""

    #     if not PersonService.is_valid_email(email):
    #         raise ValueError("Invalid email format.")

    #     if PersonService.email_exists(email, exclude_id=person_id):
    #         raise ValueError("Email already assigned to another user.")

    #     conn = get_connection()
    #     cursor = conn.cursor()

    #     cursor.execute("""
    #         UPDATE people
    #         SET name = ?, email = ?, group_name = ?
    #         WHERE id = ?
    #     """, (name, email, group_name, person_id))

    #     conn.commit()
    #     conn.close()

    # @staticmethod
    # def delete_person(person_id: int):
    #     """Delete a person."""
    #     conn = get_connection()
    #     cursor = conn.cursor()

    #     cursor.execute("DELETE FROM people WHERE id = ?", (person_id,))

    #     conn.commit()
    #     conn.close()

    @staticmethod
    def get_person(person_id: int):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM people WHERE id = ?", (person_id,))
        row = cursor.fetchone()
        conn.close()
        return dict(row) if row else None

    @staticmethod
    def get_all_people() -> list:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM people ORDER BY name ASC")
        rows = cursor.fetchall()
        conn.close()
        return [dict(r) for r in rows]
    # @staticmethod
    # def get_person(person_id: int):
    #     """Retrieve a single person as dict."""

    #     conn = get_connection()
    #     cursor = conn.cursor()

    #     cursor.execute("SELECT * FROM people WHERE id = ?", (person_id,))
    #     row = cursor.fetchone()

    #     conn.close()

    #     return dict(row) if row else None

    # @staticmethod
    # def get_all_people() -> list:
    #     """Return a list of all people as dictionaries."""
    #     conn = get_connection()
    #     cursor = conn.cursor()

    #     cursor.execute("SELECT * FROM people ORDER BY name ASC")
    #     rows = cursor.fetchall()

    #     conn.close()

    #     return [dict(r) for r in rows]
    # def get_all_people():
    #     connection = sqlite3.connect("mail_system.db")  # Replace with your database file
    #     cursor = connection.cursor()

    #     query = "SELECT name, email, group_name, created_at FROM people"
    #     cursor.execute(query)

    #     rows = cursor.fetchall()
    #     connection.close()

    #     # Convert rows to a list of dictionaries
    #     people = [
    #         {
    #             "first_name": row[0],
    #             "last_name": row[1],
    #             "email": row[2],
    #             "group_name": row[3],
    #             "status": row[4]
    #         }
    #         for row in rows
    #     ]
    #     return people
    @staticmethod
    def get_people_by_group(group_name: str) -> list:
        """Return all people belonging to a specific group."""
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM people WHERE group_name = ? ORDER BY name ASC", (group_name,))
        rows = cursor.fetchall()

        conn.close()

        return [dict(r) for r in rows]

    def get_emails_by_ids(self, person_ids):
        """
        Retrieve email addresses for the given person IDs.
        """
        if not person_ids:
            return []

        query = "SELECT email FROM people WHERE id IN ({})".format(
            ",".join("?" for _ in person_ids)
        )
        params = tuple(person_ids)

        # Use self.db directly as it is already a connection object
        cursor = self.db.cursor()
        cursor.execute(query, params)
        results = cursor.fetchall()

        return [row[0] for row in results]