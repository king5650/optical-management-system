import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem
)
#from ui_ux.patient_module.ui_patient_form2 import Ui_MainWindow  #UI form for the patient form ui_patient form_ok.py
from ui_ux.patient_module.ui_patient_form_ok import Ui_MainWindow
from medicallist import MedicalReportList
from PySide6.QtCore import Qt
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView


# BASE_URL = "http://127.0.0.1:8000/auth/"
# # BASE_URL = "http://127.0.0.1:8000/"  
from config_loader import BASE_URL
response = requests.get(f'{BASE_URL}')


class PatientForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        
        self.current_patient_id = None
        # 🔹 Ctrl+N for New (Clear Form)
        QShortcut(QKeySequence("Ctrl+N"), self).activated.connect(self.clear_form)

        # 🔹 Ctrl+S for Save (Add Patient)
        QShortcut(QKeySequence("Ctrl+S"), self).activated.connect(self.add_patient)

        # 🔹 Ctrl+F for Search
        QShortcut(QKeySequence("Ctrl+F"), self).activated.connect(self.search_patient)


        # Enable row selection and sorting
        self.tableWidget.setSelectionBehavior(self.tableWidget.SelectionBehavior.SelectRows)
        # self.tableWidget.setSortingEnabled(True)

        self.comboBox.clear()
        self.comboBox.addItems(['M', 'F', 'Other'])

        # Button connections
        self.pushButton.clicked.connect(self.add_patient)
        self.pushButton_3.clicked.connect(self.update_patient)
        self.pushButton_5.clicked.connect(self.clear_form)
        self.pushButton_6.clicked.connect(self.delete_patient)
        self.pushButton_4.clicked.connect(self.search_patient)
        self.pushButton_2.clicked.connect(self.load_patients)
        self.tableWidget.cellClicked.connect(self.load_patient)
        self.tableWidget.cellClicked.connect(self.select_patient)
        
        
        self.pushButton.setToolTip("Ctrl+S to Add Patient")
        self.pushButton_4.setToolTip("Ctrl+F to Search")
        self.pushButton_5.setToolTip("Ctrl+N to Clear")

        self.pushButton_2.setToolTip("Ctrl+M to Medical Report")
        # self.pushButton_2.clicked.connect(self.open_medical_report_list)  
        # Disable update/delete until selection
        self.pushButton_3.setEnabled(False)
        self.pushButton_6.setEnabled(False)

        self.load_patients()
        
    def retranslate_ui(self):
        """
        Called when the app language changes.
        It re-applies the translated strings to this form.
        """
        self.retranslateUi(self)        

    def get_value(self, val):
        return str(val) if val else "N/A"

    def select_patient(self, row, column):
        self.current_patient_id = self.tableWidget.item(row, 0).text()
        self.pushButton_3.setEnabled(True)
        self.pushButton_6.setEnabled(True)

    def add_patient(self):
        if not self.lineEdit.text().strip():
            QMessageBox.warning(self, "Input Error", "Name is required.")
            return
        if not self.lineEdit_2.text().strip():#.isdigit():
            QMessageBox.warning(self, "Input Error", "Phone number must be digits.")
            return
        if not self.lineEdit_4.text().strip().isdigit():
            QMessageBox.warning(self, "Input Error", "Age must be a number.")
            return

        data = {
            "name": self.lineEdit.text(),
            "contact": self.lineEdit_2.text(),
            "email": self.lineEdit_3.text(),
            "address": self.lineEdit_6.text(),
            "gender": self.comboBox.currentText(),
            "profession": self.lineEdit_5.text() or None,
            "age": int(self.lineEdit_4.text())
        }

        try:
            response = requests.post(f"{BASE_URL}/patients/add/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Patient added successfully!")
                self.clear_form()
                self.load_patients()
            else:
                QMessageBox.warning(self, "Error", response.json().get("error", "Add failed."))
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    def update_patient(self):
        if not self.current_patient_id:
            QMessageBox.warning(self, "Warning", "No patient selected!")
            return
        if not self.lineEdit_4.text().isdigit():
            QMessageBox.warning(self, "Input Error", "Age must be a number.")
            return

        data = {
            "name": self.lineEdit.text(),
            "contact": self.lineEdit_2.text(),
            "email": self.lineEdit_3.text(),
            "address": self.lineEdit_6.text(),
            "gender": self.comboBox.currentText(),
            "profession": self.lineEdit_5.text() or None,
            "age": int(self.lineEdit_4.text())
        }

        try:
            response = requests.post(f"{BASE_URL}/patients/update/{self.current_patient_id}/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Patient updated successfully!")
                self.load_patients()
            else:
                QMessageBox.critical(self, "Error", response.json().get('error', 'Failed to update patient'))
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    def delete_patient(self):
        if not self.current_patient_id:
            QMessageBox.warning(self, "Warning", "No patient selected!")
            return

        reply = QMessageBox.question(
            self, "Confirm Delete", "Are you sure you want to delete this patient?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            try:
                response = requests.delete(f"{BASE_URL}/patients/delete/{self.current_patient_id}/")
                if response.status_code == 200:
                    QMessageBox.information(self, "Success", "Patient deleted successfully!")
                    self.clear_form()
                    self.load_patients()
                else:
                    QMessageBox.critical(self, "Error", response.json().get('error', 'Failed to delete patient'))
            except requests.RequestException as e:
                QMessageBox.critical(self, "Network Error", str(e))

    def load_patients(self):
        try:
            response = requests.get(f"{BASE_URL}/patients/list/")
            if response.status_code == 200:
                patients = response.json().get('patients', [])
                self.tableWidget.setRowCount(0)
                self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                table = self.tableWidget

                for patient in patients:
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)

                    self.tableWidget.setItem(row, 0, QTableWidgetItem(self.get_value(patient.get('id'))))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(self.get_value(patient.get('name'))))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(self.get_value(patient.get('email'))))
                    self.tableWidget.setItem(row, 3, QTableWidgetItem(self.get_value(patient.get('contact'))))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(self.get_value(patient.get('profession'))))
                    self.tableWidget.setItem(row, 5, QTableWidgetItem(self.get_value(patient.get('age'))))
                    self.tableWidget.setItem(row, 6, QTableWidgetItem(self.get_value(patient.get('gender'))))
                    self.tableWidget.setItem(row, 7, QTableWidgetItem(self.get_value(patient.get('address'))))
                    self.tableWidget.setItem(row, 8, QTableWidgetItem(self.get_value(patient.get('date_registered'))))

                # ✅ Sort after data is inserted
                self.tableWidget.sortItems(1, Qt.SortOrder.AscendingOrder)
                
                table.setColumnWidth(0,  60)   # id
                table.setColumnWidth(1, 550)   # name
                table.setColumnWidth(2, 220)   # email
                table.setColumnWidth(3, 120)   # contact
                table.setColumnWidth(4, 130)   # profession
                table.setColumnWidth(5,  50)   # age
                table.setColumnWidth(6,  70)   # gender
                table.setColumnWidth(7, 250)   # address
                table.setColumnWidth(8, 10)   # date_registered
            else:
                QMessageBox.critical(self, "Error", f"Failed to load patients: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
    # def load_patients(self):
    #     try:
    #         response = requests.get(f"{BASE_URL}patients/list/")
    #         if response.status_code != 200:
    #             QMessageBox.critical(self, "Error",
    #                                 f"Failed to load patients: {response.status_code}")
    #             return

    #         patients = response.json().get('patients', [])
    #         table = self.tableWidget
    #         self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    #         # 1. Clean the table
    #         table.setRowCount(0)

    #         # 2. Fill the table (no resize yet)
    #         for patient in patients:
    #             row = table.rowCount()
    #             table.insertRow(row)

    #             table.setItem(row, 0, QTableWidgetItem(self.get_value(patient.get('id'))))
    #             table.setItem(row, 1, QTableWidgetItem(self.get_value(patient.get('name'))))
    #             table.setItem(row, 2, QTableWidgetItem(self.get_value(patient.get('email'))))
    #             table.setItem(row, 3, QTableWidgetItem(self.get_value(patient.get('contact'))))
    #             table.setItem(row, 4, QTableWidgetItem(self.get_value(patient.get('profession'))))
    #             table.setItem(row, 5, QTableWidgetItem(self.get_value(patient.get('age'))))
    #             table.setItem(row, 6, QTableWidgetItem(self.get_value(patient.get('gender'))))
    #             table.setItem(row, 7, QTableWidgetItem(self.get_value(patient.get('address'))))
    #             table.setItem(row, 8, QTableWidgetItem(self.get_value(patient.get('date_registered'))))

    #         # 3. Sort **after** all rows are inserted
    #         table.sortItems(1, Qt.AscendingOrder)

    #         # ------------------------------------------------------------------
    #         # 4. Resize columns to their *contents* (the smart way)
    #         # ------------------------------------------------------------------
    #         #   • ResizeMode.Interactive  → user can still drag the header
    #         #   • ResizeToContents        → column width = widest cell (including header)
    #         #   • Stretch (optional)     → remaining space is distributed
    #         # ------------------------------------------------------------------
    #         header = table.horizontalHeader()

    #         # First let Qt calculate the needed width for every column
    #         for col in range(table.columnCount()):
    #             header.setSectionResizeMode(col, QHeaderView.ResizeToContents)

    #         # (Optional) Give the *last* column the rest of the space
    #         # header.setSectionResizeMode(table.columnCount() - 1, QHeaderView.Stretch)

    #         # Force an immediate layout update
    #         table.resizeColumnsToContents()

    #         # ------------------------------------------------------------------
    #         # 5. (Alternative) If you prefer *Stretch* for *all* columns but
    #         #     still want them to start with a sensible width:
    #         # ------------------------------------------------------------------
    #         # header.setSectionResizeMode(QHeaderView.Stretch)
    #         # table.resizeColumnsToContents()   # still gives a good baseline
    #         # ------------------------------------------------------------------

    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))
            
            
    def load_patient(self, row, column):
        self.current_patient_id = self.get_safe_text(self.tableWidget.item(row, 0))
        self.lineEdit.setText(self.get_safe_text(self.tableWidget.item(row, 1)))
        self.lineEdit_2.setText(self.get_safe_text(self.tableWidget.item(row, 3)))
        self.lineEdit_3.setText(self.get_safe_text(self.tableWidget.item(row, 2)))
        self.lineEdit_6.setText(self.get_safe_text(self.tableWidget.item(row, 7)))
        self.comboBox.setCurrentText(self.get_safe_text(self.tableWidget.item(row, 6)))
        self.lineEdit_5.setText(self.get_safe_text(self.tableWidget.item(row, 4)))
        self.lineEdit_4.setText(self.get_safe_text(self.tableWidget.item(row, 5)))

    def get_safe_text(self, item):
        return item.text() if item else ""

    def clear_form(self):
        self.current_patient_id = None
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_6.clear()
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()

        # Reset button states
        self.pushButton_3.setEnabled(False)
        self.pushButton_6.setEnabled(False)

    def search_patient(self):
        query = self.lineEdit.text()
        try:
            response = requests.get(f"{BASE_URL}/patients/search/", params={"q": query})
            if response.status_code == 200:
                self.update_table(response.json().get('patients', []))
            else:
                QMessageBox.warning(self, "Error", "Failed to search patients.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def update_table(self, patients):
        self.tableWidget.setRowCount(0)
        for patient in patients:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(self.get_value(patient['id'])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(self.get_value(patient['name'])))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(self.get_value(patient['email'])))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(self.get_value(patient['contact'])))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(self.get_value(patient['profession'])))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(self.get_value(patient['age'])))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(self.get_value(patient['gender'])))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(self.get_value(patient['address'])))
            self.tableWidget.setItem(row, 8, QTableWidgetItem(self.get_value(patient['date_registered'])))
        self.tableWidget.sortItems(1, Qt.SortOrder.AscendingOrder)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PatientForm()
    window.show()
    sys.exit(app.exec())
