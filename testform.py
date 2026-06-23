import sys
import requests
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox
from ui_ux.prescription_module.ui_prescription_form4 import Ui_MainWindow
from datetime import datetime
from PySide6.QtCore import QDateTime, QRectF
from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PySide6.QtGui import QPainter, QFont
from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PySide6.QtGui import QPainter
from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPainter, QFont, QColor, QPen
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage
from PySide6.QtGui import QPainter, QFont, QColor, QPen, QImage
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtWidgets import QFileDialog
from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import QFontMetrics

BASE_URL = "http://127.0.0.1:8000/auth/"

class MedicalReportForm(QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id, patient_name, patient_age, patient_gender, patient_profession):
        super().__init__()
        self.setupUi(self)

        self.patient_id = patient_id
        self.patient_name = patient_name
        self.patient_age = patient_age
        self.patient_gender = patient_gender
        self.patient_profession = patient_profession
        self.last_saved_report_id = None  # Track saved report
        
        self.generate_reference_id()
        self.dateTimeEdit.setDateTime(QDateTime.currentDateTime())

        # Set the date to the current date
        # Pre-fill patient info (read-only)
        self.p_name.setText(patient_name)
        self.age.setText(str(patient_age))
        self.sex.setText(patient_gender)
        self.Profession.setText(patient_profession)

        # Button connections
        self.save_btn.clicked.connect(self.save_report)
        self.clear_btn.clicked.connect(self.clear_form)
        self.preview_btn.clicked.connect(self.preview_report)
        self.print_btn.clicked.connect(self.print_report)
        

    def generate_reference_id(self):
        try:
            response = requests.get(f"{BASE_URL}medical-reports/next-reference/")
            if response.status_code == 200:
                next_ref = response.json().get('reference_id')
                self.refferenceID.setText(next_ref)
        except requests.RequestException:
            self.refferenceID.setText("Pre-UNKNOWN")
            
    # def generate_reference_id(self):
    #     try:
    #         response = requests.get(f"{BASE_URL}medical-reports/next-reference/")
    #         if response.status_code == 200:
    #             reference_id = response.json().get("reference_id")
    #             self.reference_id = reference_id
    #             self.refferenceID.setText(reference_id)
    #     except:
    #         self.refferenceID.setText("Pre-ERROR")
    #         self.reference_id = "Pre-ERROR"
            
    def generate_reference_id(self):
        try:
            response = requests.get(f"{BASE_URL}medical-reports/next-reference/")
            if response.status_code == 200:
                reference_id = response.json().get("reference_id")
                self.reference_id_value = reference_id  # store the string
                self.refferenceID.setText(reference_id)  # update the QLineEdit
        except:
            self.refferenceID.setText("Pre-ERROR")
            self.reference_id_value = "Pre-ERROR"


    # def get_selected_checkbox_value(self, checkboxes):
    #     for cb in checkboxes:
    #         if cb.isChecked():
    #             return cb.text()
    #     return ""
    
    def get_selected_checkbox_values(self, checkboxes):
        return [cb.objectName().lower() for cb in checkboxes if cb.isChecked()]

    # def get_selected_checkbox_value(self, checkboxes):
    #     for cb in checkboxes:
    #         if cb.isChecked():
    #             return cb.objectName().lower()  # Ensure it's lowercase if your objectName matches 'myopie'
    #     return ""


    # def save_report(self):
    #     data = {
    #         "patient_id": self.patient_id,
    #         "age_at_report": int(self.patient_age),
    #         "profession_at_report": self.patient_profession,
    #         "ametropie": self.get_selected_checkbox_value([
    #             self.Myopie, self.Hypermetropie,
    #             self.Astigmatisme, #self.ametropie_presbytie,
    #             self.Emmetropie
    #         ]),
    #         "types_de_verre": self.get_selected_checkbox_value([
    #             self.Mineraux, self.Organiques, self.Polycarbonates
    #         ]),
    #         "teintes": self.get_selected_checkbox_value([
    #             self.Blanc, self.Gris, self.Antireflet,
    #             self.Blue_protect, self.Photochromique
    #         ]),
    #         "foyers": self.get_selected_checkbox_value([
    #             self.Unifocaux, self.Bifocaux, self.Progressifs
    #         ]),
    #         "port": self.get_selected_checkbox_value([
    #             self.Constant, self.Lecture
    #         ]),
    #         "indice": self.get_selected_checkbox_value([
    #             self.Normal, self.fort_indice
    #         ])
    #     }

    #     try:
    #         response = requests.post(f"{BASE_URL}medical-reports/create/", json=data)
    #         if response.status_code == 200:
    #             QMessageBox.information(self, "Success", "Medical report saved successfully.")
    #             self.clear_form()
    #         else:
    #             QMessageBox.warning(self, "Error", response.json().get("error", "Failed to save report."))
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))
    
    
    def save_report(self):
        try:
            data = {
                "patient_id": self.patient_id,
                "age_at_report": int(self.patient_age),
                "profession_at_report": self.patient_profession,
                # "reference_id": self.reference_id,  # include this in data dictionary
                "reference_id": self.reference_id_value,

                # Refraction Data
                "sphere_od": self.sphere_od.text(),
                "cyl_od": self.cyl_od.text(),
                "axe_od": self.axe_od.text(),
                "addition_od": self.addition_od.text(),
                "sphere_og": self.sphere_og.text(),
                "cyl_og": self.cyl_og.text(),
                "axe_og": self.axe_og.text(),
                "addition_og": self.addition_og.text(),

                # Prescription Details (allow multiple values)
                "ametropie": self.get_selected_checkbox_values([
                    self.Myopie, self.Hypermetropie, self.Astigmatisme, self.Emmetropie
                ]),
                "types_de_verre": self.get_selected_checkbox_values([
                    self.Mineraux, self.Organiques, self.Polycarbonates
                ]),
                "teintes": self.get_selected_checkbox_values([
                    self.Blanc, self.Gris, self.Antireflet, self.bleue_protect, self.Photochromique
                ]),
                "foyers": self.get_selected_checkbox_values([
                    self.Unifocaux, self.Bifocaux, self.Progressifs
                ]),
                "port": self.get_selected_checkbox_values([
                    self.Constant, self.Lecture
                ]),
                "indice": self.get_selected_checkbox_values([
                    self.Normal, self.fort_indice
                ])
            }

            response = requests.post(f"{BASE_URL}medical-reports/create/", json=data)
            if response.status_code == 200:
                self.last_saved_report_id = response.json().get("report_id")  # Optional
                self.report_data = data  # Save for preview/print
                QMessageBox.information(self, "Success", "Medical report saved successfully.")
                self.clear_form()
                print(self.report_data) # Debugging line to check the data
            else:
                QMessageBox.warning(self, "Error", response.json().get("error", "Failed to save report."))
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

        
    
    
    
    
    # def save_report(self):
    #     data = {
    #         "patient_id": self.patient_id,
    #         "age_at_report": int(self.patient_age),
    #         "profession_at_report": self.patient_profession,
    #         "reference_id": self.reference_id,  # include this in data dictionary

    #         # Refraction Data
    #         "sphere_od": self.sphere_od.text(),
    #         "cyl_od": self.cyl_od.text(),
    #         "axe_od": self.axe_od.text(),
    #         "addition_od": self.addition_od.text(),
    #         "sphere_og": self.sphere_og.text(),
    #         "cyl_og": self.cyl_og.text(),
    #         "axe_og": self.axe_og.text(),
    #         "addition_og": self.addition_og.text(),

    #         # Prescription Detail
    #         "ametropie": self.get_selected_checkbox_values([
    #             self.Myopie, self.Hypermetropie,
    #             self.Astigmatisme, self.Emmetropie
    #         ]),
    #         "types_de_verre": self.get_selected_checkbox_values([
    #             self.Mineraux, self.Organiques, self.Polycarbonates
    #         ]),
    #         "teintes": self.get_selected_checkbox_values([
    #             self.Blanc, self.Gris, self.Antireflet,
    #             self.bleue_protect, self.Photochromique
    #         ]),
    #         "foyers": self.get_selected_checkbox_values([
    #             self.Unifocaux, self.Bifocaux, self.Progressifs
    #         ]),
    #         "port": self.get_selected_checkbox_values([
    #             self.Constant, self.Lecture
    #         ]),
    #         "indice": self.get_selected_checkbox_values([
    #             self.Normal, self.fort_indice
    #         ])
    #     }

    #     try:
    #         # response = requests.post(f"{BASE_URL}medical-reports/create/", json=data)
    #         # if response.status_code == 200:
    #         response = requests.post(f"{BASE_URL}medical-reports/create/", json=data)
    #         if response.status_code == 200:
    #             self.last_saved_report_id = response.json().get("report_id")
    #             QMessageBox.information(self, "Success", "Medical report saved successfully.")
    #             # self.get_full_report_data()  # ✅ NEW LINE
    #             # QMessageBox.information(self, "Success", "Medical report saved successfully.")
    #             self.clear_form()
    #         else:
    #             QMessageBox.warning(self, "Error", response.json().get("error", "Failed to save report."))
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))


    def clear_form(self):
        for checkbox_group in [
            [self.Myopie, self.Hypermetropie, self.Astigmatisme,  self.Emmetropie],#self.ametropie_presbytie,
            [self.Mineraux, self.Organiques, self.Polycarbonates],
            [self.Blanc, self.Gris, self.Photochromique, self.Antireflet, self.bleue_protect],
            [self.Unifocaux, self.Bifocaux, self.Progressifs],
            [self.Constant, self.Lecture],
            [self.Normal, self.fort_indice]
        ]:
            for cb in checkbox_group:
                cb.setChecked(False)

    def fetch_report_data_by_reference(self):
        try:
            response = requests.get(f"{BASE_URL}medical-reports/view-by-ref/{self.reference_id}/")
            if response.status_code == 200:
                self.report_data = response.json()
            else:
                QMessageBox.warning(self, "Error", "Report not found")
        except:
            QMessageBox.critical(self, "Network Error", "Failed to fetch report")



    def preview_report(self):
        if not hasattr(self, "report_data"):
            QMessageBox.warning(self, "No Report", "Please save a report before previewing.")
            print("Report Data:", self.report_data)
            return

        printer = QPrinter()
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.render_pdf)
        preview_dialog.exec()

    def print_report(self):
        if not hasattr(self, "report_data"):
            QMessageBox.warning(self, "No Report", "Please save a report before printing.")
            return

        printer = QPrinter()
        file_dialog = QFileDialog(self, "Save Report", "", "PDF Files (*.pdf)")
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)

        if file_dialog.exec():
            save_path = file_dialog.selectedFiles()[0]
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(save_path)
            self.render_pdf(printer)

    # def render_pdf(self, printer):
    #    # QRectF is imported but not used here; remove or replace with actual usage if needed.

    #     painter = QPainter(printer)
    #     painter.setPen(QColor("black"))
    #     painter.setFont(QFont("Helvetica", 12))

        
    #     margin = 80
    #     line_spacing = 30
    #     y = margin
    #     width = 595  # A4 width in points (210mm)
    #     height = 842  # A4 height in points (297mm)
    #         # Dynamically get the page width and height
    #     page_rect = printer.pageRect()  # QRectF
    #     width = page_rect.width()
    #     height = page_rect.height()

    #     # Define margins and spacings based on page size
    #     margin = width * 0.07  # 7% of page width
    #     line_spacing = height * 0.03  # 3% of page height
    #     y = margin

    #     report = self.report_data
    #     print("Report Data:", report)

    #     # Dynamic font sizes
    #     large_font_size = width * 0.06
    #     medium_font_size = width * 0.022
    #     small_font_size = width * 0.017

    #     # Header
    #     painter.setFont(QFont("Helvetica-Bold", int(large_font_size), QFont.Weight.Bold))
    #     painter.setPen(QColor("red"))
    #     painter.drawText(margin + width * 0.08, y, "NGASSAM OPTIQUE")
    #     y += line_spacing

    #     painter.setFont(QFont("Helvetica-Bold", int(medium_font_size)))
    #     painter.setPen(QColor("black"))
    #     painter.drawText(width * 0.38, y + line_spacing, "Situé à l'Avenue Kennedy derrière ADAMAOUA PALACE")
    #     painter.drawText(width * 0.375, y + 2 * line_spacing, "Tél.: (237) 699 67 50 25 / 620 37 69 38 / 671 16 65 27")

    #     painter.setFont(QFont("Helvetica-Bold", int(small_font_size), italic=True))
    #     painter.setPen(QColor("red"))
    #     painter.drawText(width * 0.45, y + 3 * line_spacing, "Le professionnel de la santé visuelle")

    #     # Separator Line
    #     painter.setPen(QPen(QColor("black"), 3))
    #     painter.drawLine(margin, y + 4.2 * line_spacing, width - margin, y + 4.2 * line_spacing)

    #     y += 5 * line_spacing

    #     # Title
    #     painter.setFont(QFont("Helvetica-Bold", int(medium_font_size), QFont.Weight.Bold))
    #     painter.setPen(QColor("red"))
    #     painter.drawText(width / 2 - margin, y, "ORDONNANCE DE LUNETTES")

    #     y += 2 * line_spacing

    #     # report = self.report_data
    #     # print("Report Data:", self.report_data)

    #     # # Header
    #     # # painter.setFont(QFont("Helvetica", 18, QFont.Weight.Bold))
    #     # # painter.drawText(margin, y, "NGASSAM OPTIQUE - Medical Report")
    #     # # y += 2 * line_spacing
    #     # # # Header
    #     # painter.setFont(QFont("Helvetica-Bold", 40, QFont.Weight.Bold))
    #     # painter.setPen(QColor("red"))
    #     # painter.drawText(margin + 50, y, "NGASSAM OPTIQUE")
    #     # y += line_spacing + 10
        
    #     # painter.setFont(QFont("Helvetica-Bold", 13))
    #     # painter.setPen(QColor("black"))
    #     # # Instead of margin + 1900 and y + 700
    #     # # Move it closer to your header
    #     # # painter.drawText(margin + 100, y + 20, "Situé à l'Avenue Kennedy derrière ADAMAOUA PALACE")
    #     # # painter.drawText(margin + 100, y + 50, "Tél.: (237) 699 67 50 25 / 620 37 69 38 / 671 16 65 27")
    #     # # y += 2 * line_spacing
    #     # painter.setFont(QFont("Helvetica-Bold", 10))
    #     # painter.setPen(QColor("black"))
    #     # painter.drawText(240, 100, "Situé à l'Avenue Kennedy derrière ADAMAOUA PALACE")
    #     # painter.drawText(237, 120, "Tél.: (237) 699 67 50 25 / 620 37 69 38 / 671 16 65 27")

    #     # painter.setFont(QFont("Helvetica-Bold", 10, italic=True))
    #     # painter.setPen(QColor("red"))
    #     # painter.drawText(290, 140, "Le professionnel de la santé visuelle")

    #     # # Separator Line
    #     # painter.setPen(QPen(QColor("black"), 3))  # Thinner separator line
    #     # painter.drawLine(100, 150, width + 100, 150)  # Adjusted for A4 size

    #     # painter.setFont(QFont("Helvetica-Bold", 12, QFont.Weight.Bold))
    #     # painter.setPen(QColor("red"))
    #     # painter.drawText(280, 170, "ORDONNANCE DE LUNETTES")
    #     # y += 3 * line_spacing
        
    #     painter.setPen(QColor("black"))
    #     painter.setFont(QFont("Helvetica", 11))
    #     painter.drawText(600, 200, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    #     painter.drawText(600, 220, f"ref: {report.get('reference_id', 'N/A')}")
    #     y += 2 * line_spacing
        
    #     # Patient Info
    #     painter.setFont(QFont("Helvetica", 12))
    #     painter.setPen(QColor("black"))
    #     # painter.drawText(margin, y, f"Reference ID: {report.get('reference_id', 'N/A')}")
    #     # y += line_spacing 
    #     # painter.drawText(margin, y, f"Patient Name: {self.patient_name}")
    #     # y += line_spacing
    #     # painter.drawText(margin, y, f"Age: {report.get('age_at_report', 'N/A')}   Gender: {self.patient_gender}   Profession: {report.get('profession_at_report', 'N/A')}")
        
    #     painter.setPen(QColor("black"))
    #     painter.setFont(QFont("Helvetica-Bold", 9))
    #     painter.drawText(50, 250, f"Noms et Prénoms: {self.patient_name}")
    #     painter.drawText(50, 300, f"Age: {report.get('age_at_report', 'N/A')}")
    #     painter.drawText(250, 300, f"Sexe: {self.patient_gender} ")
    #     painter.drawText(450, 300, f"Profession: {report.get('profession_at_report', 'N/A')}")
    #     y += 3 * line_spacing

    #     # Refraction Data
    #     # Table
    #     table_x = 50
    #     table_y = 335
    #     col_width = 120  # Adjusted column width
    #     row_height = 30  # Adjusted row height
    #     headers = ["œil", "Sphère", "Cyl", "Axe", "Addition"]
    #     rows = [["OD", f"{report.get('sphere_od', 'N/A')}", f"{report.get('cyl_od', 'N/A')}", f"{report.get('axe_od', 'N/A')}", f"{report.get('addition_od', 'N/A')}"], 
    #             ["OG", f"{report.get('sphere_og', 'N/A')}", f"{report.get('cyl_og', 'N/A')}", f"{report.get('axe_og', 'N/A')}", f"{report.get('addition_og', 'N/A')}"]
    #             ]

    #     painter.setFont(QFont("Helvetica-Bold", 11, QFont.Weight.Bold))
    #     for col_index, header in enumerate(headers):
    #         painter.drawText(table_x + col_index * col_width + 30, table_y + 20, header)

    #     painter.setFont(QFont("Helvetica-Bold", 11))
    #     for row_index, row in enumerate(rows):
    #         for col_index, cell in enumerate(row):
    #             painter.drawText(table_x + col_index * col_width + 30,
    #                             table_y + (row_index + 1) * row_height + 20, cell)

    #     # Draw table grid
    #     for r in range(len(rows) + 1 + 1):
    #         painter.drawLine(table_x, table_y + r * row_height,
    #                         table_x + len(headers) * col_width, table_y + r * row_height)
    #     for c in range(len(headers) + 1):
    #         painter.drawLine(table_x + c * col_width, table_y,
    #                         table_x + c * col_width, table_y + (len(rows) + 1) * row_height)

    #     # painter.setFont(QFont("Helvetica", 14, QFont.Weight.Bold))
    #     # painter.drawText(margin, y, "Refraction (OD/OG)")
    #     # y += line_spacing
    #     # painter.setFont(QFont("Helvetica", 12))
    #     # painter.drawText(margin, y, f"Sphere OD: {report.get('sphere_od', 'N/A')} | Sphere OG: {report.get('sphere_og', 'N/A')}")
    #     # y += line_spacing
    #     # painter.drawText(margin, y, f"Cyl OD: {report.get('cyl_od', 'N/A')} | Cyl OG: {report.get('cyl_og', 'N/A')}")
    #     # y += line_spacing
    #     # painter.drawText(margin, y, f"Axe OD: {report.get('axe_od', 'N/A')} | Axe OG: {report.get('axe_og', 'N/A')}")
    #     # y += line_spacing
    #     # painter.drawText(margin, y, f"Addition OD: {report.get('addition_od', 'N/A')} | Addition OG: {report.get('addition_og', 'N/A')}")
    #     y += 4 * line_spacing

    #     # Prescription
    # # --- Checkboxes Section ---
    #     # Helper function to check if value was selected
    #     def is_selected(category, value):
    #         selected_values = report.get(category, [])
    #         if isinstance(selected_values, str):
    #             selected_values = selected_values.lower().split(",")
    #         return value.lower() in [val.lower() for val in selected_values]

    #     # def draw_checkbox(x, y, selected=False):
    #     #     painter.setPen(QPen(QColor("black")))
    #     #     painter.drawRect(x, y, 12, 12)  # Draw square
            
    #         # painter.setBrush(QColor("red"))  # Shadow effect
    #         # painter.drawRect(x + 2, y + 2, 10, 10)
    #         # painter.setBrush(QColor("blue"))
    #         # painter.drawRect(x, y, 12, 12)
    #         # painter.setPen(QPen(QColor("black"), 1))
    #         # painter.drawRect(x, y, 12, 12)

    #         # if selected:
    #         #     painter.setPen(QPen(QColor("blue"), 2))
    #         #     painter.drawLine(x + 2, y + 6, x + 5, y + 10)
    #         #     painter.drawLine(x + 5, y + 10, x + 10, y + 2)

    
    #     def draw_checkbox(x, y, selected=False):
    #         painter.setBrush(QColor("black"))  # Shadow effect
    #         painter.drawRect(x + 2, y + 2, 10, 10)
    #         painter.setBrush(QColor("white"))
    #         painter.drawRect(x, y, 14, 14)
    #         painter.setPen(QPen(QColor("black"), 2))
    #         painter.drawRect(x, y, 14, 14)
            
    #         if selected:
    #             painter.setPen(QPen(QColor("black"), 2))
    #             painter.drawLine(x + 2, y + 6, x + 5, y + 10)
    #             painter.drawLine(x + 5, y + 10, x + 10, y + 2)

    #     painter.setFont(QFont("Helvetica-Bold", 11))

    #     base_y = 480
    #     spacing_y = 20
    #     x_start = 50
        
    # # Amétropie
    #     painter.drawText(x_start, base_y, "Amétropie:")
    #     painter.drawText(x_start + 80, base_y, "Myopie")
    #     draw_checkbox(x_start + 120, base_y - 9, is_selected('ametropie', 'myopie'))
    #     painter.drawText(x_start + 160, base_y, "Hypermétropie")
    #     draw_checkbox(x_start + 247, base_y - 9, is_selected('ametropie', 'hypermetropie'))
    #     painter.drawText(x_start + 290, base_y, "Astigmatisme")
    #     draw_checkbox(x_start + 370, base_y - 9, is_selected('ametropie', 'astigmatisme'))
    #     painter.drawText(x_start + 420, base_y, "Presbytie")
    #     draw_checkbox(x_start + 477, base_y - 9, is_selected('ametropie', 'presbytie'))
    #     painter.drawText(x_start + 550, base_y, "Emmetropie")
    #     draw_checkbox(x_start + 623, base_y - 9, is_selected('ametropie', 'emmetropie'))

    #     # Types de Verre
    #     base_y += 3 * spacing_y
    #     painter.drawText(x_start, base_y, "Types de verre:")
    #     painter.drawText(x_start + 100, base_y, "minéraux")
    #     draw_checkbox(x_start + 160, base_y - 9, is_selected('types_de_verre', 'mineraux'))
    #     painter.drawText(x_start + 270, base_y, "organiques")
    #     draw_checkbox(x_start + 339, base_y - 9, is_selected('types_de_verre', 'organiques'))
    #     painter.drawText(x_start + 460, base_y, "polycarbonates")
    #     draw_checkbox(x_start + 549, base_y - 9, is_selected('types_de_verre', 'polycarbonates'))

    #     # Teintes
    #     base_y += spacing_y + 30
    #     painter.drawText(x_start, base_y, "Teintes:")
    #     painter.drawText(x_start + 60, base_y, "Blanc")
    #     draw_checkbox(x_start + 95, base_y - 9, is_selected('teintes', 'blanc'))
    #     painter.drawText(x_start + 160, base_y, "Gris")
    #     draw_checkbox(x_start + 195, base_y - 9, is_selected('teintes', 'gris'))
    #     painter.drawText(x_start + 280, base_y, "Photochromique")
    #     draw_checkbox(x_start + 373, base_y - 9, is_selected('teintes', 'photochromique'))
    #     painter.drawText(x_start + 490, base_y, "Antireflet")
    #     draw_checkbox(x_start + 545, base_y - 9, is_selected('teintes', 'antireflet'))
    #     painter.drawText(x_start + 600, base_y, "Bleue Protect")
    #     draw_checkbox(x_start + 679, base_y - 9, is_selected('teintes', 'bleue_protect'))

    #     # Foyer
    #     base_y += spacing_y + 30
    #     painter.drawText(x_start, base_y, "Foyers:")
    #     painter.drawText(x_start + 60, base_y, "Unifocaux")
    #     draw_checkbox(x_start + 120, base_y - 11, is_selected('foyers', 'unifocaux'))
    #     painter.drawText(x_start + 220, base_y, "Bifocaux")
    #     draw_checkbox(x_start + 280, base_y - 11, is_selected('foyers', 'bifocaux'))
    #     painter.drawText(x_start + 400, base_y, "Progressifs")
    #     draw_checkbox(x_start + 467, base_y - 11, is_selected('foyers', 'progressifs'))

    #     # Port
    #     base_y += spacing_y + 30
    #     painter.drawText(x_start, base_y, "Port:")
    #     painter.drawText(x_start + 60, base_y, "Constant")
    #     draw_checkbox(x_start + 120, base_y - 10, is_selected('port', 'constant'))
    #     painter.drawText(x_start + 220, base_y, "Lecture")
    #     draw_checkbox(x_start + 280, base_y - 10, is_selected('port', 'lecture'))

    #     # Indice
    #     base_y += spacing_y + 30
    #     painter.drawText(x_start, base_y, "Indice:")
    #     painter.drawText(x_start + 60, base_y, "Normal")
    #     draw_checkbox(x_start + 110, base_y - 9, is_selected('indice', 'normal'))
    #     painter.drawText(x_start + 220, base_y, "Fort Indice")
    #     draw_checkbox(x_start + 280, base_y - 9, is_selected('indice', 'fort_indice'))

    #     # Footer
    #     painter.setPen(QPen(QColor("gray")))
    #     painter.setFont(QFont("Helvetica", 13, QFont.Weight.Bold))
    #     painter.drawText(margin + 40, 775, "N.B.: Rapporter toujours vos lunettes après l'achat pour le contrôle")
    #     painter.drawText(margin + 100, 790, "Thank you for choosing NGASSAM OPTIQUE!")

    #     # painter.drawText(x_start, base_y, "Amétropie:")
    #     # painter.drawText(x_start + 80, base_y, "Myopie")
    #     # draw_checkbox(x_start + 120, base_y - 9)
    #     # painter.drawText(x_start + 160, base_y, "Hypermétropie")
    #     # draw_checkbox(x_start + 247, base_y - 9)
    #     # painter.drawText(x_start + 290, base_y, "Astigmatisme")
    #     # draw_checkbox(x_start + 370, base_y - 9)
    #     # painter.drawText(x_start + 420, base_y, "Presbytie")
    #     # draw_checkbox(x_start + 477, base_y - 9)
    #     # painter.drawText(x_start + 550, base_y, "Emmetropie")
    #     # draw_checkbox(x_start + 623, base_y - 9)

    #     # base_y += 3 * spacing_y
    #     # painter.drawText(x_start, base_y, "Types de verre :")
    #     # painter.drawText(x_start + 100, base_y, "minéraux")
    #     # draw_checkbox(x_start + 160, base_y - 9)
    #     # painter.drawText(x_start + 270, base_y, "organiques")
    #     # draw_checkbox(x_start + 339, base_y - 9)
    #     # painter.drawText(x_start + 460, base_y, "polycarbonates")
    #     # draw_checkbox(x_start + 549, base_y - 9)

    #     # base_y += spacing_y + 30
    #     # painter.drawText(x_start, base_y, "Tientes :")
    #     # painter.drawText(x_start + 60, base_y, "Blac")
    #     # draw_checkbox(x_start + 90, base_y - 9)
    #     # painter.drawText(x_start + 160, base_y, "Grise")
    #     # draw_checkbox(x_start + 195, base_y - 9)
    #     # painter.drawText(x_start + 280, base_y, "Photochromique")
    #     # draw_checkbox(x_start + 373, base_y - 9)
    #     # painter.drawText(x_start + 490, base_y, "Antireflet")
    #     # draw_checkbox(x_start + 545, base_y - 9)
    #     # painter.drawText(x_start + 600, base_y, "Blue Portect")
    #     # draw_checkbox(x_start + 669, base_y - 9)

    #     # base_y += spacing_y + 30
    #     # painter.drawText(x_start, base_y, "Foyer :")
    #     # painter.drawText(x_start + 60, base_y, "Unifocaux")
    #     # draw_checkbox(x_start + 120, base_y - 11)
    #     # painter.drawText(x_start + 220, base_y, "Bifocaux")
    #     # draw_checkbox(x_start + 280, base_y - 11)
    #     # painter.drawText(x_start + 400, base_y, "Progressifs")
    #     # draw_checkbox(x_start + 467, base_y - 11)

    #     # base_y += spacing_y + 30
    #     # painter.drawText(x_start, base_y, "Port :")
    #     # painter.drawText(x_start + 60, base_y, "Constant")
    #     # draw_checkbox(x_start + 120, base_y - 10)
    #     # painter.drawText(x_start + 220, base_y, "Lecture")
    #     # draw_checkbox(x_start + 280, base_y - 10)

    #     # base_y += spacing_y + 30
    #     # painter.drawText(x_start, base_y, "Indice :")
    #     # painter.drawText(x_start + 60, base_y, "Normal")
    #     # draw_checkbox(x_start + 110, base_y - 9)
    #     # painter.drawText(x_start + 220, base_y, "For Indice")
    #     # draw_checkbox(x_start + 280, base_y - 9)
        
        
    #     # # painter.setFont(QFont("Helvetica", 14, QFont.Weight.Bold))
    #     # # painter.drawText(margin, y, "Prescription Details")
    #     # # y += line_spacing
    #     # # painter.setFont(QFont("Helvetica", 12))
    #     # # painter.drawText(margin, y, f"Ametropie: {', '.join(report.get('ametropie', ['N/A']))}")
    #     # # y += line_spacing
    #     # # painter.drawText(margin, y, f"Type de Verre: {', '.join(report.get('types_de_verre', ['N/A']))}")
    #     # # y += line_spacing
    #     # # painter.drawText(margin, y, f"Teinte: {', '.join(report.get('teintes', ['N/A']))}")
    #     # # y += line_spacing
    #     # # painter.drawText(margin, y, f"Foyers: {', '.join(report.get('foyers', ['N/A']))}")
    #     # # y += line_spacing
    #     # # painter.drawText(margin, y, f"Port: {', '.join(report.get('port', ['N/A']))}")
    #     # # y += line_spacing
    #     # # painter.drawText(margin, y, f"Indice: {', '.join(report.get('indice', ['N/A']))}")
    #     # y += 4 * line_spacing

    #     # # Footer
    #     # painter.setPen(QPen(QColor("gray")))
    #     # painter.setFont(QFont("Helvetica", 13, QFont.Weight.Bold))
    #     # painter.drawText(margin + 40, 775, "N.B.: Rapporter toujours vos lunettes après l'achat pour le contrôle")
    #     # y += line_spacing 
    #     # painter.drawText(margin + 100, 790, "Thank you for choosing NGASSAM OPTIQUE!")
    #     # y += line_spacing
    #     painter.end()
        
    def render_pdf(self, printer):
        painter = QPainter(printer)
        painter.setPen(QColor("black"))
        painter.setFont(QFont("Helvetica", 12))

        # Dynamically get the page width and height
        # page_rect = printer.pageRect()  # QRectF
        page_rect = printer.pageRect(QPrinter.DevicePixel)

        width = page_rect.width()
        height = page_rect.height()

        # Define margins and spacings based on page size
        margin = width * 0.07  # 7% of page width
        line_spacing = height * 0.03  # 3% of page height
        y = margin

        report = self.report_data
        print("Report Data:", report)

        # Dynamic font sizes
        large_font_size = width * 0.06
        medium_font_size = width * 0.022
        small_font_size = width * 0.017

        # Header
        painter.setFont(QFont("Helvetica-Bold", int(large_font_size), QFont.Weight.Bold))
        painter.setPen(QColor("red"))
        painter.drawText(margin + width * 0.03, y, "NGASSAM OPTIQUE")
        y += line_spacing 

        painter.setFont(QFont("Helvetica-Bold", int(medium_font_size)))
        painter.setPen(QColor("black"))
        painter.drawText(width * 0.145, y + 0.27 * line_spacing, "Situé à l'Avenue Kennedy derrière ADAMAOUA PALACE")
        painter.drawText(width * 0.145, y + 1.3 * line_spacing, "Tél.: (237) 699 67 50 25 / 620 37 69 38 / 671 16 65 27")

        painter.setFont(QFont("Helvetica-Bold", int(small_font_size), italic=True))
        painter.setPen(QColor("red"))
        painter.drawText(width * 0.355, y + 2 * line_spacing, "Le professionnel de la santé visuelle")

        # Separator Line
        painter.setPen(QPen(QColor("black"), 3))
        painter.drawLine(margin, y + 2.52 * line_spacing, width - margin, y + 2.52 * line_spacing)

        y += 3.4 * line_spacing

        # Title
        painter.setFont(QFont("Helvetica-Bold", int(medium_font_size), QFont.Weight.Bold))
        painter.setPen(QColor("red"))
        painter.drawText(width / 2.5 - margin, y + 3.59, "ORDONNANCE DE LUNETTES")

        y += 2 * line_spacing

        # Patient Info
        painter.setPen(QColor("black"))
        painter.setFont(QFont("Helvetica", int(medium_font_size)))

        right_margin = width - margin
        painter.drawText(margin, y, f"Noms et Prénoms: {self.patient_name}")
        y += line_spacing + 2.5

        painter.drawText(margin, y, f"Age: {report.get('age_at_report', 'N/A')}")
        painter.drawText(width / 4 - margin / 2, y, f"Sexe: {self.patient_gender}")
        painter.drawText(right_margin - margin * 7, y, f"Profession: {report.get('profession_at_report', 'N/A')}")
        y += 1 * line_spacing

        # Table for Refraction
        table_x = margin
        table_y = y - 1
        col_width = (width - 2 * margin) / 5  # Five columns equally divided
        row_height = line_spacing * 1.5

        headers = ["œil", "Sphère", "Cyl", "Axe", "Addition"]
        rows = [
            ["OD", f"{report.get('sphere_od', 'N/A')}", f"{report.get('cyl_od', 'N/A')}", f"{report.get('axe_od', 'N/A')}", f"{report.get('addition_od', 'N/A')}"],
            ["OG", f"{report.get('sphere_og', 'N/A')}", f"{report.get('cyl_og', 'N/A')}", f"{report.get('axe_og', 'N/A')}", f"{report.get('addition_og', 'N/A')}"]
        ]

        painter.setFont(QFont("Helvetica-Bold", int(medium_font_size)))

        for col_index, header in enumerate(headers):
            painter.drawText(table_x + col_width * col_index + margin * 0.4, table_y + margin * 0.6,  header)

        for row_index, row in enumerate(rows):
            for col_index, cell in enumerate(row):
                painter.drawText(table_x + col_width * col_index + margin * 0.4,
                                table_y + (row_index + 1) * row_height + margin * 0.6,
                                cell)

        # Draw Table grid
        for r in range(len(rows) + 2):
            painter.drawLine(table_x, table_y + r * row_height, table_x + col_width * 5, table_y + r * row_height)

        for c in range(6):
            painter.drawLine(table_x + c * col_width, table_y, table_x + c * col_width, table_y + row_height * (len(rows) + 1))

        y = table_y + (len(rows) + 2) * row_height + line_spacing

        # Prescriptions checkboxes
        def is_selected(category, value):
            selected_values = report.get(category, [])
            if isinstance(selected_values, str):
                selected_values = selected_values.lower().split(",")
            return value.lower() in [val.lower() for val in selected_values]

        def draw_checkbox(x, y, selected=False):
            box_size = line_spacing * 0.7
            painter.setBrush(QColor("white"))
            painter.drawRect(x, y, box_size, box_size)
            painter.setPen(QPen(QColor("black"), 2))
            painter.drawRect(x, y, box_size, box_size)

            if selected:
                painter.setPen(QPen(QColor("black"), 5)) 
                painter.drawLine(x + 2, y + box_size / 2, x + box_size / 2, y + box_size - 2)
                painter.drawLine(x + box_size / 2, y + box_size - 2, x + box_size - 2, y + 2)

        section_spacing = line_spacing * 2

        # Amétropie
        painter.setFont(QFont("Helvetica-Bold", int(medium_font_size)))
        painter.drawText(margin, y, "Amétropie:")

        # ametropies = ["Myopie", "Hypermétropie", "Astigmatisme", "Presbytie", "Emmetropie"]
        # x_pos = margin + width * 0.15
        # for ametropie in ametropies:
        #     painter.drawText(x_pos, y, ametropie)
        #     draw_checkbox(x_pos + width * 0.08, y - line_spacing * 0.3, is_selected('ametropie', ametropie))
        #     x_pos += width * 0.2
        # y += section_spacing

        ametropies = ["Myopie", "Hypermétropie", "Astigmatisme", "Presbytie", "Emmetropie"]
        x_pos = margin + width * 0.15
        items_per_row = 3
        item_count = 0

        font_metrics = QFontMetrics(painter.font())
        checkbox_size = line_spacing * 0.4  # Checkbox size

        for ametropie in ametropies:
            # Move to a new line if 4 items have been drawn
            if item_count > 0 and item_count % items_per_row == 0:
                y += line_spacing + 1 # Move to next row
                x_pos = margin + width * 0.15  # Reset x position for new row

            # Measure text width
            text_width = font_metrics.horizontalAdvance(ametropie)

            # Draw text
            painter.drawText(x_pos + 3, y, ametropie)

            # Draw checkbox after text
            checkbox_x = x_pos + text_width + 4
            draw_checkbox(checkbox_x, y - line_spacing * 0.6, is_selected('ametropie', ametropie))

            # Advance x position for next item
            x_pos = checkbox_x + checkbox_size + 27

            item_count += 1

        y += section_spacing  # Leave space after the whole group



                # Types de verre
        # ------------------ Types de verre ------------------
        painter.drawText(margin, y, "Types de verre:")
        # y += line_spacing

        types_verre = ["Minéraux", "Organiques", "Polycarbonates"]
        x_pos = margin + width * 0.23
        item_count = 0

        for verre in types_verre:
            if item_count > 0 and item_count % items_per_row == 0:
                y += line_spacing + 1
                x_pos = margin + width * 0.15

            text_width = font_metrics.horizontalAdvance(verre)
            painter.drawText(x_pos, y, verre)
            checkbox_x = x_pos + text_width + 4
            draw_checkbox(checkbox_x, y - line_spacing * 0.5, is_selected('types_verre', verre))
            x_pos = checkbox_x + checkbox_size + 40
            item_count += 1

        y += section_spacing


        # ------------------ Teintes ------------------
        painter.drawText(margin, y, "Teintes:")
        # y += line_spacing

        teintes = ["Blanc", "Gris", "Photochromique", "Antireflet", "Bleue Protect"]
        x_pos = margin + width * 0.15
        item_count = 0

        for teinte in teintes:
            if item_count > 0 and item_count % items_per_row == 0:
                y += line_spacing + 1
                x_pos = margin + width * 0.15

            text_width = font_metrics.horizontalAdvance(teinte)
            painter.drawText(x_pos, y, teinte)
            checkbox_x = x_pos + text_width + 4
            draw_checkbox(checkbox_x, y - line_spacing * 0.5, is_selected('teintes', teinte))
            x_pos = checkbox_x + checkbox_size + 40
            item_count += 1

        y += section_spacing


        # ------------------ Foyers ------------------
        painter.drawText(margin, y, "Foyers:")
        # y += line_spacing

        foyers = ["Unifocaux", "Bifocaux", "Progressifs"]
        x_pos = margin + width * 0.15
        item_count = 0

        for foyer in foyers:
            if item_count > 0 and item_count % items_per_row == 0:
                y += line_spacing + 1
                x_pos = margin + width * 0.15

            text_width = font_metrics.horizontalAdvance(foyer)
            painter.drawText(x_pos, y, foyer)
            checkbox_x = x_pos + text_width + 4
            draw_checkbox(checkbox_x, y - line_spacing * 0.5, is_selected('foyers', foyer))
            x_pos = checkbox_x + checkbox_size + 40
            item_count += 1

        y += section_spacing


        # ------------------ Port ------------------
        painter.drawText(margin, y, "Port:")
        # y += line_spacing

        port_options = ["Constant", "Lecture"]
        x_pos = margin + width * 0.15
        item_count = 0

        for port in port_options:
            if item_count > 0 and item_count % items_per_row == 0:
                y += line_spacing + 1
                x_pos = margin + width * 0.15

            text_width = font_metrics.horizontalAdvance(port)
            painter.drawText(x_pos, y, port)
            checkbox_x = x_pos + text_width + 4
            draw_checkbox(checkbox_x, y - line_spacing * 0.5, is_selected('port', port))
            x_pos = checkbox_x + checkbox_size + 50
            item_count += 1

        y += section_spacing


        # ------------------ Indice ------------------
        painter.drawText(margin, y, "Indice:")
        # y += line_spacing

        indices = ["Normal", "fort indice"]
        x_pos = margin + width * 0.15
        item_count = 0

        for indice in indices:
            if item_count > 0 and item_count % items_per_row == 0:
                y += line_spacing + 1
                x_pos = margin + width * 0.15

            text_width = font_metrics.horizontalAdvance(indice)
            painter.drawText(x_pos, y, indice)
            checkbox_x = x_pos + text_width + 4
            draw_checkbox(checkbox_x, y - line_spacing * 0.5, is_selected('indice', indice))
            x_pos = checkbox_x + checkbox_size + 50
            item_count += 1
        # y += section_spacing
            
        #Footer
        
        #painter.setFont(QFont("Helvetica-Bold", int(medium_font_size), QFont.Weight.Bold))
        #painter.setPen(QPen(QColor("gray")))
        #painter.drawText(width / 6.5 - margin, y + 3.59, "N.B.: Rapporter toujours vos lunettes après l'achat pour le contrôle")
        #y += line_spacing 
        #painter.drawText(width / 6.5 - margin, y + 5.49, "Thank you for choosing NGASSAM OPTIQUE!")
        #y += 2 * line_spacing  
        
        painter.setFont(QFont("Helvetica-Bold", int(small_font_size)))
        painter.setPen(QColor("red"))
        painter.drawText(width * 0.082, y + 1.5 * line_spacing, "N.B.: Rapporter toujours vos lunettes après l'achat pour le contrôle")
        y += 0.5 * line_spacing
        
        painter.setPen(QPen(QColor("black"), 3))
        painter.drawLine(margin, y + 1.589 * line_spacing, width - margin, y + 1.589 * line_spacing)
        y += 1 * line_spacing
        
        
        painter.setFont(QFont("Helvetica-Bold", int(small_font_size)))
        painter.setPen(QColor("black"))
        painter.drawText(width * 0.082, y + 1.9 * line_spacing, "@copy righted by kiven")
        painter.end()
    
    def set_view_mode(self):
        self.save_btn.setEnabled(False)
        self.clear_btn.setEnabled(False)
        # Also disable form fields if needed:
        self.age.setEnabled(False)
        self.Profession.setEnabled(False)
        # self.reference_input.setEnabled(False)
        # # Add other fields to disable as needed
        # for checkbox in self.findChildren(QCheckBox):
        #     checkbox.setEnabled(False)
        # for line_edit in self.findChildren(QLineEdit):
        #     line_edit.setEnabled(False)

    def set_checked_values(self, selected_list, checkbox_group):
            for cb in checkbox_group:
                cb.setChecked(cb.objectName().lower() in selected_list)

                
    def populate_form(self, report_data):
        self.report_data = report_data  # Store for preview/print
        print(report_data)
        # Set date in QDateTimeEdit
        date_str = report_data.get('date', '')  # Expected format: 'YYYY-MM-DD'
        if date_str:
            qdatetime = QDateTime.fromString(date_str, "yyyy-MM-dd")
            if qdatetime.isValid():
                self.dateTimeEdit.setDateTime(qdatetime)
        # Set patient info
        self.p_name.setText(self.patient_name)
        self.sex.setText(self.patient_gender)
        # self.age.setText(self.patient_age)
        # self.Profession.setText(self.patient_profession)
        # self.age.setText(str(report_data.get("age_at_report", "N/A")))        
        # self.Profession.setText(report_data.get("profession_at_report", "N/A"))
        self.age.setText(str(report_data.get("age_at_report", "N/A")))
        self.Profession.setText(report_data.get("profession_at_report", "N/A"))
        self.refferenceID.setText(report_data.get("reference_id", "N/A"))

        # self.refferenceID.setText(self.reference_id_value)
        # Set refraction fields
        self.sphere_od.setText(report_data.get("sphere_od", ""))
        self.cyl_od.setText(report_data.get("cyl_od", ""))
        self.axe_od.setText(report_data.get("axe_od", ""))
        self.addition_od.setText(report_data.get("addition_od", ""))
        self.sphere_og.setText(report_data.get("sphere_og", ""))
        self.cyl_og.setText(report_data.get("cyl_og", ""))
        self.axe_og.setText(report_data.get("axe_og", ""))
        self.addition_og.setText(report_data.get("addition_og", ""))

        # Set checkboxes
        self.set_checked_values(report_data.get("ametropie", []), [
            self.Myopie, self.Hypermetropie, self.Astigmatisme, self.Emmetropie
        ])

        self.set_checked_values(report_data.get("types_de_verre", []), [
            self.Mineraux, self.Organiques, self.Polycarbonates
        ])

        self.set_checked_values(report_data.get("teintes", []), [
            self.Blanc, self.Gris, self.Photochromique, self.Antireflet, self.bleue_protect
        ])

        self.set_checked_values(report_data.get("foyers", []), [
            self.Unifocaux, self.Bifocaux, self.Progressifs
        ])

        self.set_checked_values(report_data.get("port", []), [
            self.Constant, self.Lecture
        ])

        self.set_checked_values(report_data.get("indice", []), [
            self.Normal, self.fort_indice
        ])









            
    # def populate_form(self, report_data):
    #     # Example of setting simple text fields
    #     print(report_data)  # Temporarily add this line before populate_form

    #     # self.refferenceID.setText(report_data.get('reference_id', ''))
    #     self.refferenceID.setText(report_data.get('reference_id', 'N/A'))
    #     # Set date in QDateTimeEdit
    #     date_str = report_data.get('date', '')  # Expected format: 'YYYY-MM-DD'
    #     if date_str:
    #         qdatetime = QDateTime.fromString(date_str, "yyyy-MM-dd")
    #         if qdatetime.isValid():
    #             self.dateTimeEdit.setDateTime(qdatetime)
                
                
                
    #     # Example: Set checkboxes for ametropie (assuming checkboxes are named like ametropie_myopie, etc.)
    #     ametropie_values = report_data.get('ametropie', [])
    #     for value in ametropie_values:
    #         checkbox = getattr(self, f'ametropie_{value}', None)
    #         if checkbox:
    #             checkbox.setChecked(True)

    #     # Similarly for types_de_verre
    #     verre_values = report_data.get('types_de_verre', [])
    #     for value in verre_values:
    #         checkbox = getattr(self, f'verre_{value}', None)
    #         if checkbox:
    #             checkbox.setChecked(True)

    #     # teintes
    #     teinte_values = report_data.get('teintes', [])
    #     for value in teinte_values:
    #         checkbox = getattr(self, f'teinte_{value}', None)
    #         if checkbox:
    #             checkbox.setChecked(True)

    #     # foyers
    #     foyer_values = report_data.get('foyers', [])
    #     for value in foyer_values:
    #         checkbox = getattr(self, f'foyer_{value}', None)
    #         if checkbox:
    #             checkbox.setChecked(True)

    #     # port
    #     port_values = report_data.get('port', [])
    #     for value in port_values:
    #         checkbox = getattr(self, f'port_{value}', None)
    #         if checkbox:
    #             checkbox.setChecked(True)

    #     # indice
    #     indice_values = report_data.get('indice', [])
    #     for value in indice_values:
    #         checkbox = getattr(self, f'indice_{value}', None)
    #         if checkbox:
    #             checkbox.setChecked(True)
                
    # # Set checkboxes for each category

    #     # Set eye measurement fields (example)
    #     self.sphere_od.setText(report_data.get('sphere_od', ''))
    #     self.cyl_od.setText(report_data.get('cyl_od', ''))
    #     self.axe_od.setText(report_data.get('axe_od', ''))
    #     self.addition_od.setText(report_data.get('addition_od', ''))

    #     self.sphere_og.setText(report_data.get('sphere_og', ''))
    #     self.cyl_og.setText(report_data.get('cyl_og', ''))
    #     self.axe_og.setText(report_data.get('axe_og', ''))
    #     self.addition_og.setText(report_data.get('addition_og', ''))
















    # def render_pdf(self, printer):
        
    #     painter = QPainter(printer)
    #     painter.setPen(QColor("black"))
    #     painter.setFont(QFont("Helvetica", 12))

    #     margin = 80
    #     line_spacing = 30
    #     y = margin

    #     report = self.report_data

    #     # Header
    #     painter.setFont(QFont("Helvetica", 18, QFont.Bold))
    #     painter.drawText(margin, y, "NGASSAM OPTIQUE - Medical Report")
    #     y += 2 * line_spacing

    #     # Patient Info
    #     painter.setFont(QFont("Helvetica", 12))
    #     painter.drawText(margin, y, f"Reference ID: {report.get('reference_id', 'N/A')}")
    #     y += line_spacing
    #     painter.drawText(margin, y, f"Patient Name: {self.patient_name}")
    #     y += line_spacing
    #     painter.drawText(margin, y, f"Age: {report.get('age')}   Gender: {self.patient_gender}   Profession: {report.get('profession')}")
    #     y += 2 * line_spacing

    #     # Refraction Data
    #     painter.setFont(QFont("Helvetica", 14, QFont.Bold))
    #     painter.drawText(margin, y, "Refraction (OD/OG)")
    #     y += line_spacing
    #     painter.setFont(QFont("Helvetica", 12))
    #     painter.drawText(margin, y, f"Sphere OD: {report['sphere_od']} | Sphere OG: {report['sphere_og']}")

    #     y += line_spacing
    #     painter.drawText(margin, y, f"Cyl OD: {report['cyl_od']} | Cyl OG: {report['cyl_og']}")
    #     y += line_spacing
    #     painter.drawText(margin, y, f"Axe OD: {report['axe_od']} | Axe OG: {report['axe_og']}")
    #     y += line_spacing
    #     painter.drawText(margin, y, f"Addition OD: {report['addition_od']} | Addition OG: {report['addition_og']}")
    #     y += 2 * line_spacing

    #     # Prescription
    #     painter.setFont(QFont("Helvetica", 14, QFont.Bold))
    #     painter.drawText(margin, y, "Prescription Details")
    #     y += line_spacing
    #     painter.setFont(QFont("Helvetica", 12))
    #     painter.drawText(margin, y, f"Ametropie: {report['ametropie']}")
    #     y += line_spacing
    #     painter.drawText(margin, y, f"Type de Verre: {report['types_de_verre']}")
    #     y += line_spacing
    #     painter.drawText(margin, y, f"Teinte: {report['teintes']}")
    #     y += line_spacing
    #     painter.drawText(margin, y, f"Foyers: {report['foyers']}")
    #     y += line_spacing
    #     painter.drawText(margin, y, f"Port: {report['port']}")
    #     y += line_spacing
    #     painter.drawText(margin, y, f"Indice: {report['indice']}")
    #     y += 2 * line_spacing

    #     # Footer
    #     painter.setPen(QPen(QColor("gray")))
    #     painter.drawText(margin, y, "Generated by NGASSAM OPTIQUE | Confidential")
    #     y += 1 - line_spacing
    #     painter.drawText(margin, y, f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    #     y += line_spacing
    #     painter.end()





    # def fetch_latest_report_id(self):
    #     try:
    #         response = requests.get(f"{BASE_URL}medical-reports/latest/{self.patient_id}/")
    #         if response.status_code == 200:
    #             self.last_saved_report_id = response.json().get("report_id")
    #             print(f"[INFO] Latest report ID fetched: {self.last_saved_report_id}")
    #         else:
    #             QMessageBox.warning(self, "Error", "Could not retrieve latest report.")
    #     except Exception as e:
    #         QMessageBox.critical(self, "Network Error", str(e))


    def get_full_report_data(self):
        if not self.last_saved_report_id:
            QMessageBox.warning(self, "No Report", "No report saved yet!")
            return None
        try:
            response = requests.get(f"{BASE_URL}medical-reports/view/{self.last_saved_report_id}/")
            if response.status_code == 200:
                return response.json()
            else:
                QMessageBox.warning(self, "Error", "Failed to retrieve report data.")
                return None
        except Exception as e:
            QMessageBox.critical(self, "Network Error", str(e))
            return None

    # def preview_report(self):
    #     printer = QPrinter()
    #     preview = QPrintPreviewDialog(printer, self)
    #     preview.paintRequested.connect(lambda p: self.draw_report(p))
    #     preview.exec()

    # def print_report(self):
    #     printer = QPrinter()
    #     dialog = QPrintDialog(printer, self)
    #     if dialog.exec():
    #         self.draw_report(printer)

    # def draw_report(self, printer):
    #     painter = QPainter(printer)
    #     painter.begin(printer)

    #     font = QFont("Times", 12)
    #     painter.setFont(font)

    #     x = 100
    #     y = 100
    #     line_spacing = 40

    #     # Draw report title
    #     painter.drawText(x, y, "🩺 Medical Prescription Report")
    #     y += 2 * line_spacing

    #     # Patient Info
    #     painter.drawText(x, y, f"👤 Name: {self.p_name.text()}")
    #     y += line_spacing
    #     painter.drawText(x, y, f"🎂 Age: {self.age.text()}    ⚧ Gender: {self.sex.text()}")
    #     y += line_spacing
    #     painter.drawText(x, y, f"💼 Profession: {self.Profession.text()}")
    #     y += 2 * line_spacing

    #     # Refraction
    #     painter.drawText(x, y, "🔍 Refraction (Right Eye):")
    #     y += line_spacing
    #     painter.drawText(x + 50, y, f"Sphere: {self.od_sphere.text()}  Cyl: {self.od_cyl.text()}  Axe: {self.od_axl.text()}  Add: {self.od_addition.text()}")
    #     y += line_spacing
    #     painter.drawText(x, y, "🔍 Refraction (Left Eye):")
    #     y += line_spacing
    #     painter.drawText(x + 50, y, f"Sphere: {self.og_sphere.text()}  Cyl: {self.og_cyl.text()}  Axe: {self.og_axl.text()}  Add: {self.og_addition.text()}")
    #     y += 2 * line_spacing

    #     # Prescription Details
    #     painter.drawText(x, y, f"👁️ Vision Type: {self.get_checked_text(self.vision_type)}")
    #     y += line_spacing
    #     painter.drawText(x, y, f"🧪 Lens Type: {self.get_checked_text(self.lens_type)}")
    #     y += line_spacing
    #     painter.drawText(x, y, f"🎨 Tint: {self.get_checked_text(self.tine_option)}")
    #     y += line_spacing
    #     painter.drawText(x, y, f"🔭 Focus Type: {self.get_checked_text(self.focus_type)}")
    #     y += line_spacing
    #     painter.drawText(x, y, f"📖 Usage: {self.get_checked_text(self.port_type)}")
    #     y += line_spacing
    #     painter.drawText(x, y, f"🔍 Index: {self.get_checked_text(self.port_type_2)}")
    #     y += 2 * line_spacing

    #     # Reference
    #     painter.drawText(x, y, f"🧾 Reference ID: {self.refferenceID.text()}")
    #     y += line_spacing
    #     painter.drawText(x, y, f"📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")

    #     painter.end()

    # def preview_report(self):
    #     report_data = self.get_full_report_data()
    #     if not report_data:
    #         return

    #     printer = QPrinter()
    #     preview = QPrintPreviewDialog(printer, self)
    #     preview.paintRequested.connect(lambda p: self.render_report(p, report_data))
    #     preview.exec()


    # def print_report(self):
    #     data = self.fetch_latest_report_id()
    #     if not data:
    #         return

    #     printer = QPrinter()
    #     dialog = QPrintDialog(printer, self)
    #     if dialog.exec():
    #         self.render_report(QPainter(printer), data)

    # def render_report(self, painter, data):
    #     painter.begin(painter.device())
    #     painter.drawText(100, 100, f"Patient: {data['patient']}")
    #     painter.drawText(100, 130, f"Date: {data['date']}")
    #     painter.drawText(100, 160, f"Age: {data['age']}")
    #     painter.drawText(100, 190, f"Profession: {data['profession']}")
    #     painter.drawText(100, 220, f"OD: {data['sphere_od']} {data['cyl_od']} {data['axe_od']} ADD: {data['addition_od']}")
    #     painter.drawText(100, 250, f"OG: {data['sphere_og']} {data['cyl_og']} {data['axe_og']} ADD: {data['addition_og']}")
    #     painter.drawText(100, 280, f"Ametropie: {data['ametropie']}")
    #     painter.drawText(100, 310, f"Verre: {data['types_de_verre']}")
    #     painter.drawText(100, 340, f"Teinte: {data['teintes']}")
    #     painter.drawText(100, 370, f"Foyers: {data['foyers']}")
    #     painter.drawText(100, 400, f"Port: {data['port']}")
    #     painter.drawText(100, 430, f"Indice: {data['indice']}")
    #     painter.end()

    # def preview_report(self):
    #     self.fetch_and_render_report(preview=True)

    # def print_report(self):
    #     self.fetch_and_render_report(preview=False)

    # def fetch_and_render_report(self, preview=True):
    #     if not self.last_saved_report_id:
    #         QMessageBox.warning(self, "Warning", "Please save the report before continuing.")
    #         return

    #     try:
    #         response = requests.get(f"{BASE_URL}medical-reports/view/{self.last_saved_report_id}/")
    #         if response.status_code == 200:
    #             report_data = response.json()
    #             self.render(report_data, preview=preview)
    #         else:
    #             QMessageBox.warning(self, "Error", "Could not fetch data from server.")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))




    # def render(self, painter, data, report_data, preview=True):
    #     painter.begin(painter.device())
    #     painter.setRenderHint(QPainter.Antialiasing)

    #     page_width = painter.device().width()
    #     margin = 100
    #     y = margin

    #     # Header
    #     painter.setFont(QFont("Helvetica", 16, QFont.Bold))
    #     painter.drawText(margin, y, "Medical Report")
    #     y += 40

    #     # Reference and Date
    #     painter.setFont(QFont("Helvetica", 10))
    #     painter.drawText(margin, y, f"Reference ID: {data.get('reference_id', 'N/A')}")
    #     y += 25
    #     painter.drawText(margin, y, f"Date: {data.get('date', 'N/A')}")
    #     y += 40

    #     # Patient Info
    #     painter.setFont(QFont("Helvetica", 12, QFont.Bold))
    #     painter.drawText(margin, y, "Patient Information")
    #     y += 25
    #     painter.setFont(QFont("Helvetica", 10))
    #     painter.drawText(margin, y, f"Name: {data.get('patient_name', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Age: {data.get('patient_age', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Gender: {data.get('patient_gender', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Profession: {data.get('patient_profession', '')}")
    #     y += 30

    #     # Refraction Section
    #     painter.setFont(QFont("Helvetica", 12, QFont.Bold))
    #     painter.drawText(margin, y, "Refraction")
    #     y += 25
    #     painter.setFont(QFont("Helvetica", 10))
    #     painter.drawText(margin, y, f"Sphere OD: {data.get('sphere_od', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Cyl OD: {data.get('cyl_od', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Axe OD: {data.get('axe_od', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Addition OD: {data.get('addition_od', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Sphere OG: {data.get('sphere_og', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Cyl OG: {data.get('cyl_og', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Axe OG: {data.get('axe_og', '')}")
    #     y += 20
    #     painter.drawText(margin, y, f"Addition OG: {data.get('addition_og', '')}")
    #     y += 30

    #     # Prescription Section
    #     painter.setFont(QFont("Helvetica", 12, QFont.Bold))
    #     painter.drawText(margin, y, "Prescription")
    #     y += 25
    #     painter.setFont(QFont("Helvetica", 10))
    #     painter.drawText(margin, y, f"Ametropie: {', '.join(data.get('ametropie', []))}")
    #     y += 20
    #     painter.drawText(margin, y, f"Type de Verre: {', '.join(data.get('types_de_verre', []))}")
    #     y += 20
    #     painter.drawText(margin, y, f"Teintes: {', '.join(data.get('teintes', []))}")
    #     y += 20
    #     painter.drawText(margin, y, f"Foyers: {', '.join(data.get('foyers', []))}")
    #     y += 20
    #     painter.drawText(margin, y, f"Port: {', '.join(data.get('port', []))}")
    #     y += 20
    #     painter.drawText(margin, y, f"Indice: {', '.join(data.get('indice', []))}")
    #     y += 40

    #     # Footer
    #     painter.setFont(QFont("Helvetica", 8, QFont.StyleItalic))
    #     painter.drawText(margin, y, "Generated by NGASSAM Optique")

    #     painter.end()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MedicalReportForm()
    window.show()
    sys.exit(app.exec())










