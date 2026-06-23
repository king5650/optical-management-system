

from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QTextEdit, QPushButton, QCheckBox, QDateTimeEdit,
    QTableWidget, QTableWidgetItem, QMessageBox, QTabWidget, QAbstractItemView, QHeaderView,
    QInputDialog
)
from PySide6.QtCore import Qt, QDateTime
import sys
import os
import requests
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# from job_scheduler import JobScheduler
# from contacts_manager import ContactsManager   
from whatsapp_auto.job_scheduler import JobScheduler
from whatsapp_auto.contacts_manager import ContactsManager


BASE_URL = "http://127.0.0.1:8000/auth"
qss_stle="""

QWidget {
    font-family: "Segoe UI", "Roboto", "Helvetica Neue", sans-serif;
    font-size: 14px;
    /*color: #2c3e50;*/
    color: white;
    font-weight: 700px;
    /* background-color: #f5f6fa;*/
    /*background-color: #cacaca;*/
        /*"bg_alt": "qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255))",  */
    background: qlineargradient(spread:pad, x1:0, y1:0.267, x2:1, y2:0.471, stop:0 rgba(2, 101, 195, 255), stop:1 rgba(44, 47, 132, 255));
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
    color:black;
    font-weight: 600;
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
    color: black;
    font-weight: 600;
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
    color: black;
    font-weight: 600;
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
        # tabs = QTabWidget()

        # # --- Scheduler Tab ---
        # scheduler_tab = QWidget()
        # scheduler_layout = QVBoxLayout()

        # self.chat_input = QLineEdit()
        # self.message_input = QTextEdit()
        # self.datetime_input = QDateTimeEdit(QDateTime.currentDateTime())
        # self.datetime_input.setCalendarPopup(True)
        # self.persistent_check = QCheckBox("Use Persistent Session")

        # add_btn = QPushButton("➕ Schedule Message")
        # add_btn.clicked.connect(self.add_job)

        # scheduler_layout.addWidget(QLabel("Chat Name / Number:"))
        # scheduler_layout.addWidget(self.chat_input)
        # scheduler_layout.addWidget(QLabel("Message:"))
        # scheduler_layout.addWidget(self.message_input)
        # scheduler_layout.addWidget(QLabel("Date & Time:"))
        # scheduler_layout.addWidget(self.datetime_input)
        # scheduler_layout.addWidget(self.persistent_check)
        # scheduler_layout.addWidget(add_btn)

        # # Jobs Table
        # self.jobs_table = QTableWidget(0, 4)
        # self.jobs_table.setHorizontalHeaderLabels(["Chat", "Message", "Datetime", "Status"])
        # scheduler_layout.addWidget(self.jobs_table)

        # scheduler_tab.setLayout(scheduler_layout)
        # tabs.addTab(scheduler_tab, "Scheduler")

        # # --- Contacts Tab ---
        # contacts_tab = QWidget()
        # contacts_layout = QVBoxLayout()

        # # Search bar
        # search_layout = QHBoxLayout()
        # self.search_input = QLineEdit()
        # self.search_input.setPlaceholderText("🔍 Search by name, department, or tag...")
        # search_btn = QPushButton("Search")
        # search_btn.clicked.connect(self.search_contacts)
        # search_layout.addWidget(self.search_input)
        # search_layout.addWidget(search_btn)
        # contacts_layout.addLayout(search_layout)

        # # Contacts table
        # self.contacts_table = QTableWidget(0, 4)
        # self.contacts_table.setHorizontalHeaderLabels(["Name", "Phone", "Department", "Tag"])
        # self.contacts_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.contacts_table.setSelectionMode(QAbstractItemView.MultiSelection)
        # contacts_layout.addWidget(self.contacts_table)

        # # Action buttons
        # btn_layout = QHBoxLayout()
        # add_contact_btn = QPushButton("➕ Add Contact")
        # edit_contact_btn = QPushButton("✏️ Edit Contact")
        # delete_contact_btn = QPushButton("🗑 Delete Contact")
        # use_contact_btn = QPushButton("📩 Use Selected")

        # add_contact_btn.clicked.connect(self.add_contact)
        # edit_contact_btn.clicked.connect(self.edit_contact)
        # delete_contact_btn.clicked.connect(self.delete_contact)
        # use_contact_btn.clicked.connect(self.use_selected_contacts)

        # btn_layout.addWidget(add_contact_btn)
        # btn_layout.addWidget(edit_contact_btn)
        # btn_layout.addWidget(delete_contact_btn)
        # btn_layout.addWidget(use_contact_btn)
        # contacts_layout.addLayout(btn_layout)

        # contacts_tab.setLayout(contacts_layout)
        # tabs.addTab(contacts_tab, "Contacts")

        # # Main Layout
        # main_layout = QVBoxLayout()
        # main_layout.addWidget(tabs)
        # self.setLayout(main_layout)
        
        
        # # --- Patients Tab --- #
        # patients_tab = QWidget()
        # patients_layout = QVBoxLayout()

        # # Table for displaying patients
        # self.tableWidget = QTableWidget(0, 8)
        # self.tableWidget.setHorizontalHeaderLabels([
        #     "ID", "Name", "Email", "Contact", "Address", "Profession", "Age", "Gender"
        # ])
        # self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # patients_layout.addWidget(self.tableWidget)

        # # refresh button
        # refresh_btn = QPushButton("🔄 Refresh Patients")
        # refresh_btn.clicked.connect(self.load_patients)
        # patients_layout.addWidget(refresh_btn)
        
        # # use selected button
        # use_contact_btn = QPushButton("📩 Use Selected")
        # use_contact_btn.clicked.connect(self.use_selected_patients)
        # patients_layout.addWidget(use_contact_btn)
        
        # patients_tab.setLayout(patients_layout)
        # tabs.addTab(patients_tab, "Patients")
        # ---- Main Tabs ----
        self.tabs = QTabWidget()

        # -----------------------------------------------------------
        #                    SCHEDULER TAB
        # -----------------------------------------------------------
        self.scheduler_tab = QWidget()
        scheduler_layout = QVBoxLayout(self.scheduler_tab)

        # Labels
        self.scheduler_label_chat = QLabel()
        scheduler_layout.addWidget(self.scheduler_label_chat)

        self.chat_input = QLineEdit()
        scheduler_layout.addWidget(self.chat_input)

        self.scheduler_label_message = QLabel()
        scheduler_layout.addWidget(self.scheduler_label_message)

        self.message_input = QTextEdit()
        scheduler_layout.addWidget(self.message_input)

        self.scheduler_label_datetime = QLabel()
        scheduler_layout.addWidget(self.scheduler_label_datetime)

        self.datetime_input = QDateTimeEdit(QDateTime.currentDateTime())
        self.datetime_input.setCalendarPopup(True)
        scheduler_layout.addWidget(self.datetime_input)

        self.persistent_check = QCheckBox()
        scheduler_layout.addWidget(self.persistent_check)

        # Schedule button
        self.add_btn = QPushButton()
        self.add_btn.clicked.connect(self.add_job)
        scheduler_layout.addWidget(self.add_btn)

        # Scheduler Table
        self.jobs_table = QTableWidget(0, 4)
        self.jobs_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        scheduler_layout.addWidget(self.jobs_table)

        self.tabs.addTab(self.scheduler_tab, "")

        # -----------------------------------------------------------
        #                    CONTACTS TAB
        # -----------------------------------------------------------
        self.contacts_tab = QWidget()
        contacts_layout = QVBoxLayout(self.contacts_tab)

        # Search bar
        search_layout = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_btn = QPushButton()
        self.search_btn.clicked.connect(self.search_contacts)

        search_layout.addWidget(self.search_input)
        search_layout.addWidget(self.search_btn)

        contacts_layout.addLayout(search_layout)

        # Contacts table
        self.contacts_table = QTableWidget(0, 4)
        self.contacts_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.contacts_table.setSelectionMode(QAbstractItemView.MultiSelection)
        contacts_layout.addWidget(self.contacts_table)

        # Action buttons
        btn_layout = QHBoxLayout()

        self.add_contact_btn = QPushButton()
        self.add_contact_btn.clicked.connect(self.add_contact)

        self.edit_contact_btn = QPushButton()
        self.edit_contact_btn.clicked.connect(self.edit_contact)

        self.delete_contact_btn = QPushButton()
        self.delete_contact_btn.clicked.connect(self.delete_contact)

        self.use_contact_btn = QPushButton()
        self.use_contact_btn.clicked.connect(self.use_selected_contacts)

        btn_layout.addWidget(self.add_contact_btn)
        btn_layout.addWidget(self.edit_contact_btn)
        btn_layout.addWidget(self.delete_contact_btn)
        btn_layout.addWidget(self.use_contact_btn)

        contacts_layout.addLayout(btn_layout)

        self.tabs.addTab(self.contacts_tab, "")

        # -----------------------------------------------------------
        #                    PATIENTS TAB
        # -----------------------------------------------------------
        self.patients_tab = QWidget()
        patients_layout = QVBoxLayout(self.patients_tab)

        # Patients table
        self.tableWidget = QTableWidget(0, 8)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        patients_layout.addWidget(self.tableWidget)

        # Refresh patients
        self.refresh_btn = QPushButton()
        self.refresh_btn.clicked.connect(self.load_patients)
        patients_layout.addWidget(self.refresh_btn)

        # Use selected
        self.use_patient_btn = QPushButton()
        self.use_patient_btn.clicked.connect(self.use_selected_patients)
        patients_layout.addWidget(self.use_patient_btn)

        self.tabs.addTab(self.patients_tab, "")

        # ---- Main Layout ----
        main_layout = QVBoxLayout(self)
        main_layout.addWidget(self.tabs)
        
        # Initialize
        self.refresh_table()
        self.load_contacts()
        self.load_patients()
        self._retranslate_ui()

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
            contact_item = self.tableWidget.item(row.row(), 3)  # Assuming 'Contact' is the 4th column
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
        
    def _retranslate_ui(self):
        _ = self.tr

        # ---- Window title ----
        self.setWindowTitle(_("WhatsApp Scheduler"))

        # ---- Scheduler Tab ----
        # Labels
        self.scheduler_label_chat.setText(_("Chat Name / Number:"))
        self.scheduler_label_message.setText(_("Message:"))
        self.scheduler_label_datetime.setText(_("Date & Time:"))
        self.persistent_check.setText(_("Use Persistent Session"))

        # Buttons
        self.add_btn.setText(_("➕ Schedule Message"))

        # Jobs table headers
        self.jobs_table.setHorizontalHeaderLabels([
            _("Chat"),
            _("Message"),
            _("Datetime"),
            _("Status")
        ])

        # ---- Tabs ----
        index_scheduler = self.tabs.indexOf(self.scheduler_tab)
        index_contacts = self.tabs.indexOf(self.contacts_tab)
        index_patients = self.tabs.indexOf(self.patients_tab)

        if index_scheduler != -1:
            self.tabs.setTabText(index_scheduler, _("Scheduler"))
        if index_contacts != -1:
            self.tabs.setTabText(index_contacts, _("Contacts"))
        if index_patients != -1:
            self.tabs.setTabText(index_patients, _("Patients"))

        # ---- Contacts Tab ----
        self.search_input.setPlaceholderText(_("🔍 Search by name, department, or tag..."))
        self.search_btn.setText(_("Search"))

        # Contacts table headers
        self.contacts_table.setHorizontalHeaderLabels([
            _("Name"),
            _("Phone"),
            _("Department"),
            _("Tag")
        ])

        # Buttons
        self.add_contact_btn.setText(_("➕ Add Contact"))
        self.edit_contact_btn.setText(_("✏️ Edit Contact"))
        self.delete_contact_btn.setText(_("🗑 Delete Contact"))
        self.use_contact_btn.setText(_("📩 Use Selected"))

        # ---- Patients Tab ----
        # Patients table headers
        self.tableWidget.setHorizontalHeaderLabels([
            _("ID"),
            _("Name"),
            _("Email"),
            _("Contact"),
            _("Address"),
            _("Profession"),
            _("Age"),
            _("Gender")
        ])

        # Buttons
        self.refresh_btn.setText(_("🔄 Refresh Patients"))
        self.use_patient_btn.setText(_("📩 Use Selected"))

        # ---- Standard dialog text (use inside QMessageBox elsewhere) ----
        self.error_select_edit = _("Select a contact to edit")
        self.error_select_delete = _("Select at least one contact to delete")
        self.error_missing_fields = _("Chat name and message required")
        self.error_patient_load = _("Failed to load patients.")
        self.error_server = _("Server error:")

        # ---- Contact dialogs ----
        self.txt_add_contact = _("Add Contact")
        self.txt_edit_contact = _("Edit Contact")
        self.txt_enter_name = _("Enter Name:")
        self.txt_enter_phone = _("Enter Phone:")
        self.txt_enter_department = _("Enter Department (optional):")
        self.txt_enter_tag = _("Enter Tag (optional):")
        self.txt_edit_name = _("Edit Name:")
        self.txt_edit_phone = _("Edit Phone:")
        self.txt_edit_department = _("Edit Department:")
        self.txt_edit_tag = _("Edit Tag:")
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = whatsapp_automation_MainWindow()
    window.show()
    sys.exit(app.exec())
