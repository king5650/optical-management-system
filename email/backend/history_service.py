import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime
from backend.database import get_connection


class HistoryService:

    # -------------------------------------------------------------
    # SAVE MAIL HISTORY
    # -------------------------------------------------------------
    @staticmethod
    def save_mail(subject: str, message: str, recipients: list, attachments: list):
        """
        Store a mail entry in the history table.
        recipients: list of emails
        attachments: list of file paths
        """

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO mail_history (subject, message, recipients, attachments, sent_at)
            VALUES (?, ?, ?, ?, ?)
        """, (
            subject,
            message,
            ",".join(recipients),
            ",".join(attachments),
            datetime.now().isoformat()
        ))

        conn.commit()
        conn.close()

    # -------------------------------------------------------------
    # FETCH ALL MAIL HISTORY
    # -------------------------------------------------------------
    @staticmethod
    def get_all_history() -> list:
        """Return all mail logs ordered by newest first."""

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM mail_history
            ORDER BY id DESC
        """)

        rows = cursor.fetchall()
        conn.close()

        # Convert into Python dictionaries
        history_list = []
        for row in rows:
            history_list.append({
                "id": row["id"],
                "subject": row["subject"],
                "message": row["message"],
                "recipients": row["recipients"].split(",") if row["recipients"] else [],
                "attachments": row["attachments"].split(",") if row["attachments"] else [],
                "sent_at": row["sent_at"]
            })

        return history_list

    # -------------------------------------------------------------
    # GET SINGLE HISTORY ENTRY
    # -------------------------------------------------------------
    @staticmethod
    def get_history(entry_id: int):
        """Get a specific mail history record."""

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT * FROM mail_history WHERE id = ?
        """, (entry_id,))

        row = cursor.fetchone()
        conn.close()

        if not row:
            return None

        return {
            "id": row["id"],
            "subject": row["subject"],
            "message": row["message"],
            "recipients": row["recipients"].split(",") if row["recipients"] else [],
            "attachments": row["attachments"].split(",") if row["attachments"] else [],
            "sent_at": row["sent_at"]
        }

    # -------------------------------------------------------------
    # DELETE A SPECIFIC HISTORY ENTRY
    # -------------------------------------------------------------
    @staticmethod
    def delete_history(entry_id: int):
        """Delete a log record by ID."""

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM mail_history WHERE id = ?", (entry_id,))

        conn.commit()
        conn.close()

    # -------------------------------------------------------------
    # CLEAR ALL HISTORY (Optional Feature)
    # -------------------------------------------------------------
    @staticmethod
    def clear_all_history():
        """Remove all logs from the mail_history table."""

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM mail_history")

        conn.commit()
        conn.close()
