# # send_mail.py
# from PySide6.QtWidgets import (
#     QDialog, QLabel, QLineEdit, QTextEdit, QPushButton,
#     QListWidget, QListWidgetItem, QFileDialog, QVBoxLayout,
#     QHBoxLayout, QWidget, QMessageBox
# )
# from PySide6.QtCore import Qt, Signal

# class SendMailDialog(QDialog):
#     mailSent = Signal(dict)      # Emit mail {recipients, subject, message, attachments}

#     def __init__(self, people_list: list, parent=None):
#         """
#         people_list: list of registered people (str names or dicts)
#         """
#         super().__init__(parent)
#         self.setWindowTitle("Send Mail")
#         self.setMinimumSize(580, 480)

#         self.people_list = people_list
#         self.attachments = []

#         self.apply_styles()
#         self.build_ui()

#     # ------------------------------------------------------------
#     # UI BUILDING
#     # ------------------------------------------------------------
#     def build_ui(self):
#         layout = QVBoxLayout()

#         # Title
#         title = QLabel("Compose Mail")
#         title.setStyleSheet("font-size: 22px; font-weight: bold; color: #1565C0;")
#         layout.addWidget(title)

#         # Recipients List
#         rec_label = QLabel("Select Recipients:")
#         layout.addWidget(rec_label)

#         self.recipient_list = QListWidget()
#         self.recipient_list.setSelectionMode(QListWidget.MultiSelection)

#         for person in self.people_list:
#             item = QListWidgetItem(person)
#             self.recipient_list.addItem(item)

#         self.recipient_list.setStyleSheet("background: #F7F9FC; padding: 5px; color: black;")
#         layout.addWidget(self.recipient_list)

#         # Subject
#         subject_label = QLabel("Subject:")
#         layout.addWidget(subject_label)

#         self.subject_input = QLineEdit()
#         self.subject_input.setPlaceholderText("Enter email subject…")
#         layout.addWidget(self.subject_input)

#         # Message Body
#         msg_label = QLabel("Message:")
#         layout.addWidget(msg_label)

#         self.message_input = QTextEdit()
#         self.message_input.setPlaceholderText("Write your message here…")
#         layout.addWidget(self.message_input)

#         # Attachments Button
#         attach_btn = QPushButton("Attach File")
#         attach_btn.clicked.connect(self.pick_attachment)
#         attach_btn.setStyleSheet("background: #42A5F5; color: white; padding: 8px; border-radius: 8px;")
#         layout.addWidget(attach_btn)

#         # Action Buttons (Send / Cancel)
#         btn_layout = QHBoxLayout()

#         cancel_btn = QPushButton("Cancel")
#         cancel_btn.clicked.connect(self.reject)
#         cancel_btn.setStyleSheet("background: #CFD8DC; padding: 8px; border-radius: 8px;")

#         send_btn = QPushButton("Send Mail")
#         send_btn.clicked.connect(self.send_mail)
#         send_btn.setStyleSheet("background: #1E88E5; color: white; padding: 8px; border-radius: 8px;")

#         btn_layout.addWidget(cancel_btn)
#         btn_layout.addWidget(send_btn)

#         layout.addLayout(btn_layout)
#         self.setLayout(layout)

#     # ------------------------------------------------------------
#     # STYLING
#     # ------------------------------------------------------------
#     def apply_styles(self):
#         self.setStyleSheet("""
#             QDialog {
#                 background: #FFFFFF;
#             }
#             QLabel {
#                 color: #0A273B;
#                 font-size: 15px;
#                 margin-top: 10px;
#             }
#             QLineEdit, QTextEdit {
#                 border: 1px solid #B0C4DE;
#                 border-radius: 10px;
#                 padding: 8px;
#                 background: #FFFFFF;
#                 font-size: 14px;
#                 color: black;
#             }
#             QPushButton:hover {
#                 opacity: 0.85;
#             }
#         """)

#     # ------------------------------------------------------------
#     # FILE PICKER
#     # ------------------------------------------------------------
#     def pick_attachment(self):
#         file, _ = QFileDialog.getOpenFileName(self, "Select File")
#         if file:
#             self.attachments.append(file)
#             QMessageBox.information(self, "Attachment Added", f"Added: {file}")

#     # ------------------------------------------------------------
#     # SEND MAIL HANDLER
#     # ------------------------------------------------------------
#     def send_mail(self):
#         selected = [i.text() for i in self.recipient_list.selectedItems()]
#         subject = self.subject_input.text().strip()
#         message = self.message_input.toPlainText().strip()

#         if not selected:
#             QMessageBox.warning(self, "Empty", "Please select at least one recipient.")
#             return

#         if not subject or not message:
#             QMessageBox.warning(self, "Missing Fields", "Subject and Message cannot be empty.")
#             return

#         mail_data = {
#             "recipients": selected,
#             "subject": subject,
#             "message": message,
#             "attachments": self.attachments
#         }

#         self.mailSent.emit(mail_data)
#         QMessageBox.information(self, "Success", "Mail sent successfully!")
#         self.accept()


# if __name__ == "__main__":
#     import sys
#     from PySide6.QtWidgets import QApplication

#     app = QApplication(sys.argv)

#     # Sample people list
#     people = ["Alice Johnson", "Bob Smith", "Charlie Davis", "Diana Evans"]

#     dialog = SendMailDialog(people)
#     dialog.exec()

# send_mail.py
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import os
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QFrame, QLabel, QPushButton,
    QLineEdit, QListWidget, QListWidgetItem, QTextEdit, QFileDialog,
    QMessageBox, QWidget, QListView
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from backend.person_service import PersonService
from backend.mail_service import MailService
from backend.history_service import HistoryService


# class SendMailDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.setWindowTitle("Send Email")
#         self.setMinimumSize(600, 650)
#         self.setStyleSheet(self.load_styles())

#         self.attachments = []   # store file paths

#         layout = QVBoxLayout(self)
#         layout.setContentsMargins(20, 20, 20, 20)
#         layout.setSpacing(15)

#         # --------------------------------------------------------
#         # HEADER
#         # --------------------------------------------------------
#         header = QLabel("Compose Email")
#         header.setObjectName("header")
#         layout.addWidget(header)

#         # --------------------------------------------------------
#         # RECIPIENT SECTION
#         # --------------------------------------------------------
#         rec_frame = QFrame()
#         rec_layout = QVBoxLayout(rec_frame)
#         rec_layout.setSpacing(8)

#         rec_title = QLabel("Recipients")
#         rec_title.setObjectName("sectionTitle")

#         btn_row = QHBoxLayout()
#         btn_select_all = QPushButton("Select All")
#         btn_select_all.setObjectName("smallBtn")
#         btn_deselect_all = QPushButton("Deselect")
#         btn_deselect_all.setObjectName("smallBtn")

#         btn_row.addWidget(btn_select_all)
#         btn_row.addWidget(btn_deselect_all)
#         btn_row.addStretch()

#         self.recipient_list = QListWidget()
#         self.recipient_list.setSelectionMode(QListWidget.MultiSelection)
#         self.recipient_list.setViewMode(QListView.ListMode)

#         rec_layout.addWidget(rec_title)
#         rec_layout.addLayout(btn_row)
#         rec_layout.addWidget(self.recipient_list)

#         layout.addWidget(rec_frame)

#         # --------------------------------------------------------
#         # SUBJECT
#         # --------------------------------------------------------
#         subject_label = QLabel("Subject")
#         subject_label.setObjectName("sectionTitle")

#         self.subject_input = QLineEdit()
#         self.subject_input.setPlaceholderText("Enter subject")

#         layout.addWidget(subject_label)
#         layout.addWidget(self.subject_input)

#         # --------------------------------------------------------
#         # MESSAGE BODY
#         # --------------------------------------------------------
#         msg_label = QLabel("Message")
#         msg_label.setObjectName("sectionTitle")

#         self.message_editor = QTextEdit()
#         self.message_editor.setPlaceholderText("Write your message here...")

#         layout.addWidget(msg_label)
#         layout.addWidget(self.message_editor)

#         # --------------------------------------------------------
#         # ATTACHMENTS
#         # --------------------------------------------------------
#         attach_layout = QHBoxLayout()

#         self.attach_btn = QPushButton("Add Attachment")
#         self.attach_btn.setObjectName("secondaryBtn")

#         self.attach_list = QLabel("No attachments added")
#         self.attach_list.setWordWrap(True)
#         self.attach_list.setStyleSheet("color: gray;")

#         attach_layout.addWidget(self.attach_btn)
#         attach_layout.addWidget(self.attach_list)

#         layout.addLayout(attach_layout)

#         # --------------------------------------------------------
#         # FOOTER BUTTONS
#         # --------------------------------------------------------
#         footer = QHBoxLayout()

#         send_btn = QPushButton("Send")
#         send_btn.setObjectName("primaryBtn")

#         cancel_btn = QPushButton("Cancel")
#         cancel_btn.setObjectName("secondaryBtn")

#         footer.addStretch()
#         footer.addWidget(cancel_btn)
#         footer.addWidget(send_btn)

#         layout.addLayout(footer)

#         # --------------------------------------------------------
#         # CONNECT SIGNALS
#         # --------------------------------------------------------
#         btn_select_all.clicked.connect(self.select_all)
#         btn_deselect_all.clicked.connect(self.deselect_all)
#         cancel_btn.clicked.connect(self.reject)
#         self.attach_btn.clicked.connect(self.add_attachment)
#         send_btn.clicked.connect(self.send_email)

#         # Load people into list
#         self.load_recipients()

#     # --------------------------------------------------------
#     # LOAD RECIPIENTS FROM DB
#     # --------------------------------------------------------
#     def load_recipients(self):
#         self.recipient_list.clear()

#         people = PersonService.get_all_people()

#         for p in people:
#             item = QListWidgetItem(f"{p['name']}  <{p['email']}>")
#             item.setCheckState(Qt.Unchecked)
#             item.setData(Qt.UserRole, p["email"])   # store pure email
#             self.recipient_list.addItem(item)

#     def select_all(self):
#         for i in range(self.recipient_list.count()):
#             self.recipient_list.item(i).setCheckState(Qt.Checked)

#     def deselect_all(self):
#         for i in range(self.recipient_list.count()):
#             self.recipient_list.item(i).setCheckState(Qt.Unchecked)

#     # --------------------------------------------------------
#     # ATTACHMENTS
#     # --------------------------------------------------------
#     def add_attachment(self):
#         files, _ = QFileDialog.getOpenFileNames(
#             self, "Select Attachments", "", 
#             "All Files (*.*)"
#         )
#         if files:
#             self.attachments.extend(files)
#             self.attach_list.setText("\n".join(os.path.basename(f) for f in self.attachments))

#     # --------------------------------------------------------
#     # SEND EMAIL
#     # --------------------------------------------------------
#     def send_email(self):
#         subject = self.subject_input.text().strip()
#         message = self.message_editor.toPlainText().strip()

#         recipients = [
#             self.recipient_list.item(i).data(Qt.UserRole)
#             for i in range(self.recipient_list.count())
#             if self.recipient_list.item(i).checkState() == Qt.Checked
#         ]

#         if not recipients:
#             QMessageBox.warning(self, "No Recipients", "Please select at least one recipient.")
#             return

#         if not subject:
#             QMessageBox.warning(self, "Missing Subject", "Please enter a subject.")
#             return

#         if not message:
#             QMessageBox.warning(self, "Missing Message", "Please enter a message.")
#             return

#         try:
#             # SEND EMAIL
#             MailService.send_mail(
#                 recipients=recipients,
#                 subject=subject,
#                 message=message,
#                 attachments=self.attachments
#             )

#             # SAVE HISTORY
#             HistoryService.save_mail(
#                 subject=subject,
#                 message=message,
#                 recipients=";".join(recipients),
#                 attachments=";".join(self.attachments)
#             )

#             QMessageBox.information(self, "Success", "Email sent successfully!")
#             self.accept()

#         except Exception as e:
#             QMessageBox.critical(self, "Send Failed", str(e))

#     # --------------------------------------------------------
#     # STYLESHEET
#     # --------------------------------------------------------
#     def load_styles(self):
#         return """
#         #header {
#             font-size: 26px;
#             font-weight: bold;
#             color: #0D47A1;
#         }

#         #sectionTitle {
#             font-size: 15px;
#             font-weight: bold;
#             color: #1565C0;
#         }

#         QPushButton#primaryBtn {
#             background-color: #1565C0;
#             color: white;
#             padding: 8px 18px;
#             border-radius: 6px;
#         }

#         QPushButton#primaryBtn:hover {
#             background-color: #0D47A1;
#         }

#         QPushButton#secondaryBtn {
#             background-color: #E3F2FD;
#             color: #0D47A1;
#             padding: 6px 14px;
#             border-radius: 6px;
#         }

#         QPushButton#secondaryBtn:hover {
#             background-color: #BBDEFB;
#         }

#         QPushButton#smallBtn {
#             background-color: #BBDEFB;
#             color: #0D47A1;
#             padding: 4px 10px;
#             border-radius: 4px;
#         }

#         QListWidget {
#             border: 1px solid #BBDEFB;
#             border-radius: 6px;
#             padding: 5px;
#         }

#         QLineEdit, QTextEdit {
#             border: 1px solid #BBDEFB;
#             border-radius: 6px;
#             padding: 6px;
#         }
#         """

# if __name__ == "__main__":
#     import sys
#     from PySide6.QtWidgets import QApplication

#     app = QApplication(sys.argv)

#     dialog = SendMailDialog()
#     dialog.exec()
    
    
    
# send_mail.py
# from PySide6.QtWidgets import (
#     QDialog, QLabel, QComboBox, QTextEdit, QListWidget,
#     QListWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout,
#     QFormLayout, QMessageBox, QCheckBox
# )
# from PySide6.QtCore import Qt

# from backend.person_service import PersonService
# from backend.mail_service import mail_service
# from backend.history_service import HistoryService


# class SendMailDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)

#         self.setWindowTitle("Send Email")
#         self.setMinimumWidth(500)

#         # --------------------------------------------------------
#         # Widgets
#         # --------------------------------------------------------
#         self.recipient_mode = QComboBox()
#         self.recipient_mode.addItems([
#             "Send to ALL People",
#             "Send to Group",
#             "Select Recipients Manually"
#         ])

#         self.group_selector = QComboBox()
#         self.group_selector.setEnabled(False)

#         self.subject = QTextEdit()
#         self.subject.setFixedHeight(40)

#         self.message = QTextEdit()

#         self.recipient_list = QListWidget()
#         self.recipient_list.setSelectionMode(QListWidget.MultiSelection)
#         self.recipient_list.setEnabled(False)

#         # Buttons
#         self.btnSend = QPushButton("Send Mail")
#         self.btnCancel = QPushButton("Cancel")

#         # --------------------------------------------------------
#         # Layouts
#         # --------------------------------------------------------
#         form = QFormLayout()
#         form.addRow("Recipient Mode:", self.recipient_mode)
#         form.addRow("Select Group:", self.group_selector)
#         form.addRow("Subject:", self.subject)
#         form.addRow("Message:", self.message)
#         form.addRow("Manual Recipients:", self.recipient_list)

#         btns = QHBoxLayout()
#         btns.addStretch()
#         btns.addWidget(self.btnSend)
#         btns.addWidget(self.btnCancel)

#         main = QVBoxLayout(self)
#         main.addLayout(form)
#         main.addLayout(btns)



#         # --------------------------------------------------------
#         # Load People + Groups
#         # --------------------------------------------------------
#         self.load_groups()
#         self.load_people_list()

#         # Signals
#         self.recipient_mode.currentIndexChanged.connect(self.change_recipient_mode)
#         self.btnCancel.clicked.connect(self.reject)
#         self.btnSend.clicked.connect(self.send_email)

#     # --------------------------------------------------------
#     # LOAD GROUPS FOR DROPDOWN
#     # --------------------------------------------------------
#     def load_groups(self):
#         people = PersonService.get_all_people()
#         groups = sorted(set([p["group_name"] for p in people if p["group_name"]]))

#         self.group_selector.clear()
#         self.group_selector.addItems(groups)

#     # --------------------------------------------------------
#     # MANUAL SELECTION LIST
#     # --------------------------------------------------------
#     def load_people_list(self):
#         self.recipient_list.clear()
#         people = PersonService.get_all_people()

#         for p in people:
#             item = QListWidgetItem(f"{p['name']}  ({p['email']})")
#             item.setData(Qt.UserRole, p["email"])
#             item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
#             item.setCheckState(Qt.Unchecked)
#             self.recipient_list.addItem(item)

#     # --------------------------------------------------------
#     # Mode switch
#     # --------------------------------------------------------
#     def change_recipient_mode(self):
#         mode = self.recipient_mode.currentIndex()

#         # ALL → disable everything else
#         if mode == 0:
#             self.group_selector.setEnabled(False)
#             self.recipient_list.setEnabled(False)

#         # GROUP
#         elif mode == 1:
#             self.group_selector.setEnabled(True)
#             self.recipient_list.setEnabled(False)

#         # MANUAL SELECT
#         else:
#             self.group_selector.setEnabled(False)
#             self.recipient_list.setEnabled(True)

#     # --------------------------------------------------------
#     # RESOLVE RECIPIENTS BASED ON MODE
#     # --------------------------------------------------------
#     def get_recipients(self):
#         mode = self.recipient_mode.currentIndex()
#         people = PersonService.get_all_people()

#         # ALL
#         if mode == 0:
#             return [p["email"] for p in people]

#         # GROUP
#         if mode == 1:
#             group = self.group_selector.currentText()
#             return [p["email"] for p in people if p["group_name"] == group]

#         # MANUAL SELECT
#         emails = []
#         for i in range(self.recipient_list.count()):
#             item = self.recipient_list.item(i)
#             if item.checkState() == Qt.Checked:
#                 emails.append(item.data(Qt.UserRole))
#         return emails

#     # --------------------------------------------------------
#     # SEND EMAIL
#     # --------------------------------------------------------
#     def send_email(self):
#         subject = self.subject.toPlainText().strip()
#         message = self.message.toPlainText().strip()
#         recipients = self.get_recipients()

#         if not recipients:
#             QMessageBox.warning(self, "No Recipients", "Please select at least one recipient.")
#             return

#         if not subject:
#             QMessageBox.warning(self, "Missing Subject", "Email subject cannot be empty.")
#             return

#         if not message:
#             QMessageBox.warning(self, "Missing Message", "Email body cannot be empty.")
#             return

#         # --------------------------------------------------------
#         # Attempt sending
#         # --------------------------------------------------------
#         try:
#             mail_service.send_email(
#                 to_list=recipients,
#                 subject=subject,
#                 message=message
#             )

#             QMessageBox.information(
#                 self,
#                 "Success",
#                 f"Email sent to {len(recipients)} recipient(s)."
#             )

#             # Save history
#             HistoryService.log_email(
#                 recipients="; ".join(recipients),
#                 subject=subject,
#                 message=message
#             )

#             self.accept()

#         except Exception as e:
#             QMessageBox.critical(self, "Send Failed", str(e))


# if __name__ == "__main__":
#     import sys
#     from PySide6.QtWidgets import QApplication

#     app = QApplication(sys.argv)

#     dialog = SendMailDialog()
#     dialog.exec()




from PySide6.QtWidgets import (
    QDialog, QLabel, QComboBox, QTextEdit, QListWidget,
    QListWidgetItem, QPushButton, QVBoxLayout, QHBoxLayout,
    QFormLayout, QMessageBox, QFileDialog
)
from PySide6.QtCore import Qt

from backend.person_service import PersonService
from backend.mail_service import mail_service
from backend.history_service import HistoryService


class SendMailDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Send Email")
        self.setMinimumWidth(550)

        self.attachments = []  # NEW: Store file paths

        # --------------------------------------------------------
        # Widgets
        # --------------------------------------------------------
        self.recipient_mode = QComboBox()
        self.recipient_mode.addItems([
            "Send to ALL People",
            "Send to Group",
            "Select Recipients Manually"
        ])

        self.group_selector = QComboBox()
        self.group_selector.setEnabled(False)

        self.subject = QTextEdit()
        self.subject.setFixedHeight(40)

        self.message = QTextEdit()

        self.recipient_list = QListWidget()
        self.recipient_list.setSelectionMode(QListWidget.MultiSelection)
        self.recipient_list.setEnabled(False)

        # --------------------------------------------------------
        # ATTACHMENTS UI
        # --------------------------------------------------------
        self.attach_list = QListWidget()

        self.btn_add_attachment = QPushButton("Add Attachment")
        self.btn_remove_attachment = QPushButton("Remove Selected Attachment")

        self.btn_add_attachment.clicked.connect(self.add_attachment)
        self.btn_remove_attachment.clicked.connect(self.remove_attachment)

        # Buttons
        self.btnSend = QPushButton("Send Mail")
        self.btnCancel = QPushButton("Cancel")

        # --------------------------------------------------------
        # Layouts
        # --------------------------------------------------------
        form = QFormLayout()
        form.addRow("Recipient Mode:", self.recipient_mode)
        form.addRow("Select Group:", self.group_selector)
        form.addRow("Subject:", self.subject)
        form.addRow("Message:", self.message)
        form.addRow("Manual Recipients:", self.recipient_list)

        # Attachment Section
        attach_layout = QVBoxLayout()
        attach_layout.addWidget(QLabel("Attachments:"))
        attach_layout.addWidget(self.attach_list)

        attach_btns = QHBoxLayout()
        attach_btns.addWidget(self.btn_add_attachment)
        attach_btns.addWidget(self.btn_remove_attachment)

        attach_layout.addLayout(attach_btns)
        form.addRow("Add Files:", attach_layout)

        # Bottom buttons
        btns = QHBoxLayout()
        btns.addStretch()
        btns.addWidget(self.btnSend)
        btns.addWidget(self.btnCancel)

        main = QVBoxLayout(self)
        main.addLayout(form)
        main.addLayout(btns)

        # --------------------------------------------------------
        # Load People + Groups
        # --------------------------------------------------------
        self.load_groups()
        self.load_people_list()

        # Signals
        self.recipient_mode.currentIndexChanged.connect(self.change_recipient_mode)
        self.btnCancel.clicked.connect(self.reject)
        self.btnSend.clicked.connect(self.send_email)

    # --------------------------------------------------------
    # LOAD GROUPS
    # --------------------------------------------------------
    def load_groups(self):
        people = PersonService.get_all_people()
        groups = sorted(set([p["group_name"] for p in people if p["group_name"]]))

        self.group_selector.clear()
        self.group_selector.addItems(groups)

    # --------------------------------------------------------
    # LOAD PEOPLE (Manual Selection Mode)
    # --------------------------------------------------------
    def load_people_list(self):
        self.recipient_list.clear()
        people = PersonService.get_all_people()

        for p in people:
            item = QListWidgetItem(f"{p['name']}  ({p['email']})")
            item.setData(Qt.UserRole, p["email"])
            item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
            item.setCheckState(Qt.Unchecked)
            self.recipient_list.addItem(item)

    # --------------------------------------------------------
    # Mode switch
    # --------------------------------------------------------
    def change_recipient_mode(self):
        mode = self.recipient_mode.currentIndex()

        if mode == 0:  # ALL
            self.group_selector.setEnabled(False)
            self.recipient_list.setEnabled(False)

        elif mode == 1:  # GROUP
            self.group_selector.setEnabled(True)
            self.recipient_list.setEnabled(False)

        else:  # MANUAL
            self.group_selector.setEnabled(False)
            self.recipient_list.setEnabled(True)

    # --------------------------------------------------------
    # RESOLVE RECIPIENTS
    # --------------------------------------------------------
    def get_recipients(self):
        mode = self.recipient_mode.currentIndex()
        people = PersonService.get_all_people()

        if mode == 0:  # ALL
            return [p["email"] for p in people]

        elif mode == 1:  # GROUP
            group = self.group_selector.currentText()
            return [p["email"] for p in people if p["group_name"] == group]

        else:  # MANUAL
            emails = []
            for i in range(self.recipient_list.count()):
                item = self.recipient_list.item(i)
                if item.checkState() == Qt.Checked:
                    emails.append(item.data(Qt.UserRole))
            return emails

    # --------------------------------------------------------
    # ATTACHMENTS HANDLING
    # --------------------------------------------------------
    def add_attachment(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Select Attachments")

        if files:
            for f in files:
                if f not in self.attachments:
                    self.attachments.append(f)
                    self.attach_list.addItem(QListWidgetItem(f))

    def remove_attachment(self):
        selected = self.attach_list.currentRow()
        if selected >= 0:
            self.attachments.pop(selected)
            self.attach_list.takeItem(selected)

    # --------------------------------------------------------
    # SEND EMAIL
    # --------------------------------------------------------
    def send_email(self):
        sender_name = "Optic Mailer"  # Could be dynamic
        subject = self.subject.toPlainText().strip()
        message = self.message.toPlainText().strip()
        recipients = self.get_recipients()

        if not recipients:
            QMessageBox.warning(self, "No Recipients", "Please select at least one recipient.")
            return

        if not subject:
            QMessageBox.warning(self, "Missing Subject", "Email subject cannot be empty.")
            return

        if not message:
            QMessageBox.warning(self, "Missing Message", "Email body cannot be empty.")
            return

        try:
            # 🔥 Send email with attachments
            mail_service.send_email(
                sender_name=sender_name,
                recipients=recipients,
                subject=subject,
                message=message,
                attachments=self.attachments  # <-- NEW
            )

            QMessageBox.information(
                self,
                "Success",
                f"Email sent to {len(recipients)} recipient(s)."
            )

            # Save history
            HistoryService.log_email(
                recipients="; ".join(recipients),
                subject=subject,
                message=message
            )

            self.accept()

        except Exception as e:
            QMessageBox.critical(self, "Send Failed", str(e))


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)

    dialog = SendMailDialog()
    dialog.exec()
