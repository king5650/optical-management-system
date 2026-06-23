import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
)
from ui_purchase_board2 import Ui_Form

class PurchaseBoard(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        # Initialize items combobox
        self.items.addItems(["Frame", "Lens", "Optical Accessory"])
        self.items.currentTextChanged.connect(self.populate_item_types)
        self.item_types.currentIndexChanged.connect(self.display_unit_price)

        # self.items.currentTextChanged.connect(self.update_item_types)
        # self.item_types.currentTextChanged.connect(self.update_unit_price)
        self.add_to_cart.clicked.connect(self.add_item_to_cart)
        self.delete_from_cart.clicked.connect(self.remove_item_from_cart)
        self.validate.clicked.connect(self.validate_purchase)
        self.amount_given.textChanged.connect(self.calculate_change)
        self.load_patients()
        self.patient_name.currentIndexChanged.connect(self.display_patient_details)

        # Load patient details
        self.load_patients()
        self.populate_item_types()
        self.display_unit_price()
        self.patient_name.currentTextChanged.connect(self.display_patient_details)

    # def load_patients(self):
    #     try:
    #         response = requests.get("http://127.0.0.1:8000/api/patients/list")
    #         if response.status_code == 200:
    #             patients = response.json()
    #             self.patient_name.addItems([patient["name"] for patient in patients])
    #         else:
    #             QMessageBox.warning(self, "Error", "Failed to load patients.")
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")
    def load_patients(self):
        """Fetch and populate the patient_name comboBox."""
        try:
            response = requests.get("http://127.0.0.1:8000/auth/patients/list/")
            if response.status_code == 200:
                patients = response.json().get('patients', [])
                if not patients:
                    QMessageBox.warning(self, "Error", "No patients found.")
                else:
                    self.populate_patient_dropdown(patients)
            else:
                QMessageBox.warning(self, "Error", f"Failed to load patients: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")
            
            
    def populate_patient_dropdown(self, patients):
        """Populate the patient_name comboBox with patient data."""
        self.patient_name.clear()
        for patient in patients:
            self.patient_name.addItem(patient['name'], patient)

    def display_patient_details(self):
        """Fetch and display details of the selected patient."""
        current_index = self.patient_name.currentIndex()
        selected_patient = self.patient_name.itemData(current_index)
        print("Selected Patient Data:", selected_patient)  # Debugging
        if current_index < 0:
            # No valid selection
            return

        # Get the patient data associated with the selected name amount_given
        selected_patient = self.patient_name.itemData(current_index)
        if not selected_patient or "id" not in selected_patient:
            QMessageBox.warning(self, "Error", "Failed to fetch patient details.")
            return

        try:
            # Make a request to fetch the details of the selected patient
            response = requests.get(f"http://127.0.0.1:8000/auth/patients/{selected_patient['id']}/details/")
            if response.status_code == 200:
                patient_details = response.json()
                self.p_email.setText(patient_details.get('email', 'N/A'))
                self.p_contact.setText(patient_details.get('contact', 'N/A'))
                self.p_address.setText(patient_details.get('address', 'N/A'))
                self.p_gender.setText(patient_details.get('gender', 'N/A'))
                self.p_age.setText(str(patient_details.get('age', 'N/A')))
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch patient details: {response.status_code}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")




    # def display_patient_details(self):
    #     patient_name = self.patient_name.currentText()
    #     try:
    #         response = requests.get(f"http://127.0.0.1:8000/api/patients/{patient_name}/")
    #         if response.status_code == 200:
    #             patient = response.json()
    #             self.p_email.setText(patient.get("email", ""))
    #             self.p_address.setText(patient.get("address", ""))
    #             self.p_contact.setText(patient.get("contact", ""))
    #             self.p_gender.setText(patient.get("gender", ""))
    #             self.p_age.setText(str(patient.get("age", "")))
    #         else:
    #             QMessageBox.warning(self, "Error", "Failed to fetch patient details.")
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")


    def populate_item_types(self):
        """Populate item_types comboBox based on the selected item."""
        selected_item = self.items.currentText()

        if not selected_item:
            return

        # Clear the item_types comboBox
        self.item_types.clear()

        # Determine the endpoint based on the selected item
        endpoint_map = {
            "Frame": "frames",
            "Lens": "lenses",
            "Optical Accessory": "accessories",
        }
        endpoint = endpoint_map.get(selected_item)

        if not endpoint:
            QMessageBox.warning(self, "Error", "Invalid item type selected.")
            return

        try:
            # Fetch item types or names from the backend
            response = requests.get(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/list/")
            if response.status_code == 200:
                items = response.json().get("items", [])

                if selected_item == "Optical Accessory":
                    # Populate names for Optical Accessories
                    for item in items:
                        self.item_types.addItem(item["name"], item)
                else:
                    # Populate subtypes for Frames or Lenses
                    for item in items:
                        subtype_key = "frame_type" if selected_item == "Frame" else "lens_type"
                        self.item_types.addItem(item[subtype_key], item)
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch {selected_item} types: {response.json().get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def display_unit_price(self):
        """Display the unit price for the selected subtype or name."""
        current_index = self.item_types.currentIndex()
        if current_index < 0:
            return

        # Get the selected item's data
        selected_data = self.item_types.itemData(current_index)
        if selected_data:
            self.unit_price.setText(f"{selected_data['unit_price']}")





    # def update_item_types(self):
    #     selected_item = self.items.currentText()
    #     self.item_types.clear()

    #     if selected_item == "Frame":
    #         self.item_types.addItems(["VIP", "VIP+", "VIP++", "CLASSIC"])
    #     elif selected_item == "Lens":
    #         self.item_types.addItems(["Simple Vision", "Progressive Stock", "Progressive Commande", "Bi-focaux"])
    #     elif selected_item == "Optical Accessory":
    #         try:
    #             response = requests.get("http://127.0.0.1:8000/api/optical_accessories/")
    #             if response.status_code == 200:
    #                 accessories = response.json()
    #                 self.item_types.addItems([accessory["name"] for accessory in accessories])
    #             else:
    #                 QMessageBox.warning(self, "Error", "Failed to load optical accessories.")
    #         except requests.exceptions.RequestException as e:
    #             QMessageBox.critical(self, "Error", f"Server error: {e}")

    # def update_unit_price(self):
    #     selected_item = self.items.currentText()
    #     selected_type = self.item_types.currentText()

    #     try:
    #         response = requests.get(f"http://127.0.0.1:8000/api/{selected_item.lower()}/{selected_type}/price/")
    #         if response.status_code == 200:
    #             price_data = response.json()
    #             self.unit_price.setText(str(price_data.get("unit_price", "")))
    #         else:
    #             QMessageBox.warning(self, "Error", "Failed to fetch unit price.")
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")

    def add_item_to_cart(self):
        quantity = self.quantity.text()
        unit_price = self.unit_price.text()
        item = self.items.currentText()
        item_type = self.item_types.currentText()

        if not quantity.isdigit() or int(quantity) <= 0:
            QMessageBox.warning(self, "Error", "Please enter a valid quantity.")
            return

        total_price = int(quantity) * float(unit_price)
        row_position = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_position)
        self.tableWidget.setItem(row_position, 0, QTableWidgetItem(quantity))
        self.tableWidget.setItem(row_position, 1, QTableWidgetItem(f"{item} ({item_type})"))
        self.tableWidget.setItem(row_position, 2, QTableWidgetItem(unit_price))
        self.tableWidget.setItem(row_position, 3, QTableWidgetItem(f"{total_price:.2f}"))
        
        self.calculate_totals()
        self.calculate_change()

    def remove_item_from_cart(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            self.tableWidget.removeRow(selected_row)
            self.calculate_totals()
            self.calculate_change()
        else:
            QMessageBox.warning(self, "Error", "Please select an item to remove.")

    def calculate_totals(self):
        total_without_tax = 0
        vat_on_frames = vat_on_lenses = vat_on_accessories = 0
        vat_rate = 0.1925

        for row in range(self.tableWidget.rowCount()):
            quantity = int(self.tableWidget.item(row, 0).text())
            item = self.tableWidget.item(row, 1).text()
            unit_price = float(self.tableWidget.item(row, 2).text())

            total_without_tax += quantity * unit_price

            if "Frame" in item:
                vat_on_frames += quantity * unit_price * vat_rate
            elif "Lens" in item:
                vat_on_lenses += quantity * unit_price * vat_rate
            elif "Accessory" in item:
                vat_on_accessories += quantity * unit_price * vat_rate

        self.total_amount_without_tax.setText(f"{total_without_tax:.2f}")
        self.VAT_on_frame.setText(f"{vat_on_frames:.2f}")
        self.VAT_on_lens.setText(f"{vat_on_lenses:.2f}")
        self.VAT_on_aceessory.setText(f"{vat_on_accessories:.2f}")

        total_vat = vat_on_frames + vat_on_lenses + vat_on_accessories
        self.total_VAT_on_items.setText(f"{total_vat:.2f}")

        total_balance = total_without_tax + total_vat
        self.total_balance.setText(f"{total_balance:.2f}")

    def calculate_change(self):
        try:
            amount_given = float(self.amount_given.text())
            total_balance = float(self.total_balance.text())
            change = amount_given - total_balance
            self.change_to_give.setText(f"{change:.2f}")
        except ValueError:
            self.change_to_give.setText("0.00")
            
            
            
    def validate_purchase(self):
        """Validate and save the purchase in the database."""
        try:
            # Initialize total amount and VAT
            total_without_tax = 0
            total_vat = 0

            purchase_details = []

            # Loop through all rows in the cart table
            for row in range(self.tableWidget.rowCount()):
                # Fetch data from the table
                item_entry = self.tableWidget.item(row, 1).text()  # Example: "Frame (VIP+)"
                unit_price_raw = self.tableWidget.item(row, 2).text()
                quantity_raw = self.tableWidget.item(row, 0).text()

                # Extract item_type and item_name separately
                if "(" in item_entry and ")" in item_entry:
                    item_name, item_type = item_entry.split(" (")
                    item_type = item_type.strip(")")  # Remove the trailing parenthesis
                else:
                    item_name = item_entry
                    item_type = "N/A"

                # Sanitize the unit price and quantity inputs
                unit_price = float(unit_price_raw.replace(',', '').strip())
                quantity = int(quantity_raw.replace(',', '').strip())

                # Calculate total and VAT for the item
                total_item_price = unit_price * quantity
                vat_item_price = total_item_price * 0.1925

                total_without_tax += total_item_price
                total_vat += vat_item_price

                # Prepare data for the database
                purchase_details.append({
                    "item_name": item_name,
                    "item_type": item_type,
                    "unit_price": unit_price,
                    "quantity": quantity,
                    "total": total_item_price,
                })

            # Prepare the data for the request
            data = {
                "patient_name": self.patient_name.currentText(),
                "total_amount": total_without_tax,
                "vat_total": total_vat,
                "purchase_details": purchase_details,
            }

            # Debugging: Print the data to the console
            print("Data being sent to the backend:", data)

            # Send data to the backend
            response = requests.post("http://127.0.0.1:8000/auth/purchase/add/", json=data)

            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Purchase validated successfully!")
            else:
                QMessageBox.warning(self, "Error", f"Failed to save purchase: {response.json().get('error', 'Unknown error')}")

        except ValueError as e:
            QMessageBox.critical(self, "Error", f"Invalid input: {e}")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")


            
                
            
            
    
            
    # def validate_purchase(self):
    #     """Validate and save the purchase in the database."""
    #     try:
    #         # Initialize total amount and VAT
    #         total_without_tax = 0
    #         total_vat = 0

    #         # Loop through all rows in the cart table
    #         for row in range(self.tableWidget.rowCount()):
    #             # Fetch data from the table
    #             item = self.tableWidget.item(row, 1).text()
    #             item_type = self.tableWidget.item(row, 1).text()
    #             unit_price_raw = self.tableWidget.item(row, 2).text()
    #             quantity_raw = self.tableWidget.item(row, 3).text()

    #             # Sanitize the unit price and quantity inputs
    #             unit_price = float(unit_price_raw.replace(',', '').strip())
    #             quantity = int(quantity_raw.replace(',', '').strip())

    #             # Calculate total and VAT for the item
    #             total_item_price = unit_price * quantity
    #             vat_item_price = total_item_price * 0.1925

    #             total_without_tax += total_item_price
    #             total_vat += vat_item_price

    #             # Prepare data for the database
    #             data = {
    #                 "item": item,
    #                 "item_type": item_type,
    #                 "unit_price": unit_price,
    #                 "quantity": quantity,
    #                 "total_item_price": total_item_price,
    #                 "vat_item_price": vat_item_price,
    #             }

    #             # Send data to the backend
    #             response = requests.post("http://127.0.0.1:8000/auth/purchase/add/", json=data)
    #             if response.status_code != 200:
    #                 QMessageBox.warning(self, "Error", f"Failed to save item: {item_type}")

    #         # Update the total values in the UI
    #         self.total_amount_without_tax.setText(f"{total_without_tax:.2f}")
    #         self.total_VAT_on_items.setText(f"{total_vat:.2f}")
    #         self.total_balance.setText(f"{(total_without_tax + total_vat):.2f}")

    #         QMessageBox.information(self, "Success", "Purchase validated successfully!")
    #     except ValueError as e:
    #         QMessageBox.critical(self, "Error", f"Invalid input: {e}")
    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"An unexpected error occurred: {e}")


    # def validate_purchase(self):
    #     """Validate the purchase and save the transaction in the database."""
    #     if self.tableWidget.rowCount() == 0:
    #         QMessageBox.warning(self, "Error", "The cart is empty! Add items before validating.")
    #         return

    #     try:
    #         # Gather purchase data
    #         patient_name = self.patient_name.currentText() if not self.patient_name.isEditable() else self.patient_name.currentText()
    #         total_amount = float(self.total_balance.text())
    #         vat_total = float(self.total_VAT_on_items.text())
    #         purchase_details = []

    #         # Prepare purchase details for the database
    #         for row in range(self.tableWidget.rowCount()):
    #             item_name = self.tableWidget.item(row, 0).text()
    #             item_type = self.tableWidget.item(row, 1).text()
    #             unit_price = float(self.tableWidget.item(row, 2).text())
    #             quantity = int(self.tableWidget.item(row, 3).text())
    #             total = float(self.tableWidget.item(row, 4).text())

    #             purchase_details.append({
    #                 "item_name": item_name,
    #                 "item_type": item_type,
    #                 "unit_price": unit_price,
    #                 "quantity": quantity,
    #                 "total": total
    #             })

    #         # Prepare request payload
    #         payload = {
    #             "patient_name": patient_name,
    #             "total_amount": total_amount,
    #             "vat_total": vat_total,
    #             "purchase_details": purchase_details,
    #         }

    #         # Send POST request to save the purchase
    #         response = requests.post("http://127.0.0.1:8000/auth/purchase/validate/", json=payload)
    #         if response.status_code == 200:
    #             QMessageBox.information(self, "Success", "Purchase validated successfully! ✅")
    #             self.clear_cart()  # Clear the cart after successful validation
    #         else:
    #             QMessageBox.critical(self, "Error", f"Failed to validate purchase: {response.json().get('error', 'Unknown error')}")

    #     except Exception as e:
    #         QMessageBox.critical(self, "Error", f"An unexpected error occurred: {str(e)}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PurchaseBoard()
    window.show()
    sys.exit(app.exec())
























































































# import sys
# import requests
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
# from ui_purchase_board2 import Ui_Form

# # class PurchaseBoard(QMainWindow, Ui_Form):
# class PurchaseBoard(QWidget, Ui_Form):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

#         # Initialize items and connect signals
#         self.populate_items()  
#         self.items.currentTextChanged.connect(self.update_item_types)
#         self.item_types.currentTextChanged.connect(self.update_unit_price)

#         # Connect patient selection
#         self.patient_name.currentTextChanged.connect(self.load_patient_details)
#         self.toolButton.clicked.connect(self.handle_tool_button)

#         # Connect cart actions
#         self.add_to_cart.clicked.connect(self.add_item_to_cart)
#         self.delete_from_cart.clicked.connect(self.remove_item_from_cart)
#         self.validate.clicked.connect(self.validate_purchase)
#         self.amount_given.textChanged.connect(self.calculate_change)

#         # Initialize data
#         self.cart = []
#         self.update_totals()

#     # def __init__(self):
#     #     super().__init__()
#     #     self.setupUi(self)  # Call setupUi only once
#     #     # Initialize additional functionality here, if needed

#     #     # Populate item combo box
#     #     self.items.addItems(["Frame", "Lens", "Optical Accessory"])
#     #     self.items.currentTextChanged.connect(self.update_item_types)
#     #     self.populate_items()  # Populate items on startup
#     #     self.items.currentTextChanged.connect(self.update_item_types)
#     #     self.item_types.currentTextChanged.connect(self.update_unit_price)


#     #     # Connect patient selection
#     #     self.patient_name.currentTextChanged.connect(self.load_patient_details)
#     #     self.toolButton.clicked.connect(self.handle_tool_button)

#     #     # Connect cart actions
#     #     self.add_to_cart.clicked.connect(self.add_item_to_cart)
#     #     self.delete_from_cart.clicked.connect(self.remove_item_from_cart)
#     #     self.validate.clicked.connect(self.validate_purchase)
#     #     self.amount_given.textChanged.connect(self.calculate_change)

#     #     # Initialize data
#     #     self.cart = []
#     #     self.update_totals()
        
#     def update_item_types(self):
#         """Update the item types ComboBox dynamically based on the selected item."""
#         selected_item = self.items.currentText()
#         self.item_types.clear()

#         # Map the selected item to its types
#         endpoint_map = {
#             "Frame": "frames",
#             "Lens": "lenses",
#             "Optical Accessory": "accessories"
#         }

#         # Ensure case-insensitive matching and endpoint mapping
#         endpoint = endpoint_map.get(selected_item)

#         if not endpoint:
#             QMessageBox.warning(self, "Error", "Invalid item type selected.")
#             return

#         try:
#             # Make a GET request to fetch item types
#             response = requests.get(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/types/")
#             if response.status_code == 200:
#                 types = response.json().get("types", [])
#                 self.item_types.addItems(types)
#             else:
#                 QMessageBox.warning(self, "Error", f"Failed to fetch item types: {response.json().get('error', 'Unknown error')}")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")

            
#     def populate_items(self):
#         """Populate the items ComboBox dynamically from the database."""
#         try:
#             response = requests.get("http://127.0.0.1:8000/auth/inventory/categories/")
#             if response.status_code == 200:
#                 categories = response.json().get("categories", [])
#                 self.items.addItems(categories)
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch item categories.")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")


#     # def update_item_types(self):
#     #     """Update the item types combo box based on the selected item."""
#     #     selected_item = self.items.currentText()
#     #     self.item_types.clear()

#     #     if selected_item == "Frame":
#     #         self.item_types.addItems(["VIP", "VIP+", "VIP++", "CLASSIC"])
#     #     elif selected_item == "Lens":
#     #         self.item_types.addItems([
#     #             "Simple Vision", "Progressive Stock", "Progressive Commande", "Bi-focaux"
#     #         ])

#     #     # Fetch unit price for the selected item type
#     #     self.fetch_unit_price()

#     def update_unit_price(self):
#         """Fetch the unit price from the database for the selected item type."""
#         selected_item = self.items.currentText()
#         selected_type = self.item_types.currentText()

#         # Validate selection
#         if not selected_item or not selected_type:
#             self.unit_price.clear()
#             return

#         # Map the selected item to its types
#         endpoint_map = {
#             "Frame": "frames",
#             "Lens": "lenses",
#             "Optical Accessory": "accessories"
#         }

#         # Ensure case-insensitive matching and endpoint mapping
#         endpoint = endpoint_map.get(selected_item)

#         if not endpoint:
#             QMessageBox.warning(self, "Error", "Invalid item type selected.")
#             return

#         try:
#             # Make a GET request to fetch the unit price
#             response = requests.get(
#                 f"http://127.0.0.1:8000/auth/inventory/{endpoint}/price/",
#                 params={"type": selected_type}
#             )
#             if response.status_code == 200:
#                 unit_price = response.json().get("unit_price", 0.0)
#                 self.unit_price.setText(f"{unit_price:.2f}")
#             else:
#                 QMessageBox.warning(self, "Error", f"Failed to fetch unit price: {response.json().get('error', 'Unknown error')}")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")


#     def load_patient_details(self):
#         """Load patient details when a patient is selected."""
#         patient_name = self.patient_name.currentText()

#         if patient_name:
#             try:
#                 response = requests.get(f"http://127.0.0.1:8000/auth/patient/{patient_name}/details/")
#                 if response.status_code == 200:
#                     details = response.json()
#                     self.p_email.setText(details.get("email", ""))
#                     self.p_address.setText(details.get("address", ""))
#                     self.p_contact.setText(details.get("contact", ""))
#                     self.p_gender.setText(details.get("gender", ""))
#                     self.p_age.setText(str(details.get("age", "")))
#                 else:
#                     self.clear_patient_details()
#             except requests.exceptions.RequestException:
#                 QMessageBox.warning(self, "Error", "Failed to fetch patient details.")

#     def clear_patient_details(self):
#         """Clear patient details fields."""
#         self.p_email.clear()
#         self.p_address.clear()
#         self.p_contact.clear()
#         self.p_gender.clear()
#         self.p_age.clear()

#     def handle_tool_button(self):
#         """Handle tool button actions (search/insert)."""
#         # Placeholder for search/insert functionality
#         QMessageBox.information(self, "Info", "Tool button clicked.")

#     def add_item_to_cart(self):
#         """Add the selected item to the cart."""
#         item = self.items.currentText()
#         item_type = self.item_types.currentText()
#         quantity = self.quantity.text()
#         unit_price = self.unit_price.text()

#         if not item or not item_type or not quantity or not unit_price:
#             QMessageBox.warning(self, "Error", "Please fill all fields.")
#             return

#         try:
#             quantity = int(quantity)
#             unit_price = float(unit_price)
#         except ValueError:
#             QMessageBox.warning(self, "Error", "Invalid quantity or unit price.")
#             return

#         total_price = quantity * unit_price

#         # Add to cart
#         self.cart.append({
#             "item": item,
#             "item_type": item_type,
#             "quantity": quantity,
#             "unit_price": unit_price,
#             "total_price": total_price
#         })

#         # Update table
#         row = self.tableWidget.rowCount()
#         self.tableWidget.insertRow(row)
#         self.tableWidget.setItem(row, 0, QTableWidgetItem(str(quantity)))
#         self.tableWidget.setItem(row, 1, QTableWidgetItem(item_type))
#         self.tableWidget.setItem(row, 2, QTableWidgetItem(f"{unit_price:.2f}"))
#         self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{total_price:.2f}"))

#         self.update_totals()

#     def remove_item_from_cart(self):
#         """Remove the selected item from the cart."""
#         selected_row = self.tableWidget.currentRow()

#         if selected_row < 0:
#             QMessageBox.warning(self, "Error", "No item selected.")
#             return

#         self.cart.pop(selected_row)
#         self.tableWidget.removeRow(selected_row)
#         self.update_totals()

#     def update_totals(self):
#         """Calculate and display totals and VAT."""
#         total_without_tax = sum(item["total_price"] for item in self.cart)
#         vat_on_frames = sum(item["total_price"] * 0.1925 for item in self.cart if item["item"] == "Frame")
#         vat_on_lens = sum(item["total_price"] * 0.1925 for item in self.cart if item["item"] == "Lens")
#         vat_on_accessories = sum(item["total_price"] * 0.1925 for item in self.cart if item["item"] == "Optical Accessory")

#         total_vat = vat_on_frames + vat_on_lens + vat_on_accessories
#         total_balance = total_without_tax + total_vat

#         self.total_amount_without_tax.setText(f"{total_without_tax:.2f}")
#         self.VAT_on_frame.setText(f"{vat_on_frames:.2f}")
#         self.VAT_on_lens.setText(f"{vat_on_lens:.2f}")
#         self.VAT_on_aceessory.setText(f"{vat_on_accessories:.2f}")
#         self.total_VAT_on_items.setText(f"{total_vat:.2f}")
#         self.total_balance.setText(f"{total_balance:.2f}")

#     def calculate_change(self):
#         """Calculate change based on the amount given."""
#         amount_given = self.amount_given.text()

#         try:
#             amount_given = float(amount_given)
#             total_balance = float(self.total_balance.text())
#             change = amount_given - total_balance
#             self.change_to_give.setText(f"{change:.2f}")
#         except ValueError:
#             self.change_to_give.clear()

#     def validate_purchase(self):
#         """Validate the purchase and save to the database."""
#         if not self.cart:
#             QMessageBox.warning(self, "Error", "Cart is empty.")
#             return

#         try:
#             response = requests.post("http://127.0.0.1:8000/auth/inventory/sales/", json={"cart": self.cart})
#             if response.status_code == 200:
#                 QMessageBox.information(self, "Success", "Purchase validated successfully.")
#                 self.cart.clear()
#                 self.tableWidget.setRowCount(0)
#                 self.update_totals()
#             else:
#                 QMessageBox.critical(self, "Error", "Failed to validate purchase.")
#         except requests.exceptions.RequestException:
#             QMessageBox.critical(self, "Error", "Failed to connect to the server.")
            
            
#     def populate_items(self):
#         """Populate the items ComboBox dynamically from the database."""
#         self.items.clear()
#         self.items.addItems(["Frame", "Lens", "Optical Accessory"])  # Categories fetched from models

#     def update_unit_price(self):
#         """Fetch the unit price from the database for the selected item type."""
#         selected_item = self.items.currentText()
#         selected_type = self.item_types.currentText()

#         # Validate selection
#         if not selected_item or not selected_type:
#             self.unit_price.clear()
#             return

#         # Map the selected item to its types
#         endpoint_map = {
#             "Frame": "frames",
#             "Lens": "lenses",
#             "Optical Accessory": "accessories"
#         }

#         endpoint = endpoint_map.get(selected_item.lower())

#         if not endpoint:
#             QMessageBox.warning(self, "Error", "Invalid item type selected.")
#             return

#         try:
#             # Make a GET request to fetch the unit price
#             response = requests.get(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/price/", params={"type": selected_type})
#             if response.status_code == 200:
#                 unit_price = response.json().get("unit_price", 0.0)
#                 self.unit_price.setText(f"{unit_price:.2f}")
#             else:
#                 QMessageBox.warning(self, "Error", "Failed to fetch unit price from the database.")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")



# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PurchaseBoard()
#     window.show()
#     sys.exit(app.exec())
