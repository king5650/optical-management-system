import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
from ui_ux.medical_module.ui_MedicalList import Ui_MainWindow  
from medicalrepotForms import MedicalReportForm  
from ui_ux.medical_module.ui_patient_medical_reportList3 import Ui_Form
from PySide6.QtCore import Qt

class MedicalReportSystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Connect buttons
        self.searchButton.clicked.connect(self.search_patient)  # Search
        self.searchButton.clicked.connect(self.search_patient)  # Search button
        self.pushButton_2.clicked.connect(self.view_medical_report)  # View button
        self.pushButton.clicked.connect(self.create_medical_report)  # Create button

        # Load patients into the table on startup
        self.load_patients()

    def load_patients(self):
        """Load all patients and populate the table."""
        try:
            response = requests.get("http://127.0.0.1:8000/auth/patients/list/")
            if response.status_code == 200:
                self.update_table(response.json()['patients'])
            else:
                QMessageBox.warning(self, "Error", "Failed to load patients.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def update_table(self, patients):
        """Update the table with a list of patients."""
        self.tableWidget.setRowCount(0)
        for patient in patients:
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)
            self.tableWidget.setItem(row, 0, QTableWidgetItem(str(patient['id'])))
            self.tableWidget.setItem(row, 1, QTableWidgetItem(patient['name']))
            self.tableWidget.setItem(row, 2, QTableWidgetItem(patient['email']))
            self.tableWidget.setItem(row, 3, QTableWidgetItem(patient['contact']))
            self.tableWidget.setItem(row, 4, QTableWidgetItem(patient['address']))
            self.tableWidget.setItem(row, 5, QTableWidgetItem(patient['profession']))
            self.tableWidget.setItem(row, 6, QTableWidgetItem(str(patient['age'])))
            self.tableWidget.setItem(row, 7, QTableWidgetItem(patient['gender']))


    def view_medical_report(self):
        """Open the Medical Report List for the selected patient."""
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Error", "Please select a patient to view their medical reports.")
            return

        patient_id = self.tableWidget.item(current_row, 0).text()
        patient_name = self.tableWidget.item(current_row, 1).text()
        patient_email = self.tableWidget.item(current_row, 2).text()
        patient_contact = self.tableWidget.item(current_row, 3).text()
        patient_address = self.tableWidget.item(current_row, 4).text()
        patient_profession = self.tableWidget.item(current_row, 5).text()
        patient_age = self.tableWidget.item(current_row, 6).text()
        patient_gender = self.tableWidget.item(current_row, 7).text()
        

        # Open the Medical Report List window
        self.medical_report_list = MedicalReportList(patient_id, patient_name, patient_age, patient_gender, patient_profession, patient_email, patient_contact, patient_address)
        self.medical_report_list.show()

    # def view_medical_report(self):
    #     """Open the Medical Report List for the selected patient."""
    #     current_row = self.tableWidget.currentRow()
    #     if current_row < 0:
    #         QMessageBox.warning(self, "Error", "Please select a patient to view their medical reports.")
    #         return

    #     patient_id = self.tableWidget.item(current_row, 0).text()
    #     patient_name = self.tableWidget.item(current_row, 1).text()

    #     # Open the Medical Report List window
    #     self.medical_report_list = MedicalReportList(patient_id, patient_name)
        # self.medical_report_list.show()
        
    # def view_medical_report(self):
    #     """Display a placeholder message for viewing a medical report."""
    #     current_row = self.tableWidget.currentRow()
    #     if current_row < 0:
    #         QMessageBox.warning(self, "Error", "Please select a patient to view their medical report.")
    #         return
    #     patient_name = self.tableWidget.item(current_row, 1).text()
    #     QMessageBox.information(self, "Medical Report", f"Report list for {patient_name}")



    def search_patient(self):
        """Search for a patient and display the results."""
        query = self.lineEdit.text()
        try:
            response = requests.get(f"http://127.0.0.1:8000/auth/patients/search/?q={query}")
            if response.status_code == 200:
                self.update_table(response.json()['patients'])
            else:
                QMessageBox.warning(self, "Error", "Failed to search patients.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def create_medical_report(self):
        """Redirect to the Medical Report Form for the selected patient."""
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Error", "Please select a patient to create a medical report.")
            return

        patient_id = self.tableWidget.item(current_row, 0).text()
        patient_name = self.tableWidget.item(current_row, 1).text()
        patient_age = self.tableWidget.item(current_row, 6).text()
        patient_gender = self.tableWidget.item(current_row, 7).text()
        patient_profession = self.tableWidget.item(current_row, 5).text()

        self.medical_report_form = MedicalReportForm(patient_id, patient_name, patient_age, patient_gender, patient_profession)
        self.medical_report_form.show()
        self.close()


class MedicalReportList(QMainWindow):
    def __init__(self, patient_id, patient_name, patient_age, patient_gender, patient_profession, patient_email, patient_contact, patient_address):
        super().__init__()
        

        # Create a new QWidget and set it as the central widget
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        # Set up the UI on the new QWidget
        self.ui = Ui_Form()
        self.ui.setupUi(self.central_widget)

        

        self.patient_id = patient_id
        self.patient_name = patient_name
        self.ui.label.setText(f"Medical Reports for {self.patient_name}")  # Update the label
        self.patient_age = patient_age
        self.patient_gender = patient_gender
        self.patient_profession = patient_profession
        self.patient_email = patient_email
        self.patient_contact = patient_contact
        self.patient_address = patient_address
        

        self.ui.p_name.setText(self.patient_name)
        self.ui.p_age.setText(str(self.patient_age))
        self.ui.p_gender.setText(self.patient_gender)
        self.ui.p_profession.setText(self.patient_profession)
        self.ui.p_mail.setText(self.patient_email)
        self.ui.p_contact.setText(self.patient_contact)
        self.ui.p_address.setText(self.patient_address)
        
        self.ui.deleteButton.clicked.connect(self.delete_medical_report)
        self.ui.viewButton.clicked.connect(self.view_medical_report)


        # Load medical reports for the patient
        self.load_medical_reports()

    def load_medical_reports(self):
        """Load and display medical reports associated with the patient."""
        try:
            response = requests.get(f"http://127.0.0.1:8000/auth/medical-reports/list/{self.patient_id}/")
            if response.status_code == 200:
                self.update_table(response.json()['reports'])
            else:
                QMessageBox.warning(self, "Error", "Failed to load medical reports.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def update_table(self, reports):
        """Update the table with a list of medical reports."""
        self.ui.tableWidget.setRowCount(0)  # Clear the table
        for report in reports:
            row = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(report['id'])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(report['ametropie']))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(report['types_de_verre']))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(report['teintes']))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(report['foyers']))
            self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(report['port']))
            self.ui.tableWidget.setItem(row, 6, QTableWidgetItem(report['indice']))
            self.ui.tableWidget.setItem(row, 7, QTableWidgetItem(report['date_registered']))
            
            # self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(report['patient_id']))
    
    def delete_medical_report(self):
        """Delete the selected medical report."""
        current_row = self.ui.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Error", "Please select a medical report to delete.")
            return

        report_id = self.ui.tableWidget.item(current_row, 0).text()
        confirmation = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Are you sure you want to delete the selected medical report (ID: {report_id},)?",
            QMessageBox.Yes | QMessageBox.No
        )

        if confirmation == QMessageBox.Yes:
            try:
                response = requests.delete(f"http://127.0.0.1:8000/auth/medical-reports/delete/{report_id}/")
                if response.status_code == 200:
                    QMessageBox.information(self, "Success", "Medical report deleted successfully!✅ ")
                    self.ui.tableWidget.removeRow(current_row)  # Remove from the table
                else:
                    QMessageBox.warning(self, "Error", "Failed to delete the medical report.")
            except requests.exceptions.RequestException as e:
                QMessageBox.critical(self, "Error", f"Server error: {e}")

    def view_medical_report(self):
        """Open the Medical Report Form with the selected medical report's data."""
        current_row = self.ui.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Error", "Please select a medical report to view.")
            return

        report_id = self.ui.tableWidget.item(current_row, 0).text()
        try:
            response = requests.get(f"http://127.0.0.1:8000/auth/medical-reports/view/{report_id}/")
            if response.status_code == 200:
                report_data = response.json()

                # Open MedicalReportForm with the report data
                self.medical_report_form = MedicalReportForm(
                    patient_id=report_data['patient_id'],
                    patient_name=report_data['patient_name'],
                    patient_age=report_data['age'],
                    patient_gender=report_data['sexe'],
                    patient_profession=report_data['profession']
                )

                # Populate additional fields
                self.medical_report_form.populate_form(report_data)  # New method to populate the form
                self.medical_report_form.show()

            else:
                QMessageBox.critical(self, "Error", "Failed to fetch the medical report data.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

# class MedicalReportList(QMainWindow, Ui_Form):
#     def __init__(self, patient_id, patient_name,):
#         super().__init__()
#         self.setupUi(self)
#         self.patient_id = patient_id
#         self.patient_name = patient_name
#         # self.patient_age = patient_age
#         # self.patient_gender = patient_gender
#         # self.patient_profession = patient_profession
#         # self.patient_email = patient_email
#         # self.patient_contact = patient_contact
#         # patient_age, patient_gender, patient_profession, patient_email, patient_contact
#         self.label.setText(f"Medical Reports for {self.patient_name}")

#         # Load medical reports for the patient
#         self.load_medical_reports()

#     def load_medical_reports(self):
#         """Load and display medical reports associated with the patient."""
#         try:
#             response = requests.get(f"http://127.0.0.1:8000/auth/medical-reports/list/{self.patient_id}/")
#             if response.status_code == 200:
#                 self.update_table(response.json()['reports'])
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to load medical reports.")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")

#     def update_table(self, reports):
#         """Update the table with a list of medical reports."""
#         self.tableWidget.setRowCount(0)
#         for report in reports:
#             row = self.tableWidget.rowCount()
#             self.tableWidget.insertRow(row)
#             self.tableWidget.setItem(row, 0, QTableWidgetItem(str(report['id'])))
#             self.tableWidget.setItem(row, 1, QTableWidgetItem(report['ametropie']))
#             self.tableWidget.setItem(row, 2, QTableWidgetItem(report['types_de_verre']))
#             self.tableWidget.setItem(row, 3, QTableWidgetItem(report['date_registered']))




if __name__ == "__main__":
    QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    window = MedicalReportSystem()
    window.show()
    sys.exit(app.exec())













# if __name__ == "__main__":
#     from PySide6.QtCore import Qt
#     from PySide6.QtWidgets import QApplication

#     # Set the OpenGL context attribute before creating QApplication
#     QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)

#     app = QApplication(sys.argv)
#     window = MedicalReportSystem()
#     window.show()
#     sys.exit(app.exec())






# import sys
# import requests
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
# from ui_MedicalList import Ui_MainWindow  # Replace with the correct import for your UI file
# from medicalrepotForms import MedicalReportForm


# class MedicalReportSystem(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

#         # Connect buttons
#         self.searchButton.clicked.connect(self.search_patient)  # Search button
#         self.pushButton_2.clicked.connect(self.view_medical_report)  # View button
#         self.pushButton.clicked.connect(self.create_medical_report)  # Create button

#         # Load patients into the table on startup
#         self.load_patients()

#     def load_patients(self):
#         """Fetch and display all patients in the table."""
#         try:
#             response = requests.get('http://127.0.0.1:8000/auth/patients/list/')
#             if response.status_code == 200:
#                 self.update_table(response.json()['patients'])
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to load patients.")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")

#     def search_patient(self):
#         """Search for a patient and display the results in the table."""
#         query = self.lineEdit.text()  # Get search query from the line edit
#         try:
#             response = requests.get(f'http://127.0.0.1:8000/auth/patients/search/?q={query}')
#             if response.status_code == 200:
#                 self.update_table(response.json()['patients'])
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to search patients.")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")

#     def update_table(self, patients):
#         """Update the table with a list of patients."""
#         self.tableWidget.setRowCount(0)  # Clear existing rows
#         for patient in patients:
#             row = self.tableWidget.rowCount()
#             self.tableWidget.insertRow(row)
#             self.tableWidget.setItem(row, 0, QTableWidgetItem(patient['name']))
#             self.tableWidget.setItem(row, 1, QTableWidgetItem(patient['email']))
#             self.tableWidget.setItem(row, 2, QTableWidgetItem(patient['contact']))
#             self.tableWidget.setItem(row, 3, QTableWidgetItem(patient['address']))
#             self.tableWidget.setItem(row, 4, QTableWidgetItem(patient['profession']))
#             self.tableWidget.setItem(row, 5, QTableWidgetItem(str(patient['age'])))
#             self.tableWidget.setItem(row, 6, QTableWidgetItem(patient['gender']))

#     def view_medical_report(self):
#         """Display a placeholder message for viewing a medical report."""
#         current_row = self.tableWidget.currentRow()
#         if current_row < 0:
#             QMessageBox.warning(self, "Error", "Please select a patient to view their medical report.")
#             return
#         patient_name = self.tableWidget.item(current_row, 0).text()
#         QMessageBox.information(self, "Medical Report", f"Report list for {patient_name}")



#     def create_medical_report(self):
#         current_row = self.tableWidget.currentRow()
#         if current_row < 0:
#             QMessageBox.warning(self, "Error", "Please select a patient to create a medical report.")
#             return

#         patient_id = self.tableWidget.item(current_row, 0).text()  # Assuming patient ID is in column 0
#         patient_name = self.tableWidget.item(current_row, 1).text()  # Assuming patient name is in column 1
#         patient_age = self.tableWidget.item(current_row, 5).text()  # Assuming patient age is in column 5
#         patient_gender = self.tableWidget.item(current_row, 6).text()  # Assuming patient gender is in column 6
#         patient_profession = self.tableWidget.item(current_row, 4).text()  # Assuming patient profession is in column 4

#         self.medical_report_form = MedicalReportForm(patient_id, patient_name, patient_age, patient_gender, patient_profession)
#         self.medical_report_form.show()
#         self.close()

#     # def create_medical_report(self):
#     #     """Display a placeholder message for creating a medical report."""
#     #     current_row = self.tableWidget.currentRow()
#     #     if current_row < 0:
#     #         QMessageBox.warning(self, "Error", "Please select a patient to create a medical report.")
#     #         return
#     #     patient_name = self.tableWidget.item(current_row, 0).text()
#     #     QMessageBox.information(self, "Create Medical Report", f"Medical report for {patient_name}")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MedicalReportSystem()
#     window.show()
#     sys.exit(app.exec())





















# import sys
# import requests
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from ui_MedicalList import Ui_MainWindow  
# import requests
# from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
# from ui_MedicalList import Ui_MainWindow  # Import the Medical Report List UI
# from medicalrepotForm import MedicalReporForm  # Import the Medical Report Form for adding/editing reports



# class MedicalReportList(QMainWindow, Ui_MainWindow):
#     def __init__(self, patient_id, patient_name):
#         super().__init__()
#         self.setupUi(self)
#         self.patient_id = patient_id
#         self.patient_name = patient_name

#         # Set the patient's name in the UI
#         self.label.setText(f"Name: {self.patient_name}")

#         # Connect "Add Medical Report" button to open the form
#         self.pushButton.clicked.connect(self.add_medical_report)

#         # Connect table cell click to view details of the medical report
#         self.tableWidget.cellClicked.connect(self.view_medical_report)

#         # Load all medical reports for the selected patient
#         self.load_medical_reports()
#     def open_add_report_form(self):
#         """Open the form to add a new medical report."""
#         self.medical_report_form = MedicalReporForm(patient_id=self.patient_id)
#         self.medical_report_form.show()
#         self.close()  # Close the current window 
        
#     def load_medical_reports(self):
#         """Fetch and display all medical reports for the selected patient."""
#         response = requests.get(f'http://127.0.0.1:8000/auth/medical_reports/{self.patient_id}/')  # Adjust URL as needed
#         if response.status_code == 200:
#             reports = response.json().get('medical_reports', [])
#             self.update_table(reports)
#         else:
#             QMessageBox.critical(self, "Error", "Failed to load medical reports.")

#     def update_table(self, reports):
#         """Update the table with medical report data."""
#         self.tableWidget.setRowCount(0)  # Clear the table
#         for report in reports:
#             row = self.tableWidget.rowCount()
#             self.tableWidget.insertRow(row)
#             self.tableWidget.setItem(row, 0, QTableWidgetItem(str(report['id'])))
#             self.tableWidget.setItem(row, 1, QTableWidgetItem(report['date']))
#             self.tableWidget.setItem(row, 2, QTableWidgetItem("File"))

#     def view_medical_report(self, row, column):
#         """Open the selected medical report in a form."""
#         report_id = self.tableWidget.item(row, 0).text()
#         self.medical_report_form = MedicalReporForm(report_id=report_id)
#         self.medical_report_form.show()
#         self.close()  # Close the current window

#     def add_medical_report(self):
#         """Open the form to add a new medical report for the selected patient."""
#         self.medical_report_form = MedicalReporForm(patient_id=self.patient_id)
#         self.medical_report_form.show()
#         self.close()  # Close the current window


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MedicalReportList()
#     window.show()
#     sys.exit(app.exec())
