"""
windows/panels/patients_panel.py — Patient management

CONNECTION FLOWS:
  Load     → GET /api/patients/list/
  Search   → GET /api/patients/search/?q=<query>
  Add      → POST /api/patients/add/
  Edit     → POST /api/patients/update/<id>/
  Delete   → DELETE /api/patients/delete/<id>/
"""

from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton,
    QTableWidget, QTableWidgetItem, QLineEdit, QDialog,
    QFormLayout, QComboBox, QSpinBox, QMessageBox, QHeaderView
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from api_client import api
from assets.styles import PRIMARY, TEXT_MUTED, DANGER
from workers.api_worker import ApiWorker


class PatientsPanel(QWidget):
    def __init__(self):
        super().__init__()
        self._workers = []
        self._all_patients = []
        self._build_ui()
        self.refresh()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(28, 24, 28, 24)
        root.setSpacing(16)

        # Header
        header = QHBoxLayout()
        col = QVBoxLayout()
        col.addWidget(self._h1("Patients"))
        col.addWidget(self._sub("Register, search, and manage patient records"))
        header.addLayout(col)
        header.addStretch()

        add_btn = QPushButton("＋  Add Patient")
        add_btn.setObjectName("primary_btn")
        add_btn.setFixedHeight(38)
        add_btn.clicked.connect(self._open_add_dialog)
        header.addWidget(add_btn)
        root.addLayout(header)

        # Search
        search_row = QHBoxLayout()
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name, email or contact…")
        self.search_input.setFixedHeight(34)
        self.search_input.returnPressed.connect(self._do_search)
        search_row.addWidget(self.search_input)

        search_btn = QPushButton("Search")
        search_btn.setObjectName("secondary_btn")
        search_btn.setFixedHeight(34)
        search_btn.clicked.connect(self._do_search)
        search_row.addWidget(search_btn)

        clear_btn = QPushButton("Show All")
        clear_btn.setObjectName("secondary_btn")
        clear_btn.setFixedHeight(34)
        clear_btn.clicked.connect(self.refresh)
        search_row.addWidget(clear_btn)
        root.addLayout(search_row)

        # Table
        self.table = QTableWidget(0, 7)
        self.table.setHorizontalHeaderLabels([
            "ID", "Name", "Contact", "Email", "Age", "Gender", "Registered"
        ])
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setAlternatingRowColors(True)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.doubleClicked.connect(self._open_edit_dialog)
        root.addWidget(self.table)

        # Row action buttons
        action_row = QHBoxLayout()
        self.edit_btn = QPushButton("✏ Edit Selected")
        self.edit_btn.setObjectName("secondary_btn")
        self.edit_btn.clicked.connect(self._open_edit_dialog_from_btn)

        self.delete_btn = QPushButton("🗑 Delete Selected")
        self.delete_btn.setObjectName("danger_btn")
        self.delete_btn.clicked.connect(self._delete_selected)

        action_row.addStretch()
        action_row.addWidget(self.edit_btn)
        action_row.addWidget(self.delete_btn)
        root.addLayout(action_row)

        self.status_bar = QLabel("")
        self.status_bar.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 12px;")
        root.addWidget(self.status_bar)

    def refresh(self):
        self.search_input.clear()
        w = ApiWorker(api.list_patients)
        w.success.connect(self._on_patients)
        w.error.connect(self._on_error)
        w.start()
        self._workers.append(w)

    def _do_search(self):
        query = self.search_input.text().strip()
        if not query:
            self.refresh()
            return
        w = ApiWorker(api.search_patients, query)
        w.success.connect(self._on_patients)
        w.error.connect(self._on_error)
        w.start()
        self._workers.append(w)

    def _on_patients(self, data: dict):
        self._all_patients = data.get("patients", [])
        self.table.setRowCount(0)
        for p in self._all_patients:
            row = self.table.rowCount()
            self.table.insertRow(row)
            registered = str(p.get("date_registered", ""))[:10]
            self.table.setItem(row, 0, QTableWidgetItem(str(p.get("id", ""))))
            self.table.setItem(row, 1, QTableWidgetItem(p.get("name", "")))
            self.table.setItem(row, 2, QTableWidgetItem(p.get("contact", "")))
            self.table.setItem(row, 3, QTableWidgetItem(p.get("email", "")))
            self.table.setItem(row, 4, QTableWidgetItem(str(p.get("age", ""))))
            self.table.setItem(row, 5, QTableWidgetItem(p.get("gender", "")))
            self.table.setItem(row, 6, QTableWidgetItem(registered))
            self.table.item(row, 0).setData(Qt.UserRole, p)
        self.table.resizeColumnsToContents()
        self.status_bar.setText(f"{len(self._all_patients)} patients")

    def _get_selected_patient(self):
        selected = self.table.selectedItems()
        if not selected:
            return None
        row = self.table.currentRow()
        item = self.table.item(row, 0)
        return item.data(Qt.UserRole) if item else None

    def _open_add_dialog(self):
        dialog = PatientFormDialog(parent=self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh()

    def _open_edit_dialog(self, index=None):
        patient = self._get_selected_patient()
        if not patient:
            return
        dialog = PatientFormDialog(patient=patient, parent=self)
        if dialog.exec() == QDialog.Accepted:
            self.refresh()

    def _open_edit_dialog_from_btn(self):
        self._open_edit_dialog()

    def _delete_selected(self):
        patient = self._get_selected_patient()
        if not patient:
            QMessageBox.warning(self, "No selection", "Select a patient first.")
            return

        confirm = QMessageBox.question(
            self, "Delete Patient",
            f"Delete '{patient.get('name', '')}'? This cannot be undone.",
            QMessageBox.Yes | QMessageBox.No
        )
        if confirm != QMessageBox.Yes:
            return

        w = ApiWorker(api.delete_patient, patient["id"])
        w.success.connect(lambda _: self.refresh())
        w.error.connect(self._on_error)
        w.start()
        self._workers.append(w)

    def _on_error(self, message: str):
        self.status_bar.setText(f"Error: {message}")

    def _h1(self, text):
        l = QLabel(text)
        l.setFont(QFont("Segoe UI", 18, QFont.Bold))
        return l

    def _sub(self, text):
        l = QLabel(text)
        l.setStyleSheet(f"color: {TEXT_MUTED}; font-size: 12px;")
        return l


class PatientFormDialog(QDialog):
    """Add or edit a patient."""

    def __init__(self, patient: dict = None, parent=None):
        super().__init__(parent)
        self.patient = patient
        self.is_edit = patient is not None
        self.setWindowTitle("Edit Patient" if self.is_edit else "Add Patient")
        self.setFixedSize(420, 400)
        self._workers = []
        self._build_ui()
        if self.is_edit:
            self._fill_form()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(24, 24, 24, 24)
        root.setSpacing(14)

        title = QLabel("Edit Patient" if self.is_edit else "Add New Patient")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        root.addWidget(title)

        form = QFormLayout()
        form.setSpacing(10)

        self.name_input    = QLineEdit()
        self.contact_input = QLineEdit()
        self.email_input   = QLineEdit()
        self.address_input = QLineEdit()
        self.address_input.setText("Yaoundé")
        self.profession_input = QLineEdit()

        self.age_spin = QSpinBox()
        self.age_spin.setRange(1, 120)

        self.gender_combo = QComboBox()
        self.gender_combo.addItems(["M", "F", "X"])

        form.addRow("Name *",       self.name_input)
        form.addRow("Contact *",    self.contact_input)
        form.addRow("Email *",      self.email_input)
        form.addRow("Address",      self.address_input)
        form.addRow("Profession",   self.profession_input)
        form.addRow("Age *",        self.age_spin)
        form.addRow("Gender",       self.gender_combo)
        root.addLayout(form)

        self.error_lbl = QLabel("")
        self.error_lbl.setStyleSheet("color: #d93025; font-size: 12px;")
        self.error_lbl.setVisible(False)
        root.addWidget(self.error_lbl)

        btn_row = QHBoxLayout()
        btn_row.addStretch()
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setObjectName("secondary_btn")
        cancel_btn.clicked.connect(self.reject)
        self.save_btn = QPushButton("Save")
        self.save_btn.setObjectName("primary_btn")
        self.save_btn.clicked.connect(self._submit)
        btn_row.addWidget(cancel_btn)
        btn_row.addWidget(self.save_btn)
        root.addLayout(btn_row)

    def _fill_form(self):
        p = self.patient
        self.name_input.setText(p.get("name", ""))
        self.contact_input.setText(p.get("contact", ""))
        self.email_input.setText(p.get("email", ""))
        self.address_input.setText(p.get("address", "Yaoundé"))
        self.profession_input.setText(p.get("profession", ""))
        self.age_spin.setValue(int(p.get("age") or 1))
        gender = p.get("gender", "M")
        idx = self.gender_combo.findText(gender)
        if idx >= 0:
            self.gender_combo.setCurrentIndex(idx)

    def _submit(self):
        data = {
            "name":       self.name_input.text().strip(),
            "contact":    self.contact_input.text().strip(),
            "email":      self.email_input.text().strip(),
            "address":    self.address_input.text().strip() or "Yaoundé",
            "profession": self.profession_input.text().strip(),
            "age":        self.age_spin.value(),
            "gender":     self.gender_combo.currentText(),
        }

        if not data["name"]:
            self._show_error("Name is required")
            return
        if not data["email"]:
            self._show_error("Email is required")
            return

        self.save_btn.setEnabled(False)
        self.save_btn.setText("Saving…")

        if self.is_edit:
            w = ApiWorker(api.update_patient, self.patient["id"], data)
        else:
            w = ApiWorker(api.add_patient, data)

        w.success.connect(lambda _: self.accept())
        w.error.connect(self._on_error)
        w.start()
        self._workers.append(w)

    def _on_error(self, message: str):
        self.save_btn.setEnabled(True)
        self.save_btn.setText("Save")
        self._show_error(message)

    def _show_error(self, msg: str):
        self.error_lbl.setText(msg)
        self.error_lbl.setVisible(True)
