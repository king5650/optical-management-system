import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from ui_ordnances2 import Ui_MainWindow  # Import the UI file for the medical report form
from reportlab.pdfgen import canvas  # Library to generate PDFs
import os
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtGui import QPixmap, QPainter
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QMessageBox
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import QPainter
from PySide6.QtCore import QRect
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter
from PySide6.QtCore import QRect, QPoint
from PySide6.QtWidgets import QWidget
from ui_ux.medical_module.ui_ordnance1 import Ui_MainWindow 
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QGridLayout
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtGui import QPainter, QFont, QRegion
from PySide6.QtCore import QRect, QPoint
from print_template import Ui_Form  # Import the generated template class
# from ui_pdf_print import Ui_Form  # Import the generated Python class
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtGui import QPainter, QFont, QRegion, QPageSize
from PySide6.QtCore import QRect, QPoint
from print_template import Ui_Form 
from datetime import datetime
from PySide6.QtGui import QPainter, QFont  # Import QFont here
from PySide6.QtCore import Qt
import time



class MedicalReportForm(QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id, patient_name, patient_age, patient_gender, patient_profession):
        super().__init__()
        self.setupUi(self)
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_gender = patient_gender
        self.patient_profession = patient_profession
        
        

        # Populate patient details
        self.patientName.setText(self.patient_name)
        self.pateintage.setText(str(self.patient_age))
        self.comboBox.addItems(['Male', 'Female', 'Other'])
        self.comboBox.setCurrentText(self.patient_gender)
        self.patientprofesion.setText(self.patient_profession)
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format as needed
        self.label_3.setText(current_datetime)
        
        
    def populate_form(self, report_data):
        """Populate the form with medical report data."""
        self.lineEdit_4.setText(report_data['sphere_od'])
        self.lineEdit_5.setText(report_data['cyl_od'])
        self.lineEdit_6.setText(report_data['axe_od'])
        self.lineEdit_7.setText(report_data['addition_od'])
        self.lineEdit_8.setText(report_data['sphere_og'])
        self.lineEdit_9.setText(report_data['cyl_og'])
        self.lineEdit_10.setText(report_data['axe_og'])
        self.lineEdit_11.setText(report_data['addition_og'])
        self.comboBox_2.setCurrentText(report_data['ametropie'])
        self.comboBox_3.setCurrentText(report_data['types_de_verre'])
        self.comboBox_4.setCurrentText(report_data['teintes'])
        self.comboBox_5.setCurrentText(report_data['foyers'])
        self.comboBox_6.setCurrentText(report_data['port'])
        self.comboBox_7.setCurrentText(report_data['indice'])
        
                
        # Populate dropdowns
        ametropie_choices = ['Myopie', 'Hypermétropie', 'Astigmatisme', 'Presbytie', 'Emmétropie']
        verre_choices = ['Minéraux', 'Organiques', 'Polycarbonates']
        teintes_choices = ['Blanc', 'Gris', 'Photochromique', 'Antireflet', 'Bleue Protect']
        foyers_choices = ['Unifocaux', 'Bifocaux', 'Progressifs']
        port_choices = ['Constant', 'Lecture']
        indice_choices = ['Normal', 'Fort Indice']

        self.comboBox_2.addItems(ametropie_choices)
        self.comboBox_3.addItems(verre_choices)
        self.comboBox_4.addItems(teintes_choices)
        self.comboBox_5.addItems(foyers_choices)
        self.comboBox_6.addItems(port_choices)
        self.comboBox_7.addItems(indice_choices)

        # Set default values (optional)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.comboBox_6.setCurrentIndex(0)
        self.comboBox_7.setCurrentIndex(0)

        # Connect buttons
        self.saveButton.clicked.connect(self.save_report)
        self.pirintBUtton.clicked.connect(self.print_report)

    def save_report(self):
        """Save the medical report to the database."""
        data = {
            "patient_id": int(self.patient_id),
            "patient_name": self.patient_name, 
            "age": self.pateintage.text(),
            "sexe": self.comboBox.currentText(),
            "profession": self.patientprofesion.text(),
            "sphere_od": self.lineEdit_4.text(),
            "cyl_od": self.lineEdit_5.text(),
            "axe_od": self.lineEdit_6.text(),
            "addition_od": self.lineEdit_7.text(),
            "sphere_og": self.lineEdit_8.text(),
            "cyl_og": self.lineEdit_9.text(),
            "axe_og": self.lineEdit_10.text(),
            "addition_og": self.lineEdit_11.text(),
            "ametropie": self.comboBox_2.currentText(),
            "types_de_verre": self.comboBox_3.currentText(),
            "teintes": self.comboBox_4.currentText(),
            "foyers": self.comboBox_5.currentText(),
            "port": self.comboBox_6.currentText(),
            "indice": self.comboBox_7.currentText(),
        }

        print("Data to send:", data)  # Debugging

        try:
            response = requests.post("http://127.0.0.1:8000/auth/medical-reports/save/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Medical report saved successfully!")
                return True
            else:
                QMessageBox.critical(
                    self, "Error", f"Failed to save the report. {response.json().get('error', '')}"
                )
                return False
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")
            return False
        
        
    # def print_report(self):
    #     """Retrieve data and display it for printing."""
    #     try:
    #         # Use the local data (from save or previously loaded)
    #         data = {
    #             "patient_name": self.patient_name,
    #             # "date_registered": self.date_registered.text(),  # Example date; replace with dynamic value
    #             "age": self.pateintage.text(),
    #             "sexe": self.comboBox.currentText(),
    #             "profession": self.patientprofesion.text(),
    #             "sphere_od": self.lineEdit_4.text(),
    #             "cyl_od": self.lineEdit_5.text(),
    #             "axe_od": self.lineEdit_6.text(),
    #             "addition_od": self.lineEdit_7.text(),
    #             "sphere_og": self.lineEdit_8.text(),
    #             "cyl_og": self.lineEdit_9.text(),
    #             "axe_og": self.lineEdit_10.text(),
    #             "addition_og": self.lineEdit_11.text(),
    #             "ametropie": self.comboBox_2.currentText(),
    #             "types_de_verre": self.comboBox_3.currentText(),
    #             "teintes": self.comboBox_4.currentText(),
    #             "foyers": self.comboBox_5.currentText(),
    #             "port": self.comboBox_6.currentText(),
    #             "indice": self.comboBox_7.currentText(),
    #         }

    #         # Generate the printable report
    #         self.generate_printable_report(data)
    #         print("Local Data for Printing:", data)  # Debugging: Verify the local data

    #         # Generate and display the printable report directly using local data
    #         self.generate_printable_report(data)
    #         time.sleep(2)  # Give time to process fully before sending

    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"Error generating report: {e}")



    def print_report(self):
        """Retrieve data and display it for printing."""
        try:
            # Use local variable for patient name
            patient_name = self.patient_name  # Local variable for patient name

            # Make a GET request to fetch the report data
            response = requests.get(f"http://127.0.0.1:8000/auth/medical-reports/search/{self.patient_id}/")

            if response.status_code == 200:
                report_data = response.json()
                print("Retrieved Data:", report_data)  # Debugging: Check fetched data

                # Check if patient_name is in the retrieved data
                if "patient_name" in report_data:
                    print(f"Patient Name: {report_data['patient_name']}")  # Debugging line
                else:
                    print("Patient name not found in retrieved data.")  # Debugging line

                # Add the local patient name to the report data
                report_data["patient_name"] = patient_name  # Override with local patient name

                # Generate and display the printable report
                self.generate_printable_report(report_data)

            else:
                QMessageBox.critical(self, "Error", "Failed to search report data.")
                print("Error:", response.status_code, response.text)  # Debugging

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")
            print("Exception:", e)  # Debugging
        
        
        
        
        
    # def print_report(self):
    # # Ensure file is completely generated before sending

    #     """Retrieve data and display it for printing."""
    #     # Use the same data structure you send to the API during 'save'
    #     data = {
    #         "patient_id": int(self.patient_id),
    #         "patient_name": self.patient_name, 
    #         "age": self.pateintage.text(),
    #         "sexe": self.comboBox.currentText(),
    #         "profession": self.patientprofesion.text(),
    #         "sphere_od": self.lineEdit_4.text(),
    #         "cyl_od": self.lineEdit_5.text(),
    #         "axe_od": self.lineEdit_6.text(),
    #         "addition_od": self.lineEdit_7.text(),
    #         "sphere_og": self.lineEdit_8.text(),
    #         "cyl_og": self.lineEdit_9.text(),
    #         "axe_og": self.lineEdit_10.text(),
    #         "addition_og": self.lineEdit_11.text(),
    #         "ametropie": self.comboBox_2.currentText(),
    #         "types_de_verre": self.comboBox_3.currentText(),
    #         "teintes": self.comboBox_4.currentText(),
    #         "foyers": self.comboBox_5.currentText(),
    #         "port": self.comboBox_6.currentText(),
    #         "indice": self.comboBox_7.currentText(),
    #     }

    #     print("Local Data for Printing:", data)  # Debugging: Verify the local data

    #     # Generate and display the printable report directly using local data
    #     self.generate_printable_report(data)
    #     try:
    #         self.generate_printable_report(data)
    #         time.sleep(2)  # Give time to process fully before sending
    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"Error generating report: {e}")
            
            
    # def print_report(self):
    #     """Retrieve data and display it for printing."""
    #     try:
    #         # Make a GET request to fetch the report data
    #         response = requests.get(f"http://127.0.0.1:8000/auth/medical-reports/search/{self.patient_id}/")

    #         if response.status_code == 200:
    #             report_data = response.json()
    #             print("Retrieved Data:", report_data)  # Debugging: Check fetched data

    #             # Check if patient_name is in the retrieved data
    #             if "patient_name" in report_data:
    #                 print(f"Patient Name: {report_data['patient_name']}")  # Debugging line
    #             else:
    #                 print("Patient name not found in retrieved data.")  # Debugging line

    #             # Generate and display the printable report
    #             self.generate_printable_report(report_data)

    #         else:
    #             QMessageBox.critical(self, "Error", "Failed to search report data.")
    #             print("Error:", response.status_code, response.text)  # Debugging

    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")
    #         print("Exception:", e)  # Debugging


    def generate_printable_report(self, report_data):
        """Generate a printable report using the UI template and fit to any page size."""
        try:
            # Create a QWidget for the print template
            template_widget = QWidget()
            ui = Ui_Form()
            ui.setupUi(template_widget)

            # Populate the template with report data
            ui.patientNmae_label.setText(report_data.get("patient_name", "N/A"))
             # Capture the current date and time
            current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Format as needed
            ui.dateLabel.setText(current_datetime)  # Set the current date and time
            # ui.dateLabel.setText(report_data.get("date_registered", "N/A"))
            ui.patientAgeLabel.setText(str(report_data.get("age", "")))
            ui.genderLabel.setText(report_data.get("sexe", ""))
            ui.patientProfessionLabel.setText(report_data.get("profession", ""))
            ui.lineEdit_12.setText(report_data.get("sphere_od", ""))
            ui.lineEdit_13.setText(report_data.get("cyl_od", ""))
            ui.lineEdit_14.setText(report_data.get("axe_od", ""))
            ui.lineEdit_15.setText(report_data.get("addition_od", ""))
            ui.lineEdit_16.setText(report_data.get("sphere_og", ""))
            ui.lineEdit_17.setText(report_data.get("cyl_og", ""))
            ui.lineEdit_18.setText(report_data.get("axe_og", ""))
            ui.lineEdit_19.setText(report_data.get("addition_og", ""))
            ui.ametropieLable.setText(report_data.get("ametropie", ""))
            ui.typeDeVerreLabel.setText(report_data.get("types_de_verre", ""))
            ui.teintesLabel.setText(report_data.get("teintes", ""))
            ui.foyers.setText(report_data.get("foyers", ""))
            ui.port.setText(report_data.get("port", ""))
            ui.indice.setText(report_data.get("indice", ""))

            # Prepare the printer
            printer = QPrinter(QPrinter.HighResolution)
            printer.setPageSize(QPageSize(QPageSize.A4))  # Default to A4; can dynamically change to A3, A5, etc.
            printer.setFullPage(True)

            # Create a print dialog
            dialog = QPrintDialog(printer, self)
            if dialog.exec() == QPrintDialog.Accepted:
                # Render the template widget to the printer with proper scaling
                self.render_to_printer(template_widget, printer)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to generate report: {e}")
            print("Error generating report:", e)






    # def generate_printable_report(self, report_data):
    #     """Generate a printable report using the UI template."""
    #     try:
    #         # Create a QWidget to serve as the parent for the template
    #         parent_widget = QWidget()
    #         template_widget = Ui_Form()
    #         template_widget.setupUi(parent_widget)  # Set up the UI on the parent widget

    #         # Populate the template with report data
    #         # Access the patient's name through the report_data
    #         patient = report_data.get("patient_name")  # Ensure this retrieves the patient object
    #         template_widget.patientNmae_label.setText(report_data.get("patient_name", "N/A"))
    #         template_widget.patientAgeLabel.setText(str(report_data.get("age", "")))
    #         template_widget.genderLabel.setText(report_data.get("sexe", ""))
    #         template_widget.patientProfessionLabel.setText(report_data.get("profession", ""))
    #         template_widget.lineEdit_12.setText(report_data.get("sphere_od", ""))
    #         template_widget.lineEdit_13.setText(report_data.get("cyl_od", ""))
    #         template_widget.lineEdit_14.setText(report_data.get("axe_od", ""))
    #         template_widget.lineEdit_15.setText(report_data.get("addition_od", ""))
    #         template_widget.lineEdit_16.setText(report_data.get("sphere_og", ""))
    #         template_widget.lineEdit_17.setText(report_data.get("cyl_og", ""))
    #         template_widget.lineEdit_18.setText(report_data.get("axe_og", ""))
    #         template_widget.lineEdit_19.setText(report_data.get("addition_og", ""))
    #         template_widget.ametropieLable.setText(report_data.get("ametropie", ""))
    #         template_widget.typeDeVerreLabel.setText(report_data.get("types_de_verre", ""))
    #         template_widget.teintesLabel.setText(report_data.get("teintes", ""))
    #         template_widget.foyers.setText(report_data.get("foyers", ""))
    #         template_widget.port.setText(report_data.get("port", ""))
    #         template_widget.indice.setText(report_data.get("indice", ""))
    #         template_widget.dateLabel.setText(report_data.get("date", "N/A"))  # Set the date label

            # Print the populated template
        #     printer = QPrinter(QPrinter.HighResolution)
        #     dialog = QPrintDialog(printer, self)

        #     if dialog.exec():
        #         painter = QPainter(printer)
        #         # Render the parent widget to the painter
        #         parent_widget.render(painter, QPoint(0, 0))  # Specify the position (0, 0)
        #         painter.end()
        #         QMessageBox.information(self, "Success", "Report ready for printing.")

        # except Exception as e:
        #     QMessageBox.critical(self, "Error", f"Failed to generate report: {e}")
        #     print("Error generating report:", e)
            
            
            
    def render_to_printer(self, template_widget, printer):
        """Render the given template to the printer and fit it to the page."""
        try:
            # Initialize QPainter
            painter = QPainter(printer)
            painter.setRenderHint(QPainter.Antialiasing)

            # Get the page rectangle and content rectangle
            page_rect = printer.pageRect(QPrinter.DevicePixel)
            margin = 1  # Adjust margin size in pixels
            content_rect = page_rect.adjusted(margin, margin, -margin, -margin)

            # Calculate scaling factors
            widget_size = template_widget.size()
            scale_x = content_rect.width() / widget_size.width()
            scale_y = content_rect.height() / widget_size.height()
            scale = min(scale_x, scale_y)  # Scale proportionally to fit within content rect

            # Center the widget within the page
            translate_x = content_rect.left() + (content_rect.width() - widget_size.width() * scale) / 2
            translate_y = content_rect.top() + (content_rect.height() - widget_size.height() * scale) / 2
            painter.translate(translate_x, translate_y)
            painter.scale(scale, scale)

            # Render the widget onto the printer
            template_widget.render(
                painter,
                QPoint(0, 0),  # Top-left corner for rendering
                QRegion(),     # Render the entire widget
                QWidget.RenderFlags(QWidget.RenderFlag.DrawChildren | QWidget.RenderFlag.DrawWindowBackground)
            )

            painter.end()  # End the painter
            QMessageBox.information(self, "Success", "Report printed successfully.........!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Error during printing: {e}")
            print("Exception in render_to_printer:", e)


    # def generate_printable_report(self, report_data):
    #     """Generate a printable report using the UI template."""
    #     try:
    #         # Create a QWidget to serve as the parent for the template
    #         parent_widget = QWidget()
    #         template_widget = Ui_Form()
    #         template_widget.setupUi(parent_widget)  # Set up the UI on the parent widget

    #         # Populate the template with report data

    #         template_widget.patientNmae_label.setText(report_data.get("patient_name", "N/A"))  # Patient name
    #         template_widget.dateLabel.setText(report_data.get("date_registered", "N/A"))  # Date created
    #         date = report_data.get("created_at", "N/A")  # Assume the key is 'created_at'
    #         template_widget.dateLabel.setText(date)
    #         template_widget.patientAgeLabel.setText(str(report_data.get("age", "")))
    #         template_widget.genderLabel.setText(report_data.get("sexe", ""))
    #         template_widget.patientProfessionLabel.setText(report_data.get("profession", ""))
    #         template_widget.lineEdit_12.setText(report_data.get("sphere_od", ""))
    #         template_widget.lineEdit_13.setText(report_data.get("cyl_od", ""))
    #         template_widget.lineEdit_14.setText(report_data.get("axe_od", ""))
    #         template_widget.lineEdit_15.setText(report_data.get("addition_od", ""))
    #         template_widget.lineEdit_16.setText(report_data.get("sphere_og", ""))
    #         template_widget.lineEdit_17.setText(report_data.get("cyl_og", ""))
    #         template_widget.lineEdit_18.setText(report_data.get("axe_og", ""))
    #         template_widget.lineEdit_19.setText(report_data.get("addition_og", ""))
    #         template_widget.ametropieLable.setText(report_data.get("ametropie", ""))
    #         template_widget.typeDeVerreLabel.setText(report_data.get("types_de_verre", ""))
    #         template_widget.teintesLabel.setText(report_data.get("teintes", ""))
    #         template_widget.foyers.setText(report_data.get("foyers", ""))
    #         template_widget.port.setText(report_data.get("port", ""))
    #         template_widget.indice.setText(report_data.get("indice", ""))
 
            

    #         # Print the populated template
    #         printer = QPrinter(QPrinter.HighResolution)
    #         dialog = QPrintDialog(printer, self)

    #         if dialog.exec():
    #             painter = QPainter(printer)
    #             # Render the parent widget to the painter
    #             parent_widget.render(painter, QPoint(0, 0))  # Specify the position (0, 0)
    #             painter.end()
    #             QMessageBox.information(self, "Success", "Report ready for printing.")

    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"Failed to generate report: {e}")
    #         print("Error generating report:", e)
            
            
            
    # def generate_printable_report(self, report_data):
    #     """Generate a printable PDF or display for the medical report."""
    #     try:
    #         printer = QPrinter(QPrinter.HighResolution)
    #         dialog = QPrintDialog(printer, self)

    #         if dialog.exec():
    #             painter = QPainter(printer)
    #             # painter.setFont(QtGui.QFont("Arial", 12))

    #             # Print report details
    #             y_position = 100  # Starting Y position

    #             for key, value in report_data.items():
    #                 painter.drawText(100, y_position, f"{key.capitalize()}: {value}")
    #                 y_position += 40  # Adjust line spacing

    #             painter.end()
    #             QMessageBox.information(self, "Success", "Report ready for printing.")

    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"Failed to generate report: {e}")
    #         print("Error generating report:", e)









    # def print_report(self):
    #     """Fetch the medical report from the server and print it."""
    #     try:
    #         # Fetch the report data for this patient
    #         response = requests.get(f"http://127.0.0.1:8000/auth/medical-reports/{self.patient_id}/")
    #         if response.status_code != 200:
    #             QMessageBox.critical(self, "Error", f"Failed to retrieve data: {response.json().get('error', '')}")
    #             return
            
    #         report_data = response.json()  # Retrieve report details as JSON
    #         print("Report Data:", report_data)  # Debugging

    #         # Initialize QPrinter and QPrintDialog for printing
    #         printer = QPrinter(QPrinter.HighResolution)
    #         printer.setOutputFormat(QPrinter.PdfFormat)
    #         printer.setOutputFileName("medical_report.pdf")

    #         print_dialog = QPrintDialog(printer, self)
    #         if print_dialog.exec() == QPrintDialog.Accepted:
    #             self.generate_printable_report(printer, report_data)

    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")



    # def print_report(self):
    #     """Retrieve and print the medical report details."""
    #     try:
    #         # Fetch the medical report data from the server
    #         response = requests.get(f"http://127.0.0.1:8000/auth/medical_reports/{self.patient_id}/")

    #         if response.status_code == 200:
    #             report_data = response.json()

    #             # Generate and display printable content
    #             printer = QPrinter()
    #             printer.setOutputFormat(QPrinter.PdfFormat)  # Can be 'NativeFormat' for direct printing
    #             printer.setOutputFileName("medical_report.pdf")

    #             # Start rendering the content to PDF
    #             painter = QPainter()
    #             if painter.begin(printer):
    #                 # Customize content formatting
    #                 title = "Medical Report"
    #                 painter.setFont(QPainter.Font("Arial", 16))
    #                 painter.drawText(QPoint(100, 100), title)

    #                 # Print Patient Details
    #                 details = [
    #                     f"Patient Name: {self.patient_name}",
    #                     f"Age: {report_data['age']}",
    #                     f"Gender: {report_data['sexe']}",
    #                     f"Profession: {report_data['profession']}",
    #                     f"Sphere OD: {report_data['sphere_od']}  Cyl OD: {report_data['cyl_od']}",
    #                     f"Axe OD: {report_data['axe_od']}  Addition OD: {report_data['addition_od']}",
    #                     f"Sphere OG: {report_data['sphere_og']}  Cyl OG: {report_data['cyl_og']}",
    #                     f"Axe OG: {report_data['axe_og']}  Addition OG: {report_data['addition_og']}",
    #                     f"Ametropie: {report_data['ametropie']}",
    #                     f"Types de Verre: {report_data['types_de_verre']}",
    #                     f"Teintes: {report_data['teintes']}",
    #                     f"Foyers: {report_data['foyers']}",
    #                     f"Port: {report_data['port']}",
    #                     f"Indice: {report_data['indice']}",
    #                 ]

    #                 y = 150
    #                 for detail in details:
    #                     painter.setFont(QPainter.Font("Arial", 12))
    #                     painter.drawText(QPoint(100, y), detail)
    #                     y += 30

    #                 painter.end()
    #                 QMessageBox.information(self, "Print Success", "Medical report ready for printing!")
    #             else:
    #                 QMessageBox.warning(self, "Error", "Failed to print the report.")
    #         else:
    #             QMessageBox.critical(self, "Error", "Failed to fetch the report data.")
    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"An error occurred: {e}")

    # def print_report(self):
    #     """Generate and print the medical report."""
    #     printer = QPrinter(QPrinter.HighResolution)
    #     print_dialog = QPrintDialog(printer, self)

    #     if print_dialog.exec() == QPrintDialog.Accepted:
    #         # Collect patient data for the print template
    #         patient_data = {
    #             "name": self.patientName.text(),
    #             "age": self.pateintage.text(),
    #             "gender": self.comboBox.currentText(),
    #             "profession": self.patientprofesion.text(),
    #             "date": self.dateEdit.text(),  # Assuming you have a date field
    #         }

    #         # Create the print template and render it to the printer
    #         print_template = PrintTemplate(patient_data)  # Replace with the class you defined above
    #         print_template.render_to_printer(printer)
    #         QMessageBox.information(self, "Success", "The report has been sent to the printer.")





# class MedicalReportForm(QMainWindow, Ui_MainWindow):
#     def __init__(self, patient_id, patient_name, patient_age, patient_gender, patient_profession):
#         super().__init__()
#         self.setupUi(self)
#         self.patient_id = patient_id
#         self.patient_name = patient_name
#         self.patient_age = patient_age
#         self.patient_gender = patient_gender
#         self.patient_profession = patient_profession

#         # Populate patient details
#         self.patientName.setText(self.patient_name)
#         self.pateintage.setText(str(self.patient_age))
#         self.comboBox.addItems(['Male', 'Female', 'Other'])  # Populate gender options
#         self.comboBox.setCurrentText(self.patient_gender)
#         self.patientprofesion.setText(self.patient_profession)

#         # Populate dropdowns
#         ametropie_choices = [
#             'Myopie', 'Hypermétropie', 'Astigmatisme', 'Presbytie', 'Emmétropie'
#         ]
#         verre_choices = ['Minéraux', 'Organiques', 'Polycarbonates']
#         teintes_choices = [
#             'Blanc', 'Gris', 'Photochromique', 'Antireflet', 'Bleue Protect'
#         ]
#         foyers_choices = ['Unifocaux', 'Bifocaux', 'Progressifs']
#         port_choices = ['Constant', 'Lecture']
#         indice_choices = ['Normal', 'Fort Indice']

#         self.comboBox_2.addItems(ametropie_choices)
#         self.comboBox_3.addItems(verre_choices)
#         self.comboBox_4.addItems(teintes_choices)
#         self.comboBox_5.addItems(foyers_choices)
#         self.comboBox_6.addItems(port_choices)
#         self.comboBox_7.addItems(indice_choices)

#         # Set default values (optional)
#         self.comboBox_2.setCurrentIndex(0)  # Set default to the first choice
#         self.comboBox_3.setCurrentIndex(0)
#         self.comboBox_4.setCurrentIndex(0)
#         self.comboBox_5.setCurrentIndex(0)
#         self.comboBox_6.setCurrentIndex(0)
#         self.comboBox_7.setCurrentIndex(0)


#         # Connect buttons
#         self.saveButton.clicked.connect(self.save_report)  # Save button
#         self.pirintBUtton.clicked.connect(self.print_patient_report)  # Print button


#     def save_report(self):
#         """Save the medical report to the database."""
#         self.data = {
#             "patient_id": int(self.patient_id),
#             "age": self.pateintage.text(),
#             "sexe": self.comboBox.currentText(),
#             "profession": self.patientprofesion.text(),
#             "sphere_od": self.lineEdit_4.text(),
#             "cyl_od": self.lineEdit_5.text(),
#             "axe_od": self.lineEdit_6.text(),
#             "addition_od": self.lineEdit_7.text(),
#             "sphere_og": self.lineEdit_8.text(),
#             "cyl_og": self.lineEdit_9.text(),
#             "axe_og": self.lineEdit_10.text(),
#             "addition_og": self.lineEdit_11.text(),
#             "ametropie": self.comboBox_2.currentText(),
#             "types_de_verre": self.comboBox_3.currentText(),
#             "teintes": self.comboBox_4.currentText(),
#             "foyers": self.comboBox_5.currentText(),
#             "port": self.comboBox_6.currentText(),
#             "indice": self.comboBox_7.currentText(),
#         }

#         print("Data to send:", self.data)  # Debugging

#         try:
#             response = requests.post("http://127.0.0.1:8000/auth/medical-reports/save/", json=self.data)
#             if response.status_code == 200:
#                 QMessageBox.information(self, "Success", "Medical report saved successfully!")
#                 return True
#             else:
#                 QMessageBox.critical(
#                     self, "Error", f"Failed to save the report. {response.json().get('error', '')}"
#                 )
#                 return False
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")
#             return False


#     def print_patient_report(self):
#         """Handles printing of the medical report."""
#         if not self.patient_name:
#             QMessageBox.warning(self, "Warning", "No patient data available to print!")
#             return

#         printer = QPrinter(QPrinter.HighResolution)
#         print_dialog = QPrintDialog(printer, self)

#         if print_dialog.exec() == QPrintDialog.Accepted:
#             self.render_to_printer(printer)

#     def render_to_printer(self, printer):
#         """Renders the medical form onto the printer."""
#         template_widget = QWidget()
#         self.setupUi(template_widget)

#         # Populate template with current patient data
#         self.patientName.setText(self.patient_name)
#         self.pateintage.setText(str(self.patient_age))
#         self.comboBox.setCurrentText(self.patient_gender)
#         self.patientprofesion.setText(self.patient_profession)

#         # Prepare the painter
#         painter = QPainter(printer)
#         painter.setRenderHint(QPainter.Antialiasing)
#         page_rect = printer.pageRect()

#         # Add margins
#         margin = 50  # Margin in pixels
#         content_rect = page_rect.adjusted(margin, margin, -margin, -margin)

#         # Calculate scaling factors to fit the content
#         widget_size = template_widget.size()
#         scale_x = content_rect.width() / widget_size.width()
#         scale_y = content_rect.height() / widget_size.height()
#         scale = min(scale_x, scale_y)

#         # Center the template in the printable area
#         translate_x = content_rect.left() + (content_rect.width() - widget_size.width() * scale) / 2
#         translate_y = content_rect.top() + (content_rect.height() - widget_size.height() * scale) / 2
#         painter.translate(translate_x, translate_y)
#         painter.scale(scale, scale)

#         # Render the template onto the printer
#         template_widget.render(painter)
#         painter.end()
















    # def print_report(self):
    #     """Print the medical report in the same UI format."""
    #     # Ensure the report is saved before printing
    #     if not self.save_report():
    #         QMessageBox.warning(self, "Warning", "Please save the report before printing.")
    #         return

    #     # Hide the print button before capturing the UI
    #     self.pirintBUtton.setVisible(False)

    #     # Capture the widget as a QPixmap
    #     pixmap = QPixmap(self.size())
    #     self.render(pixmap)

    #     # Save the captured pixmap to a temporary image file
    #     temp_image_path = "temp_report.png"
    #     pixmap.save(temp_image_path, "PNG")

    #     # Open the print dialog
    #     printer = QPrinter(QPrinter.HighResolution)
    #     printer.setOutputFormat(QPrinter.PdfFormat)
    #     printer.setOutputFileName("medical_report.pdf")  # Save as a PDF file

    #     # Create a painter and draw the image onto the PDF
    #     painter = QPainter(printer)
    #     painter.drawPixmap(0, 0, pixmap)
    #     painter.end()

    #     # Restore the print button visibility
    #     self.pirintBUtton.setVisible(True)

    #     QMessageBox.information(self, "Success", "Report printed and saved as medical_report.pdf!")





    # def generate_pdf(self, file_path):
    #     """Generate a PDF using the converted UI Python file."""
    #     # Create an instance of the QWidget and load the UI
    #     report_widget = QWidget()
    #     ui = Ui_MainWindow()
    #     ui.setupUi(report_widget)

    #     # Populate the UI with data
    #     ui.patientNmae_label.setText(self.patient_name)
    #     # ui.patientIdLabel.setText(self.patient_id)
    #     ui.patientAgeLabel.setText(str(self.patient_age))
    #     ui.genderLabel.setText(self.patient_gender)
    #     ui.patientProfessionLabel.setText(self.patient_profession)
    #     ui.ametropieLable.setText(self.comboBox_2.currentText())
    #     ui.typeDeVerreLabel.setText(self.comboBox_3.currentText())
    #     ui.teintesLabel.setText(self.comboBox_4.currentText())
    #     ui.foyers.setText(self.comboBox_5.currentText())
    #     ui.port.setText(self.comboBox_6.currentText())
    #     ui.indice.setText(self.comboBox_7.currentText())

    #     # Create a QPrinter instance
    #     printer = QPrinter(QPrinter.PrinterMode.HighResolution)
    #     printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
    #     printer.setOutputFileName(file_path)

    #     # Render the loaded template to the printer
    #     painter = QPainter(printer)
    #     report_widget.render(painter)
    #     painter.end()

    #     QMessageBox.information(self, "Success", "PDF generated successfully!")


    # def generate_pdf(self, file_path):
    #     """Generate a PDF for the medical report."""
    #     c = canvas.Canvas(file_path)
    #     c.setFont("Helvetica", 12)
    #     c.drawString(100, 800, f"Medical Report for {self.patient_name}")
    #     c.drawString(100, 780, f"Patient ID: {self.patient_id}")
    #     c.drawString(100, 760, f"Age: {self.patient_age}")
    #     c.drawString(100, 740, f"Gender: {self.patient_gender}")
    #     c.drawString(100, 720, f"Profession: {self.patient_profession}")
    #     c.drawString(100, 700, f"Ametropie: {self.comboBox_2.currentText()}")
    #     c.drawString(100, 680, f"Type de Verre: {self.comboBox_3.currentText()}")
    #     c.drawString(100, 660, f"Teintes: {self.comboBox_4.currentText()}")
    #     c.drawString(100, 640, f"Foyers: {self.comboBox_5.currentText()}")
    #     c.drawString(100, 620, f"Port: {self.comboBox_6.currentText()}")
    #     c.drawString(100, 600, f"Indice: {self.comboBox_7.currentText()}")
    #     c.drawString(100, 580, "End of Report.")
    #     c.save()



    # def print_medical_report(self):
    #     """Load the custom UI template and print the medical report."""
    #     # Load the UI template
    #     loader = QUiLoader()
    #     pdf_template = loader.load("front_end/pdf_print.ui")  # Replace with your actual file path

    #     # Populate the template with medical report data
    #     pdf_template.patientNmae_label.setText(self.patient_name)  # Ensure the widget names are correct
    #     pdf_template.patientAgeLabel.setText(str(self.patient_age))
    #     pdf_template.genderLabel.setText(self.patient_gender)
    #     pdf_template.patientProfessionLabel.setText(self.patient_profession)
    #     pdf_template.ametropieLable.setText(self.comboBox_2.currentText())
    #     pdf_template.typeDeVerreLabel.setText(self.comboBox_3.currentText())
    #     pdf_template.teintesLabel.setText(self.comboBox_4.currentText())
    #     pdf_template.foyers.setText(self.comboBox_5.currentText())
    #     pdf_template.port.setText(self.comboBox_6.currentText())
    #     pdf_template.indice.setText(self.comboBox_7.currentText())

    #     # Configure the printer
    #     printer = QPrinter(QPrinter.HighResolution)
    #     printer.setOutputFormat(QPrinter.PdfFormat)
    #     printer.setOutputFileName(f"{self.patient_name}_medical_report.pdf")

    #     # Render the template to the printer
    #     painter = QPainter(printer)

    #     # Render the full widget to the printer
    #     pdf_template.render(
    #         painter,
    #         targetOffset=QPoint(0, 0),  # Render starting at the top-left corner
    #         sourceRegion=QRect(),      # Use the entire widget's area
    #         renderFlags=QWidget.RenderFlags(QWidget.RenderFlag.DrawWindowBackground | QWidget.RenderFlag.DrawChildren)
    #     )
    #     painter.end()

    #     # Notify the user
    #     QMessageBox.information(self, "Success", "The medical report has been printed as a PDF!")

    # def print_medical_report(self):
    #     """Load the custom UI template and print the medical report."""
    #     # Load the UI template
    #     loader = QUiLoader()
    #     pdf_template = loader.load("front_end/pdf_print.ui")  # Replace with your actual file path

    #     # Populate the template with medical report data
    #     pdf_template.patientNmae_label.setText(self.patient_name)  # Replace with widget names in `pdf_print.ui`
    #     pdf_template.patientAgeLabel.setText(str(self.patient_age))
    #     pdf_template.genderLabel.setText(self.patient_gender)
    #     pdf_template.patientProfessionLabel.setText(self.patient_profession)
    #     pdf_template.ametropieLable.setText(self.comboBox_2.currentText())
    #     pdf_template.typeDeVerreLabel.setText(self.comboBox_3.currentText())
    #     pdf_template.teintesLabel.setText(self.comboBox_4.currentText())
    #     pdf_template.foyers.setText(self.comboBox_5.currentText())
    #     pdf_template.port.setText(self.comboBox_6.currentText())
    #     pdf_template.indice.setText(self.comboBox_7.currentText())

    #     # Configure the printer
    #     printer = QPrinter(QPrinter.HighResolution)
    #     printer.setOutputFormat(QPrinter.PdfFormat)
    #     printer.setOutputFileName(f"{self.patient_name}_medical_report.pdf")

    #     # Render the template to the printer
    #     painter = QPainter(printer)

    #     rect = QRect(0, 0, pdf_template.width(), pdf_template.height())  # Define the rendering region
    #     pdf_template.render(
    #         painter,
    #         targetOffset=QPoint(0, 0),  # Render starting at the top-left corner
    #         sourceRegion=rect,         # Use the entire widget's area
    #         renderFlags=QWidget.RenderFlags(QWidget.RenderFlag.DrawChildren)  # Render children widgets
    #     )
    #     painter.end()

    #     # Notify the user
    #     QMessageBox.information(self, "Success", "The medical report has been printed as a PDF!")













    # def print_medical_report(self):
    #     """Load the custom UI template and print the medical report."""
    #     # Load the UI template
    #     loader = QUiLoader()
    #     pdf_template = loader.load("front_end\pdf_print.ui")  # Replace with your file path

    #     # Populate the template with medical report data
    #     pdf_template.patientNmae_label.setText(self.patient_name)  # Replace with widget names in `pdf_print.ui`
    #     # pdf_template.patientIdLabel.setText(self.patient_id)
    #     pdf_template.patientAgeLabel.setText(str(self.patient_age))
    #     pdf_template.genderLabel.setText(self.patient_gender)
    #     pdf_template.patientProfessionLabel.setText(self.patient_profession)
    #     pdf_template.ametropieLable.setText(self.comboBox_2.currentText())
    #     pdf_template.typeDeVerreLabel.setText(self.comboBox_3.currentText())
    #     pdf_template.teintesLabel.setText(self.comboBox_4.currentText())
    #     pdf_template.foyers.setText(self.comboBox_5.currentText())
    #     pdf_template.port.setText(self.comboBox_6.currentText())
    #     pdf_template.indice.setText(self.comboBox_7.currentText())

    #     # Configure the printer
    #     printer = QPrinter(QPrinter.PrinterMode.HighResolution)
    #     printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
    #     printer.setOutputFileName(f"{self.patient_name}_medical_report.pdf")

    #     # Render the template to the printer
    #     painter = QPainter(printer)
    # # Adjust the render rectangle
    #     rect = QRect(0, 0, pdf_template.width(), pdf_template.height())
    #     pdf_template.render(
    #         painter,
    #         targetOffset=QPoint(0, 0),  # Starting at the top-left corner
    #         sourceRegion=rect,          # The region to render
    #         flags=QWidget.RenderFlag.DrawChildren  # Render children as well
    #     )
    #     painter.end()

    #     # Notify the user
    #     QMessageBox.information(self, "Success", "The medical report has been printed as a PDF!")


















    # def print_report(self):
    #     """Print the medical report."""
    #     # Ensure the report is saved before printing
    #     if not self.save_report():
    #         QMessageBox.warning(self, "Warning", "Please save the report before printing.")
    #         return

    #     # Generate PDF
    #     output_dir = "medical_reports"
    #     if not os.path.exists(output_dir):
    #         os.makedirs(output_dir)
    #     file_path = os.path.join(output_dir, f"medical_report_{self.patient_id}.pdf")
    #     self.generate_pdf(file_path)

    #     QMessageBox.information(self, "Print", f"Medical report for {self.patient_name} has been saved as a PDF:\n{file_path}")

    # def print_report(self):
    #     """Print the medical report."""
    #     # Ensure the report is saved before printing
    #     if not self.save_report():
    #         QMessageBox.warning(self, "Warning", "Please save the report before printing.")
    #         return

    #     # Hide the print button before printing
    #     self.pirintBUtton.setVisible(False)
    #     QMessageBox.information(self, "Print", f"Printing medical report for {self.patient_name}...")
    #     self.pirintBUtton.setVisible(True)
















    # def save_report(self):
    #     """Save the medical report to the database."""
    #     data = {
    #         "patient_id": self.patient_id,
            
    #         # "patient_name": self.patient_name,
    #         "age": self.pateintage.text(),
    #         "sexe": self.comboBox.currentText(),
    #         "profession": self.patientprofesion.text(),
    #         "sphere_od": self.lineEdit_4.text(),
    #         "cyl_od": self.lineEdit_5.text(),
    #         "axe_od": self.lineEdit_6.text(),
    #         "addition_od": self.lineEdit_7.text(),
    #         "sphere_og": self.lineEdit_8.text(),
    #         "cyl_og": self.lineEdit_9.text(),
    #         "axe_og": self.lineEdit_10.text(),
    #         "addition_og": self.lineEdit_11.text(),
    #         "ametropie": self.comboBox_2.currentText(),
    #         "types_de_verre": self.comboBox_3.currentText(),
    #         "teintes": self.comboBox_4.currentText(),
    #         "foyers": self.comboBox_5.currentText(),
    #         "port": self.comboBox_6.currentText(),
    #         "indice": self.comboBox_7.currentText(),
    #     }

    #     try:
    #         response = requests.post("http://127.0.0.1:8000/auth/medical-reports/save/", json=data)
    #         if response.status_code == 200:
    #             QMessageBox.information(self, "Success", "Medical report saved successfully!")
    #             return True  # Report successfully saved
    #         else:
    #             QMessageBox.critical(
    #                 self, "Error", f"Failed to save the report. {response.json().get('error', '')}"
    #             )
    #             return False
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")
    #         return False



# import sys
# import requests
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from optical.management.models import MedicalReport
# from ui_ordnances2 import Ui_MainWindow  # Import the UI file for the medical report form

# class MedicalReportForm(QMainWindow, Ui_MainWindow):
#     def __init__(self, patient_id, patient_name, patient_age, patient_gender, patient_profession):
#         super().__init__()
#         self.setupUi(self)
#         self.patient_id = patient_id
#         self.patient_name = patient_name
#         self.patient_age = patient_age
#         self.patient_gender = patient_gender
#         self.patient_profession = patient_profession

#         # Populate patient details
#         self.patientName.setText(self.patient_name)
#         self.pateintage.setText(str(self.patient_age))
#         self.comboBox.addItems(['Male', 'Female', 'Other'])  # Populate gender options
#         self.comboBox.setCurrentText(self.patient_gender)
#         self.patientprofesion.setText(self.patient_profession)

#         # Populate dropdowns
#         self.comboBox_2.addItems([choice[1] for choice in MedicalReport.ametropie_choices])
#         self.comboBox_3.addItems([choice[1] for choice in MedicalReport.verre_choices])
#         self.comboBox_4.addItems([choice[1] for choice in MedicalReport.teintes_choices])
#         self.comboBox_5.addItems([choice[1] for choice in MedicalReport.foyers_choices])
#         self.comboBox_6.addItems([choice[1] for choice in MedicalReport.port_choices])
#         self.comboBox_7.addItems([choice[1] for choice in MedicalReport.indice_choices])

#         # Connect buttons
#         self.pushButton_2.clicked.connect(self.save_report)  # Save button
#         self.pushButton.clicked.connect(self.print_report)  # Print button

#     def save_report(self):
#         """Save the medical report to the database."""
#         data = {
#             "patient_id": self.patient_id,
#             "age": self.pateintage.text(),
#             "sexe": self.comboBox.currentText(),
#             "profession": self.patientprofesion.text(),
#             "sphere_od": self.lineEdit_4.text(),
#             "cyl_od": self.lineEdit_5.text(),
#             "axe_od": self.lineEdit_6.text(),
#             "addition_od": self.lineEdit_7.text(),
#             "sphere_og": self.lineEdit_8.text(),
#             "cyl_og": self.lineEdit_9.text(),
#             "axe_og": self.lineEdit_10.text(),
#             "addition_og": self.lineEdit_11.text(),
#             "ametropie": self.comboBox_2.currentText(),
#             "types_de_verre": self.comboBox_3.currentText(),
#             "teintes": self.comboBox_4.currentText(),
#             "foyers": self.comboBox_5.currentText(),
#             "port": self.comboBox_6.currentText(),
#             "indice": self.comboBox_7.currentText(),
#         }

#         try:
#             response = requests.post("http://127.0.0.1:8000/auth/medical-reports/save/", json=data)
#             if response.status_code == 200:
#                 QMessageBox.information(self, "Success", "Medical report saved successfully!")
#             else:
#                 QMessageBox.critical(self, "Error", "Failed to save the report.")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")

#     def print_report(self):
#         """Print the medical report."""
#         # Ensure the report is saved before printing
#         if not self.save_report():
#             QMessageBox.warning(self, "Warning", "Please save the report before printing.")
#             return

#         # Hide the print button before printing
#         self.pushButton.setVisible(False)
#         QMessageBox.information(self, "Print", f"Printing medical report for {self.patient_name}...")
#         self.pushButton.setVisible(True)





# import sys
# import requests
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from ui_ordnances2 import Ui_MainWindow  # Import the UI for the Medical Report Form


# import sys
# import requests
# from datetime import datetime
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
# from ui_ordnances2 import Ui_MainWindow  # Import the Medical Report Form UI


# class MedicalReporForm(QMainWindow, Ui_MainWindow):
#     def __init__(self, patient_id=None, patient_name=None, patient_age=None, patient_gender=None, patient_profession=None, report_id=None):
#         super().__init__()
#         self.setupUi(self)

#         # Store patient and report details
#         self.patient_id = patient_id
#         self.report_id = report_id

#         # Automatically populate the form fields
#         self.lineEdit_name.setText(patient_name)  # Assuming there's a Name field
#         self.lineEdit_age.setText(str(patient_age))
#         self.lineEdit_sexe.setText(patient_gender)
#         self.lineEdit_profession.setText(patient_profession)

#         # Set the current date
#         self.lineEdit_date.setText(datetime.now().strftime('%Y-%m-%d'))

#         # Connect buttons to their respective actions
#         self.pushButton_submit.clicked.connect(self.save_report)  # Submit button
#         self.pushButton_print.clicked.connect(self.print_report)  # Print button

#         # If viewing an existing report, load its details
#         if self.report_id:
#             self.load_report_details()

#     def load_report_details(self):
#         """Load the details of an existing report into the form."""
#         response = requests.get(f'http://127.0.0.1:8000/medical_reports/{self.report_id}/detail/')
#         if response.status_code == 200:
#             report = response.json()['medical_report']
#             self.populate_form(report)
#         else:
#             QMessageBox.critical(self, "Error", "Failed to load report details.")

#     def populate_form(self, report):
#         """Populate the form fields with the details of the report."""
#         self.lineEdit_sphere_od.setText(report['sphere_od'])
#         self.lineEdit_cyl_od.setText(report['cyl_od'])
#         self.lineEdit_axe_od.setText(report['axe_od'])
#         self.lineEdit_addition_od.setText(report['addition_od'])
#         self.lineEdit_sphere_og.setText(report['sphere_og'])
#         self.lineEdit_cyl_og.setText(report['cyl_og'])
#         self.lineEdit_axe_og.setText(report['axe_og'])
#         self.lineEdit_addition_og.setText(report['addition_og'])
#         self.comboBox_ametropie.setCurrentText(report['ametropie'])
#         self.comboBox_types_de_verre.setCurrentText(report['types_de_verre'])
#         self.comboBox_teintes.setCurrentText(report['teintes'])
#         self.comboBox_foyers.setCurrentText(report['foyers'])
#         self.comboBox_port.setCurrentText(report['port'])
#         self.comboBox_indice.setCurrentText(report['indice'])

#     def save_report(self):
#         """Save the medical report details to the database."""
#         if not self.patient_id:
#             QMessageBox.critical(self, "Error", "No patient selected.")
#             return

#         data = {
#             "patient_id": self.patient_id,
#             "age": self.lineEdit_age.text(),
#             "sexe": self.lineEdit_sexe.text(),
#             "profession": self.lineEdit_profession.text(),
#             "sphere_od": self.lineEdit_sphere_od.text(),
#             "cyl_od": self.lineEdit_cyl_od.text(),
#             "axe_od": self.lineEdit_axe_od.text(),
#             "addition_od": self.lineEdit_addition_od.text(),
#             "sphere_og": self.lineEdit_sphere_og.text(),
#             "cyl_og": self.lineEdit_cyl_og.text(),
#             "axe_og": self.lineEdit_axe_og.text(),
#             "addition_og": self.lineEdit_addition_og.text(),
#             "ametropie": self.comboBox_ametropie.currentText(),
#             "types_de_verre": self.comboBox_types_de_verre.currentText(),
#             "teintes": self.comboBox_teintes.currentText(),
#             "foyers": self.comboBox_foyers.currentText(),
#             "port": self.comboBox_port.currentText(),
#             "indice": self.comboBox_indice.currentText(),
#         }

#         try:
#             if self.report_id:
#                 # Update existing report
#                 response = requests.post(f'http://127.0.0.1:8000/medical_reports/update/{self.report_id}/', json=data)
#             else:
#                 # Create a new report
#                 response = requests.post('http://127.0.0.1:8000/medical_reports/add/', json=data)

#             if response.status_code == 200:
#                 QMessageBox.information(self, "Success", "Medical report saved successfully!")
#                 self.close()  # Close the form
#             else:
#                 QMessageBox.critical(self, "Error", "Failed to save the report.")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")

#     def print_report(self):
#         """Print the medical report (requires saving first)."""
#         if not self.report_id:
#             QMessageBox.warning(self, "Error", "Please save the report before printing.")
#             return

#         QMessageBox.information(self, "Print", "Printing report... (Feature under development)")





# class MedicalReporForm(QMainWindow, Ui_MainWindow):
#     def __init__(self, patient_id=None, patient_name=None, patient_age=None, patient_gender=None, patient_profession=None, report_id=None):
#         super().__init__()
#         self.setupUi(self)

#         # Store patient ID and report ID
#         self.patient_id = patient_id
#         self.report_id = report_id

#             # Automatically populate the form fields
#         self.lineEdit_name.setText(patient_name)  # Assuming there's a Name field
#         self.lineEdit_age.setText(str(patient_age))
#         self.lineEdit_sexe.setText(patient_gender)
#         self.lineEdit_profession.setText(patient_profession)

#         # Set the current date
#         self.lineEdit_date.setText(datetime.now().strftime('%Y-%m-%d'))

#         # Connect buttons to their respective actions
#         self.pushButton.clicked.connect(self.save_report)  # Submit button
#         self.pushButton_2.clicked.connect(self.print_report)  # Print button

#         # If viewing an existing report, load its details
#         if self.report_id:
#             self.load_report_details()

#     def load_report_details(self):
#         """Load the details of an existing report into the form."""
#         response = requests.get(f'http://127.0.0.1:8000/auth/medical_reports/{self.report_id}/detail/')
#         if response.status_code == 200:
#             report = response.json()['medical_report']
#             self.populate_form(report)
#         else:
#             QMessageBox.critical(self, "Error", "Failed to load report details.")

#     def populate_form(self, report):
#         """Populate the form fields with the details of the report."""
#         self.lineEdit_age.setText(str(report['age']))
#         self.lineEdit_sexe.setText(report['sexe'])
#         self.lineEdit_profession.setText(report['profession'])
#         self.lineEdit_sphere_od.setText(report['sphere_od'])
#         self.lineEdit_cyl_od.setText(report['cyl_od'])
#         self.lineEdit_axe_od.setText(report['axe_od'])
#         self.lineEdit_addition_od.setText(report['addition_od'])
#         self.lineEdit_sphere_og.setText(report['sphere_og'])
#         self.lineEdit_cyl_og.setText(report['cyl_og'])
#         self.lineEdit_axe_og.setText(report['axe_og'])
#         self.lineEdit_addition_og.setText(report['addition_og'])
#         self.comboBox_ametropie.setCurrentText(report['ametropie'])
#         self.comboBox_types_de_verre.setCurrentText(report['types_de_verre'])
#         self.comboBox_teintes.setCurrentText(report['teintes'])
#         self.comboBox_foyers.setCurrentText(report['foyers'])
#         self.comboBox_port.setCurrentText(report['port'])
#         self.comboBox_indice.setCurrentText(report['indice'])

#     def save_report(self):
#         """Save the medical report details to the database."""
#         if not self.patient_id:
#             QMessageBox.critical(self, "Error", "No patient selected.")
#             return

#         data = {
#             "patient_id": self.patient_id,
#             "age": self.lineEdit_age.text(),
#             "sexe": self.lineEdit_sexe.text(),
#             "profession": self.lineEdit_profession.text(),
#             "sphere_od": self.lineEdit_sphere_od.text(),
#             "cyl_od": self.lineEdit_cyl_od.text(),
#             "axe_od": self.lineEdit_axe_od.text(),
#             "addition_od": self.lineEdit_addition_od.text(),
#             "sphere_og": self.lineEdit_sphere_og.text(),
#             "cyl_og": self.lineEdit_cyl_og.text(),
#             "axe_og": self.lineEdit_axe_og.text(),
#             "addition_og": self.lineEdit_addition_og.text(),
#             "ametropie": self.comboBox_ametropie.currentText(),
#             "types_de_verre": self.comboBox_types_de_verre.currentText(),
#             "teintes": self.comboBox_teintes.currentText(),
#             "foyers": self.comboBox_foyers.currentText(),
#             "port": self.comboBox_port.currentText(),
#             "indice": self.comboBox_indice.currentText(),
#         }

#         try:
#             if self.report_id:
#                 # Update existing report
#                 response = requests.post(f'http://127.0.0.1:8000/auth/medical_reports/update/{self.report_id}/', json=data)
#             else:
#                 # Create a new report
#                 response = requests.post('http://127.0.0.1:8000/auth/medical_reports/add/', json=data)

#             if response.status_code == 200:
#                 QMessageBox.information(self, "Success", "Medical report saved successfully!")
#                 self.close()  # Close the form
#             else:
#                 QMessageBox.critical(self, "Error", "Failed to save the report.")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")

#     def print_report(self):
#         """Print the medical report (requires saving first)."""
#         if not self.report_id:
#             QMessageBox.warning(self, "Error", "Please save the report before printing.")
#             return

#         QMessageBox.information(self, "Print", "Printing report... (Feature under development)")




