# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QGridLayout
# from PySide6.QtPrintSupport import QPrintDialog, QPrinter
# from PySide6.QtGui import QPainter, QFont, QRegion, QPageSize
# from PySide6.QtCore import QRect, QPoint
# from print_template import Ui_Form  # Import the generated template class

# class PatientForm(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Patient Form")
#         self.setGeometry(100, 100, 400, 300)

#         # Initialize patient_data
#         self.patient_data = {}

#         # Central widget and layout
#         central_widget = QWidget(self)
#         self.setCentralWidget(central_widget)
#         layout = QGridLayout(central_widget)

#         # Patient information fields
#         self.nameLabel = QLabel("Name:", self)
#         self.nameLineEdit = QLineEdit(self)
#         self.contactLabel = QLabel("Contact:", self)
#         self.contactLineEdit = QLineEdit(self)
#         self.emailLabel = QLabel("Email:", self)
#         self.emailLineEdit = QLineEdit(self)
#         self.genderLabel = QLabel("Gender:", self)
#         self.genderComboBox = QComboBox(self)
#         self.genderComboBox.addItems(["Male", "Female", "Other"])
#         self.professionLabel = QLabel("Profession:", self)
#         self.professionLineEdit = QLineEdit(self)
#         self.ageLabel = QLabel("Age:", self)
#         self.ageLineEdit = QLineEdit(self)

#         # Add fields to layout
#         layout.addWidget(self.nameLabel, 0, 0)
#         layout.addWidget(self.nameLineEdit, 0, 1)
#         layout.addWidget(self.contactLabel, 1, 0)
#         layout.addWidget(self.contactLineEdit, 1, 1)
#         layout.addWidget(self.emailLabel, 2, 0)
#         layout.addWidget(self.emailLineEdit, 2, 1)
#         layout.addWidget(self.genderLabel, 3, 0)
#         layout.addWidget(self.genderComboBox, 3, 1)
#         layout.addWidget(self.professionLabel, 4, 0)
#         layout.addWidget(self.professionLineEdit, 4, 1)
#         layout.addWidget(self.ageLabel, 5, 0)
#         layout.addWidget(self.ageLineEdit, 5, 1)

#         # Save and Print buttons
#         self.saveButton = QPushButton("Save", self)
#         self.printButton = QPushButton("Print", self)
#         layout.addWidget(self.saveButton, 6, 0)
#         layout.addWidget(self.printButton, 6, 1)

#         # Connect buttons to methods
#         self.saveButton.clicked.connect(self.save_patient)
#         self.printButton.clicked.connect(self.print_patient_report)

#     def save_patient(self):
#         # Simulate saving patient data
#         self.patient_data = {
#             "name": self.nameLineEdit.text(),
#             "contact": self.contactLineEdit.text(),
#             "email": self.emailLineEdit.text(),
#             "gender": self.genderComboBox.currentText(),
#             "profession": self.professionLineEdit.text(),
#             "age": self.ageLineEdit.text(),
#             "date": "2024-12-05"  # Example date, you can adjust as needed
#         }
#         QMessageBox.information(self, "Success", f"Patient data saved: {self.patient_data}")

#     def print_patient_report(self):
#         if not self.patient_data:
#             QMessageBox.warning(self, "Warning", "No patient data available to print!")
#             return

#         printer = QPrinter(QPrinter.HighResolution)
#         printer.setPageSize(QPageSize(QPageSize.A4))
#         printer.setPageMargins(15, 15, 15, 15, QPrinter.Millimeter)

#         # Create a print dialog
#         print_dialog = QPrintDialog(printer, self)
#         if print_dialog.exec() == QPrintDialog.Accepted:
#             # Render the template to the printer
#             self.render_to_printer(printer)

#     def render_to_printer(self, printer):
#         # Load and populate the custom print template
#         template_widget = QWidget()
#         ui = Ui_Form()
#         ui.setupUi(template_widget)

#         # Populate the template with patient data
#         ui.patientNmae_label.setText(self.patient_data['name'])
#         ui.patientAgeLabel.setText(self.patient_data['age'])
#         ui.genderLabel.setText(self.patient_data['gender'])
#         ui.patientProfessionLabel.setText(self.patient_data['profession'])
#         ui.dateLabel.setText(self.patient_data['date'])
#         # Add more fields as needed

#         painter = QPainter(printer)
#         template_widget.render(
#             painter,
#             QPoint(0, 0),
#             QRegion(0, 0, template_widget.width(), template_widget.height()),
#             QWidget.RenderFlags(QWidget.RenderFlag.DrawChildren)
#         )
#         painter.end()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PatientForm()
#     window.show()
#     sys.exit(app.exec())


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QGridLayout
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtGui import QPainter, QFont, QRegion, QPageSize
from PySide6.QtCore import QRect, QPoint
from print_template import Ui_Form  # Import the generated template class


import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QPushButton, QVBoxLayout, QWidget, QLabel, QLineEdit, QComboBox, QGridLayout
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtGui import QPainter, QFont, QRegion
from PySide6.QtCore import QRect, QPoint
from print_template import Ui_Form  # Import the generated template class

class PatientForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Patient Form")
        self.setGeometry(100, 100, 400, 300)

        # Initialize patient_data
        self.patient_data = {}

        # Central widget and layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QGridLayout(central_widget)

        # Patient information fields
        self.nameLabel = QLabel("Name:", self)
        self.nameLineEdit = QLineEdit(self)
        self.contactLabel = QLabel("Contact:", self)
        self.contactLineEdit = QLineEdit(self)
        self.emailLabel = QLabel("Email:", self)
        self.emailLineEdit = QLineEdit(self)
        self.genderLabel = QLabel("Gender:", self)
        self.genderComboBox = QComboBox(self)
        self.genderComboBox.addItems(["Male", "Female", "Other"])
        self.professionLabel = QLabel("Profession:", self)
        self.professionLineEdit = QLineEdit(self)
        self.ageLabel = QLabel("Age:", self)
        self.ageLineEdit = QLineEdit(self)

        # Add fields to layout
        layout.addWidget(self.nameLabel, 0, 0)
        layout.addWidget(self.nameLineEdit, 0, 1)
        layout.addWidget(self.contactLabel, 1, 0)
        layout.addWidget(self.contactLineEdit, 1, 1)
        layout.addWidget(self.emailLabel, 2, 0)
        layout.addWidget(self.emailLineEdit, 2, 1)
        layout.addWidget(self.genderLabel, 3, 0)
        layout.addWidget(self.genderComboBox, 3, 1)
        layout.addWidget(self.professionLabel, 4, 0)
        layout.addWidget(self.professionLineEdit, 4, 1)
        layout.addWidget(self.ageLabel, 5, 0)
        layout.addWidget(self.ageLineEdit, 5, 1)

        # Save and Print buttons
        self.saveButton = QPushButton("Save", self)
        self.printButton = QPushButton("Print", self)
        layout.addWidget(self.saveButton, 6, 0)
        layout.addWidget(self.printButton, 6, 1)

        # Connect buttons to methods
        self.saveButton.clicked.connect(self.save_patient)
        self.printButton.clicked.connect(self.print_patient_report)

    def save_patient(self):
        # Simulate saving patient data
        self.patient_data = {
            "name": self.nameLineEdit.text(),
            "contact": self.contactLineEdit.text(),
            "email": self.emailLineEdit.text(),
            "gender": self.genderComboBox.currentText(),
            "profession": self.professionLineEdit.text(),
            "age": self.ageLineEdit.text(),
            "date": "2024-12-05"  # Example date, you can adjust as needed
        }
        QMessageBox.information(self, "Success", f"Patient data saved: {self.patient_data}")


    def print_patient_report(self):
        if not self.patient_data:
            QMessageBox.warning(self, "Warning", "No patient data available to print!")
            return

        printer = QPrinter(QPrinter.HighResolution)

        # Set the page size to A4
        printer.setPageSize(QPageSize(QPageSize.A4))
        # printer.setOrientation(QPrinter.Portrait)  # Portrait orientation
        printer.setFullPage(True)  # Use the full page for rendering

        # Create a print dialog
        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec() == QPrintDialog.Accepted:
            # Render the template to the printer
            self.render_to_printer(printer)

    def render_to_printer(self, printer):
        # Load and populate the custom print template
        template_widget = QWidget()
        ui = Ui_Form()
        ui.setupUi(template_widget)

        # Populate the template with patient data
        ui.patientNmae_label.setText(self.patient_data['name'])
        ui.patientAgeLabel.setText(self.patient_data['age'])
        ui.genderLabel.setText(self.patient_data['gender'])
        ui.patientProfessionLabel.setText(self.patient_data['profession'])
        ui.dateLabel.setText(self.patient_data['date'])

        # Prepare the painter and set up the printer's page rectangle
        painter = QPainter(printer)
        painter.setRenderHint(QPainter.Antialiasing)
        page_rect = printer.pageRect(QPrinter.DevicePixel)

        # Add margins/padding
        margin = 50  # Adjust margin size in pixels
        content_rect = page_rect.adjusted(margin, margin, -margin, -margin)

        # Calculate scaling factors
        widget_size = template_widget.size()
        scale_x = content_rect.width() / widget_size.width()
        scale_y = content_rect.height() / widget_size.height()
        scale = min(scale_x, scale_y)  # Scale proportionally to fit within content rect

        # Center the widget with added padding
        translate_x = content_rect.left() + (content_rect.width() - widget_size.width() * scale) / 2
        translate_y = content_rect.top() + (content_rect.height() - widget_size.height() * scale) / 2
        painter.translate(translate_x, translate_y)
        painter.scale(scale, scale)

        # Render the widget
        template_widget.render(
            painter,
            QPoint(0, 0),  # Render starting at the top-left corner
            QRegion(),     # Render the entire widget
            QWidget.RenderFlags(QWidget.RenderFlag.DrawChildren | QWidget.RenderFlag.DrawWindowBackground)
        )
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PatientForm()
    window.show()
    sys.exit(app.exec())



































    # def render_to_printer(self, printer):
    #     # Load and populate the custom print template
    #     template_widget = QWidget()
    #     ui = Ui_Form()
    #     ui.setupUi(template_widget)

    #     # Populate the template with patient data
    #     ui.patientNmae_label.setText(self.patient_data['name'])
    #     ui.patientAgeLabel.setText(self.patient_data['age'])
    #     ui.genderLabel.setText(self.patient_data['gender'])
    #     ui.patientProfessionLabel.setText(self.patient_data['profession'])
    #     ui.dateLabel.setText(self.patient_data['date'])

    #     # Prepare the painter and set up the printer's page rectangle
    #     painter = QPainter(printer)
    #     painter.setRenderHint(QPainter.Antialiasing)
    #     page_rect = printer.pageRect(QPrinter.DevicePixel)

    #     # Calculate scaling factors
    #     widget_size = template_widget.size()
    #     scale_x = page_rect.width() / widget_size.width()
    #     scale_y = page_rect.height() / widget_size.height()
    #     scale = min(scale_x, scale_y)  # Scale proportionally to fit the page

    #     # Center the widget on the page
    #     translate_x = (page_rect.width() - widget_size.width() * scale) / 2
    #     translate_y = (page_rect.height() - widget_size.height() * scale) / 2
    #     painter.translate(translate_x, translate_y)
    #     painter.scale(scale, scale)

    #     # Render the widget
    #     template_widget.render(
    #         painter,
    #         QPoint(0, 0),  # Render starting at the top-left corner
    #         QRegion(),     # Render the entire widget
    #         QWidget.RenderFlags(QWidget.RenderFlag.DrawChildren | QWidget.RenderFlag.DrawWindowBackground)
    #     )
    #     painter.end()



    # def render_to_printer(self, printer):
    #     # Load and populate the custom print template
    #     template_widget = QWidget()
    #     ui = Ui_Form()
    #     ui.setupUi(template_widget)

    #     # Populate the template with patient data
    #     ui.patientNmae_label.setText(self.patient_data['name'])
    #     ui.patientAgeLabel.setText(self.patient_data['age'])
    #     ui.genderLabel.setText(self.patient_data['gender'])
    #     ui.patientProfessionLabel.setText(self.patient_data['profession'])
    #     ui.dateLabel.setText(self.patient_data['date'])

    #     # Get the printer's page size in pixels
    #     page_rect = printer.pageRect(QPrinter.DevicePixel)
    #     template_widget.resize(page_rect.width(), page_rect.height())

    #     # Scale fonts and other elements to fit the page
    #     font = template_widget.font()
    #     font.setPointSize(12)  # Adjust the font size as needed
    #     template_widget.setFont(font)

    #     # Render the widget to the printer
    #     painter = QPainter(printer)
    #     template_widget.render(
    #         painter,
    #         QPoint(0, 0),
    #         QRegion(0, 0, template_widget.width(), template_widget.height()),
    #         QWidget.RenderFlags(QWidget.RenderFlag.DrawChildren)
    #     )
    #     painter.end()

    # def render_to_printer(self, printer):
    #     # Load and populate the custom print template
    #     template_widget = QWidget()
    #     ui = Ui_Form()
    #     ui.setupUi(template_widget)

    #     # Populate the template with patient data
    #     ui.patientNmae_label.setText(self.patient_data['name'])
    #     ui.patientAgeLabel.setText(self.patient_data['age'])
    #     ui.genderLabel.setText(self.patient_data['gender'])
    #     ui.patientProfessionLabel.setText(self.patient_data['profession'])
    #     ui.dateLabel.setText(self.patient_data['date'])
    #     # Add more fields as needed

    #     # Resize the widget to fit the printer's page size
    #     template_widget.resize(printer.pageRect(QPrinter.DevicePixel).size().toSize())

    #     # Render the widget to the printer
    #     painter = QPainter(printer)
    #     template_widget.render(
    #         painter,
    #         QPoint(0, 0),
    #         QRegion(0, 0, template_widget.width(), template_widget.height()),
    #         QWidget.RenderFlags(QWidget.RenderFlag.DrawChildren)
    #     )
    #     painter.end()
