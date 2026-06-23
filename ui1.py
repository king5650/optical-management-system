# # # # from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QSpinBox
# # # # from PyQt6.QtGui import QFont, QColor
# # # # import sys

# # # # class PatientInfoWidget(QWidget):
# # # #     def __init__(self):
# # # #         super().__init__()

# # # #         self.setStyleSheet("""
# # # #             /* Container for the whole section */
# # # #             .patient-info-container {
# # # #                 background-color: #eff6ff; /* bg-blue-50 */
# # # #                 border-radius: 8px; /* rounded-lg */
# # # #                 padding: 16px; /* p-4 */
# # # #                 margin-bottom: 24px; /* mb-6 */
# # # #             }

# # # #             /* Header (h2) */
# # # #             .patient-info-header {
# # # #                 font-size: 1.125em; /* text-lg */
# # # #                 font-weight: 600; /* font-semibold */
# # # #                 color: #2d3748; /* text-gray-800 */
# # # #                 margin-bottom: 12px; /* mb-3 */
# # # #                 display: flex;
# # # #                 align-items: center;
# # # #             }

# # # #             /* Icon (i) - Requires custom icon rendering or a font icon library */
# # # #             .patient-info-icon {
# # # #                 font-size: 1.5em; /* ri-lg */
# # # #                 margin-right: 8px; /* mr-2 */
# # # #                 color: QColor(0, 123, 255); /* Approximate for text-primary */
# # # #             }

# # # #             /* Label */
# # # #             .form-label {
# # # #                 display: block;
# # # #                 font-size: 0.875em; /* text-sm */
# # # #                 font-weight: 500; /* font-medium */
# # # #                 color: #4a5568; /* text-gray-700 */
# # # #                 margin-bottom: 4px; /* mb-1 */
# # # #             }

# # # #             /* Required asterisk */
# # # #             .required {
# # # #                 color: #dc2626; /* text-red-500 */
# # # #             }

# # # #             /* Input (text, tel) */
# # # #             .form-input {
# # # #                 width: 100%;
# # # #                 padding: 8px 12px; /* px-3 py-2 */
# # # #                 border: 1px solid #cbd5e0; /* border-gray-300 */
# # # #                 border-radius: 4px; /* rounded-button */
# # # #                 font-size: 0.875em; /* text-sm */
# # # #             }

# # # #             /* Input (number - QSpinBox) */
# # # #             .form-number-input {
# # # #                 width: 100%;
# # # #                 padding: 8px 12px; /* px-3 py-2 */
# # # #                 border: 1px solid #cbd5e0; /* border-gray-300 */
# # # #                 border-radius: 4px; /* rounded-button */
# # # #                 font-size: 0.875em; /* text-sm */
# # # #             }

# # # #             /* Gender container */
# # # #             .gender-container {
# # # #                 display: flex;
# # # #                 align-items: center;
# # # #                 margin-top: 8px; /* mt-2 */
# # # #             }

# # # #             /* Custom radio button (visual - needs actual logic) */
# # # #             .custom-radio {
# # # #                 width: 16px;
# # # #                 height: 16px;
# # # #                 border: 1px solid #9ca3af; /* border-gray-400 or similar */
# # # #                 border-radius: 50%;
# # # #                 margin-right: 8px; /* mr-2 */
# # # #             }

# # # #             .custom-radio.checked {
# # # #                 border-color: QColor(0, 123, 255); /* Primary color when checked */
# # # #                 background-color: QColor(0, 123, 255);
# # # #                 /* Add inner circle for visual indication */
# # # #             }

# # # #             .custom-radio.checked::after {
# # # #                 content: '';
# # # #                 display: block;
# # # #                 width: 8px;
# # # #                 height: 8px;
# # # #                 border-radius: 50%;
# # # #                 background-color: white;
# # # #                 margin: 3px;
# # # #             }

# # # #             /* Gender label */
# # # #             .gender-label {
# # # #                 font-size: 0.875em; /* text-sm */
# # # #             }

# # # #             /* Grid Layout (first row - Full Name, Patient ID) */
# # # #             .grid-cols-2 {
# # # #                 display: grid;
# # # #                 grid-template-columns: 1fr; /* Default to 1 column */
# # # #                 gap: 16px; /* gap-4 */
# # # #                 margin-bottom: 16px; /* mb-4 */
# # # #             }

# # # #             @media (min-width: 768px) { /* md: */
# # # #                 .grid-cols-2 {
# # # #                     grid-template-columns: repeat(2, 1fr); /* md:grid-cols-2 */
# # # #                 }
# # # #             }

# # # #             /* Grid Layout (second row - Age, Gender, Contact) */
# # # #             .grid-cols-3 {
# # # #                 display: grid;
# # # #                 grid-template-columns: 1fr; /* Default to 1 column */
# # # #                 gap: 16px; /* gap-4 */
# # # #             }

# # # #             @media (min-width: 768px) { /* md: */
# # # #                 .grid-cols-3 {
# # # #                     grid-template-columns: repeat(3, 1fr); /* md:grid-cols-3 */
# # # #                 }
# # # #             }

# # # #             /* Insurance Information container */
# # # #             .insurance-container {
# # # #                 margin-top: 16px; /* mt-4 */
# # # #                 display: flex;
# # # #                 align-items: center;
# # # #             }
# # # #         """)

# # # #         # Create widgets
# # # #         container = QWidget()
# # # #         container.setObjectName("patient-info-container")

# # # #         header_label = QLabel("Patient Information")
# # # #         header_label.setObjectName("patient-info-header")

# # # #         icon_label = QLabel()
# # # #         icon_label.setObjectName("patient-info-icon")
# # # #         icon_label.setText("\uf007") # Placeholder for user icon

# # # #         header_layout = QHBoxLayout()
# # # #         header_layout.addWidget(icon_label)
# # # #         header_layout.addWidget(header_label)

# # # #         # First Row (Full Name, Patient ID)
# # # #         full_name_label = QLabel("Full Name <span class='required'>*</span>")
# # # #         full_name_label.setObjectName("form-label")
# # # #         full_name_input = QLineEdit("Robert Johnson")
# # # #         full_name_input.setObjectName("form-input")

# # # #         patient_id_label = QLabel("Patient ID <span class='required'>*</span>")
# # # #         patient_id_label.setObjectName("form-label")
# # # #         patient_id_input = QLineEdit("PT-10045782")
# # # #         patient_id_input.setObjectName("form-input")

# # # #         grid_layout_1 = QGridLayout()
# # # #         grid_layout_1.addWidget(full_name_label, 0, 0)
# # # #         grid_layout_1.addWidget(full_name_input, 1, 0)
# # # #         grid_layout_1.addWidget(patient_id_label, 0, 1)
# # # #         grid_layout_1.addWidget(patient_id_input, 1, 1)
# # # #         grid_container_1 = QWidget()
# # # #         grid_container_1.setObjectName("grid-cols-2")
# # # #         grid_container_1.setLayout(grid_layout_1)

# # # #         # Second Row (Age, Gender, Contact Number)
# # # #         age_label = QLabel("Age <span class='required'>*</span>")
# # # #         age_label.setObjectName("form-label")
# # # #         age_input = QSpinBox()
# # # #         age_input.setValue(42)
# # # #         age_input.setObjectName("form-number-input")

# # # #         gender_label = QLabel("Gender <span class='required'>*</span>")
# # # #         gender_label.setObjectName("form-label")
# # # #         male_radio_container = QWidget()
# # # #         male_radio_container_layout = QHBoxLayout()
# # # #         male_radio = QWidget()
# # # #         male_radio.setObjectName("custom-radio checked")
# # # #         male_radio_container_layout.addWidget(male_radio)
# # # #         male_label = QLabel("Male")
# # # #         male_label.setObjectName("gender-label")
# # # #         male_radio_container_layout.addWidget(male_label)
# # # #         male_radio_container.setLayout(male_radio_container_layout)

# # # #         female_radio_container = QWidget()
# # # #         female_radio_container_layout = QHBoxLayout()
# # # #         female_radio = QWidget()
# # # #         female_radio.setObjectName("custom-radio")
# # # #         female_radio_container_layout.addWidget(female_radio)
# # # #         female_label = QLabel("Female")
# # # #         female_label.setObjectName("gender-label")
# # # #         female_radio_container_layout.addWidget(female_label)
# # # #         female_radio_container.setLayout(female_radio_container_layout)

# # # #         other_radio_container = QWidget()
# # # #         other_radio_container_layout = QHBoxLayout()
# # # #         other_radio = QWidget()
# # # #         other_radio.setObjectName("custom-radio")
# # # #         other_radio_container_layout.addWidget(other_radio)
# # # #         other_label = QLabel("Other")
# # # #         other_label.setObjectName("gender-label")
# # # #         other_radio_container_layout.addWidget(other_label)
# # # #         other_radio_container.setLayout(other_radio_container_layout)

# # # #         gender_widget = QWidget()
# # # #         gender_layout = QVBoxLayout()
# # # #         gender_layout.addWidget(gender_label)
# # # #         gender_layout.addWidget(QWidget()) # Spacer for alignment with radios
# # # #         gender_layout.addWidget(male_radio_container)
# # # #         gender_layout.addWidget(female_radio_container)
# # # #         gender_layout.addWidget(other_radio_container)
# # # #         gender_widget.setLayout(gender_layout)

# # # #         contact_label = QLabel("Contact Number")
# # # #         contact_label.setObjectName("form-label")
# # # #         contact_input = QLineEdit("(555) 123-4567")
# # # #         contact_input.setObjectName("form-input")

# # # #         grid_layout_2 = QGridLayout()
# # # #         grid_layout_2.addWidget(age_label, 0, 0)
# # # #         grid_layout_2.addWidget(age_input, 1, 0)
# # # #         grid_layout_2.addWidget(gender_label, 0, 1)
# # # #         grid_layout_2.addWidget(gender_widget, 1, 1)
# # # #         grid_layout_2.addWidget(contact_label, 0, 2)
# # # #         grid_layout_2.addWidget(contact_input, 1, 2)
# # # #         grid_container_2 = QWidget()
# # # #         grid_container_2.setObjectName("grid-cols-3")
# # # #         grid_container_2.setLayout(grid_layout_2)

# # # #         # Insurance Information
# # # #         insurance_label = QLabel("Insurance Information")
# # # #         insurance_label.setObjectName("form-label")
# # # #         insurance_input = QLineEdit("BlueCross Health Plan - Policy #BC876543")
# # # #         insurance_input.setObjectName("form-input")
# # # #         insurance_container = QWidget()
# # # #         insurance_layout = QVBoxLayout()
# # # #         insurance_layout.addWidget(insurance_label)
# # # #         insurance_layout.addWidget(insurance_input)
# # # #         insurance_container.setObjectName("insurance-container")
# # # #         insurance_container.setLayout(insurance_layout)

# # # #         main_layout = QVBoxLayout(container)
# # # #         main_layout.addLayout(header_layout)
# # # #         main_layout.addWidget(grid_container_1)
# # # #         main_layout.addWidget(grid_container_2)
# # # #         main_layout.addWidget(insurance_container)

# # # #         layout = QVBoxLayout(self)
# # # #         layout.addWidget(container)

# # # # if __name__ == '__main__':
# # # #     app = QApplication(sys.argv)
# # # #     patient_info = PatientInfoWidget()
# # # #     patient_info.show()
# # # #     sys.exit(app.exec())



# # # from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem, QCheckBox
# # # from PyQt6.QtGui import QFont, QColor
# # # import sys

# # # class OpticalPrescriptionWidget(QWidget):

# # #     def __init__(self):
# # #         super().__init__()

   
# # #         self.setStyleSheet("""
# # #             /* Container for the whole section */
# # #             .optical-prescription-container {
# # #                 margin-bottom: 24px; /* mb-6 */
# # #             }

# # #             /* Header (h2) */
# # #             .optical-prescription-header {
# # #                 font-size: 1.125em; /* text-lg */
# # #                 font-weight: 600; /* font-semibold */
# # #                 color: #2d3748; /* text-gray-800 */
# # #                 margin-bottom: 12px; /* mb-3 */
# # #                 display: flex;
# # #                 align-items: center;
# # #             }

# # #             /* Icon (i) - Requires custom icon rendering or a font icon library */
# # #             .optical-prescription-icon {
# # #                 font-size: 1.5em; /* ri-lg */
# # #                 margin-right: 8px; /* mr-2 */
# # #                 color: QColor(0, 123, 255); /* Approximate for text-primary */
# # #             }

# # #             /* Table container */
# # #             .table-container {
# # #                 overflow-x: auto;
# # #             }

# # #             /* Table */
# # #             .prescription-table {
# # #                 min-width: 100%;
# # #                 border-collapse: collapse;
# # #             }

# # #             /* Table header (thead) */
# # #             .prescription-table thead th {
# # #                 background-color: #f9fafb; /* bg-gray-50 */
# # #                 color: #6b7280; /* text-gray-500 */
# # #                 font-size: 0.75em; /* text-xs */
# # #                 font-weight: 500; /* font-medium */
# # #                 text-align: left;
# # #                 padding: 12px; /* px-3 py-3 */
# # #                 letter-spacing: 0.025em; /* tracking-wider */
# # #             }

# # #             /* Table body (tbody) */
# # #             .prescription-table tbody td {
# # #                 padding: 12px; /* px-3 py-3 */
# # #                 white-space: nowrap;
# # #             }

# # #             .prescription-table tbody tr {
# # #                 border-bottom: 1px solid #e5e7eb; /* divide-gray-200 */
# # #                 background-color: white; /* bg-white */
# # #             }

# # #             .prescription-table tbody tr:last-child {
# # #                 border-bottom: none;
# # #             }

# # #             .prescription-table tbody td:first-child {
# # #                 font-weight: 500; /* font-medium */
# # #             }

# # #             /* Input fields within the table */
# # #             .table-input {
# # #                 width: 100%;
# # #                 padding: 4px 8px; /* px-2 py-1 */
# # #                 border: 1px solid #cbd5e0; /* border-gray-300 */
# # #                 border-radius: 4px; /* rounded-button */
# # #                 font-size: 0.875em; /* text-sm */
# # #             }

# # #             /* Vision/Lens/Tint/Focus/Port/Index Type containers */
# # #             .options-grid {
# # #                 display: grid;
# # #                 grid-template-columns: 1fr; /* grid-cols-1 */
# # #                 gap: 24px; /* gap-6 */
# # #                 margin-top: 24px; /* mt-6 */
# # #             }

# # #             @media (min-width: 768px) { /* md: */
# # #                 .options-grid {
# # #                     grid-template-columns: repeat(3, 1fr); /* md:grid-cols-3 */
# # #                 }
# # #             }

# # #             .options-grid > div {
# # #                 /* Styles for each section (Vision Type, Lens Type, etc.) */
# # #             }

# # #             .options-header {
# # #                 font-size: 0.875em; /* text-sm */
# # #                 font-weight: 500; /* font-medium */
# # #                 color: #4a5568; /* text-gray-700 */
# # #                 margin-bottom: 8px; /* mb-2 */
# # #             }

# # #             .options-list {
# # #                 display: flex;
# # #                 flex-direction: column;
# # #                 gap: 8px; /* space-y-2 */
# # #             }

# # #             .option-item {
# # #                 display: flex;
# # #                 align-items: center;
# # #             }

# # #             /* Custom radio button */
# # #             .custom-radio {
# # #                 width: 16px;
# # #                 height: 16px;
# # #                 border: 1px solid #9ca3af; /* border-gray-400 or similar */
# # #                 border-radius: 50%;
# # #                 margin-right: 8px; /* mr-2 */
# # #             }

# # #             .custom-radio.checked {
# # #                 border-color: QColor(0, 123, 255); /* Primary color when checked */
# # #                 background-color: QColor(0, 123, 255);
# # #             }

# # #             .custom-radio.checked::after {
# # #                 content: '';
# # #                 display: block;
# # #                 width: 8px;
# # #                 height: 8px;
# # #                 border-radius: 50%;
# # #                 background-color: white;
# # #                 margin: 3px;
# # #             }

# # #             /* Custom checkbox */
# # #             .custom-checkbox {
# # #                 width: 16px;
# # #                 height: 16px;
# # #                 border: 1px solid #9ca3af; /* border-gray-400 or similar */
# # #                 border-radius: 4px;
# # #                 margin-right: 8px; /* mr-2 */
# # #                 display: flex;
# # #                 align-items: center;
# # #                 justify-content: center;
# # #             }

# # #             .custom-checkbox.checked::after {
# # #                 content: '\\2713'; /* Checkmark Unicode */
# # #                 font-size: 12px;
# # #                 color: white;
# # #             }

# # #             .option-label {
# # #                 font-size: 0.875em; /* text-sm */
# # #             }
# # #         """)


# # #         # Create widgets
# # #         container = QWidget()
# # #         container.setObjectName("optical-prescription-container")

# # #         header_label = QLabel("Optical Prescription Details")
# # #         header_label.setObjectName("optical-prescription-header")

# # #         icon_label = QLabel()
# # #         icon_label.setObjectName("optical-prescription-icon")
# # #         icon_label.setText("\uf06e") # Placeholder for eye icon

# # #         header_layout = QHBoxLayout()
# # #         header_layout.addWidget(icon_label)
# # #         header_layout.addWidget(header_label)

# # #         # Create a widget to hold the header layout
# # #         header_widget = QWidget()
# # #         header_widget.setLayout(header_layout)

# # #         # Prescription Table
# # #         table_container = QWidget()
# # #         table_container.setObjectName("table-container")
# # #         prescription_table = QTableWidget(2, 5)
# # #         prescription_table.setObjectName("prescription-table")
# # #         prescription_table.setHorizontalHeaderLabels(["Eye", "Sphere", "Cyl", "Axe", "Addition"])
# # #         prescription_table.setItem(0, 0, QTableWidgetItem("OD (Right)"))
# # #         prescription_table.setItem(1, 0, QTableWidgetItem("OG (Left)"))
# # #         for row in range(2):
# # #             for col in range(1, 5):
# # #                 input_field = QLineEdit()
# # #                 input_field.setObjectName("table-input")
# # #                 prescription_table.setCellWidget(row, col, input_field)
# # #         table_layout = QVBoxLayout(table_container)
# # #         table_layout.addWidget(prescription_table)

# # #         # Vision Type
# # #         vision_type_container = QWidget()
# # #         vision_type_container_layout = QVBoxLayout()
# # #         vision_type_header = QLabel("Vision Type")
# # #         vision_type_header.setObjectName("options-header")
# # #         vision_type_container_layout.addWidget(vision_type_header)
# # #         vision_options_widget = QWidget()
# # #         vision_options_layout = QVBoxLayout()
# # #         vision_options_layout.setSpacing(8)
# # #         vision_types = ["Myopie", "Hypermetropie", "Astigmatisme", "Emmetropie"]
# # #         self.vision_radio_buttons = []
# # #         for vision in vision_types:
# # #             item_widget = QWidget()
# # #             item_layout = QHBoxLayout()
# # #             radio = QWidget()
# # #             radio.setObjectName("custom-radio")
# # #             if vision == "Myopie":
# # #                 radio.setProperty("class", "custom-radio checked")
# # #                 radio.style().polish(radio) # Force style update
# # #             self.vision_radio_buttons.append(radio)
# # #             label = QLabel(vision)
# # #             label.setObjectName("option-label")
# # #             item_layout.addWidget(radio)
# # #             item_layout.addWidget(label)
# # #             item_widget.setLayout(item_layout)
# # #             vision_options_layout.addWidget(item_widget)
# # #         vision_options_widget.setLayout(vision_options_layout)
# # #         vision_type_container_layout.addWidget(vision_options_widget)
# # #         vision_type_container.setLayout(vision_type_container_layout)

# # #         # Lens Type
# # #         lens_type_container = QWidget()
# # #         lens_type_container_layout = QVBoxLayout()
# # #         lens_type_header = QLabel("Lens Type")
# # #         lens_type_header.setObjectName("options-header")
# # #         lens_type_container_layout.addWidget(lens_type_header)
# # #         lens_options_widget = QWidget()
# # #         lens_options_layout = QVBoxLayout()
# # #         lens_options_layout.setSpacing(8)
# # #         lens_types = ["Mineraux", "Organiques", "Polycarbonates"]
# # #         self.lens_checkboxes = []
# # #         for lens in lens_types:
# # #             item_widget = QWidget()
# # #             item_layout = QHBoxLayout()
# # #             checkbox = QCheckBox(lens)
# # #             checkbox.setObjectName("option-label")
# # #             checkbox_widget = QWidget()
# # #             checkbox_widget.setObjectName("custom-checkbox")
# # #             self.lens_checkboxes.append(checkbox_widget)
# # #             item_layout.addWidget(checkbox_widget)
# # #             item_layout.addWidget(checkbox)
# # #             item_widget.setLayout(item_layout)
# # #             lens_options_layout.addWidget(item_widget)
# # #         lens_options_widget.setLayout(lens_options_layout)
# # #         lens_type_container_layout.addWidget(lens_options_widget)
# # #         lens_type_container.setLayout(lens_type_container_layout)

# # #         # Tint Options
# # #         tint_options_container = QWidget()
# # #         tint_options_container_layout = QVBoxLayout()
# # #         tint_options_header = QLabel("Tint Options")
# # #         tint_options_header.setObjectName("options-header")
# # #         tint_options_container_layout.addWidget(tint_options_header)
# # #         tint_options_widget = QWidget()
# # #         tint_options_layout = QVBoxLayout()
# # #         tint_options_layout.setSpacing(8)
# # #         tint_types = ["Blanc", "Gris", "Antireflet", "Bleue protect", "Photochromique"]
# # #         self.tint_checkboxes = []
# # #         for tint in tint_types:
# # #             item_widget = QWidget()
# # #             item_layout = QHBoxLayout()
# # #             checkbox = QCheckBox(tint)
# # #             checkbox.setObjectName("option-label")
# # #             checkbox_widget = QWidget()
# # #             checkbox_widget.setObjectName("custom-checkbox")
# # #             self.tint_checkboxes.append(checkbox_widget)
# # #             item_layout.addWidget(checkbox_widget)
# # #             item_layout.addWidget(checkbox)
# # #             item_widget.setLayout(item_layout)
# # #             tint_options_layout.addWidget(item_widget)
# # #         tint_options_widget.setLayout(tint_options_layout)
# # #         tint_options_container_layout.addWidget(tint_options_widget)
# # #         tint_options_container.setLayout(tint_options_container_layout)

# # #         options_grid = QWidget()
# # #         options_grid.setObjectName("options-grid")
# # #         options_grid_layout = QGridLayout(options_grid)
# # #         options_grid_layout.addWidget(vision_type_container, 0, 0)
# # #         options_grid_layout.addWidget(lens_type_container, 0, 1)
# # #         options_grid_layout.addWidget(tint_options_container, 0, 2)

# # #         # Focus Type
# # #         focus_type_container = QWidget()
# # #         focus_type_container_layout = QVBoxLayout()
# # #         focus_type_header = QLabel("Focus Type")
# # #         focus_type_header.setObjectName("options-header")
# # #         focus_type_container_layout.addWidget(focus_type_header)
# # #         focus_options_widget = QWidget()
# # #         focus_options_layout = QVBoxLayout()
# # #         focus_options_layout.setSpacing(8)
# # #         focus_types = ["Unifocaux", "Bifocaux", "Progressifs"]
# # #         self.focus_checkboxes = []
# # #         for focus in focus_types:
# # #             item_widget = QWidget()
# # #             item_layout = QHBoxLayout()
# # #             checkbox = QCheckBox(focus)
# # #             checkbox.setObjectName("option-label")
# # #             checkbox_widget = QWidget()
# # #             checkbox_widget.setObjectName("custom-checkbox")
# # #             self.focus_checkboxes.append(checkbox_widget)
# # #             item_layout.addWidget(checkbox_widget)
# # #             item_layout.addWidget(checkbox)
# # #             item_widget.setLayout(item_layout)
# # #             focus_options_layout.addWidget(item_widget)
# # #         focus_options_widget.setLayout(focus_options_layout)
# # #         focus_type_container_layout.addWidget(focus_options_widget)
# # #         focus_type_container.setLayout(focus_type_container_layout)

# # #         # Port Type
# # #         port_type_container = QWidget()
# # #         port_type_container_layout = QVBoxLayout()
# # #         port_type_header = QLabel("Port Type")
# # #         port_type_header.setObjectName("options-header")
# # #         port_type_container_layout.addWidget(port_type_header)
# # #         port_options_widget = QWidget()
# # #         port_options_layout = QVBoxLayout()
# # #         port_options_layout.setSpacing(8)
# # #         port_types = ["Constant", "Lecture"]
# # #         self.port_checkboxes = []
# # #         for port in port_types:
# # #             item_widget = QWidget()
# # #             item_layout = QHBoxLayout()
# # #             checkbox = QCheckBox(port)
# # #             checkbox.setObjectName("option-label")
# # #             checkbox_widget = QWidget()
# # #             checkbox_widget.setObjectName("custom-checkbox")
# # #             self.port_checkboxes.append(checkbox_widget)
# # #             item_layout.addWidget(checkbox_widget)
# # #             item_layout.addWidget(checkbox)
# # #             item_widget.setLayout(item_layout)
# # #             port_options_layout.addWidget(item_widget)
# # #         port_options_widget.setLayout(port_options_layout)
# # #         port_type_container_layout.addWidget(port_options_widget)
# # #         port_type_container.setLayout(port_type_container_layout)

# # #         # Index Type
# # #         index_type_container = QWidget()
# # #         index_type_container_layout = QVBoxLayout()
# # #         index_type_header = QLabel("Index Type")
# # #         index_type_header.setObjectName("options-header")
# # #         index_type_container_layout.addWidget(index_type_header)
# # #         index_options_widget = QWidget()
# # #         index_options_layout = QVBoxLayout()
# # #         index_options_layout.setSpacing(8)
# # #         index_types = ["Normal", "Fort indice"]
# # #         self.index_checkboxes = []
# # #         for index in index_types:
# # #             item_widget = QWidget()
# # #             item_layout = QHBoxLayout()
# # #             checkbox = QCheckBox(index)
# # #             checkbox.setObjectName("option-label")
# # #             checkbox_widget = QWidget()
# # #             checkbox_widget.setObjectName("custom-checkbox")
# # #             self.index_checkboxes.append(checkbox_widget)
# # #             item_layout.addWidget(checkbox_widget)
# # #             item_layout.addWidget(checkbox)
# # #             item_widget.setLayout(item_layout)
# # #             index_options_layout.addWidget(item_widget)
# # #         index_options_widget.setLayout(index_options_layout)
# # #         index_type_container_layout.addWidget(index_options_widget)
# # #         index_type_container.setLayout(index_type_container_layout)

# # #         options_grid_2 = QWidget()
# # #         options_grid_2.setObjectName("options-grid")
# # #         options_grid_2_layout = QGridLayout(options_grid_2)
# # #         options_grid_2_layout.addWidget(focus_type_container, 0, 0)
# # #         options_grid_2_layout.addWidget(port_type_container, 0, 1)
# # #         options_grid_2_layout.addWidget(index_type_container, 0, 2)

# # #         main_layout = QVBoxLayout(container)
# # #         # Add the header widget (which contains the header layout)
# # #         header_container = QWidget()
# # #         header_container.setLayout(header_layout)
# # #         main_layout.addWidget(header_container)
# # #         main_layout.addWidget(table_container)
# # #         main_layout.addWidget(options_grid)
# # #         main_layout.addWidget(options_grid_2)

# # #         layout = QVBoxLayout(self)
# # #         layout.addWidget(container)

# # # if __name__ == '__main__':
# # #     app = QApplication(sys.argv)
# # #     optical_prescription = OpticalPrescriptionWidget()
# # #     optical_prescription.show()
# # #     sys.exit(app.exec())

# # from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QPushButton, QLabel
# # from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem, QCheckBox

# # from PyQt6.QtGui import QFont, QColor
# # import sys

# # class FormActionsWidget(QWidget):
# #     def __init__(self):
# #         super().__init__()

# #         self.setStyleSheet("""
# #             .actions-container {
# #                 display: flex;
# #                 align-items: center;
# #                 justify-content: space-between;
# #                 margin-top: 24px; /* mt-6 */
# #             }

# #             .button-group {
# #                 display: flex;
# #                 gap: 12px; /* space-x-3 (3 * 0.25rem = 0.75rem = 12px approx.) */
# #             }

# #             /* Base button styles */
# #             .form-button {
# #                 padding: 8px 16px; /* px-4 py-2 */
# #                 border-radius: 4px; /* rounded-button */
# #                 font-size: 0.875em; /* text-sm */
# #                 font-weight: 500; /* font-medium */
# #                 white-space: nowrap;
# #                 border: none;
# #             }

# #             /* Save Draft and Preview buttons */
# #             .secondary-button {
# #                 background-color: #e5e7eb; /* bg-gray-200 */
# #                 color: #4a5568; /* text-gray-700 */
# #             }

# #             .secondary-button:hover {
# #                 background-color: #d1d5db; /* hover:bg-gray-300 */
# #             }

# #             /* Clear Form button */
# #             .clear-button {
# #                 background-color: #f7fafc; /* bg-gray-100 */
# #                 color: #4a5568; /* text-gray-700 */
# #             }

# #             .clear-button:hover {
# #                 background-color: #edf2f7; /* hover:bg-gray-200 */
# #             }

# #             /* Submit & Print button */
# #             .primary-button {
# #                 background-color: QColor(0, 123, 255); /* bg-primary */
# #                 color: white; /* text-white */
# #             }

# #             .primary-button:hover {
# #                 background-color: QColor(0, 103, 207); /* hover:bg-blue-600 */
# #             }

# #             /* Icon (i) - Requires custom icon rendering or a font icon library */
# #             .button-icon {
# #                 margin-right: 4px; /* mr-1 */
# #             }
# #         """)

# #         # Create widgets
# #         actions_container = QWidget()
# #         actions_container.setObjectName("actions-container")
# #         actions_layout = QHBoxLayout(actions_container)
# #         actions_layout.setContentsMargins(0, 0, 0, 0) # Remove default margins

# #         # Left button group
# #         left_button_group = QWidget()
# #         left_button_layout = QHBoxLayout(left_button_group)
# #         left_button_layout.setSpacing(12) # space-x-3
# #         left_button_layout.setContentsMargins(0, 0, 0, 0)

# #         save_draft_button = QPushButton("Save Draft")
# #         save_draft_button.setObjectName("secondary-button form-button")
# #         save_draft_icon = QLabel("\uf0c7") # Placeholder for save icon
# #         save_draft_icon.setObjectName("button-icon")
# #         save_draft_layout = QHBoxLayout()
# #         save_draft_layout.addWidget(save_draft_icon)
# #         save_draft_layout.addWidget(save_draft_button)
# #         save_draft_button_container = QWidget()
# #         save_draft_button_container.setLayout(save_draft_layout)
# #         left_button_layout.addWidget(save_draft_button_container)

# #         preview_button = QPushButton("Preview")
# #         preview_button.setObjectName("secondary-button form-button")
# #         preview_icon = QLabel("\uf06e") # Placeholder for eye icon
# #         preview_icon.setObjectName("button-icon")
# #         preview_layout = QHBoxLayout()
# #         preview_layout.addWidget(preview_icon)
# #         preview_layout.addWidget(preview_button)
# #         preview_button_container = QWidget()
# #         preview_button_container.setLayout(preview_layout)
# #         left_button_layout.addWidget(preview_button_container)

# #         actions_layout.addWidget(left_button_group)

# #         # Right button group
# #         right_button_group = QWidget()
# #         right_button_layout = QHBoxLayout(right_button_group)
# #         right_button_layout.setSpacing(12) # space-x-3
# #         right_button_layout.setContentsMargins(0, 0, 0, 0)

# #         clear_form_button = QPushButton("Clear Form")
# #         clear_form_button.setObjectName("clear-button form-button")
# #         clear_form_icon = QLabel("\uf01e") # Placeholder for refresh icon
# #         clear_form_icon.setObjectName("button-icon")
# #         clear_form_layout = QHBoxLayout()
# #         clear_form_layout.addWidget(clear_form_icon)
# #         clear_form_layout.addWidget(clear_form_button)
# #         clear_form_button_container = QWidget()
# #         clear_form_button_container.setLayout(clear_form_layout)
# #         right_button_layout.addWidget(clear_form_button_container)

# #         submit_print_button = QPushButton("Submit & Print")
# #         submit_print_button.setObjectName("primary-button form-button")
# #         submit_print_icon = QLabel("\uf02f") # Placeholder for printer icon
# #         submit_print_icon.setObjectName("button-icon")
# #         submit_print_layout = QHBoxLayout()
# #         submit_print_layout.addWidget(submit_print_icon)
# #         submit_print_layout.addWidget(submit_print_button)
# #         submit_print_button_container = QWidget()
# #         submit_print_button_container.setLayout(submit_print_layout)
# #         right_button_layout.addWidget(submit_print_button_container)

# #         actions_layout.addWidget(right_button_group)

# #         layout = QVBoxLayout(self)
# #         layout.addWidget(actions_container)

# # if __name__ == '__main__':
# #     app = QApplication(sys.argv)
# #     actions = FormActionsWidget()
# #     actions.show()
# #     sys.exit(app.exec())



# dashboard.py
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QFont, QAction
from PySide6.QtWidgets import (
    QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QFrame, QSizePolicy, QButtonGroup, QSpacerItem,
    QGraphicsDropShadowEffect
)
import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from PySide6.QtCore import Qt

# ---- Theme (Dark Mode Professional) ----
THEME = {
    "bg": "#1E1E2F",
    "bg_alt": "#222236",
    "card": "#2A2A40",
    "border": "#343454",
    "text": "#E5E7EB",
    "text_dim": "#C7CBD1",
    "muted": "#9AA0A6",
    "primary": "#3B82F6",   # Blue
    "success": "#10B981",   # Emerald
    "warning": "#F59E0B",   # Amber
    "danger": "#EF4444",    # Red
    "highlight": "#334155"  # Active/hover background tint
}

FONT_FAMILY = "Segoe UI, Inter, Roboto, Arial"
BASE_SPACING = 8  # 8px system


# def apply_shadow(widget, radius=18, opacity=0.25, y_offset=6):
#     shadow = QGraphicsDropShadowEffect()
#     shadow.setBlurRadius(radius)
#     shadow.setColor(Qt.black)
#     shadow.setOffset(0, y_offset)
#     shadow.setEnabled(True)
    # shadow.setOpacity(opacity)
    # widget.setGraphicsEffect(shadow)


def apply_shadow(widget, radius=18, opacity=0.25, y_offset=6):
    shadow = QGraphicsDropShadowEffect()
    shadow.setBlurRadius(radius)
    # Encode opacity in the color's alpha channel
    col = QColor(0, 0, 0)
    col.setAlphaF(max(0.0, min(1.0, opacity)))  # 0.0–1.0
    shadow.setColor(col)
    shadow.setOffset(0, y_offset)
    widget.setGraphicsEffect(shadow)    


class SidebarButton(QPushButton):
    def __init__(self, text, icon_char="•", parent=None):
        super().__init__(parent)
        self.setCheckable(True)
        self.setCursor(Qt.PointingHandCursor)
        self.setText(f"  {icon_char}  {text}")
        self.setMinimumHeight(40)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.setObjectName("SidebarButton")


class StatCard(QFrame):
    def __init__(self, title, value, subtitle="", accent=THEME["primary"], icon_char="•", parent=None):
        super().__init__(parent)
        self.accent = accent
        self.icon_char = icon_char
        self.setObjectName("StatCard")
        self.setStyleSheet(f"""
            QFrame#StatCard {{
                background-color: {THEME['card']};
                border: 1px solid {THEME['border']};
                border-radius: 12px;
            }}
        """)
        apply_shadow(self, radius=28, opacity=0.2, y_offset=10)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(16, 16, 16, 16)
        lay.setSpacing(8)

        # Top row: icon + title
        top = QHBoxLayout()
        top.setSpacing(8)

        icon = QLabel(self.icon_char)
        icon.setObjectName("CardIcon")
        icon.setFixedSize(28, 28)
        icon.setAlignment(Qt.AlignCenter)
        icon.setStyleSheet(f"""
            QLabel#CardIcon {{
                color: {THEME['text']};
                background-color: {self.accent}22;
                border: 1px solid {self.accent}55;
                border-radius: 6px;
                font-size: 16px;
            }}
        """)

        title_lbl = QLabel(title)
        title_lbl.setStyleSheet(f"color: {THEME['text_dim']};")
        title_font = QFont()
        title_font.setPointSize(12)
        title_font.setFamily(FONT_FAMILY)
        title_font.setWeight(QFont.Medium)
        title_lbl.setFont(title_font)

        top.addWidget(icon)
        top.addWidget(title_lbl, 1)
        top.addStretch(1)

        # Value
        value_lbl = QLabel(value)
        value_font = QFont()
        value_font.setFamily(FONT_FAMILY)
        value_font.setPointSize(28)
        value_font.setWeight(QFont.DemiBold)
        value_lbl.setFont(value_font)
        value_lbl.setStyleSheet(f"color: {THEME['text']};")

        # Subtitle
        subtitle_lbl = QLabel(subtitle)
        subtitle_lbl.setStyleSheet(f"color: {THEME['muted']};")
        subtitle_font = QFont()
        subtitle_font.setFamily(FONT_FAMILY)
        subtitle_font.setPointSize(12)
        subtitle_lbl.setFont(subtitle_font)

        lay.addLayout(top)
        lay.addSpacing(4)
        lay.addWidget(value_lbl)
        lay.addWidget(subtitle_lbl)
        lay.addStretch(1)


class Header(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Header")
        self.setStyleSheet(f"""
            QFrame#Header {{
                background-color: {THEME['bg_alt']};
                border-bottom: 1px solid {THEME['border']};
            }}
        """)
        lay = QHBoxLayout(self)
        lay.setContentsMargins(16, 10, 16, 10)
        lay.setSpacing(12)

        # App Title
        title = QLabel("Optics Dashboard")
        title_font = QFont()
        title_font.setFamily(FONT_FAMILY)
        title_font.setPointSize(18)
        title_font.setWeight(QFont.DemiBold)
        title.setFont(title_font)
        title.setStyleSheet(f"color: {THEME['text']};")

        # Search
        search = QLineEdit()
        search.setPlaceholderText("Search patients, sales, appointments…")
        search.setClearButtonEnabled(True)
        search.setObjectName("Search")
        search.setMinimumWidth(320)
        search.setStyleSheet(f"""
            QLineEdit#Search {{
                background: {THEME['bg']};
                color: {THEME['text']};
                border: 1px solid {THEME['border']};
                border-radius: 8px;
                padding: 8px 12px;
                selection-background-color: {THEME['primary']}AA;
            }}
            QLineEdit#Search:hover {{
                border-color: {THEME['primary']}66;
            }}
            QLineEdit#Search:focus {{
                border-color: {THEME['primary']};
            }}
        """)

        # Spacer
        spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        # Profile button
        profile = QPushButton("Tata")
        profile.setCursor(Qt.PointingHandCursor)
        profile.setObjectName("Profile")
        profile.setMinimumHeight(34)
        profile.setStyleSheet(f"""
            QPushButton#Profile {{
                color: {THEME['text']};
                background: {THEME['bg']};
                border: 1px solid {THEME['border']};
                border-radius: 8px;
                padding: 6px 12px;
            }}
            QPushButton#Profile:hover {{
                background: {THEME['highlight']};
                border-color: {THEME['primary']}66;
            }}
        """)

        lay.addWidget(title)
        lay.addSpacing(8)
        lay.addWidget(search)
        lay.addItem(spacer)
        lay.addWidget(profile)


class Sidebar(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Sidebar")
        self.setFixedWidth(220)
        self.setStyleSheet(f"""
            QFrame#Sidebar {{
                background-color: {THEME['bg_alt']};
                border-right: 1px solid {THEME['border']};
            }}
            QPushButton#SidebarButton {{
                color: {THEME['text']};
                background-color: transparent;
                border: none;
                border-radius: 8px;
                padding: 8px 10px;
                text-align: left;
                font-size: 14px;
            }}
            QPushButton#SidebarButton:hover {{
                background-color: {THEME['highlight']};
            }}
            QPushButton#SidebarButton:checked {{
                background-color: {THEME['primary']}22;
                border: 1px solid {THEME['primary']}55;
            }}
        """)

        lay = QVBoxLayout(self)
        lay.setContentsMargins(12, 16, 12, 16)
        lay.setSpacing(6)

        brand = QLabel("OptiCare")
        brand_font = QFont()
        brand_font.setFamily(FONT_FAMILY)
        brand_font.setPointSize(16)
        brand_font.setWeight(QFont.DemiBold)
        brand.setFont(brand_font)
        brand.setStyleSheet(f"color: {THEME['text']};")

        muted = QLabel("v1.0")
        muted.setStyleSheet(f"color: {THEME['muted']}; font-size: 12px;")

        header_box = QVBoxLayout()
        header_box.setSpacing(2)
        header_box.addWidget(brand)
        header_box.addWidget(muted)

        lay.addLayout(header_box)
        lay.addSpacing(12)

        self.group = QButtonGroup(self)
        self.group.setExclusive(True)

        # Menu
        self.btn_home = SidebarButton("Home", "🏠")
        self.btn_patients = SidebarButton("Patients", "👤")
        self.btn_sales = SidebarButton("Sales", "🛒")
        self.btn_appts = SidebarButton("Appointments", "📅")
        self.btn_settings = SidebarButton("Settings", "⚙️")

        for i, b in enumerate([self.btn_home, self.btn_patients, self.btn_sales, self.btn_appts, self.btn_settings]):
            lay.addWidget(b)
            self.group.addButton(b, i)

        lay.addStretch(1)

        # CTA
        cta = QPushButton("➕ New patient")
        cta.setCursor(Qt.PointingHandCursor)
        cta.setMinimumHeight(40)
        cta.setObjectName("CTA")
        cta.setStyleSheet(f"""
            QPushButton#CTA {{
                color: {THEME['bg']};
                background-color: {THEME['success']};
                border: none;
                border-radius: 8px;
                font-weight: 600;
            }}
            QPushButton#CTA:hover {{
                background-color: #0AA173;
            }}
        """)
        lay.addWidget(cta)

        self.btn_home.setChecked(True)


class DashboardView(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("DashboardView")
        self.setStyleSheet(f"background-color: {THEME['bg']};")
        outer = QVBoxLayout(self)
        outer.setContentsMargins(16, 16, 16, 16)
        outer.setSpacing(16)

        # Row 1: stat cards
        row1 = QHBoxLayout()
        row1.setSpacing(16)

        card_patients = StatCard(
            title="Patients", value="20", subtitle="Total registered",
            accent=THEME["primary"], icon_char="👤"
        )
        card_sales = StatCard(
            title="Sales", value="150", subtitle="Sales count",
            accent=THEME["success"], icon_char="🛒"
        )
        card_appts = StatCard(
            title="Appointments", value="20", subtitle="Scheduled today",
            accent=THEME["warning"], icon_char="📅"
        )
        card_new = StatCard(
            title="New Patient", value="Loading…", subtitle="Preparing form",
            accent=THEME["primary"], icon_char="➕"
        )

        # Make them expand evenly
        for c in [card_patients, card_sales, card_appts, card_new]:
            c.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
            row1.addWidget(c)

        outer.addLayout(row1)

        # Row 2: placeholder panels (e.g., charts, lists)
        row2 = QHBoxLayout()
        row2.setSpacing(16)

        panel_left = self._panel("Today’s appointments", "No-shows, new bookings, follow-ups")
        panel_right = self._panel("Recent activity", "Sales updates, new registrations")

        row2.addWidget(panel_left, 2)
        row2.addWidget(panel_right, 3)
        outer.addLayout(row2)

    def _panel(self, title, subtitle):
        panel = QFrame()
        panel.setObjectName("Panel")
        panel.setStyleSheet(f"""
            QFrame#Panel {{
                background-color: {THEME['card']};
                border: 1px solid {THEME['border']};
                border-radius: 12px;
            }}
        """)
        apply_shadow(panel, radius=24, opacity=0.18, y_offset=10)

        v = QVBoxLayout(panel)
        v.setContentsMargins(16, 16, 16, 16)
        v.setSpacing(8)

        title_lbl = QLabel(title)
        tf = QFont()
        tf.setFamily(FONT_FAMILY)
        tf.setPointSize(14)
        tf.setWeight(QFont.DemiBold)
        title_lbl.setFont(tf)
        title_lbl.setStyleSheet(f"color: {THEME['text']};")

        subtitle_lbl = QLabel(subtitle)
        sf = QFont()
        sf.setFamily(FONT_FAMILY)
        sf.setPointSize(12)
        subtitle_lbl.setFont(sf)
        subtitle_lbl.setStyleSheet(f"color: {THEME['muted']};")

        placeholder = QFrame()
        placeholder.setFixedHeight(180)
        placeholder.setStyleSheet(f"""
            background-color: {THEME['bg']};
            border: 1px dashed {THEME['border']};
            border-radius: 10px;
        """)

        v.addWidget(title_lbl)
        v.addWidget(subtitle_lbl)
        v.addSpacing(4)
        v.addWidget(placeholder)
        v.addStretch(1)
        return panel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Optics Dashboard")
        self.resize(1200, 760)
        central = QWidget()
        self.setCentralWidget(central)

        # Global stylesheet (scrollbars, tooltips, etc.)
        self.setStyleSheet(f"""
            QToolTip {{
                background-color: {THEME['card']};
                color: {THEME['text']};
                border: 1px solid {THEME['border']};
            }}
            QScrollBar:vertical {{
                background: {THEME['bg_alt']};
                width: 10px;
                margin: 0px;
            }}
            QScrollBar::handle:vertical {{
                background: {THEME['border']};
                min-height: 24px;
                border-radius: 5px;
            }}
            QScrollBar::handle:vertical:hover {{
                background: {THEME['primary']};
            }}
        """)

        root = QVBoxLayout(central)
        root.setContentsMargins(0, 0, 0, 0)
        root.setSpacing(0)

        # Header
        self.header = Header()
        root.addWidget(self.header)

        # Body: sidebar + content
        body = QHBoxLayout()
        body.setContentsMargins(0, 0, 0, 0)
        body.setSpacing(0)

        self.sidebar = Sidebar()
        self.dashboard = DashboardView()

        body.addWidget(self.sidebar)
        body.addWidget(self.dashboard, 1)
        root.addLayout(body)

        # Actions (optional)
        self._create_actions()

        # Connect sidebar to content switching (placeholder behavior)
        self.sidebar.group.idClicked.connect(self.on_nav_clicked)

    def _create_actions(self):
        self.act_quit = QAction("Quit", self)
        self.act_quit.triggered.connect(QApplication.instance().quit)
        self.addAction(self.act_quit)

    def on_nav_clicked(self, idx):
        # Placeholder: in a real app, swap stacked widgets here.
        # Provide a subtle visual cue by updating header title.
        titles = ["Home", "Patients", "Sales", "Appointments", "Settings"]
        new_title = f"Optics Dashboard · {titles[idx]}"
        self.header.findChild(QLabel).setText(new_title)


def main():
    app = QApplication(sys.argv)
    # High-DPI friendly text
    app.setApplicationDisplayName("Optics Dashboard")
    win = MainWindow()
    win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
    
    
# # optics_dashboard.py
# import sys
# from PySide6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, QParallelAnimationGroup
# from PySide6.QtGui import QFont, QColor, QAction
# from PySide6.QtWidgets import (
#     QApplication, QWidget, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel,
#     QLineEdit, QPushButton, QFrame, QSizePolicy, QButtonGroup, QSpacerItem,
#     QGraphicsDropShadowEffect
# )

# # ---- Theme ----
# THEME = {
#     "bg": "#1E1E2F",
#     "bg_alt": "#222236",
#     "card": "#2A2A40",
#     "border": "#343454",
#     "text": "#E5E7EB",
#     "text_dim": "#C7CBD1",
#     "muted": "#9AA0A6",
#     "primary": "#3B82F6",
#     "success": "#10B981",
#     "warning": "#F59E0B",
#     "highlight": "#334155"
# }
# FONT_FAMILY = "Segoe UI, Inter, Roboto, Arial"


# def apply_shadow(widget, radius=18, opacity=0.25, y_offset=6):
#     shadow = QGraphicsDropShadowEffect()
#     shadow.setBlurRadius(radius)
#     col = QColor(0, 0, 0)
#     col.setAlphaF(opacity)
#     shadow.setColor(col)
#     shadow.setOffset(0, y_offset)
#     widget.setGraphicsEffect(shadow)


# class SidebarButton(QPushButton):
#     def __init__(self, text, icon_char="•", parent=None):
#         super().__init__(parent)
#         self.setCheckable(True)
#         self.setCursor(Qt.PointingHandCursor)
#         self.icon_char = icon_char
#         self.full_text = f"  {icon_char}  {text}"
#         self.setText(self.full_text)
#         self.setMinimumHeight(40)
#         self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#         self.setObjectName("SidebarButton")


# class StatCard(QFrame):
#     def __init__(self, title, value, subtitle="", accent=THEME["primary"], icon_char="•", parent=None):
#         super().__init__(parent)
#         self.setObjectName("StatCard")
#         self.setStyleSheet(f"""
#             QFrame#StatCard {{
#                 background-color: {THEME['card']};
#                 border: 1px solid {THEME['border']};
#                 border-radius: 12px;
#             }}
#         """)
#         apply_shadow(self, radius=28, opacity=0.2, y_offset=10)

#         lay = QVBoxLayout(self)
#         lay.setContentsMargins(16, 16, 16, 16)
#         lay.setSpacing(8)

#         top = QHBoxLayout()
#         top.setSpacing(8)

#         icon = QLabel(icon_char)
#         icon.setFixedSize(28, 28)
#         icon.setAlignment(Qt.AlignCenter)
#         icon.setStyleSheet(f"""
#             color: {THEME['text']};
#             background-color: {accent}22;
#             border: 1px solid {accent}55;
#             border-radius: 6px;
#             font-size: 16px;
#         """)

#         title_lbl = QLabel(title)
#         title_lbl.setStyleSheet(f"color: {THEME['text_dim']};")
#         title_font = QFont(FONT_FAMILY, 12, QFont.Medium)
#         title_lbl.setFont(title_font)

#         top.addWidget(icon)
#         top.addWidget(title_lbl, 1)
#         top.addStretch(1)

#         value_lbl = QLabel(value)
#         value_lbl.setFont(QFont(FONT_FAMILY, 28, QFont.DemiBold))
#         value_lbl.setStyleSheet(f"color: {THEME['text']};")

#         subtitle_lbl = QLabel(subtitle)
#         subtitle_lbl.setFont(QFont(FONT_FAMILY, 12))
#         subtitle_lbl.setStyleSheet(f"color: {THEME['muted']};")

#         lay.addLayout(top)
#         lay.addWidget(value_lbl)
#         lay.addWidget(subtitle_lbl)
#         lay.addStretch(1)


# class Header(QFrame):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setStyleSheet(f"""
#             QFrame {{
#                 background-color: {THEME['bg_alt']};
#                 border-bottom: 1px solid {THEME['border']};
#             }}
#         """)
#         lay = QHBoxLayout(self)
#         lay.setContentsMargins(16, 10, 16, 10)
#         lay.setSpacing(12)

#         # Sidebar toggle button
#         self.toggle_btn = QPushButton("☰")
#         self.toggle_btn.setFixedSize(34, 34)
#         self.toggle_btn.setCursor(Qt.PointingHandCursor)
#         self.toggle_btn.setStyleSheet(f"""
#             QPushButton {{
#                 color: {THEME['text']};
#                 background: {THEME['bg']};
#                 border: 1px solid {THEME['border']};
#                 border-radius: 6px;
#             }}
#             QPushButton:hover {{
#                 background: {THEME['highlight']};
#             }}
#         """)

#         title = QLabel("Optics Dashboard")
#         title.setFont(QFont(FONT_FAMILY, 18, QFont.DemiBold))
#         title.setStyleSheet(f"color: {THEME['text']};")

#         search = QLineEdit()
#         search.setPlaceholderText("Search...")
#         search.setClearButtonEnabled(True)
#         search.setMinimumWidth(280)
#         search.setStyleSheet(f"""
#             QLineEdit {{
#                 background: {THEME['bg']};
#                 color: {THEME['text']};
#                 border: 1px solid {THEME['border']};
#                 border-radius: 8px;
#                 padding: 6px 10px;
#             }}
#             QLineEdit:focus {{
#                 border-color: {THEME['primary']};
#             }}
#         """)

#         spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

#         profile = QPushButton("Tata")
#         profile.setCursor(Qt.PointingHandCursor)
#         profile.setStyleSheet(f"""
#             QPushButton {{
#                 color: {THEME['text']};
#                 background: {THEME['bg']};
#                 border: 1px solid {THEME['border']};
#                 border-radius: 8px;
#                 padding: 6px 12px;
#             }}
#             QPushButton:hover {{
#                 background: {THEME['highlight']};
#             }}
#         """)

#         lay.addWidget(self.toggle_btn)
#         lay.addWidget(title)
#         lay.addWidget(search)
#         lay.addItem(spacer)
#         lay.addWidget(profile)


# class Sidebar(QFrame):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.expanded = True
#         self.full_width = 220
#         self.collapsed_width = 60
#         self.setFixedWidth(self.full_width)
#         self.setStyleSheet(f"""
#             QFrame {{
#                 background-color: {THEME['bg_alt']};
#                 border-right: 1px solid {THEME['border']};
#             }}
#             QPushButton#SidebarButton {{
#                 color: {THEME['text']};
#                 background-color: transparent;
#                 border: none;
#                 border-radius: 8px;
#                 padding: 8px 10px;
#                 text-align: left;
#                 font-size: 14px;
#             }}
#             QPushButton#SidebarButton:hover {{
#                 background-color: {THEME['highlight']};
#             }}
#             QPushButton#SidebarButton:checked {{
#                 background-color: {THEME['primary']}22;
#                 border: 1px solid {THEME['primary']}55;
#             }}
#         """)

#         lay = QVBoxLayout(self)
#         lay.setContentsMargins(12, 16, 12, 16)
#         lay.setSpacing(6)

#         self.group = QButtonGroup(self)
#         self.group.setExclusive(True)

#         self.btn_home = SidebarButton("Home", "🏠")
#         self.btn_patients = SidebarButton("Patients", "👤")
#         self.btn_sales = SidebarButton("Sales", "🛒")
#         self.btn_appts = SidebarButton("Appointments", "📅")
#         self.btn_settings = SidebarButton("Settings", "⚙️")

#         for i, b in enumerate([self.btn_home, self.btn_patients, self.btn_sales, self.btn_appts, self.btn_settings]):
#             lay.addWidget(b)
#             self.group.addButton(b, i)

#         lay.addStretch(1)

#         cta = QPushButton("➕ New patient")
#         cta.setMinimumHeight(40)
#         cta.setStyleSheet(f"""
#             QPushButton {{
#                 color: {THEME['bg']};
#                 background-color: {THEME['success']};
#                 border: none;
#                 border-radius: 8px;
#                 font-weight: 600;
#             }}
#             QPushButton:hover {{
#                 background-color: #0AA173;
#             }}
#         """)
#         lay.addWidget(cta)

#         self.btn_home.setChecked(True)

#     def toggle(self):
#         self.expanded = not self.expanded
#         start = self.width()
#         end = self.full_width if self.expanded else self.collapsed_width

#         anim = QPropertyAnimation(self, b"minimumWidth")
#         anim.setDuration(300)
#         anim.setStartValue(start)
#         anim.setEndValue(end)
#         anim.setEasingCurve(QEasingCurve.InOutCubic)
#         anim.start()
#         self._anim = anim  # keep reference

#         # Update button labels
#         for btn in self.findChildren(SidebarButton):
#             if self.expanded:
#                 btn.setText(btn.full_text)
#                 btn.setToolTip("")
#             else:
#                 btn.setText(btn.icon_char)
#                 btn.setToolTip(btn.full_text)


# class DashboardView(QWidget):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setStyleSheet(f"background-color: {THEME['bg']};")
#         outer = QVBoxLayout(self)
#         outer.setContentsMargins(16, 16, 16, 16)
#         outer.setSpacing(16)

#         # Stat cards row
#         row1 = QHBoxLayout()
#         row1.setSpacing(16)

#         self.cards = [
#             StatCard("Patients", "20", "Total registered", THEME["primary"], "👤"),
#             StatCard("Sales", "150", "Sales count", THEME["success"], "🛒"),
#             StatCard("Appointments", "20", "Scheduled today", THEME["warning"], "📅"),
#             StatCard("New Patient", "Loading…", "Preparing form", THEME["primary"], "➕"),
#         ]

#         for c in self.cards:
#             c.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
#             c.setWindowOpacity(0)  # start invisible for animation
#             row1.addWidget(c)

#         outer.addLayout(row1)
#         self.animate_cards()

#     def animate_cards(self):
#         group = QParallelAnimationGroup()
#         for i, card in enumerate(self.cards):
#             anim = QPropertyAnimation(card, b"windowOpacity")
#             anim.setDuration(500)
#             anim.setStartValue(0)
#             anim.setEndValue(1)
#             anim.setEasingCurve(QEasingCurve.OutCubic)
#             # anim.setDelay(i * 120)  # stagger
#             group.addAnimation(anim)
#         group.start()
#         self._anim_group = group


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setWindowTitle("Optics Dashboard")
#         self.resize(1200, 760)
#         central = QWidget()
#         self.setCentralWidget(central)

#         root = QVBoxLayout(central)
#         root.setContentsMargins(0, 0, 0, 0)
#         root.setSpacing(0)

#         # Header
#         self.header = Header()
#         root.addWidget(self.header)

#         # Body
#         body = QHBoxLayout()
#         body.setContentsMargins(0, 0, 0, 0)
#         body.setSpacing(0)

#         self.sidebar = Sidebar()
#         self.dashboard = DashboardView()

#         body.addWidget(self.sidebar)
#         body.addWidget(self.dashboard, 1)
#         root.addLayout(body)

#         # Connect toggle button
#         self.header.toggle_btn.clicked.connect(self.sidebar.toggle)

#         # Quit action
#         self.act_quit = QAction("Quit", self)
#         self.act_quit.triggered.connect(QApplication.instance().quit)
#         self.addAction(self.act_quit)


# def main():
#     app = QApplication(sys.argv)
#     app.setApplicationDisplayName("Optics Dashboard")
#     win = MainWindow()
#     win.show()
#     sys.exit(app.exec())


# if __name__ == "__main__":
#     main()