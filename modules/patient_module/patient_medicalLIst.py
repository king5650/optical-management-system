import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
    
    
import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView, QCheckBox, QLineEdit
)
from PySide6.QtCore import Qt


# from ui_ux.medical_module.ui_p_MedicalList1 import Ui_MainWindow 
from ui_ux.medical_module.ui_patient_MedicalList_ok import Ui_MainWindow 
from testform import MedicalReportForm
from ui_ux.medical_module.ui_patient_medical_reportList3 import Ui_Form

 
from config_loader import BASE_URL
response = requests.get(f'{BASE_URL}')


# BASE_URL = "http://127.0.0.1:8000/auth"

class MedicalReportSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)        

        self.searchButton.clicked.connect(self.search_patient)  # Search button
        self.create_form.clicked.connect(self.view_medical_report)  # View button
        self.pushButton.clicked.connect(self.load_patients)  # View button
        self.view_prescription.clicked.connect(self.create_medical_report)  # Create button
        self.lineEdit.setPlaceholderText("Search by name, email, or contact...")

        self.tableWidget.setSelectionBehavior(self.tableWidget.SelectionBehavior.SelectRows)
        self.tableWidget.setSortingEnabled(True)

        self.load_patients()
        
    def retranslate_ui(self):
        """
        Called when the app language changes.
        It re-applies the translated strings to this form.
        """
        self.retranslateUi(self) 
    def load_patients(self):
        try:
            response = requests.get(f"{BASE_URL}/patients/list/")
            if response.status_code == 200:
                self.update_table(response.json()['patients'])
            else:
                QMessageBox.warning(self, "Error", "Failed to load patients.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def get_value(self, val):
        return str(val) if val not in (None, '', 'null') else 'N/A'


    def update_table(self, patients):
        """Update the table with a list of patients."""
        self.tableWidget.setRowCount(0)
        self.tableWidget.setSortingEnabled(False)  # Disable sorting while loading
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

        # Enable sorting and sort alphabetically by Name (column 1)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.sortItems(1, Qt.SortOrder.AscendingOrder)



    def get_selected_patient_info(self):
        row = self.tableWidget.currentRow()
        if row < 0:
            return None
        return {
            'id': self.tableWidget.item(row, 0).text(),
            'name': self.tableWidget.item(row, 1).text(),
            'email': self.tableWidget.item(row, 2).text(),
            'contact': self.tableWidget.item(row, 3).text(),
            'address': self.tableWidget.item(row, 4).text(),
            'profession': self.tableWidget.item(row, 5).text(),
            'age': self.tableWidget.item(row, 6).text(),
            'gender': self.tableWidget.item(row, 7).text(),
        }

    def create_medical_report(self):
        patient = self.get_selected_patient_info()
        if not patient:
            QMessageBox.warning(self, "No Selection", "Please select a patient to create a medical report.")
            return

        #self.medical_report_form = MedicalReportForm(
        self.medical_report_form = MedicalReportForm(
            patient_id=patient['id'],
            patient_name=patient['name'],
            patient_age=patient['age'],
            patient_gender=patient['gender'],
            patient_profession=patient['profession']
        )
        self.medical_report_form.show()
        self.medical_report_form.generate_reference_id()
        # self.close()

    def view_medical_report(self):
        patient = self.get_selected_patient_info()
        if not patient:
            QMessageBox.warning(self, "No Selection", "Please select a patient to view medical reports.")
            return

        self.medical_report_list = MedicalReportList(
            patient['id'], patient['name'], patient['age'], patient['gender'],
            patient['profession'], patient['email'], patient['contact'], patient['address']
        )
        self.medical_report_list.show()

    def search_patient(self):
        query = self.lineEdit.text()
        try:
            response = requests.get(f"{BASE_URL}/patients/search/", params={"q": query})
            if response.status_code == 200:
                self.update_table(response.json()['patients'])
            else:
                QMessageBox.warning(self, "Error", "Failed to search patients.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

class MedicalReportList(QMainWindow):
    def __init__(self, patient_id, patient_name, patient_age, patient_gender, patient_profession, patient_email, patient_contact, patient_address):
        super().__init__()

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.ui = Ui_Form()
        self.ui.setupUi(self.central_widget)

        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_gender = patient_gender
        self.patient_profession = patient_profession
        self.patient_email = patient_email
        self.patient_contact = patient_contact
        self.patient_address = patient_address

        self.ui.label.setText(f"Medical Reports for {self.patient_name}")
        self.ui.p_name.setText(self.patient_name)
        self.ui.p_age.setText(str(self.patient_age))
        self.ui.p_gender.setText(self.patient_gender)
        self.ui.p_profession.setText(self.patient_profession)
        self.ui.p_mail.setText(self.patient_email)
        self.ui.p_contact.setText(self.patient_contact)
        self.ui.p_address.setText(self.patient_address)

        self.ui.deleteButton.clicked.connect(self.delete_medical_report)
        self.ui.viewButton.clicked.connect(self.view_medical_report)
        self.ui.tableWidget.setSelectionBehavior(self.ui.tableWidget.SelectionBehavior.SelectRows)

        self.load_medical_reports()

    def load_medical_reports(self):
        try:
            response = requests.get(f"{BASE_URL}/medical-reports/list/{self.patient_id}/")
            if response.status_code == 200:
                self.update_table(response.json()['reports'])
                
            else:
                QMessageBox.warning(self, "Error", "Failed to load medical reports.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def update_table(self, reports):
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
                
        for report in reports:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(report['id'])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(report.get('ametropie', '')))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(report.get('types_de_verre', '')))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(report.get('teintes', '')))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(report.get('foyers', '')))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(report.get('port', '')))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(report.get('indice', '')))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(report.get('date_registered', '')))
  
    
    def delete_medical_report(self):
        row = self.ui.tableWidget.currentRow()
        if row < 0:
            QMessageBox.warning(self, "No Selection", "Select a report to delete.")
            return

        report_id = self.ui.tableWidget.item(row, 0).text()
        confirm = QMessageBox.question(
            self, "Confirm Deletion",
            f"Are you sure you want to delete medical report ID {report_id}?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirm == QMessageBox.Yes:
            try:
                response = requests.delete(f"{BASE_URL}/medical-reports/delete/{report_id}/")
                if response.status_code == 200:
                    self.ui.tableWidget.removeRow(row)
                    QMessageBox.information(self, "Success", "Report deleted successfully.")
                else:
                    QMessageBox.warning(self, "Error", "Deletion failed.")
            except requests.RequestException as e:
                QMessageBox.critical(self, "Error", str(e))




    def view_medical_report(self):
        row = self.ui.tableWidget.currentRow()
        if row < 0:
            QMessageBox.warning(self, "No Selection", "Select a medical report to view.")
            return

        report_id = self.ui.tableWidget.item(row, 0).text()
        try:
            response = requests.get(f"{BASE_URL}/medical-reports/view/{report_id}/")
            if response.status_code == 200:
                report_data = response.json()
                self.medical_report_form = MedicalReportForm(
                    patient_id=report_data['patient_id'],
                    patient_name=report_data['patient_name'],
                    patient_age=report_data['age_at_report'],
                    patient_gender=report_data['sexe'],
                    patient_profession=report_data['profession_at_report']
                )
                self.medical_report_form.populate_form(report_data)
                self.medical_report_form.set_view_mode()  # 🔒 Disable buttons & inputs
                self.medical_report_form.show()
            else:
                QMessageBox.warning(self, "Error", "Failed to fetch medical report.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")


if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window = MedicalReportSystem()
    window.show()
    sys.exit(app.exec())
