# """
# PySide6 UI/UX for WhatsApp Scheduler (Phase 1: UI only)
# - Clean, soft (neumorphism-inspired) styling
# - Inputs: Name, Number, Message, DateTime
# - Actions: Schedule Message
# - Table for scheduled jobs with Edit/Delete actions
# - Log panel
# - Non-blocking UX hooks (signals) for integration with the scheduler/automation layers later

# Note: This file focuses on UI/UX. No Playwright automation or real scheduling yet.
# """
# from __future__ import annotations

# import sys
# import uuid
# from dataclasses import dataclass, asdict
# from datetime import datetime

# from PySide6.QtCore import (
#     Qt, QDateTime, QRect, QSize, Signal, Slot
# )
# from PySide6.QtGui import (
#     QIcon, QAction, QColor, QFont, QPalette
# )
# from PySide6.QtWidgets import (
#     QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
#     QLabel, QLineEdit, QTextEdit, QPushButton, QDateTimeEdit, QCheckBox,
#     QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView,
#     QFrame, QMessageBox, QStyle, QSpacerItem, QSizePolicy, QGridLayout,
#     QGraphicsDropShadowEffect
# )


# # ------------------------------
# # Data Model (UI layer only)
# # ------------------------------
# @dataclass
# class ScheduledJob:
#     id: str
#     name: str
#     number: str
#     message: str
#     send_time_iso: str  # ISO string for easier persistence later
#     status: str = "Scheduled"  # Scheduled | Sent | Failed | Missed | Canceled

#     @property
#     def send_dt(self) -> datetime:
#         return datetime.fromisoformat(self.send_time_iso)


# # ------------------------------
# # Helpers
# # ------------------------------4682B4    e9edf3
# SOFT_QSS = """
# /* ----- Global palette (soft, neumorphism-inspired) ----- */
# * { font-family: 'Segoe UI', 'Inter', 'Roboto', sans-serif; }

# QMainWindow#MainWindow { background: #4682B4;}

# /* Cards */
# QFrame#Card {
#     background: #f7f9fc;
#     border-radius: 16px;
#     color: black;
# }

# QLineEdit, QTextEdit, QDateTimeEdit {
#     background: #ffffff;
#     border: 1px solid #e2e8f0;
#     border-radius: 10px;
#     padding: 8px 10px;
#     color: black;
# }
# QLineEdit:focus, QTextEdit:focus, QDateTimeEdit:focus {
#     border: 1px solid #5b9bff;
#     color: black;
# }

# QPushButton#PrimaryBtn {
#     background: #4f8cff; /* soft blue */
#     color: black;
#     border: none;
#     border-radius: 12px;
#     padding: 10px 16px  10px 16px;
#     font-weight: 600;
# }
# QPushButton#PrimaryBtn:hover { filter: brightness(1.05); }
# QPushButton#PrimaryBtn:disabled { background: #aabdec; color: #eef2ff; }

# QPushButton#DangerBtn {
#     background: #ef4444; color: white; border: none; border-radius: 10px; padding: 6px 10px;
# }
# QPushButton#GhostBtn { 
#     background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 6px 10px; 
# }

# QTableWidget {
#     background: #ffffff;
#     border: 1px solid #e2e8f0;
#     border-radius: 12px;
#     gridline-color: #eef2f7;
# }
# QHeaderView::section {
#     background: #f3f6fb;
#     border: none;
#     padding: 8px;
#     font-weight: 600;
#     color: black;
# }
# QTableWidget::item { padding: 8px; }

# QTextEdit#LogBox { background: #0d1117; color: #e6edf3; border-radius: 12px; border: 1px solid #1f2937; }
# """


# def soft_shadow(widget: QWidget, radius: int = 24, opacity: float = 0.25, x: int = 0, y: int = 6):
#     shadow = QGraphicsDropShadowEffect()
#     shadow.setBlurRadius(radius)
#     shadow.setColor(QColor(0, 0, 0, int(255 * opacity)))
#     shadow.setOffset(x, y)
#     widget.setGraphicsEffect(shadow)


# # ------------------------------
# # Main Window
# # ------------------------------
# class MainWindow(QMainWindow):
#     scheduleRequested = Signal(dict)  # Emits a dict with job data (UI -> scheduler later)
#     deleteRequested = Signal(str)     # job_id
#     editRequested = Signal(str)       # job_id

#     def __init__(self):
#         super().__init__()
#         self.setObjectName("MainWindow")
#         self.setWindowTitle("WhatsApp Scheduler · UI")
#         self.setMinimumSize(1024, 680)
#         self.jobs: list[ScheduledJob] = []

#         # Central container
#         central = QWidget()
#         root = QVBoxLayout(central)
#         root.setContentsMargins(20, 20, 20, 20)
#         root.setSpacing(16)

#         # Top banner / title
#         header = self._build_header()
#         root.addWidget(header)

#         # Content grid: left (form) | right (log)
#         grid = QGridLayout()
#         grid.setHorizontalSpacing(16)
#         grid.setVerticalSpacing(16)

#         form_card = self._build_form_card()
#         soft_shadow(form_card)
#         grid.addWidget(form_card, 0, 0)

#         log_card = self._build_log_card()
#         soft_shadow(log_card)
#         grid.addWidget(log_card, 0, 1)

#         # Full-width table
#         table_card = self._build_table_card()
#         soft_shadow(table_card)

#         root.addLayout(grid, stretch=3)
#         root.addWidget(table_card, stretch=4)

#         self.setCentralWidget(central)
#         self._apply_style()

#     # ---------- Header ----------
#     def _build_header(self) -> QWidget:
#         card = QFrame()
#         card.setObjectName("Card")
#         layout = QHBoxLayout(card)
#         layout.setContentsMargins(18, 18, 18, 18)

#         title = QLabel("📅 WhatsApp Message Scheduler")
#         title.setStyleSheet("font-size: 20px; font-weight: 700; color: black")
#         subtitle = QLabel("Schedule messages to be sent automatically at a chosen date & time")
#         subtitle.setStyleSheet("color: #6b7280; margin-top: 2px;")

#         title_col = QVBoxLayout()
#         title_col.addWidget(title)
#         title_col.addWidget(subtitle)

#         layout.addLayout(title_col, stretch=1)
#         layout.addStretch(1)

#         self.persist_session_chk = QCheckBox("Use persistent WhatsApp session")
#         self.persist_session_chk.setStyleSheet("font-weight: 700; color: black")
#         self.persist_session_chk.setChecked(True)
#         layout.addWidget(self.persist_session_chk)

#         return card

#     # ---------- Form Card ----------
#     def _build_form_card(self) -> QWidget:
#         card = QFrame()
#         card.setObjectName("Card")
#         v = QVBoxLayout(card)
#         v.setContentsMargins(18, 18, 18, 18)
#         v.setSpacing(12)

#         # Row 1: Name & Number
#         row1 = QHBoxLayout()
#         self.name_edit = QLineEdit()
#         self.name_edit.setPlaceholderText("Contact name (exact as in WhatsApp)")
#         self.number_edit = QLineEdit()
#         self.number_edit.setPlaceholderText("Phone number with country code e.g. +237680785677")
#         row1.addWidget(self._labeled("Name", self.name_edit))
        
#         row1.addSpacing(12)
#         row1.addWidget(self._labeled("Number", self.number_edit))
#         self.number_edit.setStyleSheet("font-weight: 200; color: black")

#         # Row 2: Message
#         self.message_edit = QTextEdit()
#         self.message_edit.setPlaceholderText("Type the message to send…")
#         self.message_edit.setFixedHeight(110)
#         msg_box = self._labeled("Message", self.message_edit)
#         self.message_edit.setStyleSheet("font-weight: 200; color: black")

#         # Row 3: DateTime & Action
#         row3 = QHBoxLayout()
#         self.datetime_edit = QDateTimeEdit(QDateTime.currentDateTime())
#         self.datetime_edit.setCalendarPopup(True)
#         self.datetime_edit.setDisplayFormat("yyyy-MM-dd HH:mm")
#         row3.addWidget(self._labeled("Send Date & Time", self.datetime_edit))

#         row3.addSpacing(12)
#         self.schedule_btn = QPushButton("Schedule Message")
#         self.schedule_btn.setObjectName("PrimaryBtn")
#         self.schedule_btn.setIcon(self.style().standardIcon(QStyle.SP_ArrowRight))
#         self.schedule_btn.clicked.connect(self._on_schedule_clicked)
#         row3.addWidget(self.schedule_btn, stretch=0)
#         row3.addStretch(1)

#         v.addLayout(row1)
#         v.addWidget(msg_box)
#         v.addLayout(row3)

#         return card

#     def _labeled(self, label: str, widget: QWidget) -> QWidget:
#         box = QVBoxLayout()
#         lbl = QLabel(label)
#         lbl.setStyleSheet("font-weight: 600; margin-bottom: 6px; color: black")
#         container = QWidget()
#         inner = QVBoxLayout(container)
#         inner.setContentsMargins(0, 0, 0, 0)
#         inner.addWidget(widget)
#         box.addWidget(lbl)
#         box.addWidget(container)
#         holder = QWidget()
#         holder.setLayout(box)
#         return holder

#     # ---------- Log Card ----------
#     def _build_log_card(self) -> QWidget:
#         card = QFrame()
#         card.setObjectName("Card")
#         v = QVBoxLayout(card)
#         v.setContentsMargins(18, 18, 18, 18)
#         v.setSpacing(10)

#         lbl = QLabel("Log")
#         lbl.setStyleSheet("font-weight: 700; color: black;")
#         self.log_box = QTextEdit()
#         self.log_box.setReadOnly(True)
#         self.log_box.setObjectName("LogBox")
#         self.log_box.setPlaceholderText("Logs will appear here…")

#         v.addWidget(lbl)
#         v.addWidget(self.log_box)
#         return card

#     # ---------- Table Card ----------
#     def _build_table_card(self) -> QWidget:
#         card = QFrame()
#         card.setObjectName("Card")
#         v = QVBoxLayout(card)
#         v.setContentsMargins(18, 18, 18, 18)
#         v.setSpacing(10)

#         header = QHBoxLayout()
#         title = QLabel("Scheduled Messages")
#         title.setStyleSheet("font-weight: 700; color: black;")
#         header.addWidget(title)
#         header.addStretch(1)

#         self.table = QTableWidget(0, 7)
#         self.table.setHorizontalHeaderLabels([
#             "ID", "Name", "Number", "Send Time", "Status", "Message", "Actions"
#         ])
#         self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#         self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
#         self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
#         self.table.verticalHeader().setVisible(False)
#         self.table.setAlternatingRowColors(True)

#         v.addLayout(header)
#         v.addWidget(self.table)
#         return card

#     # ---------- Actions ----------
#     @Slot()
#     def _on_schedule_clicked(self):
#         name = self.name_edit.text().strip()
#         number = self.number_edit.text().strip()
#         message = self.message_edit.toPlainText().strip()
#         dt = self.datetime_edit.dateTime()
#         send_dt = dt.toPython()  # datetime

#         # Basic validation
#         if not (name or number):
#             self._warn("Please enter a contact name or phone number.")
#             return
#         if not message:
#             self._warn("Please enter a message to send.")
#             return
#         if send_dt <= datetime.now():
#             self._warn("Please choose a future date & time.")
#             return

#         job = ScheduledJob(
#             id=str(uuid.uuid4())[:8],
#             name=name,
#             number=number,
#             message=message,
#             send_time_iso=send_dt.isoformat(timespec="minutes"),
#             status="Scheduled"
#         )

#         # Update UI table immediately
#         self._append_job_row(job)

#         # Emit to the (future) scheduler layer
#         payload = asdict(job)
#         payload["persist_session"] = self.persist_session_chk.isChecked()
#         self.scheduleRequested.emit(payload)

#         self._log(f"🗓️ Scheduled message to {job.name or job.number} at {send_dt.strftime('%Y-%m-%d %H:%M')}.")
#         self._clear_form()

#     def _append_job_row(self, job: ScheduledJob):
#         self.jobs.append(job)
#         row = self.table.rowCount()
#         self.table.insertRow(row)

#         self.table.setItem(row, 0, QTableWidgetItem(job.id))
#         self.table.setItem(row, 1, QTableWidgetItem(job.name))
#         self.table.setItem(row, 2, QTableWidgetItem(job.number))
#         self.table.setItem(row, 3, QTableWidgetItem(job.send_dt.strftime('%Y-%m-%d %H:%M')))
#         self.table.setItem(row, 4, QTableWidgetItem(job.status))

#         # Truncate message in table for readability
#         msg_preview = (job.message[:60] + '…') if len(job.message) > 60 else job.message
#         self.table.setItem(row, 5, QTableWidgetItem(msg_preview))

#         # Actions cell with Edit/Delete buttons
#         action_widget = QWidget()
#         h = QHBoxLayout(action_widget)
#         h.setContentsMargins(0, 0, 0, 0)
#         h.setSpacing(6)
#         btn_edit = QPushButton("Edit")
#         btn_edit.setObjectName("GhostBtn")
#         btn_edit.setProperty("job_id", job.id)
#         btn_edit.clicked.connect(lambda: self._on_edit_job(job.id))
#         btn_del = QPushButton("Delete")
#         btn_del.setObjectName("DangerBtn")
#         btn_del.setProperty("job_id", job.id)
#         btn_del.clicked.connect(lambda: self._on_delete_job(job.id))
#         h.addWidget(btn_edit)
#         h.addWidget(btn_del)
#         h.addStretch(1)
#         self.table.setCellWidget(row, 6, action_widget)

#     @Slot()
#     def _on_delete_job(self, job_id: str):
#         idx = next((i for i, j in enumerate(self.jobs) if j.id == job_id), -1)
#         if idx == -1:
#             return
#         job = self.jobs[idx]
#         confirm = QMessageBox.question(
#             self, "Delete Scheduled Job",
#             f"Delete the scheduled message to {job.name or job.number} at {job.send_dt.strftime('%Y-%m-%d %H:%M')}?",
#             QMessageBox.Yes | QMessageBox.No,
#             QMessageBox.No
#         )
#         if confirm != QMessageBox.Yes:
#             return
#         self.jobs.pop(idx)
#         self._refresh_table()
#         self.deleteRequested.emit(job_id)
#         self._log(f"🗑️ Deleted scheduled job {job_id}.")

#     @Slot()
#     def _on_edit_job(self, job_id: str):
#         # Phase 2: open an edit dialog; for now, just notify
#         self._log(f"✏️ Edit requested for job {job_id} (to be implemented).")
#         self.editRequested.emit(job_id)

#     def _refresh_table(self):
#         self.table.setRowCount(0)
#         for job in self.jobs:
#             self._append_job_row(job)

#     def _clear_form(self):
#         # Keep name/number to allow batching; clear message by default
#         self.message_edit.clear()
#         self.datetime_edit.setDateTime(QDateTime.currentDateTime())

#     def _apply_style(self):
#         self.setStyleSheet(SOFT_QSS)

#     # ---------- Logging & Alerts ----------
#     def _log(self, text: str):
#         ts = datetime.now().strftime('%H:%M:%S')
#         self.log_box.append(f"[{ts}] {text}")

#     def _warn(self, text: str):
#         QMessageBox.warning(self, "Validation", text)
#         self._log(f"⚠️ {text}")


# # ------------------------------
# # App bootstrap
# # ------------------------------
# def main():
#     app = QApplication(sys.argv)
#     win = MainWindow()
#     win.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()





# from PySide6.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
#     QLineEdit, QTextEdit, QPushButton, QCheckBox, QDateTimeEdit,
#     QTableWidget, QTableWidgetItem, QMessageBox
# )
# from PySide6.QtCore import Qt, QDateTime
# import sys
# import datetime

# from job_scheduler import JobScheduler 

# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("WhatsApp Scheduler")

#         # Scheduler
#         self.scheduler = JobScheduler(ui_callback=self.log_message)
#         self.scheduler.load_jobs()
#         self.scheduler.start()

#         # Layout
#         layout = QVBoxLayout()

#         # --- Input Fields ---
#         self.chat_input = QLineEdit()
#         self.message_input = QTextEdit()
#         self.datetime_input = QDateTimeEdit(QDateTime.currentDateTime())
#         self.datetime_input.setCalendarPopup(True)
#         self.persistent_check = QCheckBox("Use Persistent Session")

#         add_btn = QPushButton("➕ Schedule Message")
#         add_btn.clicked.connect(self.add_job)

#         layout.addWidget(QLabel("Chat Name / Number:"))
#         layout.addWidget(self.chat_input)
#         layout.addWidget(QLabel("Message:"))
#         layout.addWidget(self.message_input)
#         layout.addWidget(QLabel("Date & Time:"))
#         layout.addWidget(self.datetime_input)
#         layout.addWidget(self.persistent_check)
#         layout.addWidget(add_btn)

#         # --- Jobs Table ---
#         self.jobs_table = QTableWidget(0, 4)
#         self.jobs_table.setHorizontalHeaderLabels(["Chat", "Message", "Datetime", "Status"])
#         layout.addWidget(self.jobs_table)

#         self.setLayout(layout)
#         self.refresh_table()

#     def add_job(self):
#         chat = self.chat_input.text().strip()
#         msg = self.message_input.toPlainText().strip()
#         dt = self.datetime_input.dateTime().toString("yyyy-MM-dd HH:mm")
#         persistent = self.persistent_check.isChecked()

#         if not chat or not msg:
#             QMessageBox.warning(self, "Error", "Chat name and message required")
#             return

#         job = {
#             "chat_name": chat,
#             "message": msg,
#             "datetime": dt,
#             "persistent": persistent,
#             "done": False
#         }

#         self.scheduler.add_job(job)
#         self.refresh_table()
#         self.log_message(f"✅ Scheduled job for {chat} at {dt}")

#     def refresh_table(self):
#         self.scheduler.load_jobs()
#         self.jobs_table.setRowCount(len(self.scheduler.jobs))
#         for i, job in enumerate(self.scheduler.jobs):
#             self.jobs_table.setItem(i, 0, QTableWidgetItem(job["chat_name"]))
#             self.jobs_table.setItem(i, 1, QTableWidgetItem(job["message"]))
#             self.jobs_table.setItem(i, 2, QTableWidgetItem(job["datetime"]))
#             status = "✅ Done" if job.get("done") else "⏳ Pending"
#             self.jobs_table.setItem(i, 3, QTableWidgetItem(status))

#     def log_message(self, text):
#         print(text)  # can also connect to a UI log panel

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())





# from PySide6.QtWidgets import (
#     QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
#     QLineEdit, QTextEdit, QPushButton, QCheckBox, QDateTimeEdit,
#     QTableWidget, QTableWidgetItem, QMessageBox, QTabWidget, QAbstractItemView
# )
# from PySide6.QtCore import Qt, QDateTime
# import sys
# import datetime

# from job_scheduler import JobScheduler
# # Later we will import: from contacts_manager import ContactsManager


# class MainWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("WhatsApp Scheduler")

#         # Scheduler
#         self.scheduler = JobScheduler(ui_callback=self.log_message)
#         self.scheduler.load_jobs()
#         self.scheduler.start()

#         # Tabs
#         tabs = QTabWidget()

#         # --- Scheduler Tab ---
#         scheduler_tab = QWidget()
#         scheduler_layout = QVBoxLayout()

#         self.chat_input = QLineEdit()
#         self.message_input = QTextEdit()
#         self.datetime_input = QDateTimeEdit(QDateTime.currentDateTime())
#         self.datetime_input.setCalendarPopup(True)
#         self.persistent_check = QCheckBox("Use Persistent Session")

#         add_btn = QPushButton("➕ Schedule Message")
#         add_btn.clicked.connect(self.add_job)

#         scheduler_layout.addWidget(QLabel("Chat Name / Number:"))
#         scheduler_layout.addWidget(self.chat_input)
#         scheduler_layout.addWidget(QLabel("Message:"))
#         scheduler_layout.addWidget(self.message_input)
#         scheduler_layout.addWidget(QLabel("Date & Time:"))
#         scheduler_layout.addWidget(self.datetime_input)
#         scheduler_layout.addWidget(self.persistent_check)
#         scheduler_layout.addWidget(add_btn)

#         # Jobs Table
#         self.jobs_table = QTableWidget(0, 4)
#         self.jobs_table.setHorizontalHeaderLabels(["Chat", "Message", "Datetime", "Status"])
#         scheduler_layout.addWidget(self.jobs_table)

#         scheduler_tab.setLayout(scheduler_layout)
#         tabs.addTab(scheduler_tab, "Scheduler")

#         # --- Contacts Tab ---
#         contacts_tab = QWidget()
#         contacts_layout = QVBoxLayout()

#         # Search bar
#         search_layout = QHBoxLayout()
#         self.search_input = QLineEdit()
#         self.search_input.setPlaceholderText("🔍 Search by name, department, or tag...")
#         search_btn = QPushButton("Search")
#         search_btn.clicked.connect(self.search_contacts)
#         search_layout.addWidget(self.search_input)
#         search_layout.addWidget(search_btn)

#         contacts_layout.addLayout(search_layout)

#         # Contacts table
#         self.contacts_table = QTableWidget(0, 4)
#         self.contacts_table.setHorizontalHeaderLabels(["Name", "Phone", "Department", "Tag"])
#         self.contacts_table.setSelectionBehavior(QAbstractItemView.SelectRows)
#         self.contacts_table.setSelectionMode(QAbstractItemView.MultiSelection)
#         contacts_layout.addWidget(self.contacts_table)

#         # Action buttons
#         btn_layout = QHBoxLayout()
#         add_contact_btn = QPushButton("➕ Add Contact")
#         edit_contact_btn = QPushButton("✏️ Edit Contact")
#         delete_contact_btn = QPushButton("🗑 Delete Contact")
#         use_contact_btn = QPushButton("📩 Use Selected")

#         add_contact_btn.clicked.connect(self.add_contact)
#         edit_contact_btn.clicked.connect(self.edit_contact)
#         delete_contact_btn.clicked.connect(self.delete_contact)
#         use_contact_btn.clicked.connect(self.use_selected_contacts)

#         btn_layout.addWidget(add_contact_btn)
#         btn_layout.addWidget(edit_contact_btn)
#         btn_layout.addWidget(delete_contact_btn)
#         btn_layout.addWidget(use_contact_btn)

#         contacts_layout.addLayout(btn_layout)

#         contacts_tab.setLayout(contacts_layout)
#         tabs.addTab(contacts_tab, "Contacts")

#         # Main Layout
#         main_layout = QVBoxLayout()
#         main_layout.addWidget(tabs)
#         self.setLayout(main_layout)

#         # Initialize
#         self.refresh_table()
#         self.load_contacts()

#     # ---------------- Scheduler ---------------- #
#     def add_job(self):
#         chat = self.chat_input.text().strip()
#         msg = self.message_input.toPlainText().strip()
#         dt = self.datetime_input.dateTime().toString("yyyy-MM-dd HH:mm")
#         persistent = self.persistent_check.isChecked()

#         if not chat or not msg:
#             QMessageBox.warning(self, "Error", "Chat name and message required")
#             return

#         job = {
#             "chat_name": chat,
#             "message": msg,
#             "datetime": dt,
#             "persistent": persistent,
#             "done": False
#         }

#         self.scheduler.add_job(job)
#         self.refresh_table()
#         self.log_message(f"✅ Scheduled job for {chat} at {dt}")

#     def refresh_table(self):
#         self.scheduler.load_jobs()
#         self.jobs_table.setRowCount(len(self.scheduler.jobs))
#         for i, job in enumerate(self.scheduler.jobs):
#             self.jobs_table.setItem(i, 0, QTableWidgetItem(job["chat_name"]))
#             self.jobs_table.setItem(i, 1, QTableWidgetItem(job["message"]))
#             self.jobs_table.setItem(i, 2, QTableWidgetItem(job["datetime"]))
#             status = "✅ Done" if job.get("done") else "⏳ Pending"
#             self.jobs_table.setItem(i, 3, QTableWidgetItem(status))

#     # ---------------- Contacts ---------------- #
#     def load_contacts(self, filter_text=None):
#         """
#         Placeholder: Will load contacts from contacts_manager (SQLite).
#         For now, we simulate with dummy data.
#         """
#         dummy_contacts = [
#             {"name": "Alice", "phone": "+123456789", "department": "HR", "tag": "Manager"},
#             {"name": "Bob", "phone": "+987654321", "department": "IT", "tag": "Engineer"},
#         ]
#         self.contacts_table.setRowCount(len(dummy_contacts))
#         for i, c in enumerate(dummy_contacts):
#             self.contacts_table.setItem(i, 0, QTableWidgetItem(c["name"]))
#             self.contacts_table.setItem(i, 1, QTableWidgetItem(c["phone"]))
#             self.contacts_table.setItem(i, 2, QTableWidgetItem(c["department"]))
#             self.contacts_table.setItem(i, 3, QTableWidgetItem(c["tag"]))

#     def search_contacts(self):
#         query = self.search_input.text().strip()
#         self.load_contacts(filter_text=query)

#     def add_contact(self):
#         QMessageBox.information(self, "Info", "➕ Add Contact dialog will open (to be implemented)")

#     def edit_contact(self):
#         QMessageBox.information(self, "Info", "✏️ Edit Contact dialog will open (to be implemented)")

#     def delete_contact(self):
#         QMessageBox.information(self, "Info", "🗑 Delete Contact will be handled (to be implemented)")

#     def use_selected_contacts(self):
#         selected = self.contacts_table.selectionModel().selectedRows()
#         phones = []
#         for row in selected:
#             phone_item = self.contacts_table.item(row.row(), 1)
#             if phone_item:
#                 phones.append(phone_item.text())
#         if phones:
#             self.chat_input.setText(", ".join(phones))

#     def log_message(self, text):
#         print(text)  # can also connect to a UI log panel


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec())


from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QTextEdit, QPushButton, QCheckBox, QDateTimeEdit,
    QTableWidget, QTableWidgetItem, QMessageBox, QTabWidget, QAbstractItemView, QHeaderView,
    QInputDialog
)
from PySide6.QtCore import Qt, QDateTime
import sys
import requests
from job_scheduler import JobScheduler
from contacts_manager import ContactsManager   

BASE_URL = "http://127.0.0.1:8000/auth"
qss_stle="""

QWidget {
    font-family: "Segoe UI", "Roboto", "Helvetica Neue", sans-serif;
    font-size: 14px;
    color: #2c3e50;
    /* background-color: #f5f6fa;*/
    background-color: #cacaca;
}


QPushButton {
    background-color: #3498db;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    font-weight: bold;
}
QPushButton:hover {
    background-color: #2980b9;
}
QPushButton:pressed {
    background-color: #2471a3;
}

/* Special Icon Buttons (like ➕ or 🗑) */
QPushButton[text^="➕"], QPushButton[text^="✏️"], QPushButton[text^="🗑"], QPushButton[text^="📩"] {
    background-color: #2ecc71;
}
QPushButton[text^="✏️"] {
    background-color: #f1c40f;
}
QPushButton[text^="🗑"] {
    background-color: #e74c3c;
}
QPushButton[text^="📩"] {
    background-color: #9b59b6;
}
QPushButton[text^="➕"]:hover,
QPushButton[text^="✏️"]:hover,
QPushButton[text^="🗑"]:hover,
QPushButton[text^="📩"]:hover {
    
}

/* ==== QLineEdit & QTextEdit ==== */
QLineEdit, QTextEdit, QDateTimeEdit {
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 4px;
    padding: 6px;
}
QLineEdit:focus, QTextEdit:focus, QDateTimeEdit:focus {
    border: 1px solid #3498db;
    background-color: #ecf0f1;
}

/* ==== QCheckBox ==== */
QCheckBox {
    spacing: 5px;
}
QCheckBox::indicator {
    width: 16px;
    height: 16px;
}
QCheckBox::indicator:checked {
    image: url(:/qt-project.org/styles/commonstyle/images/checkbox_checked.png);
}

/* ==== TABLES ==== */
QTableWidget {
    border: 1px solid #ccc;
    background-color: white;
    gridline-color: #ddd;
    border-radius: 4px;
}
QHeaderView::section {
    background-color: #34495e;
    color: white;
    padding: 6px;
    font-weight: bold;
    border: none;
}
QTableWidget::item:selected {
    background-color: #dff9fb;
}

/* ==== TABS ==== */
QTabWidget::pane {
    border: 1px solid #ccc;
    padding: 6px;
    background: white;
}
QTabBar::tab {
    background: #cacaca;
    padding: 8px 20px;
    font-weight: bold;
    margin-right: 2px;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
}
QTabBar::tab:selected {
    background: white;
    font-weight: bold;
    color: #3498db;
}

/* ==== QDialogs (QInputDialog, QMessageBox) ==== */
QMessageBox, QInputDialog {
    background-color: #ffffff;
    font-size: 14px;
}



"""

class whatsapp_automation_MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp Scheduler")
        

        # Scheduler
        self.scheduler = JobScheduler(ui_callback=self.log_message)
        self.scheduler.load_jobs()
        self.scheduler.start()
        self._apply_style()
        
        # Contacts Manager (SQLite)
        self.cm = ContactsManager()

        # Tabs
        tabs = QTabWidget()

        # --- Scheduler Tab ---
        scheduler_tab = QWidget()
        scheduler_layout = QVBoxLayout()

        self.chat_input = QLineEdit()
        self.message_input = QTextEdit()
        self.datetime_input = QDateTimeEdit(QDateTime.currentDateTime())
        self.datetime_input.setCalendarPopup(True)
        self.persistent_check = QCheckBox("Use Persistent Session")

        add_btn = QPushButton("➕ Schedule Message")
        add_btn.clicked.connect(self.add_job)

        scheduler_layout.addWidget(QLabel("Chat Name / Number:"))
        scheduler_layout.addWidget(self.chat_input)
        scheduler_layout.addWidget(QLabel("Message:"))
        scheduler_layout.addWidget(self.message_input)
        scheduler_layout.addWidget(QLabel("Date & Time:"))
        scheduler_layout.addWidget(self.datetime_input)
        scheduler_layout.addWidget(self.persistent_check)
        scheduler_layout.addWidget(add_btn)

        # Jobs Table
        self.jobs_table = QTableWidget(0, 4)
        self.jobs_table.setHorizontalHeaderLabels(["Chat", "Message", "Datetime", "Status"])
        scheduler_layout.addWidget(self.jobs_table)

        scheduler_tab.setLayout(scheduler_layout)
        tabs.addTab(scheduler_tab, "Scheduler")

        # --- Contacts Tab ---
        contacts_tab = QWidget()
        contacts_layout = QVBoxLayout()

        # Search bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("🔍 Search by name, department, or tag...")
        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.search_contacts)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_btn)
        contacts_layout.addLayout(search_layout)

        # Contacts table
        self.contacts_table = QTableWidget(0, 4)
        self.contacts_table.setHorizontalHeaderLabels(["Name", "Phone", "Department", "Tag"])
        self.contacts_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.contacts_table.setSelectionMode(QAbstractItemView.MultiSelection)
        contacts_layout.addWidget(self.contacts_table)

        # Action buttons
        btn_layout = QHBoxLayout()
        add_contact_btn = QPushButton("➕ Add Contact")
        edit_contact_btn = QPushButton("✏️ Edit Contact")
        delete_contact_btn = QPushButton("🗑 Delete Contact")
        use_contact_btn = QPushButton("📩 Use Selected")

        add_contact_btn.clicked.connect(self.add_contact)
        edit_contact_btn.clicked.connect(self.edit_contact)
        delete_contact_btn.clicked.connect(self.delete_contact)
        use_contact_btn.clicked.connect(self.use_selected_contacts)

        btn_layout.addWidget(add_contact_btn)
        btn_layout.addWidget(edit_contact_btn)
        btn_layout.addWidget(delete_contact_btn)
        btn_layout.addWidget(use_contact_btn)
        contacts_layout.addLayout(btn_layout)

        contacts_tab.setLayout(contacts_layout)
        tabs.addTab(contacts_tab, "Contacts")

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(tabs)
        self.setLayout(main_layout)
        
        
        # --- Patients Tab --- #
        patients_tab = QWidget()
        patients_layout = QVBoxLayout()

        # Table for displaying patients
        self.tableWidget = QTableWidget(0, 8)
        self.tableWidget.setHorizontalHeaderLabels([
            "ID", "Name", "Email", "Contact", "Address", "Profession", "Age", "Gender"
        ])
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        patients_layout.addWidget(self.tableWidget)

        # refresh button
        refresh_btn = QPushButton("🔄 Refresh Patients")
        refresh_btn.clicked.connect(self.load_patients)
        patients_layout.addWidget(refresh_btn)
        
        # use selected button
        use_contact_btn = QPushButton("📩 Use Selected")
        use_contact_btn.clicked.connect(self.use_selected_patients)
        patients_layout.addWidget(use_contact_btn)
        
        patients_tab.setLayout(patients_layout)
        tabs.addTab(patients_tab, "Patients")

        # Initialize
        self.refresh_table()
        self.load_contacts()
        self.load_patients()

    # ---------------- Scheduler ---------------- #
    def add_job(self):
        chat = self.chat_input.text().strip()
        msg = self.message_input.toPlainText().strip()
        dt = self.datetime_input.dateTime().toString("yyyy-MM-dd HH:mm")
        persistent = self.persistent_check.isChecked()

        if not chat or not msg:
            QMessageBox.warning(self, "Error", "Chat name and message required")
            return

        job = {
            "chat_name": chat,
            "message": msg,
            "datetime": dt,
            "persistent": persistent,
            "done": False
        }

        self.scheduler.add_job(job)
        self.refresh_table()
        self.log_message(f"✅ Scheduled job for {chat} message:{msg} at {dt}")

    def refresh_table(self):
        self.jobs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)        
        self.scheduler.load_jobs()
        self.jobs_table.setRowCount(len(self.scheduler.jobs))
        for i, job in enumerate(self.scheduler.jobs):
            self.jobs_table.setItem(i, 0, QTableWidgetItem(job["chat_name"]))
            self.jobs_table.setItem(i, 1, QTableWidgetItem(job["message"]))
            self.jobs_table.setItem(i, 2, QTableWidgetItem(job["datetime"]))
            status = "✅ Done" if job.get("done") else "⏳ Pending"
            self.jobs_table.setItem(i, 3, QTableWidgetItem(status))

    # ---------------- Contacts ---------------- #
    def load_contacts(self, filter_text=None):
        self.contacts_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        if filter_text:
            contacts = self.cm.search_contacts(filter_text)
        else:
            contacts = self.cm.list_contacts()

        self.contacts_table.setRowCount(len(contacts))
        for i, c in enumerate(contacts):
            self.contacts_table.setItem(i, 0, QTableWidgetItem(c["name"]))
            self.contacts_table.setItem(i, 1, QTableWidgetItem(c["phone"]))
            self.contacts_table.setItem(i, 2, QTableWidgetItem(c["department"] or ""))
            self.contacts_table.setItem(i, 3, QTableWidgetItem(c["tag"] or ""))

    def search_contacts(self):
        query = self.search_input.text().strip()
        self.load_contacts(filter_text=query)

    def add_contact(self):
        name, ok = QInputDialog.getText(self, "Add Contact", "Enter Name:")
        if not ok or not name.strip():
            return
        phone, ok = QInputDialog.getText(self, "Add Contact", "Enter Phone:")
        if not ok or not phone.strip():
            return
        department, _ = QInputDialog.getText(self, "Add Contact", "Enter Department (optional):")
        tag, _ = QInputDialog.getText(self, "Add Contact", "Enter Tag (optional):")

        self.cm.add_contact(name.strip(), phone.strip(), department.strip(), tag.strip())
        self.load_contacts()

    def edit_contact(self):
        selected = self.contacts_table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self, "Error", "Select a contact to edit")
            return

        row = selected[0].row()
        contact_id = self.cm.list_contacts()[row]["id"]

        name, _ = QInputDialog.getText(self, "Edit Contact", "Edit Name:", text=self.contacts_table.item(row, 0).text())
        phone, _ = QInputDialog.getText(self, "Edit Contact", "Edit Phone:", text=self.contacts_table.item(row, 1).text())
        department, _ = QInputDialog.getText(self, "Edit Contact", "Edit Department:", text=self.contacts_table.item(row, 2).text())
        tag, _ = QInputDialog.getText(self, "Edit Contact", "Edit Tag:", text=self.contacts_table.item(row, 3).text())

        self.cm.edit_contact(contact_id, name.strip(), phone.strip(), department.strip(), tag.strip())
        self.load_contacts()

    def delete_contact(self):
        selected = self.contacts_table.selectionModel().selectedRows()
        if not selected:
            QMessageBox.warning(self, "Error", "Select at least one contact to delete")
            return

        for row in selected:
            contact_id = self.cm.list_contacts()[row.row()]["id"]
            self.cm.delete_contact(contact_id)

        self.load_contacts()

    def use_selected_contacts(self):
        selected = self.contacts_table.selectionModel().selectedRows()
        phones = []
        for row in selected:
            phone_item = self.contacts_table.item(row.row(), 0)
            if phone_item:
                phones.append(phone_item.text())
        if phones:
            self.chat_input.setText(", ".join(phones))
            
    # ---------------- Patients ---------------- #
    def use_selected_patients(self):
        selected = self.tableWidget.selectionModel().selectedRows()
        contacts = []
        for row in selected:
            contact_item = self.tableWidget.item(row.row(), 1)  # Assuming 'Contact' is the 4th column
            if contact_item:
                contacts.append(contact_item.text())
        if contacts:
            self.chat_input.setText(", ".join(contacts))

    def log_message(self, text):
        print(text)  # could be extended to UI log
        # QMessageBox.information(self, "Log", text)

    def _apply_style(self):
        self.setStyleSheet(qss_stle)

    def load_patients(self):
        try:
            response = requests.get(f"{BASE_URL}/patients/list/")
            if response.status_code == 200:
                self.update_table(response.json().get('patients', []))
            else:
                QMessageBox.warning(self, "Error", "Failed to load patients.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def get_value(self, val):
        return str(val) if val not in (None, '', 'null') else 'N/A'

    def update_table(self, patients):
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        for patient in patients:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(self.get_value(patient.get('id'))))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(self.get_value(patient.get('name'))))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(self.get_value(patient.get('email'))))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(self.get_value(patient.get('contact'))))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(self.get_value(patient.get('address'))))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(self.get_value(patient.get('profession'))))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(self.get_value(patient.get('age'))))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(self.get_value(patient.get('gender'))))

        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.sortItems(1, Qt.SortOrder.AscendingOrder)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = whatsapp_automation_MainWindow()
    window.show()
    sys.exit(app.exec())
