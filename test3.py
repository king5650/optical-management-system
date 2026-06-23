# import sys
# import requests
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
# from ui_item_inventorys1 import Ui_MainWindow


# class InventorySystem(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

#         # Set default items in the comboBox
#         self.itemsSelect.addItems(["Frame", "Lens", "Optical Accessory"])
#         self.itemsSelect.currentTextChanged.connect(self.update_item_types_and_table)

#         # Initially hide the QLineEdit widget for Optical Accessory
#         self.opticalAccessoryName.setVisible(False)

#         # Connect buttons to functionalities
#         self.pushButton_2.clicked.connect(self.add_item)  # Add button

#         # Load initial data for the default selected item
#         self.update_item_types_and_table()

#     def update_item_types_and_table(self):
#         """Update item types, show/hide widgets, and load the table data based on the selected category."""
#         self.update_item_types_and_visibility()
#         self.load_table_data()

#     def update_item_types_and_visibility(self):
#         """Update item types dynamically based on the selected category and show/hide relevant widgets."""
#         selected_item = self.itemsSelect.currentText()

#         if selected_item == "Frame" or selected_item == "Lens":
#             # Show the combo box for item type
#             self.itemtype.setVisible(True)
#             self.itemtype.setEnabled(True)
#             self.label.setText("Item Type:")
#             # Hide the QLineEdit for Optical Accessory
#             self.opticalAccessoryName.setVisible(False)
#         elif selected_item == "Optical Accessory":
#             # Hide the combo box for item type
#             self.itemtype.setVisible(False)
#             self.itemtype.setEnabled(False)
#             self.label.setText("Accessory Name:")
#             # Show the QLineEdit for Optical Accessory
#             self.opticalAccessoryName.setVisible(True)

#     def add_item(self):
#         """Add a new item to the inventory."""
#         selected_item = self.itemsSelect.currentText()

#         # Determine item subtype based on the selected category
#         if selected_item == "Optical Accessory":
#             item_subtype = self.opticalAccessoryName.text()  # Use the QLineEdit value
#         else:
#             item_subtype = self.itemtype.currentText()  # Use the ComboBox value

#         try:
#             unit_price = float(self.itemAmount.text())  # Ensure it's a valid float
#             stock_level = int(self.itemquant.text())  # Ensure it's a valid integer
#         except ValueError:
#             QMessageBox.warning(self, "Error", "Please enter valid numeric values for price and quantity.")
#             return

#         if not item_subtype:
#             QMessageBox.warning(self, "Error", "Please provide an item type or accessory name!")
#             return

#         # Prepare the data
#         data = {
#             "item_type": selected_item,
#             "item_subtype": item_subtype,
#             "unit_price": unit_price,
#             "stock_level": stock_level,
#         }

#         try:
#             response = requests.post("http://127.0.0.1:8000/auth/inventory/add/", json=data)
#             if response.status_code == 200:
#                 QMessageBox.information(self, "Success", "Item added successfully!")
#                 self.load_table_data()  # Reload the table with updated data
#             else:
#                 QMessageBox.critical(self, "Error", f"Failed to add item: {response.json().get('error', '')}")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")

#     def load_table_data(self):
#         """Load data dynamically based on the selected item type."""
#         self.tableWidget.setRowCount(0)  # Clear existing rows in the table

#         # Get the selected item type
#         selected_item = self.itemsSelect.currentText().lower()

#         # Map the selected item to the corresponding API endpoint
#         endpoint_map = {
#             "frame": "frames",
#             "lens": "lenses",
#             "optical accessory": "accessories"
#         }

#         endpoint = endpoint_map.get(selected_item)
#         if not endpoint:
#             QMessageBox.warning(self, "Error", "Invalid item type selected.")
#             return

#         try:
#             # Make a GET request to the server
#             response = requests.get(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/list/")
#             if response.status_code == 200:
#                 # Populate the table with data from the response
#                 items = response.json().get("items", [])
#                 for item in items:
#                     row = self.tableWidget.rowCount()
#                     self.tableWidget.insertRow(row)

#                     # Insert data into the table
#                     self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["id"])))
#                     self.tableWidget.setItem(row, 1, QTableWidgetItem(item.get("name", item.get("frame_type", item.get("lens_type", "")))))
#                     self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))
#                     self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{item['unit_price']}"))
#                     self.tableWidget.setItem(row, 4, QTableWidgetItem(item.get("date_added", "")))
#             else:
#                 QMessageBox.warning(self, "Error", f"Failed to load data: {response.json().get('error', 'Unknown error')}")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = InventorySystem()
#     window.show()
#     sys.exit(app.exec())



import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from ui_item_inventorys1 import Ui_MainWindow


class InventorySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set default items in the comboBox
        self.itemsSelect.addItems(["Frame", "Lens", "Optical Accessory"])
        self.itemsSelect.currentTextChanged.connect(self.update_item_types_and_table)

        # Connect buttons to functionalities
        self.pushButton_2.clicked.connect(self.add_item)  # Add button
        self.pushButton_8.clicked.connect(self.update_item)  # Update button

        # Connect table row selection to populate the form
        self.tableWidget.itemSelectionChanged.connect(self.populate_form_with_selected_item)

        # Load initial data for the default selected item
        self.update_item_types_and_table()

    def update_item_types_and_table(self):
        """Update item types and load the table data based on the selected category."""
        self.update_item_types()
        self.load_table_data()

    def update_item_types(self):
        """Update item types dynamically based on the selected category."""
        selected_item = self.itemsSelect.currentText()

        # Ensure the ComboBox is visible by default
        self.itemtype.setVisible(True)
        self.label_3.setText("Amount:")  # Reset label text

        if selected_item == "Frame":
            self.itemtype.clear()
            self.itemtype.addItems(["VIP", "VIP+", "VIP++", "CLASSIC"])
            self.label.setText("Item Type:")
            self.label.setVisible(True)
            
            self.opticalAccessoryName.setVisible(False)
            self.label_7.setVisible(False)             
        elif selected_item == "Lens":
            self.itemtype.clear()
            self.itemtype.addItems([
                "Simple Vision", "Progressive Stock",
                "Progressive Commande", "Bi-focaux"
            ])
            self.label.setText("Item Type:")
            self.label.setVisible(True)
            
            self.opticalAccessoryName.setVisible(False)
            self.label_7.setVisible(False)            
        elif selected_item == "Optical Accessory":
            # Hide the ComboBox and use a label instead for Optical Accessory
            self.itemtype.setVisible(False)
            self.label.setVisible(False)
            
            self.label_7.setText("Optical Accessory Name:")
            self.opticalAccessoryName.setVisible(True)
            self.label_7.setVisible(True)
            
    def add_item(self):
        """Add a new item to the inventory."""
        selected_item = self.itemsSelect.currentText()
        item_subtype = self.itemtype.currentText() if selected_item != "Optical Accessory" else self.opticalAccessoryName.text()

        try:
            unit_price = float(self.itemAmount.text())  # Ensure it's a valid float
            stock_level = int(self.itemquant.text())  # Ensure it's a valid integer
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numeric values for price and quantity.")
            return

        if not item_subtype and selected_item != "Optical Accessory":
            QMessageBox.warning(self, "Error", "Please select an item type!")
            return

        # Prepare the data
        data = {
            "item_type": selected_item,
            "item_subtype": item_subtype,
            "unit_price": unit_price,
            "stock_level": stock_level,
        }

        try:
            response = requests.post("http://127.0.0.1:8000/auth/inventory/add/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item added successfully!")
                self.load_table_data()  # Reload the table with updated data
            else:
                QMessageBox.critical(self, "Error", f"Failed to add item: {response.json().get('error', '')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def load_table_data(self):
        """Load data dynamically based on the selected item type."""
        self.tableWidget.setRowCount(0)  # Clear existing rows in the table

        # Get the selected item type
        selected_item = self.itemsSelect.currentText().lower()

        # Map the selected item to the corresponding API endpoint
        endpoint_map = {
            "frame": "frames",
            "lens": "lenses",
            "optical accessory": "accessories"
        }

        endpoint = endpoint_map.get(selected_item)
        if not endpoint:
            QMessageBox.warning(self, "Error", "Invalid item type selected.")
            return

        try:
            # Make a GET request to the server
            response = requests.get(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/list/")
            if response.status_code == 200:
                # Populate the table with data from the response
                items = response.json().get("items", [])
                for item in items:
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)

                    # Insert data into the table
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["id"])))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(item.get("name", item.get("frame_type", item.get("lens_type", "")))))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))
                    self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{item['unit_price']}"))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(item.get("date_added", "")))
            else:
                QMessageBox.warning(self, "Error", f"Failed to load data: {response.json().get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def populate_form_with_selected_item(self):
        """Populate the form with the selected item details for updating."""
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            return  # No row selected

        # Populate the form with selected item details
        self.item_id = self.tableWidget.item(current_row, 0).text()
        self.itemtype.setCurrentText(self.tableWidget.item(current_row, 1).text())
        self.itemquant.setText(int(self.tableWidget.item(current_row, 2).text()))
        self.itemAmount.setText(self.tableWidget.item(current_row, 3).text())

    def update_item(self):
        """Update the selected item in the inventory."""
        if not hasattr(self, 'item_id'):
            QMessageBox.warning(self, "Error", "No item selected to update!")
            return

        selected_item = self.itemsSelect.currentText()
        item_subtype = self.itemtype.currentText() if selected_item != "Optical Accessory" else self.opticalAccessoryName.text()

        try:
            unit_price = float(self.itemAmount.text())  # Ensure it's a valid float
            stock_level = int(self.itemquant.text())  # Ensure it's a valid integer
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numeric values for price and quantity.")
            return

        # Prepare the updated data
        data = {
            "item_type": selected_item,
            "item_subtype": item_subtype,
            "unit_price": unit_price,
            "stock_level": stock_level,
        }

        try:
            # Send a PUT request to update the item
            response = requests.put(f"http://127.0.0.1:8000/auth/inventory/update/{self.item_id}/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item updated successfully!")
                self.load_table_data()  # Reload the table with updated data
            else:
                QMessageBox.critical(self, "Error", f"Failed to update item: {response.json().get('error', '')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventorySystem()
    window.show()
    sys.exit(app.exec())





# selected_item = self.items_types.currentText()

                # if selected_item == "Frame":
                #     self.items_types.clear()
                #     self.items_types.addItems(["VIP", "VIP+", "VIP++", "CLASSIC"])
                    
                    
                #     self.label_9.setText(f"VIP Total: {float(item_type_totals.get('VIP', 0.0)):.2f}")
                #     self.label_9.setVisible(True)
                    
                #     self.label_10.setText("Total VIP+ Amount:")
                #     self.label_10.setVisible(True)
                    
                #     self.label_11.setText("Total VIP++: Amount")
                #     self.label_11.setVisible(True)
                    
                #     self.label_12.setText("Total Classique Amount:")
                #     self.label_12.setVisible(True)

                # elif selected_item == "Lens":
                #     self.items_types.clear()
                #     self.items_types.addItems([
                #         "Simple Vision", "Progressive Stock",
                #         "Progressive Commande", "Bi-focaux"
                #     ])

                                        
                #     self.label_9.setText("Total Simple Vision Amount:")
                #     self.label_9.setVisible(True)
                    
                #     self.label_10.setText("Total Progressive Stock Amount:")
                #     self.label_10.setVisible(True)
                    
                #     self.label_11.setText("Total Progressive Commande Amount:")
                #     self.label_11.setVisible(True)
                    
                #     self.label_12.setText("Bi-focaux Amount:")
                #     self.label_12.setVisible(True)
                              
                #     # self.label_7.hide()
                # elif selected_item == "Optical Accessory":
                #     # Hide the ComboBox and use a label instead for Optical Accessory
                #     # self.items_types.hide()
                #     # self.label.hide()
                #     self.items_types.setVisible(False)
                    
                #     self.label.setVisible(False)
                    
                #     self.label_9.setText("Total OPticalAccessory Amount:")
                #     self.label_9.setVisible(True)
                    
                    
                #     self.label_10.setVisible(False)
                    
                #     self.label_11.setVisible(False)
                    
                #     self.label_12.setVisible(False)         
                    
                    


import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from ui_item_inventorys5 import Ui_MainWindow


class InventorySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set default items in the comboBox
        self.itemsSelect.addItems(["Frame", "Lens", "Optical Accessory"])
        self.itemsSelect.currentTextChanged.connect(self.update_item_types_and_table)

        # Connect buttons to functionalities
        self.pushButton_2.clicked.connect(self.add_item)  # Add button
        self.pushButton.clicked.connect(self.delete_item)  # Delete button
        self.pushButton_7.clicked.connect(self.clear_form)  # Clear form
        self.pushButton_8.clicked.connect(self.update_item)  # Update button
        self.pushButton_9.clicked.connect(self.show_monthly_entries_sales)  # Monthly report button

        self.tableWidget.itemSelectionChanged.connect(self.populate_form_with_selected_item)

        # Load initial data
        self.update_item_types_and_table()

    def show_monthly_entries_sales(self):
        """Open the Monthly Entries/Sales window."""
        # self.monthly_entries_sales_window = MonthlyEntriesSales()
        self.monthly_entries_sales_window.show()

    def update_item_types_and_table(self):
        """Update item types and table data based on the selected category."""
        self.update_item_types()
        self.load_table_data()
        self.calculate_totals()  # Ensure totals are recalculated every time an item is selected

    def update_item_types(self):
        """Update item types dynamically based on the selected category."""
        selected_item = self.itemsSelect.currentText()

        # Ensure the ComboBox is visible by default
        self.itemtype.setVisible(True)
        self.label_3.setText("Amount:")  # Reset label text

        if selected_item == "Frame":
            self.itemtype.clear()
            self.itemtype.addItems(["VIP", "VIP+", "VIP++", "CLASSIC"])
        elif selected_item == "Lens":
            self.itemtype.clear()
            self.itemtype.addItems([
                "Simple Vision", "Progressive Stock",
                "Progressive Commande", "Bi-focaux"
            ])
        else:  # Optical Accessory
            self.itemtype.clear()
            self.itemtype.setVisible(False)  # Hide the item type comboBox for Optical Accessory

    def add_item(self):
        """Add a new item to the inventory."""
        selected_item = self.itemsSelect.currentText()
        item_subtype = self.itemtype.currentText() if selected_item != "Optical Accessory" else self.opticalAccessoryName.text()

        try:
            unit_price = float(self.itemAmount.text())
            stock_level = int(self.itemquant.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numeric values for price and quantity.")
            return

        if not item_subtype and selected_item != "Optical Accessory":
            QMessageBox.warning(self, "Error", "Please select an item type!")
            return

        # Prepare the data
        data = {
            "item_type": selected_item,
            "item_subtype": item_subtype,
            "unit_price": unit_price,
            "stock_level": stock_level,
        }

        try:
            response = requests.post("http://127.0.0.1:8000/auth/inventory/add/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item added successfully!✅")
                self.load_table_data()  # Refresh table
                self.calculate_totals()  # Refresh totals
            else:
                QMessageBox.critical(self, "Error", f"Failed to add item: {response.json().get('error', '')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def delete_item(self):
        """Delete the selected item from the inventory."""
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Error", "Please select an item to delete.")
            return

        # Get the selected item ID and type
        item_id = self.tableWidget.item(current_row, 0).text()
        selected_item = self.itemsSelect.currentText().lower()

        endpoint_map = {
            "frame": "frames",
            "lens": "lenses",
            "optical accessory": "accessories"
        }
        endpoint = endpoint_map.get(selected_item)

        try:
            response = requests.delete(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/delete/{item_id}/")
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item deleted successfully!✅")
                self.load_table_data()  # Refresh table
                self.calculate_totals()  # Refresh totals
            else:
                QMessageBox.critical(self, "Error", f"Failed to delete item: {response.json().get('error', '')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def update_item(self):
        """Update the selected item in the inventory."""
        if not hasattr(self, 'item_id'):
            QMessageBox.warning(self, "Error", "No item selected to update!")
            return

        selected_item = self.itemsSelect.currentText()
        item_subtype = self.itemtype.currentText() if selected_item != "Optical Accessory" else self.opticalAccessoryName.text()

        try:
            unit_price = float(self.itemAmount.text())
            stock_level = int(self.itemquant.text())
        except ValueError:
            QMessageBox.warning(self, "Error", "Please enter valid numeric values for price and quantity.")
            return

        # Prepare the updated data
        data = {
            "item_type": selected_item,
            "item_subtype": item_subtype,
            "unit_price": unit_price,
            "stock_level": stock_level,
        }

        try:
            response = requests.put(f"http://127.0.0.1:8000/auth/inventory/update/{self.item_id}/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item updated successfully!✅")
                self.load_table_data()  # Refresh table
                self.calculate_totals()  # Refresh totals
            else:
                QMessageBox.critical(self, "Error", f"Failed to update item: {response.json().get('error', '')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def calculate_totals(self):
        """Calculate and display the total stock, total price, and stock levels for each type."""
        self.load_table_data()  # Ensure the table is refreshed before recalculating totals
