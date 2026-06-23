import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import os
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QLabel,  QScrollArea, QVBoxLayout
from PySide6.QtCore import Slot
# from ui_ux.purchase_module.ui_purchase_board8 import Ui_Form  # Import the analyzed UI file ui_purchase_board1_ok.
from ui_ux.purchase_module.ui_purchase_board1_ok import Ui_Form 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A3
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Image
from PySide6.QtCore import Slot, Qt
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from PySide6.QtGui import QPainter, QFont, QRegion, QPageSize
import datetime  # Import datetime module
from PySide6.QtWidgets import QMenu, QToolButton
from PySide6.QtGui import QAction  # ✅ Corrected Import
from PySide6.QtWidgets import QDialog, QVBoxLayout, QLineEdit, QPushButton, QListWidget, QListWidgetItem
from PySide6.QtWidgets import QInputDialog, QTableWidget, QTableWidgetItem, QVBoxLayout, QDialog, QComboBox, QHeaderView

#BASE_URL = "http://127.0.0.1:8000/" 
from collections import defaultdict


from config_loader import BASE_URL
response = requests.get(f'{BASE_URL}')


from modules.sales_module.PaymentHistoryDialog import PaymentHistoryDialog
from PySide6.QtCore import QTimer
VAT_PERCENTAGE = 19.25  # VAT Percentage

LOW_STOCK_THRESHOLD = 5  # Set threshold for low stock alerts

class PurchaseBoardManager(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
        self.setup_connections()
        self.populate_category_combobox()  # Populate category combobox on startup
        self.populate_patient_combobox()
        self.cart = []
        self.last_transaction = None  # Initialize last transaction storage
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # Setup scroll area for category totals
        self.setup_scrollable_category_totals()
        # self.search_patient_action.triggered.connect(self.search_patient)
        # ✅ Initialize Timer for Real-Time Stock Updates
        self.stock_update_timer = QTimer(self)
        self.stock_update_timer.timeout.connect(self.refresh_stock_levels)
        self.stock_update_timer.start(10000)  # Refresh every 10 seconds

    def setup_scrollable_category_totals(self):
        """Make the category totals section scrollable."""
        self.scroll_area = QScrollArea(self.ui.frame_10)
        self.scroll_area.setWidgetResizable(True)

        self.category_totals_widget = QWidget()
        self.category_totals_layout = QVBoxLayout(self.category_totals_widget)
        self.scroll_area.setWidget(self.category_totals_widget)
        
    # Set stylesheet for the menu
        self.scroll_area.setStyleSheet("""
            QWidget {
                 /*background-color: rgb(88, 162, 157);  Background color of the menu */
                border: 2px solid #CCCCCC;  /* Border color of the menu */
                background-color: rgba(44, 47, 134, 200);
                color: rgb(255, 255, 255);
                border-radius: 5px;
                height: 70px;
                padding:10px;
            }
            QWidget::item {
                background-color: transparent;
                color: #FFFFFF;  /* Text color of the items */
                border-radius: 1px;  
                
            }
            QWidget::item:selected {
                background-color: #555555;  /* Background color of selected item */
                color: #ffffff;  /* Text color of selected item */
            }
        """)
        # Set layout for frame_10
        self.ui.frame_10.setLayout(QVBoxLayout())
        self.ui.frame_10.layout().addWidget(self.scroll_area)

    def setup_connections(self):
        """Connect signals to their respective slots."""
        self.ui.category.currentIndexChanged.connect(self.populate_item_type_combobox)  # Category selection
        self.ui.item_types.currentIndexChanged.connect(self.fetch_and_display_unit_price)  # Item type selection
        self.ui.patient_name.currentIndexChanged.connect(self.display_patient_details)
        self.ui.add_to_cart.clicked.connect(self.add_to_cart)
        self.ui.delete_from_cart.clicked.connect(self.remove_item_from_cart)
        self.ui.amount_given.textChanged.connect(self.calculate_change)
        self.ui.validate.clicked.connect(self.validate_transaction)
        self.ui.receipt_print.clicked.connect(self.print_receipt)
        self.ui.payment_history_button.clicked.connect(self.open_payment_history)

    def retranslate_ui(self):
        """
        Called when the app language changes.
        It re-applies the translated strings to this form.
        """
        self.ui.retranslateUi(self)         
        
    # 🔽 Setup dropdown menu for toolButton
        self.setup_toolButton_menu()
        
        
    @Slot()
    def open_payment_history(self):
        """Open the Payment History dialog."""
        self.payment_history_dialog = PaymentHistoryDialog(self)
        self.payment_history_dialog.exec()  # Open as modal dialog

    def setup_toolButton_menu(self):
        """Create a dropdown menu for the toolButton."""
        menu = QMenu(self)

    # Set stylesheet for the menu
        menu.setStyleSheet("""
            QMenu {
                background-color: rgb(88, 162, 157);  /* Background color of the menu */
                border: 2px solid #CCCCCC;  /* Border color of the menu */
                border-radius: 5px;
                height: 120;
                padding:10px;
            }
            QMenu::item {
                background-color: transparent;
                color: #FFFFFF;  /* Text color of the items */
                border-radius: 1px;  
                
            }
            QMenu::item:selected {
                background-color: #555555;  /* Background color of selected item */
                color: #ffffff;  /* Text color of selected item */
            }
        """)

        # Create actions
        search_patient_action = QAction("Search Patient", self)
        manual_patient_action = QAction("Manually Enter Patient Name", self)
        price_update_action = QAction("Item Price Update", self)

        # Connect actions to functions (implement these later)
        search_patient_action.triggered.connect(self.search_patient)
        manual_patient_action.triggered.connect(self.enter_patient_manually)
        price_update_action.triggered.connect(self.update_item_price)

        # Add actions to menu
        menu.addAction(search_patient_action)
        menu.addAction(manual_patient_action)
        menu.addAction(price_update_action)

        # Assign menu to toolButton
        self.ui.toolButton.setMenu(menu)
        
        # ✅ Set the button to show the menu instantly when clicked
        self.ui.toolButton.setPopupMode(QToolButton.InstantPopup)

    def populate_category_combobox(self):
        """Fetch and populate the category combobox from the backend."""
        try:
            response = requests.get(f"{BASE_URL}/categories/")
            if response.status_code == 200:
                categories = response.json()
                self.ui.category.clear()
                self.ui.category.addItem("Select Category", None)
                for category in categories:
                    self.ui.category.addItem(category["name"], category["id"])
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch categories: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    def populate_item_type_combobox(self):
        """Fetch and populate the item type combobox based on the selected category."""
        category_id = self.ui.category.currentData()
        if not category_id:
            self.ui.item_types.clear()
            self.ui.item_types.addItem("Select Item Type", None)
            return

        try:
            response = requests.get(f"{BASE_URL}/item-types/", params={"category_id": category_id})
            if response.status_code == 200:
                item_types = response.json().get("item_types", [])
                self.ui.item_types.clear()
                self.ui.item_types.addItem("Select Item Type", None)
                for item_type in item_types:
                    self.ui.item_types.addItem(item_type["name"], item_type)  # Store the entire item_type dict as data
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch item types: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
####################################################################
#refresh stock levels

    # @Slot()
    # def refresh_stock_levels(self):
    #     """Fetch and update stock levels dynamically every 10 seconds."""
    #     category_id = self.ui.category.currentData()
    #     selected_item = self.ui.item_types.currentData()

    #     if not category_id or not selected_item:
    #         return  # No category or item selected, nothing to update

    #     item_type_id = selected_item.get("id")

    #     try:
    #         response = requests.get(
    #             f"{BASE_URL}/get-stock-level/",
    #             params={"category_id": category_id, "item_type_id": item_type_id}
    #         )

    #         if response.status_code == 200:
    #             data = response.json()
    #             stock_level = data.get("stock_level", 0)  # Fetch latest stock level 

    #             # ✅ Update stock display
    #             self.ui.stock_level_display.setText(f"Stock: {stock_level} units")

    #             # ✅ Show low stock alert if needed
    #             if stock_level <= LOW_STOCK_THRESHOLD:
    #                 self.ui.stock_level_display.setStyleSheet("color: red; font-weight: bold;")
    #             else:
    #                 self.ui.stock_level_display.setStyleSheet("color: black;")
    #                 # self.ui.stock_level_display.setText(f"Stock: {stock_level} units") 
    #                 self.ui.stock_level_display.setText(self, "Low Stock Alert", f"STock level: Only [{stock_level}]  left in stock!")
    #         else:
    #             print("Failed to fetch stock updates:", response.json())

    #     except requests.RequestException as e:
    #         print("Network Error:", str(e))

    @Slot()
    def refresh_stock_levels(self):
        """Fetch and update stock levels dynamically every 10 seconds."""
        category_id = self.ui.category.currentData()
        selected_item = self.ui.item_types.currentData()

        # Assuming LOW_STOCK_THRESHOLD is defined, setting a sensible default
        LOW_STOCK_THRESHOLD = getattr(self, 'LOW_STOCK_THRESHOLD', 5) 

        if not category_id or not selected_item:
            self.ui.stock_level_display.setText("Stock: N/A")
            self.ui.stock_level_display.setStyleSheet("color: black; font-weight: normal;")
            return

        item_type_id = selected_item.get("id")

        try:
            response = requests.get(
                f"{BASE_URL}/get-stock-level/",
                params={"category_id": category_id, "item_type_id": item_type_id}
            )

            if response.status_code == 200:
                data = response.json()
                stock_level = data.get("stock_level", 0)

                # --- Core Logic Correction ---
                if stock_level <= LOW_STOCK_THRESHOLD:
                    # 1. Low Stock: Set style to RED and text to the ALERT message
                    self.ui.stock_level_display.setStyleSheet("color: red; font-weight: bold;")
                    self.ui.stock_level_display.setText(f"Low Stock Alert: Only [{stock_level}] left!")
                else:
                    # 2. Sufficient Stock: Set style to default and text to the STOCK count
                    self.ui.stock_level_display.setStyleSheet("color: black; font-weight: normal;")
                    self.ui.stock_level_display.setText(f"Stock: {stock_level} units")
                # -----------------------------
                    
            else:
                # Handle API failure
                print("Failed to fetch stock updates:", response.json())
                self.ui.stock_level_display.setText("Stock: Error")
                self.ui.stock_level_display.setStyleSheet("color: red; font-weight: normal;")

        except requests.RequestException as e:
            # Handle Network failure
            print("Network Error:", str(e))
            self.ui.stock_level_display.setText("Stock: Net Error")
            self.ui.stock_level_display.setStyleSheet("color: red; font-weight: normal;")

####################################################################
    @Slot()
    def fetch_and_display_unit_price(self):
        """Fetch and display the unit price and stock level of the selected item type."""
        category_id = self.ui.category.currentData()
        selected_item = self.ui.item_types.currentData()  # Get the entire dictionary

        if not category_id or not selected_item:
            self.ui.unit_price.clear()  # Clear the unit price field if no valid selection
            return

        item_type_id = selected_item.get("id")  # Extract the ID from the dictionary
        item_name = selected_item.get("name", "Unknown Item")  # Get the item name

        try:
            response = requests.get(
                f"{BASE_URL}/get-unit-price/",
                params={"category_id": category_id, "item_type_id": item_type_id}
                
            )
            if response.status_code == 200:
                data = response.json()
                
                unit_price = data.get("unit_price", 0.0)
                stock_level = data.get("stock_level", 0)  # Fetch stock level

                self.ui.unit_price.setText(f"{unit_price:,.2f} XAF")  # Update price field

                # ✅ Store unit price in item data
                selected_item["unit_price"] = unit_price
                selected_item["stock_level"] = stock_level  # ✅ Store stock level
                self.ui.item_types.setItemData(self.ui.item_types.currentIndex(), selected_item)

                # 🚨 Low Stock Warning
                if stock_level <= LOW_STOCK_THRESHOLD:
                    self.ui.unit_price.setStyleSheet("background-color: red; color: white; font-weight: bold;")
                    
                    QMessageBox.warning(self, "Low Stock Alert", f"⚠️⚠️ Warning: Only [{stock_level}] items of '{item_name}' left in stock!")
                else:
                    self.ui.unit_price.setStyleSheet("background-color: green; color: white; font-weight: bold;")  # Reset style if stock is okay
                    QMessageBox.warning(self, "Low Stock Alert", f"STock level: Only [{stock_level}] items of '{item_name}' left in stock!")
            else:
                error_message = response.json().get("error", "Failed to fetch unit price.")
                QMessageBox.warning(self, "Error", error_message)
        except requests.RequestException as e:   
            QMessageBox.critical(self, "Network Error", str(e))

    @Slot()
    def update_item_price(self):
        """Open a dialog to update the unit price of an item type for the selected category."""
        selected_category_id = self.ui.category.currentData()  # Get selected category ID

        if not selected_category_id:
            QMessageBox.warning(self, "Selection Error", "Please select a category first.")
            return

        # Create a dialog window
        self.price_dialog = QDialog(self)
        self.price_dialog.setWindowTitle("Update Item Price")
        self.price_dialog.setMinimumWidth(400)

        layout = QVBoxLayout(self.price_dialog)

        # Item Type Selection
        self.item_type_label = QLabel("Select Item Type:")
        self.item_type_combo = QComboBox()
        
        # Populate with item types of the selected category
        self.populate_item_types_for_dialog(selected_category_id)

        # New Price Input
        self.new_price_label = QLabel("Enter New Price (XAF):")
        self.new_price_input = QLineEdit()
        self.new_price_input.setPlaceholderText("Enter new price")

        # Buttons
        self.update_price_btn = QPushButton("Update Price")
        self.update_price_btn.clicked.connect(self.save_updated_price)

        self.cancel_btn = QPushButton("Cancel")
        self.cancel_btn.clicked.connect(self.price_dialog.close)

        # Add widgets to layout
        layout.addWidget(self.item_type_label)
        layout.addWidget(self.item_type_combo)
        layout.addWidget(self.new_price_label)
        layout.addWidget(self.new_price_input)
        layout.addWidget(self.update_price_btn)
        layout.addWidget(self.cancel_btn)

        self.price_dialog.setLayout(layout)
        self.price_dialog.exec()
        
    def populate_item_types_for_dialog(self, category_id):
        """Fetch and populate item types for the selected category in the dialog."""
        try:
            response = requests.get(f"{BASE_URL}/item-types/", params={"category_id": category_id})
            if response.status_code == 200:
                item_types = response.json().get("item_types", [])
                self.item_type_combo.clear()
                self.item_type_combo.addItem("Select Item Type", None)
                for item_type in item_types:
                    self.item_type_combo.addItem(item_type["name"], item_type)  # Store dict as data
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch item types: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    @Slot()
    def save_updated_price(self):
        """Send the updated price to the backend and refresh UI."""
        selected_item = self.item_type_combo.currentData()  # Get selected item
        new_price = self.new_price_input.text().strip()

        # Validate inputs
        if not selected_item:
            QMessageBox.warning(self, "Input Error", "Please select an item.")
            return

        if not new_price.replace('.', '', 1).isdigit() or float(new_price) <= 0:
            QMessageBox.warning(self, "Input Error", "Enter a valid price.")
            return

        item_type_id = selected_item["id"]  # Extract item ID
        new_price = float(new_price)

        # Send update request to backend
        try:
            response = requests.post(f"{BASE_URL}/update-item-price/", json={"item_type_id": item_type_id, "new_price": new_price})

            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item price updated successfully!")
                self.populate_item_types_for_dialog(self.ui.category.currentData())  # Refresh item types
                self.price_dialog.close()
            else:
                error_message = response.json().get("error", "Failed to update price.")
                QMessageBox.warning(self, "Error", error_message)

        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
    @Slot()
    def open_update_price_dialog(self):
        """Opens the update price dialog only when a category is selected."""
        if not self.ui.category.currentData():
            QMessageBox.warning(self, "Selection Error", "Please select a category first.")
            return
        self.update_item_price()

    def populate_patient_combobox(self):
            """Fetch and populate the patient_name combobox with patient names."""
            try:
                response = requests.get(f"{BASE_URL}/fetch-patients/")
                if response.status_code == 200:
                    patients = response.json().get('patients', [])
                    self.ui.patient_name.clear()
                    self.ui.patient_name.addItem("Select Patient", None)
                    for patient in patients:
                        self.ui.patient_name.addItem(patient['name'], patient)
                else:
                    QMessageBox.warning(self, "Error", f"Failed to fetch patients: {response.status_code}")
            except requests.RequestException as e:
                QMessageBox.critical(self, "Network Error", str(e))

    @Slot()
    def display_patient_details(self):
        """Display the selected patient's details in their respective widgets."""
        selected_patient = self.ui.patient_name.currentData()
        if not selected_patient:
            # Clear all fields if no valid patient is selected
            self.ui.p_contact.clear()
            self.ui.p_email.clear()
            self.ui.p_address.clear()
            # self.ui.p_profession.clear()
            self.ui.p_age.clear()
            self.ui.p_gender.clear()
            return

        # Display patient details
        self.ui.p_contact.setText(selected_patient.get('contact', ''))
        self.ui.p_email.setText(selected_patient.get('email', ''))
        self.ui.p_address.setText(selected_patient.get('address', ''))
        # self.ui.patient_profession.setText(selected_patient.get('profession', ''))
        self.ui.p_age.setText(str(selected_patient.get('age', '')))
        self.ui.p_gender.setText(selected_patient.get('gender', ''))
        
    @Slot()
    def search_patient(self):
        """Prompt user to enter a patient name and search for it in the database."""
        # Step 1: Get patient name from user input
        patient_name, ok = QInputDialog.getText(self, "Search Patient", "Enter patient name:")
        if not ok or not patient_name.strip():
            return  # User cancelled or entered empty name
        try:
            # Step 2: Request patient details from backend
            response = requests.get(f"{BASE_URL}/search-patient/", params={"name": patient_name.strip()})

            if response.status_code == 200:
                patients = response.json().get("patients", [])
                
                if not patients:
                    QMessageBox.information(self, "No Results", "No patient found with that name.")
                    return

                # Step 3: Display results in a table toolButton
                self.show_patient_results(patients)

            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch patient data: {response.status_code}")

        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
            
    def show_patient_results(self, patients):
        """Display patient search results in a QTableWidget inside a QDialog."""
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Search Results")
        self.dialog.resize(600, 400)

        layout = QVBoxLayout()
        self.table = QTableWidget(len(patients), 5)  # 5 columns: Name, Contact, Email, Address, Age
        self.table.setHorizontalHeaderLabels(["Name", "Contact", "Email", "Address", "Age"])

        self.patient_data = patients  # Store patients for easy reference

        for row, patient in enumerate(patients):
            self.table.setItem(row, 0, QTableWidgetItem(patient.get("name", "")))
            self.table.setItem(row, 1, QTableWidgetItem(patient.get("contact", "")))
            self.table.setItem(row, 2, QTableWidgetItem(patient.get("email", "")))
            self.table.setItem(row, 3, QTableWidgetItem(patient.get("address", "")))
            self.table.setItem(row, 4, QTableWidgetItem(str(patient.get("age", ""))))

        self.table.resizeColumnsToContents()

        # Connect double-click event
        self.table.itemDoubleClicked.connect(self.display_selected_patient)

        layout.addWidget(self.table)
        self.dialog.setLayout(layout)
        self.dialog.exec()  # Show the dialog

    @Slot()
    def display_selected_patient(self, item):
        """Populate patient details in the main UI when a row is double-clicked."""
        row = item.row()
        selected_patient = self.patient_data[row]  # Get patient from stored data

        # Populate main UI fields
        self.ui.patient_name.setCurrentText(selected_patient.get("name", ""))
        self.ui.p_contact.setText(selected_patient.get("contact", ""))
        self.ui.p_email.setText(selected_patient.get("email", ""))
        self.ui.p_address.setText(selected_patient.get("address", ""))
        self.ui.p_age.setText(str(selected_patient.get("age", "")))

        # Close the dialog after selecting a patient
        self.dialog.close()

    @Slot()
    def enter_patient_manually(self):
        """Open a dialog to manually enter patient details."""
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Enter Patient Manually")
        self.dialog.resize(400, 300)

        layout = QVBoxLayout()

        # Name Field
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Enter patient name")

        # Contact Field
        self.contact_input = QLineEdit()
        self.contact_input.setPlaceholderText("Enter contact")

        # Email Field
        self.email_input = QLineEdit()
        self.email_input.setPlaceholderText("Enter email")

        # Address Field
        self.address_input = QLineEdit()
        self.address_input.setPlaceholderText("Enter address")

        # Age Field
        self.age_input = QLineEdit()
        self.age_input.setPlaceholderText("Enter age")

        # Submit Button
        submit_button = QPushButton("Save Patient")
        submit_button.clicked.connect(self.save_manual_patient)

        # Add widgets to layout
        layout.addWidget(QLabel("Patient Name:"))
        layout.addWidget(self.name_input)
        layout.addWidget(QLabel("Contact:"))
        layout.addWidget(self.contact_input)
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)
        layout.addWidget(QLabel("Address:"))
        layout.addWidget(self.address_input)
        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.age_input)
        layout.addWidget(submit_button)

        self.dialog.setLayout(layout)
        self.dialog.exec()  # Show dialog
        
    @Slot()
    def save_manual_patient(self):
        """Save manually entered patient details to the main UI and add to combobox."""
        name = self.name_input.text().strip()
        contact = self.contact_input.text().strip()
        email = self.email_input.text().strip()
        address = self.address_input.text().strip()
        age = self.age_input.text().strip()

        if not name:
            QMessageBox.warning(self, "Input Error", "Patient name is required.")
            return

        # Check if the patient is already in the comboBox
        existing_patients = [self.ui.patient_name.itemText(i) for i in range(self.ui.patient_name.count())]

        if name not in existing_patients:
            # Add manually entered patient to the combobox
            self.ui.patient_name.addItem(name, {
                "name": name,
                "contact": contact,
                "email": email,
                "address": address,
                "age": age
            })

        # Set the newly added patient as the selected item
        index = self.ui.patient_name.findText(name)
        if index != -1:
            self.ui.patient_name.setCurrentIndex(index)

        # Populate the other patient details in the UI
        self.ui.p_contact.setText(contact)
        self.ui.p_email.setText(email)
        self.ui.p_address.setText(address)
        self.ui.p_age.setText(age)

        # Close the dialog after saving
        self.dialog.close()

    @Slot()
    def update_totals(self):
        """Calculate and update all totals based on the shopping cart."""
        total_amount_without_tax = 0.0
        category_totals = defaultdict(float)  # To track totals per category
        category_vat = defaultdict(float)  # Track VAT per category
        total_vat = 0.0

        # Iterate through the cart to calculate totals frame_5
        for item in self.cart:
            category_name = item.get("category_name", "Unknown")  # Assume each item has a category_name
            unit_price = item.get("unit_price", 0)
            quantity = item.get("quantity", 0)
            total_price = unit_price * quantity
            vat = (total_price * VAT_PERCENTAGE) / 100

            # Accumulate totals
            total_amount_without_tax += total_price
            category_totals[category_name] += total_price
            category_vat[category_name] += vat  # Store VAT per category
            total_vat += vat

        # Calculate total balance (amount to be paid)
        total_balance = total_amount_without_tax + total_vat

        # Update total amount without tax
        self.ui.total_amount_without_tax.setText(f"{total_amount_without_tax:,.2f}")

        # Update VAT label
        self.ui.total_VAT_on_items.setText(f"{total_vat:,.2f}")

        # Update total balance label
        self.ui.total_balance.setText(f"{total_balance:,.2f}")
        
        # Update category VAT values for the receipt
        self.category_vat_data = category_vat  # Store VAT per category for printing

        # Dynamically update category totals
        self.update_category_totals(category_totals)
        self.calculate_change()

    def update_category_totals(self, category_totals=None):
        """Dynamically update labels for category totals."""
        if category_totals is None:  # If no argument is given, reset to empty
            category_totals = {}

        # Clear existing labels
        for i in reversed(range(self.ui.frame_10.layout().count())):
            widget = self.ui.frame_10.layout().itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Add labels dynamically based on category_totals
        for category_name, total in category_totals.items():
            label = QLabel(f"{category_name}: {total:,.2f}")
            label.setStyleSheet("font-size: 14px; font-weight: bold; color: #ffffff;")
            self.ui.frame_10.layout().addWidget(label)

    @Slot()
    def add_to_cart(self):
        """Add the selected item type and quantity to the cart."""
        selected_item = self.ui.item_types.currentData()
        quantity = self.ui.quantity.text().strip()

        # Validate inputs
        if not selected_item or not isinstance(selected_item, dict):
            QMessageBox.warning(self, "Input Error", "Please select an item type.")
            return

        if not quantity.isdigit() or int(quantity) <= 0:
            QMessageBox.warning(self, "Input Error", "Please enter a valid quantity.")
            return

        # Ensure the unit price is available
        unit_price = selected_item.get("unit_price")
        if unit_price is None:
            QMessageBox.warning(self, "Error", "Unit price not available for the selected item.")
            return

        # Get category name for the item
        category_name = self.ui.category.currentText()
        item_type_id = selected_item.get("id")  # Extract the ID of the item type

        # Calculate total price
        quantity = int(quantity)
        total_price = unit_price * quantity

        # Add to cart
        self.cart.append({
            "item_type_id": item_type_id, 
            "item_type": selected_item["name"],
            "category_name": category_name,
            "unit_price": unit_price,
            "quantity": quantity,
            "total_price": total_price,
        })
        # Update the cart table
        self.update_cart_table()
        self.update_totals()
        self.ui.quantity.clear()
        self.ui.item_types.setCurrentIndex(0)
        self.calculate_change()

    @Slot()
    def remove_item_from_cart(self):
        """Remove the selected item from the cart."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select an item to remove.")
            return

        # Remove the item from the cart
        self.cart.pop(selected_row)

        # Update the cart table
        self.update_cart_table()
        # Recalculate totals
        self.update_totals()
        self.calculate_change()

    def update_cart_table(self):
        """Update the cart table with items in the cart."""
        self.ui.tableWidget.setRowCount(0)  # Clear existing rows

        for row, item in enumerate(self.cart):
            self.ui.tableWidget.insertRow(row)
             
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["quantity"])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["item_type"]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(f"{item['unit_price']:,.2f}"))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(f"{item['total_price']:,.2f}"))

        
    @Slot()
    def calculate_change(self):
        """Calculate and display the change to give based on the amount given."""
        amount_given_text = self.ui.amount_given.text().strip()
        total_balance_text = self.ui.total_balance.text().strip()

        # Ensure valid input values
        try: 
            amount_given = float(amount_given_text.replace(",", "")) if amount_given_text else 0.0
            total_balance = float(total_balance_text.replace(",", "")) if total_balance_text else 0.0
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Invalid amount entered.")
            return

        # Calculate change 
        change_to_give = amount_given - total_balance

        # Update change label
        self.ui.change_to_give.setText(f"{change_to_give:,.2f}")
        
    @Slot()
    def validate_transaction(self):
        """Send the sales transaction to the backend for validation and stock update."""
        if not self.cart:
            QMessageBox.warning(self, "Validation Error", "No items in the cart to validate.")
            return

        # Get patient ID (optional)
        selected_patient = self.ui.patient_name.currentData()
        patient_id = selected_patient.get("id") if selected_patient else None
        patient_name = selected_patient.get("name", "Unknown") if selected_patient else "N/A"

        # Prepare transaction data
        items = [
            {
                "item_type_id": item["item_type_id"],
                "unit_price": item["unit_price"],
                "quantity": item["quantity"],
                "item_type": item["item_type"],  # ✅ Include the item name
                "category_name": item["category_name"],
            }
            for item in self.cart
        ]

        transaction_data = {
            "patient_name": patient_name, 
            "patient_id": patient_id,
            "items": items,
            "total_amount": float(self.ui.total_amount_without_tax.text().replace(",", "")),
            "total_vat": float(self.ui.total_VAT_on_items.text().replace(",", "")),
            "total_balance": float(self.ui.total_balance.text().replace(",", "")),
        }

        try:
            response = requests.post(f"{BASE_URL}/process-sale/", json=transaction_data)

            if response.status_code == 201:
                QMessageBox.information(self, "Success", "Transaction validated successfully!")

                # ✅ Store the last transaction before clearing the cart
                self.last_transaction = transaction_data  

                self.clear_cart()  # Clear cart after successful validation
            else:
                try:
                    error_message = response.json().get("error", "Unknown error occurred.")
                except ValueError:  # JSON decode error
                    error_message = "Invalid response from server. Please check the backend."

                QMessageBox.warning(self, "Error", f"Failed to validate transaction: {error_message}")

        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
            


    def clear_cart(self):
        """Clear the shopping cart after a successful sale transaction."""
        self.cart.clear()
        self.ui.tableWidget.setRowCount(0)  # Clear cart table
        self.ui.total_amount_without_tax.setText("0.00")
        self.ui.total_VAT_on_items.setText("0.00")
        self.ui.total_balance.setText("0.00")
        self.ui.amount_given.clear()
        self.ui.change_to_give.clear()
        self.update_category_totals({})  # ✅ Pass an empty dictionary to clear category totals

    def generate_receipt(self, transaction_data):
        """Generate a receipt PDF using ReportLab."""
        filename = "sales_receipt.pdf"
        c = canvas.Canvas(filename, pagesize=A3)
        width, height = A3
        margin = 1.5 * inch  
        
        # 🕒 Capture the current date and time
        current_datetime = datetime.datetime.now().strftime("%d-%b-%Y %H:%M")  # Example: "10-Feb-2025 14:30"
        # Header Section
        logo_path = "add_shopping_cart_16px.png"
        c.drawImage(logo_path, margin, height - 2.5 * inch, width=.4 * inch, height=.4 * inch, mask="auto")
        c.drawImage(logo_path, width / 1.2, height - 2.6 * inch, width=.4 * inch, height=.4 * inch, mask="auto")

        c.setFillColor(colors.HexColor('#062440'))
        c.setFont("Helvetica-Bold", 64)
        c.drawString(width / 8.0, height - 1.5 * inch, "NGASSAM OPTIQUE")
        c.setFont("Helvetica-Bold", 16)
        c.drawString(width / 2.34, height - 1.87 * inch, "CABINET OPTIQUE")
        c.drawString(margin + 0.59 * inch, height - 2.1 * inch, "Vente de matériel Ophtalmique médical-Verre ophtalmique - Montures de marque")
        c.drawString(margin + 2.5 * inch, height - 2.5 * inch, "N.I.U: P039116571318-RC/YAO/2023/A/351")
        c.drawString(margin + 0.1 * inch, height - 2.9 * inch, "Situé derrière ADAMAQUA PALACE - Tél.: (237) 699 67 50 25/620 37 69 28/651 63 06 45")

        c.setStrokeColor(colors.black)
        c.setLineWidth(2)
        c.line(margin, height - 3.15 * inch, width - margin, height - 3.15 * inch)

        c.setFont("Helvetica-Bold", 17)
        c.drawString(margin + 2.67 * inch, height - 3.6 * inch, "Le professionnel de la santé visuelle")

        c.setFont("Helvetica-Bold", 22)
        c.drawString(width / 2.6, height - 4.5 * inch, "FACTURE PROFORMA")
        
        def informations_section():
            # 🧾 Receipt date
            c.setFont("Helvetica-Bold", 16)
            c.drawString(width / 1.3, height - 4 * inch, f"Date: {current_datetime}")

            # 📜 Transaction Details
            c.setFont("Helvetica-Bold", 14)
            y_position = height - 5.5 * inch
            patient_name = transaction_data.get("patient_name", "Unknown")
            c.drawString(margin, y_position, f"Doit: {patient_name}")
            # c.drawString(width / 2, y_position, f"Transaction ID: {transaction_data['transaction_id']}")
            c.drawString(margin, y_position - 0.5 * inch, f"N.U.I: iii")
            # c.drawString(width / 2, y_position - 0.5 * inch, f"Patient: {transaction_data['patient_name']}")
        informations_section()
        def draw_watermark():
            c.setFont("Helvetica-Bold", 100)
            c.setFillColor(colors.lightgrey, alpha=0.5)
            c.saveState()
            c.translate(width / 6, height / 5)
            c.rotate(45)
            c.drawString(0, 0, "NGASSAM OPTIQUE")
            c.restoreState()
            
        draw_watermark()
        # Items Table
        table_data = [["Qty", "Item", "Unit Price (XAF)", "Total (XAF)"]]
        for item in transaction_data["items"]:
            table_data.append([item["quantity"],  item['category_name'] +' - ' + item['item_type'] , f"{item['unit_price']:,.2f}", f"{item['unit_price'] * item['quantity']:,.2f}"])
        max_rows_first_page = 25
        max_rows_other_pages = 40
        rows = table_data[1:]
        first_page = True

        while rows:
            if first_page:
                max_rows_per_page = max_rows_first_page
                y_position = height - 7.8 * inch
            else:
                max_rows_per_page = max_rows_other_pages
                y_position = height - 11.7 * inch

            table_slice = [table_data[0]] + rows[:max_rows_per_page]
            rows = rows[max_rows_per_page:]
            
            table = Table(table_slice, colWidths=[1 * inch, 4 * inch, 2 * inch, 2 * inch])
            table.setStyle(TableStyle([
                ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "CENTER"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 14),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]))
            
            table.wrapOn(c, width, height)
            table.drawOn(c, margin, y_position)
            
            if rows:
                c.showPage()
                draw_watermark()
                first_page = False
        # Total and VAT Section
        y_summary = height - 12.0 * inch
        c.setFillColor(colors.HexColor('#062440'))
        c.setFont("Helvetica-Bold", 16)
        
        c.drawString(margin, y_summary, "Total hors taxes:")
        c.drawString(margin + 6.5 * inch, y_summary, f"{transaction_data['total_amount']:,.2f} XAF")
        
        # 🧾 VAT Breakdown for Each Category
        y_vat = y_summary - 0.5 * inch  # Start position for VAT details
        for category, vat_amount in self.category_vat_data.items():
            c.drawString(margin, y_vat, f"TVA sur {category} (19.25%):")
            c.drawString(margin + 6.5 * inch, y_vat, f"{vat_amount:,.2f} XAF")
            y_vat -= 0.5 * inch  # Move down for next VAT line
        c.drawString(margin + .01 * inch, height / 6.0, "TVA sur Frais montage (19.25%):")
        c.drawString(margin + 6.5 * inch, height /  6.0, f"  XAF")
        c.drawString(margin, height / 7.2, "Total TVA (19.25%):")
        c.drawString(margin + 6.5 * inch, height / 7.2, f"{transaction_data['total_vat']:,.2f} XAF")
        c.drawString(margin, height / 9.0, "Total Amount Due:")
        c.drawString(margin + 6.5 * inch, height / 9.0, f"{transaction_data['total_balance']:,.2f} XAF")
        # Save PDF
        c.save()
        return filename

    @Slot()
    def print_receipt(self):
        """Generate and print the receipt automatically."""
        if not self.last_transaction:
            QMessageBox.warning(self, "Print Error", "No transaction found to print. Please validate a sale first.")
            return
        receipt_path = self.generate_receipt(self.last_transaction)
        printer = QPrinter()
        printer.setPrinterName("Default Printer")  # Adjust as necessary
        # printer.setPageSize(QPrinter.A3)  # ✅ Correct
        printer.setPageSize(QPageSize(QPageSize.A4))


        print_dialog = QPrintDialog(printer, self)
        if print_dialog.exec() == QPrintDialog.Accepted:
            os.system(f"start {receipt_path}")  # Open the PDF for preview (Windows)
            QMessageBox.information(self, "Printing", "Receipt sent to the printer.")
if __name__ == "__main__":
    app = QApplication([])
    window = PurchaseBoardManager()
    window.show()
    app.exec()