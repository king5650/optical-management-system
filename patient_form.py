import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
# from ui_patient_forms import Ui_MainWindow  # Import your form
from ui_patient_form2 import Ui_MainWindow  # Import your form
from medicallist import MedicalReportList  # Import the generated MedicalList UI


class PatientForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.current_patient_id = None  # For tracking selected patient background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1715909, stop:0.375 rgba(0, 0, 0, 50), stop:0.835227 rgba(0, 0, 0, 75));
                                # border-radius: 10px;


        
        self.comboBox.clear()  # Clear existing options
        self.comboBox.addItems(['M', 'F', 'Other'])  # Add gender choices


        # Connect buttons to methods
        self.pushButton.clicked.connect(self.add_patient)  # Add
        self.pushButton_3.clicked.connect(self.update_patient)  # Update
        self.pushButton_5.clicked.connect(self.clear_form)  # Clear
        self.pushButton_6.clicked.connect(self.delete_patient)  # Delete
        self.pushButton_4.clicked.connect(self.search_patient)  # Search
        self.tableWidget.cellClicked.connect(self.load_patient)  # Load patient on cell click
        # Load patients on startup
        self.load_patients()

            # Connect "Medical Report" button to open the Medical Report List
        self.pushButton_2.clicked.connect(self.open_medical_report_list)
        # Connect table row selection to track the selected patient
        self.tableWidget.cellClicked.connect(self.select_patient)
        
    def select_patient(self, row, column):
        """Get the selected patient's ID from the table."""
        self.current_patient_id = self.tableWidget.item(row, 0).text()  # Assume the patient ID is in column 0

    def open_medical_report_list(self):
        """Open the Medical Report List for the selected patient."""
        if not self.current_patient_id:
            QMessageBox.warning(self, "No Patient Selected", "Please select a patient first.")
            return

        patient_name = self.tableWidget.item(self.tableWidget.currentRow(), 1).text()  # Get the patient's name (column 1)
        self.medical_report_list = MedicalReportList(self.current_patient_id, patient_name)
        self.medical_report_list.show()
        self.close()  # Close the current window



    def add_patient(self):
        data = {
            "name": self.lineEdit.text(),
            "contact": self.lineEdit_2.text(),
            "email": self.lineEdit_3.text(),
            "address": self.lineEdit_6.text(),
            "gender": self.comboBox.currentText(),
            "profession": self.lineEdit_5.text(),
            "age": int(self.lineEdit_4.text())
        }
        response = requests.post('http://127.0.0.1:8000/auth/patients/add/', json=data)
        if response.status_code == 200:
            QMessageBox.information(self, "Success", "Patient added successfully!")
            self.load_patients()
        else:
            QMessageBox.critical(self, "Error", response.json().get('error', 'Failed to add patient'))

    def update_patient(self):
        if not self.current_patient_id:
            QMessageBox.warning(self, "Warning", "No patient selected!")
            return
        data = {
            "name": self.lineEdit.text(),
            "contact": self.lineEdit_2.text(),
            "email": self.lineEdit_3.text(),
            "address": self.lineEdit_6.text(),
            "gender": self.comboBox.currentText(),
            "profession": self.lineEdit_5.text(),
            "age": int(self.lineEdit_4.text())
        }
        response = requests.post(f'http://127.0.0.1:8000/auth/patients/update/{self.current_patient_id}/', json=data)
        if response.status_code == 200:
            msgBox = QMessageBox
            
            # msgBox.information(self, "Success", "Patient updated successfully!")
            # msgBox.setStyleSheet('QMessageBox {color: green}')
            QMessageBox.information(self, "Success", "Patient updated successfully!")
            self.load_patients()
        else:
            QMessageBox.critical(self, "Error", response.json().get('error', 'Failed to update patient'))

    def delete_patient(self):
        if not self.current_patient_id:
            QMessageBox.warning(self, "Warning", "No patient selected!")
            return
        response = requests.delete(f'http://127.0.0.1:8000/auth/patients/delete/{self.current_patient_id}/')
        if response.status_code == 200:
            QMessageBox.information(self, "Success", "Patient deleted successfully!")
            self.load_patients()
        else:
            QMessageBox.critical(self, "Error", response.json().get('error', 'Failed to delete patient'))

    # def load_patients(self):
    #     response = requests.get('http://127.0.0.1:8000/auth/patients/list/')
    #     if response.status_code == 200:
    #         self.tableWidget.setRowCount(0)  # Clear table
    #         for patient in response.json()['patients']:
    #             row = self.tableWidget.rowCount()
    #             self.tableWidget.insertRow(row)
    #             self.tableWidget.setItem(row, 0, QTableWidgetItem(str(patient['id'])))
    #             self.tableWidget.setItem(row, 1, QTableWidgetItem(patient['name']))
    #             self.tableWidget.setItem(row, 2, QTableWidgetItem(patient['email']))
    #             self.tableWidget.setItem(row, 3, QTableWidgetItem(patient['contact']))
    #             self.tableWidget.setItem(row, 4, QTableWidgetItem(patient['profession']))
    #             self.tableWidget.setItem(row, 5, QTableWidgetItem(str(patient['age'])))
    #             self.tableWidget.setItem(row, 6, QTableWidgetItem(patient['gender']))
    #             self.tableWidget.setItem(row, 8, QTableWidgetItem(patient['date_registered']))
    #             self.tableWidget.setItem(row, 7, QTableWidgetItem(patient['address']))
    #     else:
    #         QMessageBox.critical(self, "Error", "Failed to load patients")
    def load_patients(self):
        response = requests.get('http://127.0.0.1:8000/auth/patients/list/')
        if response.status_code == 200:
            self.tableWidget.setRowCount(0)  # Clear table
            for patient in response.json()['patients']:
                row = self.tableWidget.rowCount()
                self.tableWidget.insertRow(row)
                self.tableWidget.setItem(row, 0, QTableWidgetItem(str(patient.get('id', ''))))
                self.tableWidget.setItem(row, 1, QTableWidgetItem(patient.get('name', '')))
                self.tableWidget.setItem(row, 2, QTableWidgetItem(patient.get('email', 'N/A')))  # Default to 'N/A'
                self.tableWidget.setItem(row, 3, QTableWidgetItem(patient.get('contact', '')))
                self.tableWidget.setItem(row, 4, QTableWidgetItem(patient.get('profession', '')))
                self.tableWidget.setItem(row, 5, QTableWidgetItem(str(patient.get('age', ''))))
                self.tableWidget.setItem(row, 6, QTableWidgetItem(patient.get('gender', '')))
                self.tableWidget.setItem(row, 7, QTableWidgetItem(patient.get('address', '')))
                self.tableWidget.setItem(row, 8, QTableWidgetItem(patient.get('date_registered', '')))
        else:
            QMessageBox.critical(self, "Error", "Failed to load patients")

    def load_patient(self, row, column):
        self.current_patient_id = self.tableWidget.item(row, 0).text()  # Get ID from first column
        self.lineEdit.setText(self.tableWidget.item(row, 1).text())
        self.lineEdit_2.setText(self.tableWidget.item(row, 3).text())
        self.lineEdit_3.setText(self.tableWidget.item(row, 2).text())
        self.lineEdit_6.setText(self.tableWidget.item(row, 7).text())
        self.comboBox.setCurrentText(self.tableWidget.item(row, 6).text())
        self.lineEdit_5.setText(self.tableWidget.item(row, 4).text())
        self.lineEdit_4.setText(self.tableWidget.item(row, 5).text())

    def clear_form(self):
        self.current_patient_id = None
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_6.clear()
        self.comboBox.setCurrentIndex(0)
        self.lineEdit_5.clear()
        self.lineEdit_4.clear()
    def search_patient(self):
        query = self.lineEdit.text()  # Use the Name field for the search query
        try:
            response = requests.get(f'http://127.0.0.1:8000/auth/patients/search/?q={query}')
            if response.status_code == 200:
                patients = response.json()['patients']
                self.update_table(patients)
            else:
                QMessageBox.warning(self, "Error", "Failed to search patients.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")



    def update_table(self, patients):
        """Update the table with the given list of patients."""
        self.tableWidget.setRowCount(0)  # Clear the table
        for patient in patients:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(patient['id'])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(patient['name']))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(patient['email']))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(patient['contact']))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(patient['profession']))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(str(patient['age'])))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(patient['gender']))
            
            self.tableWidget.setItem(row, 8, QTableWidgetItem(patient['date_registered']))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(patient['address']))
            

        
        

            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PatientForm()
    window.show()
    sys.exit(app.exec())
