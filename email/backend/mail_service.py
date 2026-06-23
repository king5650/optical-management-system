# # backend/mail_service.py
# import smtplib
# import ssl
# import mimetypes
# from email.message import EmailMessage
# from email.utils import formatdate
# from pathlib import Path


# class MailService:

#     def __init__(self, smtp_host, smtp_port, username, password, use_tls=True):
#         """
#         smtp_host: SMTP server (e.g., smtp.gmail.com)
#         smtp_port: Port (587 for TLS, 465 for SSL)
#         username: Email login (full email)
#         password: App password / SMTP password
#         use_tls: True = STARTTLS (Port 587), False = SSL (Port 465)
#         """

#         self.smtp_host = smtp_host
#         self.smtp_port = smtp_port
#         self.username = username
#         self.password = password
#         self.use_tls = use_tls

#     # ---------------------------------------------------------
#     # BUILD EMAIL MESSAGE
#     # ---------------------------------------------------------
#     def _build_message(self, sender, recipients, subject, message_text, attachments):
#         msg = EmailMessage()

#         msg["From"] = sender
#         msg["To"] = ", ".join(recipients)
#         msg["Subject"] = subject
#         msg["Date"] = formatdate(localtime=True)

#         # Text body (HTML + plain fallback)
#         msg.set_content(message_text)
#         msg.add_alternative(f"""
#             <html>
#                 <body>
#                     <p>{message_text.replace('\n', '<br>')}</p>
#                 </body>
#             </html>
#         """, subtype="html")

#         # Attachments
#         if attachments:
#             for file_path in attachments:
#                 self._attach_file(msg, file_path)

#         return msg

#     # ---------------------------------------------------------
#     # ATTACH FILES
#     # ---------------------------------------------------------
#     def _attach_file(self, msg: EmailMessage, file_path: str):
#         file_path = Path(file_path)

#         if not file_path.exists():
#             print(f"[WARNING] Attachment not found: {file_path}")
#             return

#         mime_type, _ = mimetypes.guess_type(file_path)
#         mime_type = mime_type or "application/octet-stream"
#         maintype, subtype = mime_type.split("/", 1)

#         with open(file_path, "rb") as f:
#             msg.add_attachment(
#                 f.read(),
#                 maintype=maintype,
#                 subtype=subtype,
#                 filename=file_path.name
#             )

#     # ---------------------------------------------------------
#     # SEND EMAIL
#     # ---------------------------------------------------------
#     def send_mail(self, recipients, subject, message_text, attachments=None):
#         """
#         recipients: list of email addresses
#         subject: email subject
#         message_text: body text
#         attachments: optional list of file paths
#         """

#         attachments = attachments or []
#         sender = self.username

#         # Build the email message
#         msg = self._build_message(
#             sender=sender,
#             recipients=recipients,
#             subject=subject,
#             message_text=message_text,
#             attachments=attachments
#         )

#         # ---------------------------------------------------------
#         # SMTP CONNECTION
#         # ---------------------------------------------------------
#         try:
#             if self.use_tls:
#                 # STARTTLS mode
#                 context = ssl.create_default_context()
#                 with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
#                     server.starttls(context=context)
#                     server.login(self.username, self.password)
#                     server.send_message(msg)

#             else:
#                 # SSL mode
#                 context = ssl.create_default_context()
#                 with smtplib.SMTP_SSL(self.smtp_host, self.smtp_port, context=context) as server:
#                     server.login(self.username, self.password)
#                     server.send_message(msg)

#             return True, "Mail sent successfully."

#         except Exception as e:
#             return False, str(e)

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# mail_service.py
import smtplib
from typing import List, Optional
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import ssl
import os

from backend.database import get_connection


class MailService:
    """
    Service responsible for sending emails using SMTP.

    Supports:
    - Gmail SMTP (smtp.gmail.com)
    - Custom SMTP servers
    - Attachments
    """

    def __init__(self):
        self.settings = self.load_settings()

    # ------------------------------------------------------
    # SETTINGS LOADING
    # ------------------------------------------------------
    def load_settings(self):
        """Load SMTP configuration from the database."""
        settings = {
            "smtp_host": "",
            "smtp_port": 587,
            "email": "",
            "password": "",
            "use_tls": True,
            "use_ssl": False,
        }

        conn = get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute("SELECT key, value FROM settings")
            rows = cursor.fetchall()
            for key, value in rows:
                if key in settings:
                    if key == "smtp_port":
                        settings[key] = int(value)
                    elif key in ["use_tls", "use_ssl"]:
                        settings[key] = value == "1"
                    else:
                        settings[key] = value
        except:
            pass

        conn.close()
        return settings

    # ------------------------------------------------------
    # EMAIL SENDING
    # ------------------------------------------------------
    def send_email(
        self,
        sender_name: str,
        recipients: List[str],
        subject: str,
        message: str,
        attachments: Optional[List[str]] = None
    ):
        """
        Send an email to multiple recipients with optional attachments.

        Returns:
            (success: bool, error: str)
        """

        smtp_host = self.settings["smtp_host"]
        smtp_port = self.settings["smtp_port"]
        username = self.settings["email"]
        password = self.settings["password"]
        use_tls = self.settings["use_tls"]
        use_ssl = self.settings["use_ssl"]

        if not smtp_host or not username or not password:
            return False, "SMTP settings are incomplete. Please configure email settings."

        # -------------------------------
        # Create message container
        # -------------------------------
        msg = MIMEMultipart()
        msg["From"] = f"{sender_name} <{username}>"
        msg["To"] = ", ".join(recipients)
        msg["Subject"] = subject

        msg.attach(MIMEText(message, "html"))

        # -------------------------------
        # Attach files
        # -------------------------------
        if attachments:
            for file_path in attachments:
                if not os.path.isfile(file_path):
                    continue

                part = MIMEBase("application", "octet-stream")
                with open(file_path, "rb") as f:
                    part.set_payload(f.read())
                encoders.encode_base64(part)

                part.add_header(
                    "Content-Disposition",
                    f"attachment; filename={os.path.basename(file_path)}",
                )

                msg.attach(part)

        try:
            # ---------------------------------------
            # CONNECT SMTP
            # ---------------------------------------
            if use_ssl:
                context = ssl.create_default_context()
                server = smtplib.SMTP_SSL(smtp_host, smtp_port, context=context)
            else:
                server = smtplib.SMTP(smtp_host, smtp_port)
                server.ehlo()

                if use_tls:
                    context = ssl.create_default_context()
                    server.starttls(context=context)

            # ---------------------------------------
            # LOGIN
            # ---------------------------------------
            server.login(username, password)

            # ---------------------------------------
            # SEND
            # ---------------------------------------
            server.sendmail(username, recipients, msg.as_string())
            server.quit()

            return True, ""

        except smtplib.SMTPAuthenticationError:
            return False, "SMTP Authentication failed. Wrong email or password."

        except smtplib.SMTPConnectError:
            return False, "Unable to connect to SMTP server."

        except Exception as ex:
            return False, f"Error sending email: {str(ex)}"


# Global mail service instance
mail_service = MailService()
