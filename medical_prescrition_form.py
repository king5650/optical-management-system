import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_ux.prescription_module.ui_prescription_form3 import Ui_MainWindow  # your converted .py UI file
import uuid
from PySide6.QtCore import QTimer

BASE_URL = "http://127.0.0.1:8000/auth/"

class MedicalReportForm(QMainWindow, Ui_MainWindow):
    def __init__(self, patient_id, name, age, gender, profession):
        super().__init__()
        self.setupUi(self)
        self.patient_id = patient_id
        self.generate_reference_id()
        # Pre-fill patient info
        self.p_name.setText(name)
        self.age.setText(str(age))
        self.sex.setText(gender)
        self.Profession.setText(profession)

        # Connect buttons
        self.save_btn.clicked.connect(self.save_report)
        self.clear_btn.clicked.connect(self.clear_form)
        
        # self.refferenceID.setText(str(uuid.uuid4())[:8])  # Short ref
        
        # QTimer.singleShot(100, self.generate_reference_id)  # Wait 100 ms
        
    # def generate_reference_id(self):
    #     try:
    #         response = requests.get(f"{BASE_URL}medical-reports/next-reference/")
    #         if response.status_code == 200:
    #             next_ref = response.json().get('reference_id')
    #             print("Generated Ref:", next_ref)  # Debug
    #             print("Label Exists?", hasattr(self, "refferenceID"))
    #             self.refferenceID.setText(next_ref)
    #     except requests.RequestException:
    #         self.refferenceID.setText("Pre-UNKNOWN")
    
    def generate_reference_id(self):
        try:
            response = requests.get(f"{BASE_URL}medical-reports/next-reference/")
            if response.status_code == 200:
                next_ref = response.json().get('reference_id')
                self.refferenceID.setText(next_ref)
            else:
                self.refferenceID.setText("Pre-ERROR")
        except requests.RequestException:
            self.refferenceID.setText("Pre-UNKNOWN")

    def save_report(self):
        try:
            data = {
                "patient_id": self.patient_id,
                "age": int(self.age.text()),
                "profession": self.Profession.text(),

                # Refraction (Right Eye)
                "sphere_od": self.od_sphere.text(),
                "cyl_od": self.od_cyl.text(),
                "axe_od": self.od_axl.text(),
                "addition_od": self.od_addition.text(),

                # Refraction (Left Eye)
                "sphere_og": self.og_sphere.text(),
                "cyl_og": self.og_cyl.text(),
                "axe_og": self.og_axl.text(),
                "addition_og": self.og_addition.text(),

                # Prescription
                "ametropie": self.get_checked_text(self.vision_type),
                "types_de_verre": self.get_checked_text(self.lens_type),
                "teintes": self.get_checked_text(self.tine_option),
                "foyers": self.get_checked_text(self.focus_type),
                "port": self.get_checked_text(self.port_type),
                "indice": self.get_checked_text(self.port_type_2),
            }

            response = requests.post(f"{BASE_URL}medical-reports/create/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Medical report saved successfully.")
                self.clear_form()
            else:
                QMessageBox.warning(self, "Error", response.json().get("error", "Failed to save report."))
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def get_checked_text(self, groupBox):
        for checkbox in groupBox.findChildren(type(self.vision_type.children()[0])):
            if checkbox.isChecked():
                return checkbox.text()
        return ""

    def clear_form(self):
        for group in [self.vision_type, self.lens_type, self.tine_option, self.focus_type, self.port_type, self.port_type_2]:
            for checkbox in group.findChildren(type(self.vision_type.children()[0])):
                checkbox.setChecked(False)

        for field in [self.od_sphere, self.od_cyl, self.od_axl, self.od_addition,
                      self.og_sphere, self.og_cyl, self.og_axl, self.og_addition]:
            field.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = MedicalReportForm(patient_id="1", name="John Doe", age=30, gender="M", profession="Engineer")
    form.show()
    sys.exit(app.exec())



