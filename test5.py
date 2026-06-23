#!/usr/bin/env python3
# from PyQt6.QtWidgets import *
# import sys
# # import sys
# # class Window(QWidget):
# #     def __init__(self):
# #         QWidget.__init__(self)
# #         layout = QGridLayout()
# #         self.setLayout(layout)
# #         button = QPushButton("Simple ToolTip")
# #         button.setToolTip("This ToolTip simply displays text.")
# #         layout.addWidget(button, 0, 0)
# #         button = QPushButton("Formatted ToolTip")
# #         button.setToolTip("<b>Formatted text</b> can also be displayed.")
# #         layout.addWidget(button, 1, 0)

# # app = QApplication(sys.argv)
# # screen = Window()
# # screen.show()
# # sys.exit(app.exec())



# app = QApplication(sys.argv)
# app.setStyle('Fusion')
# #...
# app.exec()

# sys.exit(app.exec())

import os
import sys
from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import (
  QApplication,
  QLabel,
  QMainWindow,
  QStatusBar,
  QToolBar,
)
basedir = os.path.dirname(__file__)
# tag::MainWindow[]
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)
        button_action = QAction(
            QIcon(os.path.join(basedir, "bug.png")),
            "Your button",
            self,

        )
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        self.setStatusBar(QStatusBar(self))
    def onMyToolBarButtonClick(self, s):
        print("click", s)
# end::MainWindow[]
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QMessageBox, QDialog,
    QLabel, QFormLayout
)
from PySide6.QtCore import Qt

from  contacts_manager import ContactsManager


class ContactDialog(QDialog):
    """Dialog for Add/Edit Contact"""

    def __init__(self, parent=None, contact=None):
        super().__init__(parent)
        self.setWindowTitle("Add/Edit Contact")
        self.contact = contact

        self.layout = QFormLayout(self)

        self.name_input = QLineEdit()
        self.phone_input = QLineEdit()
        self.department_input = QLineEdit()
        self.tag_input = QLineEdit()

        if contact:  # prefill for edit
            self.name_input.setText(contact[1])
            self.phone_input.setText(contact[2])
            self.department_input.setText(contact[3] or "")
            self.tag_input.setText(contact[4] or "")

        self.layout.addRow("Name:", self.name_input)
        self.layout.addRow("Phone:", self.phone_input)
        self.layout.addRow("Department:", self.department_input)
        self.layout.addRow("Tag:", self.tag_input)

        btn_layout = QHBoxLayout()
        save_btn = QPushButton("Save")
        cancel_btn = QPushButton("Cancel")
        save_btn.clicked.connect(self.accept)
        cancel_btn.clicked.connect(self.reject)
        btn_layout.addWidget(save_btn)
        btn_layout.addWidget(cancel_btn)

        self.layout.addRow(btn_layout)

    def get_data(self):
        return (
            self.name_input.text(),
            self.phone_input.text(),
            self.department_input.text(),
            self.tag_input.text()
        )


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("WhatsApp Automation - With Contacts")

        # DB manager
        self.db = ContactsManager()

        # Central Widget
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        # Search
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name, dept or tag...")
        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.search_contacts)
        search_layout.addWidget(self.search_input)
        search_layout.addWidget(search_btn)
        layout.addLayout(search_layout)

        # Table
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Name", "Phone", "Department", "Tag"])
        self.table.setSelectionBehavior(self.table.SelectRows)
        self.table.setSelectionMode(self.table.MultiSelection)
        layout.addWidget(self.table)

        # Buttons
        btn_layout = QHBoxLayout()
        add_btn = QPushButton("➕ Add Contact")
        edit_btn = QPushButton("✏️ Edit Contact")
        delete_btn = QPushButton("🗑 Delete Contact")

        add_btn.clicked.connect(self.add_contact)
        edit_btn.clicked.connect(self.edit_contact)
        delete_btn.clicked.connect(self.delete_contact)

        btn_layout.addWidget(add_btn)
        btn_layout.addWidget(edit_btn)
        btn_layout.addWidget(delete_btn)
        layout.addLayout(btn_layout)

        # Chat input (prefilled with selected contacts)
        self.chat_input = QLineEdit()
        self.chat_input.setPlaceholderText("Selected contacts will appear here...")
        layout.addWidget(self.chat_input)

        # Load data initially
        self.load_contacts()

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
        self.log_message(f"✅ Scheduled job for {chat} at {dt}")

    def refresh_table(self):
        self.scheduler.load_jobs()
        self.jobs_table.setRowCount(len(self.scheduler.jobs))
        for i, job in enumerate(self.scheduler.jobs):
            self.jobs_table.setItem(i, 0, QTableWidgetItem(job["chat_name"]))
            self.jobs_table.setItem(i, 1, QTableWidgetItem(job["message"]))
            self.jobs_table.setItem(i, 2, QTableWidgetItem(job["datetime"]))
            status = "✅ Done" if job.get("done") else "⏳ Pending"
            self.jobs_table.setItem(i, 3, QTableWidgetItem(status))


    # -------------------- DB + UI Logic --------------------

    def load_contacts(self, rows=None):
        if rows is None:
            rows = self.db.get_all_contacts()

        self.table.setRowCount(len(rows))
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                self.table.setItem(i, j, QTableWidgetItem(str(col)))


    # # ---------------- Contacts ---------------- #
    # def load_contacts(self, filter_text=None):
    #     """
    #     Placeholder: Will load contacts from contacts_manager (SQLite).
    #     For now, we simulate with dummy data.
    #     """
    #     dummy_contacts = [
    #         {"name": "Alice", "phone": "+123456789", "department": "HR", "tag": "Manager"},
    #         {"name": "Bob", "phone": "+987654321", "department": "IT", "tag": "Engineer"},
    #     ]
    #     self.contacts_table.setRowCount(len(dummy_contacts))
    #     for i, c in enumerate(dummy_contacts):
    #         self.contacts_table.setItem(i, 0, QTableWidgetItem(c["name"]))
    #         self.contacts_table.setItem(i, 1, QTableWidgetItem(c["phone"]))
    #         self.contacts_table.setItem(i, 2, QTableWidgetItem(c["department"]))
    #         self.contacts_table.setItem(i, 3, QTableWidgetItem(c["tag"]))

    def search_contacts(self):
        query = self.search_input.text().strip()
        self.load_contacts(filter_text=query)

    # def add_contact(self):
    #     QMessageBox.information(self, "Info", "➕ Add Contact dialog will open (to be implemented)")

    # def edit_contact(self):
    #     QMessageBox.information(self, "Info", "✏️ Edit Contact dialog will open (to be implemented)")

    # def delete_contact(self):
    #     QMessageBox.information(self, "Info", "🗑 Delete Contact will be handled (to be implemented)")
    def add_contact(self):
        dialog = ContactDialog(self)
        if dialog.exec():
            name, phone, dept, tag = dialog.get_data()
            if not name or not phone:
                QMessageBox.warning(self, "Error", "Name and Phone are required!")
                return
            self.db.add_contact(name, phone, dept, tag)
            self.load_contacts()

    def edit_contact(self):
        selected = self.table.currentRow()
        if selected < 0:
            QMessageBox.warning(self, "Error", "Select a contact to edit!")
            return
        contact_id = int(self.table.item(selected, 0).text())
        contact = self.db.search_contacts(self.table.item(selected, 1).text())[0]

        dialog = ContactDialog(self, contact)
        if dialog.exec():
            name, phone, dept, tag = dialog.get_data()
            self.db.update_contact(contact_id, name, phone, dept, tag)
            self.load_contacts()

    def delete_contact(self):
        selected = self.table.selectedItems()
        if not selected:
            QMessageBox.warning(self, "Error", "Select contacts to delete!")
            return
        rows = list(set(item.row() for item in selected))
        for row in rows:
            contact_id = int(self.table.item(row, 0).text())
            self.db.delete_contact(contact_id)
        self.load_contacts()

    def search_contacts(self):
        keyword = self.search_input.text().strip()
        if keyword:
            results = self.db.search_contacts(keyword)
            self.load_contacts(results)
        else:
            self.load_contacts()

    def get_selected_contacts(self):
        selected = self.table.selectionModel().selectedRows()
        names = []
        phones = []
        for idx in selected:
            row = idx.row()
            names.append(self.table.item(row, 1).text())
            phones.append(self.table.item(row, 2).text())
        return names, phones

    def update_chat_input_from_selection(self):
        names, phones = self.get_selected_contacts()
        if names:
            self.chat_input.setText(", ".join(names))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(700, 500)
    window.show()
    sys.exit(app.exec())

