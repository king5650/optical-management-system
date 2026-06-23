# import sys
# import os
# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# if project_root not in sys.path:
#     sys.path.insert(0, project_root)
# # ...existing code...

# import sys
# import requests
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QDockWidget, QTableWidget
# from ui_ux.inventory_system.ui_item_inventorys5 import Ui_MainWindow
# from PySide6.QtCore import Qt
# from django.db.models.functions import ExtractMonth

# from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
# # from ui_monthly_entries_sales import Ui_Form  # The UI file for Monthly Entries/Sales
# from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem
# from ui_ux.inventory_system.ui_monthly_entries_sales1 import Ui_Form
# from inventory_report import MonthlyEntriesSales

# from config_loader import BASE_URL
# response = requests.get(f'{BASE_URL}')
# #"http://127.0.0.1:8000/"  

# class InventorySystem(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)

#         # Set default items in the comboBox
#         self.itemsSelect.addItems(["Frame", "Lens", "Optical Accessory"])
#         self.itemsSelect.currentTextChanged.connect(self.update_item_types_and_table)

#         # Connect buttons to functionalities
#         self.pushButton_2.clicked.connect(self.add_item)  # Add button background-color: rgb(88, 162, 157);
#         self.pushButton.clicked.connect(self.delete_item)  # Delete button
#         self.pushButton_7.clicked.connect(self.clear_form)
#         self.pushButton_8.clicked.connect(self.update_item)
#         self.pushButton_9.clicked.connect(self.show_monthly_entries_sales)
        
#         self.tableWidget.itemSelectionChanged.connect(self.populate_form_with_selected_item)
        
#         # Load initial data for the default selected item
#         self.update_item_types_and_table()
        


#     def show_monthly_entries_sales(self):
#         """Open the Monthly Entries/Sales window."""
#         self.monthly_entries_sales_window = MonthlyEntriesSales()
#         self.monthly_entries_sales_window.show()

#     def update_item_types_and_table(self):
#         """Update item types and load the table data based on the selected category."""
#         self.update_item_types()
#         self.load_table_data()
#         self.calculate_totals()

#     def update_item_types(self):
#         """Update item types dynamically based on the selected category."""
#         selected_item = self.itemsSelect.currentText()

#         # Ensure the ComboBox is visible by default
#         self.itemtype.setVisible(True)
#         self.label_3.setText("Amount:")  # Reset label text

#         if selected_item == "Frame":
#             self.itemtype.clear()
#             self.itemtype.addItems(["VIP", "VIP+", "VIP++", "CLASSIC"])
            
#             self.label.setText("Item Type:")
#             self.label.setVisible(True)
            
#             self.label_9.setText("Total VIP:")
#             self.label_9.setVisible(True)
            
#             self.label_11.setText("Total VIP+:")
#             self.label_11.setVisible(True)
            
#             self.label_13.setText("Total VIP++:")
#             self.label_13.setVisible(True)
            
#             self.label_15.setText("Total Classique:")
#             self.label_15.setVisible(True)
            
            
            
#             self.opticalAccessoryName.setVisible(False)
#             self.label_7.setVisible(False)             
#             # self.label_7.hide()
#         elif selected_item == "Lens":
#             self.itemtype.clear()
#             self.itemtype.addItems([
#                 "Simple Vision", "Progressive Stock",
#                 "Progressive Commande", "Bi-focaux"
#             ])
#             self.label.setText("Item Type:")
#             self.label.setVisible(True)
            
            
#             self.label_9.setText("Total Simple Vision:")
#             self.label_9.setVisible(True)
            
#             self.label_11.setText("Total Progressive Stock:")
#             self.label_11.setVisible(True)
            
#             self.label_13.setText("Total Progressive Commande:")
#             self.label_13.setVisible(True)
            
#             self.label_15.setText("Bi-focaux:")
#             self.label_15.setVisible(True)
            
#             self.opticalAccessoryName.setVisible(False)
#             self.label_7.setVisible(False)            
#             # self.label_7.hide()
#         elif selected_item == "Optical Accessory":
#             # Hide the ComboBox and use a label instead for Optical Accessory
#             # self.itemtype.hide()
#             # self.label.hide()
#             self.itemtype.setVisible(False)
            
#             self.label.setVisible(False)
            
#             self.label_9.setText("Total OPticalAccessory:")
#             self.label_9.setVisible(True)
            
            
#             self.label_11.setText("Total Progressive Stock:")
#             self.label_11.setVisible(False)
            
#             self.label_13.setText("Total Progressive Commande:")
#             self.label_13.setVisible(False)
            
#             self.label_15.setText("Total Bi-focaux:")
#             self.label_15.setVisible(False)         
            
            
#             self.label_11.setText("Total VIP+:")
#             self.label_11.setVisible(False)
            
#             self.label_13.setText("Total VIP++:")
#             self.label_13.setVisible(False)
            
#             self.label_15.setText("Total Classique:")
#             self.label_15.setVisible(False)   
        
            
#             self.label_11.setText("Total Progressive Commande:")
#             self.label_11.setVisible(False)
            
#             self.label_13.setText("Total Bi-focaux:")
#             self.label_13.setVisible(False)         
            
            
#             self.label_15.setText("Total VIP+:")
#             self.label_15.setVisible(False)
            

            
#             self.label_7.setText("optical Accessory Name:")
#             self.opticalAccessoryName.setVisible(True)
#             self.label_7.setVisible(True)
            

#     def add_item(self):
#         """Add a new item to the inventory."""
#         selected_item = self.itemsSelect.currentText()
#         item_subtype = self.itemtype.currentText() if selected_item != "Optical Accessory" else self.opticalAccessoryName.text()

#         try:
#             unit_price = float(self.itemAmount.text())  # Ensure it's a valid float
#             stock_level = int(self.itemquant.text())  # Ensure it's a valid integer
#         except ValueError:
#             QMessageBox.warning(self, "Error", "Please enter valid numeric values for price and quantity.")
#             return

#         if not item_subtype and selected_item != "Optical Accessory":
#             QMessageBox.warning(self, "Error", "Please select an item type!")
#             return

#         # Prepare the data
#         data = {
#             "item_type": selected_item,
#             "item_subtype": item_subtype if selected_item != "Optical Accessory" else self.opticalAccessoryName.text(),
#             "unit_price": unit_price,
#             "stock_level": stock_level,
#         }

#         try:
#             response = requests.post(f"{BASE_URL}/inventory/add/", json=data)
#             if response.status_code == 200:
#                 QMessageBox.information(self, "Success", "Item added successfully!✅")
#                 self.load_table_data()  # Reload the table with updated data
#                 self.calculate_totals() 
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
#             response = requests.get(f"{BASE_URL}/inventory/{endpoint}/list/")
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
            
#     def delete_item(self):
#         """Delete the selected item from the inventory."""
#         current_row = self.tableWidget.currentRow()
#         if current_row < 0:
#             QMessageBox.warning(self, "Error", "Please select an item to delete.")
#             return

#         # Get the selected item ID and type
#         item_id = self.tableWidget.item(current_row, 0).text()
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
#             # Make a DELETE request to the server
#             response = requests.delete(f"{BASE_URL}/inventory/{endpoint}/delete/{item_id}/")
#             if response.status_code == 200:
#                 QMessageBox.information(self, "Success", "Item deleted successfully!✅")
#                 self.load_table_data()  # Reload the table with updated data
#                 self.calculate_totals() 
#             else:
#                 QMessageBox.critical(self, "Error", f"Failed to delete item: {response.json().get('error', '')}")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")
            
#     def clear_form(self):
#         self.opticalAccessoryName.clear()
#         self.itemAmount.clear()
#         self.itemquant.clear()
        
        
        
#     def populate_form_with_selected_item(self):
#         """Populate the form with the selected item details for updating."""
#         current_row = self.tableWidget.currentRow()
#         if current_row < 0:
#             return  # No row selected

#         # Retrieve data from the selected row
#         self.item_id = self.tableWidget.item(current_row, 0).text()
#         item_name_or_type = self.tableWidget.item(current_row, 1).text()
#         stock_level = self.tableWidget.item(current_row, 2).text()
#         unit_price = self.tableWidget.item(current_row, 3).text()

#         # Check the selected item type
#         selected_item = self.itemsSelect.currentText()

#         if selected_item == "Optical Accessory":
#             # Show the QLineEdit for Optical Accessory
#             self.opticalAccessoryName.setVisible(True)
#             self.label_7.setVisible(True)
#             self.opticalAccessoryName.setText(item_name_or_type)

#             # Hide the ComboBox for item type
#             self.itemtype.setVisible(False)
#             self.label.setVisible(False)
#         else:
#             # Show the ComboBox for item type
#             self.itemtype.setVisible(True)
#             self.label.setVisible(True)
#             self.itemtype.setCurrentText(item_name_or_type)

#             # Hide the QLineEdit for Optical Accessory
#             self.opticalAccessoryName.setVisible(False)
#             self.label_7.setVisible(False)

#         # Set stock level and unit price
#         self.itemquant.setText(stock_level)
#         self.itemAmount.setText(unit_price)

        
#     def update_item(self):
#         """Update the selected item in the inventory."""
#         if not hasattr(self, 'item_id'):
#             QMessageBox.warning(self, "Error", "No item selected to update!")
#             return

#         selected_item = self.itemsSelect.currentText()
#         item_subtype = (
#             self.itemtype.currentText() if selected_item != "Optical Accessory" else self.opticalAccessoryName.text()
#         )

#         try:
#             unit_price = float(self.itemAmount.text())  # Ensure it's a valid float
#             stock_level = int(self.itemquant.text())  # Ensure it's a valid integer
#         except ValueError:
#             QMessageBox.warning(self, "Error", "Please enter valid numeric values for price and quantity.")
#             return

#         # Prepare the updated data
#         data = {
#             "item_type": selected_item,
#             "item_subtype": item_subtype,
#             "unit_price": unit_price,
#             "stock_level": stock_level,
#         }
#             # Prepare the updated data

#         # Debugging: Log the data being sent
#         print(f"Updating item with ID: {self.item_id}")
#         print("Data being sent:", data)

#         try:
#             # Send a PUT request to update the item
#             response = requests.put(f"{BASE_URL}/inventory/update/{self.item_id}/", json=data)
#             if response.status_code == 200:
#                 QMessageBox.information(self, "Success", "Item updated successfully!✅")
#                 self.load_table_data()  # Reload the table with updated data
#                 self.calculate_totals() 
#             else:
#                 QMessageBox.critical(self, "Error", f"Failed to update item: {response.json().get('error', '')}")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")



#     def calculate_totals(self):
#         """Calculate and display the total stock, total price, and stock levels for each type."""
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
#             # Make a GET request to the totals endpoint
#             response = requests.get(f"{BASE_URL}/inventory/{endpoint}/totals/")
#             if response.status_code == 200:
#                 totals = response.json()
#                 total_stock = totals.get("total_stock", 0)
#                 total_price = totals.get("total_price", 0.0)
#                 stock_by_type = totals.get("stock_by_type", {})

#                 # Update total stock and total price labels
#                 self.label_5.setText(f"Total Stock: {total_stock}")
#                 self.label_6.setText(f"Total Price: {total_price:,.2f}")

#                 # Update stock levels for each type
#                 type_labels = [self.label_9, self.label_11, self.label_13, self.label_15]
#                 for label, (item_type, stock) in zip(type_labels, stock_by_type.items()):
#                     label.setText(f"{item_type}: {stock}")

#                 # Hide unused labels if there are fewer subtypes
#                 for label in type_labels[len(stock_by_type):]:
#                     label.setText("")
#             else:
#                 QMessageBox.warning(self, "Error", f"Failed to fetch totals: {response.json().get('error', 'Unknown error')}")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")
            
            
#     def show_monthly_summary(self):
#         """Fetch and display the monthly summary in a dock widget."""
#         try:
#             response = requests.get(f"{BASE_URL}/inventory/monthly-summary/")
#             if response.status_code == 200:
#                 data = response.json()
#                 self.display_monthly_summary(data)
#             else:
#                 QMessageBox.warning(self, "Error", f"Failed to fetch monthly summary: {response.json().get('error', 'Unknown error')}")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")
            
            

# # Import the Monthly Entries/Sales UI


# # class MonthlyEntriesSales(QMainWindow):
# #     def __init__(self):
# #         super().__init__()

# #         # Create a new QWidget and set it as the central widget
# #         self.central_widget = QWidget(self)
# #         self.setCentralWidget(self.central_widget)

# #         # Set up the UI on the new QWidget
# #         self.ui = Ui_Form()
# #         self.ui.setupUi(self.central_widget)

# #         # Populate comboboxes
# #         self.ui.months.addItems([
# #             "January", "February", "March", "April", "May", "June",
# #             "July", "August", "September", "October", "November", "December"
# #         ])
# #         self.ui.sale_entries.addItems(["Sale", "Entry"])
# #         self.ui.items.addItems(["Frame", "Lens", "Optical Accessory"])

# #         # Connect signals
# #         self.ui.items.currentTextChanged.connect(self.update_item_types)
# #         self.ui.sale_entries.currentTextChanged.connect(self.filter_monthly_data)
# #         self.ui.months.currentTextChanged.connect(self.filter_monthly_data)

# #         # Update item types when the window opens
# #         self.update_item_types()

# #     def update_item_types(self):
# #         """Update item types dynamically based on the selected item."""
# #         selected_item = self.ui.items.currentText()
# #         self.ui.items_types.clear()

# #         if selected_item == "Frame":
# #             self.ui.items_types.addItems(["VIP", "VIP+", "VIP++", "CLASSIC"])
# #         elif selected_item == "Lens":
# #             self.ui.items_types.addItems([
# #                 "Simple Vision", "Progressive Stock", "Progressive Commande", "Bi-focaux"
# #             ])
# #         elif selected_item == "Optical Accessory":
# #             self.ui.items_types.addItems(["All"])

# #     def filter_monthly_data(self):
# #         """Filter and display data based on selected month, year, item, and sale/entry."""
# #         selected_month = self.ui.months.currentText()
# #         selected_item = self.ui.items.currentText().lower()
# #         selected_item_type = self.ui.items_types.currentText()
# #         sale_or_entry = self.ui.sale_entries.currentText().lower()

# #         if not selected_month or not selected_item or not sale_or_entry:
# #             QMessageBox.warning(self, "Error", "Please select all fields (Month, Item, Sale/Entry).")
# #             return

# #         month_mapping = {
# #             "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
# #             "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
# #         }
# #         month_number = month_mapping.get(selected_month)

# #         endpoint_map = {
# #             "sale": "sales",
# #             "entry": "entries"
# #         }
# #         endpoint = endpoint_map.get(sale_or_entry)
# #         if not endpoint:
# #             QMessageBox.warning(self, "Error", "Invalid selection for Sale/Entry.")
# #             return

# #         try:
# #             # Log the request parameters for debugging
# #             print("Request URL:", f"http://127.0.0.1:8000/auth/inventory/{endpoint}/")
# #             print("Request Params:", {"month": month_number, "item": selected_item, "item_type": selected_item_type})

# #             response = requests.get(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/",
# #                                     params={"month": month_number, "item": selected_item, "item_type": selected_item_type})
            
# #             print("Response Status Code:", response.status_code)
# #             print("Response Text:", response.text)  # Debugging: Log the response text

# #             if response.status_code == 200:
# #                 try:
# #                     data = response.json().get("items", [])
# #                 except ValueError:
# #                     QMessageBox.critical(self, "Error", "Server returned invalid JSON or no data.")
# #                     return

# #                 self.ui.tableWidget.setRowCount(0)  # Clear existing rows
# #                 for row_data in data:
# #                     row = self.ui.tableWidget.rowCount()
# #                     self.ui.tableWidget.insertRow(row)
# #                     self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(row_data["month"])))
# #                     self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(row_data["item"]))
# #                     self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(row_data["item_type"]))
# #                     self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(f"{row_data['price']:.2f}"))
# #                     self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(row_data["quantity"])))

# #                 global_amount = sum(row_data["price"] * row_data["quantity"] for row_data in data)
# #                 self.ui.globalamount.setText(f"Total: {global_amount:.2f} CFA")
# #             else:
# #                 QMessageBox.warning(self, "Error", f"Failed to retrieve data: {response.json().get('error', 'Unknown error')}")
# #         except requests.exceptions.RequestException as e:
# #             QMessageBox.critical(self, "Error", f"Server error: {e}")


            
            
            


#     # def display_monthly_summary(self, data):
#     #     """Display the monthly summary in a dock widget."""
#     #     dock = QDockWidget("Monthly Summary", self)
#     #     dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

#     #     table = QTableWidget()
#     #     table.setColumnCount(4)
#     #     table.setHorizontalHeaderLabels(["Month", "Item Type", "Total Quantity", "Total Price"])
#     #     dock.setWidget(table)
#     #     self.addDockWidget(Qt.RightDockWidgetArea, dock)

#     #     # Populate the table with data
#     #     all_data = data["frames"] + data["lenses"] + data["accessories"]
#     #     table.setRowCount(len(all_data))

#     #     for row, item in enumerate(all_data):
#     #         table.setItem(row, 0, QTableWidgetItem(item["month"]))
#     #         table.setItem(row, 1, QTableWidgetItem(item.get("frame_type") or item.get("lens_type") or item.get("name")))
#     #         table.setItem(row, 2, QTableWidgetItem(str(item["total_quantity"])))
#     #         table.setItem(row, 3, QTableWidgetItem(f"{item['total_price']}"))
#     # def load_monthly_summary(self):
#     #     """Fetch and display the monthly summary in the dock widget."""
#     #     try:
#     #         # Make a GET request to fetch the summary
#     #         response = requests.get("http://127.0.0.1:8000/auth/inventory/monthly-summary/")
#     #         if response.status_code == 200:
#     #             summary_data = response.json()

#     #             # Clear existing rows in the table
#     #             self.dockTableWidget.setRowCount(0)

#     #             # Add frame data
#     #             for frame in summary_data.get("frames", []):
#     #                 row = self.dockTableWidget.rowCount()
#     #                 self.dockTableWidget.insertRow(row)

#     #                 self.dockTableWidget.setItem(row, 0, QTableWidgetItem("Frame"))
#     #                 self.dockTableWidget.setItem(row, 1, QTableWidgetItem(frame["frame_type"]))
#     #                 self.dockTableWidget.setItem(row, 2, QTableWidgetItem(f"{frame['month']}/{frame['year']}"))
#     #                 self.dockTableWidget.setItem(row, 3, QTableWidgetItem(str(frame["total_quantity"])))
#     #                 self.dockTableWidget.setItem(row, 4, QTableWidgetItem(f"{frame['total_price']:.2f}"))

#     #             # Add lens data
#     #             for lens in summary_data.get("lenses", []):
#     #                 row = self.dockTableWidget.rowCount()
#     #                 self.dockTableWidget.insertRow(row)

#     #                 self.dockTableWidget.setItem(row, 0, QTableWidgetItem("Lens"))
#     #                 self.dockTableWidget.setItem(row, 1, QTableWidgetItem(lens["lens_type"]))
#     #                 self.dockTableWidget.setItem(row, 2, QTableWidgetItem(f"{lens['month']}/{lens['year']}"))
#     #                 self.dockTableWidget.setItem(row, 3, QTableWidgetItem(str(lens["total_quantity"])))
#     #                 self.dockTableWidget.setItem(row, 4, QTableWidgetItem(f"{lens['total_price']:.2f}"))

#     #             # Add accessory data
#     #             for accessory in summary_data.get("accessories", []):
#     #                 row = self.dockTableWidget.rowCount()
#     #                 self.dockTableWidget.insertRow(row)

#     #                 self.dockTableWidget.setItem(row, 0, QTableWidgetItem("Optical Accessory"))
#     #                 self.dockTableWidget.setItem(row, 1, QTableWidgetItem(accessory["name"]))
#     #                 self.dockTableWidget.setItem(row, 2, QTableWidgetItem(f"{accessory['month']}/{accessory['year']}"))
#     #                 self.dockTableWidget.setItem(row, 3, QTableWidgetItem(str(accessory["total_quantity"])))
#     #                 self.dockTableWidget.setItem(row, 4, QTableWidgetItem(f"{accessory['total_price']:.2f}"))

#     #         else:
#     #             QMessageBox.warning(self, "Error", f"Failed to fetch data: {response.json().get('error', 'Unknown error')}")
#     #     except requests.exceptions.RequestException as e:
#     #         QMessageBox.critical(self, "Error", f"Server error: {e}")



#     # Other methods like update_item_types_and_table, add_item, delete_item, etc., remain unchanged.


#     # def calculate_totals(self):
#     #     """Calculate and display the total stock and price for the selected item type."""
#     #     selected_item = self.itemsSelect.currentText().lower()
        
#     #     # Map the selected item to the corresponding API endpoint
#     #     endpoint_map = {
#     #         "frame": "frames",
#     #         "lens": "lenses",
#     #         "optical accessory": "accessories"
#     #     }
#     #     endpoint = endpoint_map.get(selected_item)

#     #     if not endpoint:
#     #         QMessageBox.warning(self, "Error", "Invalid item type selected.")
#     #         return

#     #     try:
#     #         # Make a GET request to the totals endpoint
#     #         response = requests.get(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/totals/")
#     #         if response.status_code == 200:
#     #             totals = response.json()
#     #             total_stock = totals.get("total_stock", 0)
#     #             total_price = totals.get("total_price", 0.0)

#     #             # Update UI labels with totals
#     #             self.label_5.setText(f"Total Stock: {total_stock}")
#     #             self.totalstockLabel.setText(" hello world")
                
#     #             self.label_6.setText(f"Total Price: {total_price:.2f}")
#     #         else:
#     #             QMessageBox.warning(self, "Error", f"Failed to fetch totals: {response.json().get('error', 'Unknown error')}")
#     #     except requests.exceptions.RequestException as e:
#     #         QMessageBox.critical(self, "Error", f"Server error: {e}")







# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = InventorySystem()
#     window.show()
#     sys.exit(app.exec())

import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)
# ...existing code...

import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QDockWidget, QTableWidget
from ui_ux.inventory_system.ui_item_inventorys5 import Ui_MainWindow
from PySide6.QtCore import Qt

from PySide6.QtWidgets import QMainWindow, QTableWidgetItem
# from ui_monthly_entries_sales import Ui_Form  # The UI file for Monthly Entries/Sales
from PySide6.QtWidgets import QMainWindow, QWidget, QTableWidgetItem
from ui_ux.inventory_system.ui_monthly_entries_sales1 import Ui_Form
from inventory_report import MonthlyEntriesSales

from config_loader import BASE_URL

class InventorySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set default items in the comboBox
        self.itemsSelect.addItems(["Frame", "Lens", "Optical Accessory"])
        self.itemsSelect.currentTextChanged.connect(self.update_item_types_and_table)

        # Connect buttons to functionalities
        self.pushButton_2.clicked.connect(self.add_item)  # Add button background-color: rgb(88, 162, 157);
        self.pushButton.clicked.connect(self.delete_item)  # Delete button
        self.pushButton_7.clicked.connect(self.clear_form)
        self.pushButton_8.clicked.connect(self.update_item)
        self.pushButton_9.clicked.connect(self.show_monthly_entries_sales)
        
        self.tableWidget.itemSelectionChanged.connect(self.populate_form_with_selected_item)
        
        # Load initial data for the default selected item
        self.update_item_types_and_table()
        


    def show_monthly_entries_sales(self):
        """Open the Monthly Entries/Sales window."""
        self.monthly_entries_sales_window = MonthlyEntriesSales()
        self.monthly_entries_sales_window.show()

    def update_item_types_and_table(self):
        """Update item types and load the table data based on the selected category."""
        self.update_item_types()
        self.load_table_data()
        self.calculate_totals()

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
            
            self.label_9.setText("Total VIP:")
            self.label_9.setVisible(True)
            
            self.label_11.setText("Total VIP+:")
            self.label_11.setVisible(True)
            
            self.label_13.setText("Total VIP++:")
            self.label_13.setVisible(True)
            
            self.label_15.setText("Total Classique:")
            self.label_15.setVisible(True)
            
            
            
            self.opticalAccessoryName.setVisible(False)
            self.label_7.setVisible(False)             
            # self.label_7.hide()
        elif selected_item == "Lens":
            self.itemtype.clear()
            self.itemtype.addItems([
                "Simple Vision", "Progressive Stock",
                "Progressive Commande", "Bi-focaux"
            ])
            self.label.setText("Item Type:")
            self.label.setVisible(True)
            
            
            self.label_9.setText("Total Simple Vision:")
            self.label_9.setVisible(True)
            
            self.label_11.setText("Total Progressive Stock:")
            self.label_11.setVisible(True)
            
            self.label_13.setText("Total Progressive Commande:")
            self.label_13.setVisible(True)
            
            self.label_15.setText("Bi-focaux:")
            self.label_15.setVisible(True)
            
            self.opticalAccessoryName.setVisible(False)
            self.label_7.setVisible(False)            
            # self.label_7.hide()
        elif selected_item == "Optical Accessory":
            # Hide the ComboBox and use a label instead for Optical Accessory
            # self.itemtype.hide()
            # self.label.hide()
            self.itemtype.setVisible(False)
            
            self.label.setVisible(False)
            
            self.label_9.setText("Total OPticalAccessory:")
            self.label_9.setVisible(True)
            
            
            self.label_11.setText("Total Progressive Stock:")
            self.label_11.setVisible(False)
            
            self.label_13.setText("Total Progressive Commande:")
            self.label_13.setVisible(False)
            
            self.label_15.setText("Total Bi-focaux:")
            self.label_15.setVisible(False)         
            
            
            self.label_11.setText("Total VIP+:")
            self.label_11.setVisible(False)
            
            self.label_13.setText("Total VIP++:")
            self.label_13.setVisible(False)
            
            self.label_15.setText("Total Classique:")
            self.label_15.setVisible(False)   
        
            
            self.label_11.setText("Total Progressive Commande:")
            self.label_11.setVisible(False)
            
            self.label_13.setText("Total Bi-focaux:")
            self.label_13.setVisible(False)         
            
            
            self.label_15.setText("Total VIP+:")
            self.label_15.setVisible(False)
            

            
            self.label_7.setText("optical Accessory Name:")
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
            "item_subtype": item_subtype if selected_item != "Optical Accessory" else self.opticalAccessoryName.text(),
            "unit_price": unit_price,
            "stock_level": stock_level,
        }

        try:
            response = requests.post(f"{BASE_URL}/inventory/add/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item added successfully!✅")
                self.load_table_data()  # Reload the table with updated data
                self.calculate_totals() 
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
            response = requests.get(f"{BASE_URL}/inventory/{endpoint}/list/")
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
            
    def delete_item(self):
        """Delete the selected item from the inventory."""
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Error", "Please select an item to delete.")
            return

        # Get the selected item ID and type
        item_id = self.tableWidget.item(current_row, 0).text()
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
            # Make a DELETE request to the server
            response = requests.delete(f"{BASE_URL}/inventory/{endpoint}/delete/{item_id}/")
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item deleted successfully!✅")
                self.load_table_data()  # Reload the table with updated data
                self.calculate_totals() 
            else:
                QMessageBox.critical(self, "Error", f"Failed to delete item: {response.json().get('error', '')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")
            
    def clear_form(self):
        self.opticalAccessoryName.clear()
        self.itemAmount.clear()
        self.itemquant.clear()
        
        
        
    def populate_form_with_selected_item(self):
        """Populate the form with the selected item details for updating."""
        current_row = self.tableWidget.currentRow()
        if current_row < 0:
            return  # No row selected

        # Retrieve data from the selected row
        self.item_id = self.tableWidget.item(current_row, 0).text()
        item_name_or_type = self.tableWidget.item(current_row, 1).text()
        stock_level = self.tableWidget.item(current_row, 2).text()
        unit_price = self.tableWidget.item(current_row, 3).text()

        # Check the selected item type
        selected_item = self.itemsSelect.currentText()

        if selected_item == "Optical Accessory":
            # Show the QLineEdit for Optical Accessory
            self.opticalAccessoryName.setVisible(True)
            self.label_7.setVisible(True)
            self.opticalAccessoryName.setText(item_name_or_type)

            # Hide the ComboBox for item type
            self.itemtype.setVisible(False)
            self.label.setVisible(False)
        else:
            # Show the ComboBox for item type
            self.itemtype.setVisible(True)
            self.label.setVisible(True)
            self.itemtype.setCurrentText(item_name_or_type)

            # Hide the QLineEdit for Optical Accessory
            self.opticalAccessoryName.setVisible(False)
            self.label_7.setVisible(False)

        # Set stock level and unit price
        self.itemquant.setText(stock_level)
        self.itemAmount.setText(unit_price)

        
    def update_item(self):
        """Update the selected item in the inventory."""
        if not hasattr(self, 'item_id'):
            QMessageBox.warning(self, "Error", "No item selected to update!")
            return

        selected_item = self.itemsSelect.currentText()
        item_subtype = (
            self.itemtype.currentText() if selected_item != "Optical Accessory" else self.opticalAccessoryName.text()
        )

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
            # Prepare the updated data

        # Debugging: Log the data being sent
        print(f"Updating item with ID: {self.item_id}")
        print("Data being sent:", data)

        try:
            # Send a PUT request to update the item
            response = requests.put(f"{BASE_URL}/inventory/update/{self.item_id}/", json=data)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item updated successfully!✅")
                self.load_table_data()  # Reload the table with updated data
                self.calculate_totals() 
            else:
                QMessageBox.critical(self, "Error", f"Failed to update item: {response.json().get('error', '')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")



    def calculate_totals(self):
        """Calculate and display the total stock, total price, and stock levels for each type."""
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
            # Make a GET request to the totals endpoint
            response = requests.get(f"{BASE_URL}/inventory/{endpoint}/totals/")
            if response.status_code == 200:
                totals = response.json()
                total_stock = totals.get("total_stock", 0)
                total_price = totals.get("total_price", 0.0)
                stock_by_type = totals.get("stock_by_type", {})

                # Update total stock and total price labels
                self.label_5.setText(f"Total Stock: {total_stock}")
                self.label_6.setText(f"Total Price: {total_price:,.2f}")

                # Update stock levels for each type
                type_labels = [self.label_9, self.label_11, self.label_13, self.label_15]
                for label, (item_type, stock) in zip(type_labels, stock_by_type.items()):
                    label.setText(f"{item_type}: {stock}")

                # Hide unused labels if there are fewer subtypes
                for label in type_labels[len(stock_by_type):]:
                    label.setText("")
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch totals: {response.json().get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")
            
            
    def show_monthly_summary(self):
        """Fetch and display the monthly summary in a dock widget."""
        try:
            response = requests.get(f"{BASE_URL}/inventory/monthly-summary/")
            if response.status_code == 200:
                data = response.json()
                self.display_monthly_summary(data)
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch monthly summary: {response.json().get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")
            
            

# Import the Monthly Entries/Sales UI


# class MonthlyEntriesSales(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Create a new QWidget and set it as the central widget
#         self.central_widget = QWidget(self)
#         self.setCentralWidget(self.central_widget)

#         # Set up the UI on the new QWidget
#         self.ui = Ui_Form()
#         self.ui.setupUi(self.central_widget)

#         # Populate comboboxes
#         self.ui.months.addItems([
#             "January", "February", "March", "April", "May", "June",
#             "July", "August", "September", "October", "November", "December"
#         ])
#         self.ui.sale_entries.addItems(["Sale", "Entry"])
#         self.ui.items.addItems(["Frame", "Lens", "Optical Accessory"])

#         # Connect signals
#         self.ui.items.currentTextChanged.connect(self.update_item_types)
#         self.ui.sale_entries.currentTextChanged.connect(self.filter_monthly_data)
#         self.ui.months.currentTextChanged.connect(self.filter_monthly_data)

#         # Update item types when the window opens
#         self.update_item_types()

#     def update_item_types(self):
#         """Update item types dynamically based on the selected item."""
#         selected_item = self.ui.items.currentText()
#         self.ui.items_types.clear()

#         if selected_item == "Frame":
#             self.ui.items_types.addItems(["VIP", "VIP+", "VIP++", "CLASSIC"])
#         elif selected_item == "Lens":
#             self.ui.items_types.addItems([
#                 "Simple Vision", "Progressive Stock", "Progressive Commande", "Bi-focaux"
#             ])
#         elif selected_item == "Optical Accessory":
#             self.ui.items_types.addItems(["All"])

#     def filter_monthly_data(self):
#         """Filter and display data based on selected month, year, item, and sale/entry."""
#         selected_month = self.ui.months.currentText()
#         selected_item = self.ui.items.currentText().lower()
#         selected_item_type = self.ui.items_types.currentText()
#         sale_or_entry = self.ui.sale_entries.currentText().lower()

#         if not selected_month or not selected_item or not sale_or_entry:
#             QMessageBox.warning(self, "Error", "Please select all fields (Month, Item, Sale/Entry).")
#             return

#         month_mapping = {
#             "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
#             "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
#         }
#         month_number = month_mapping.get(selected_month)

#         endpoint_map = {
#             "sale": "sales",
#             "entry": "entries"
#         }
#         endpoint = endpoint_map.get(sale_or_entry)
#         if not endpoint:
#             QMessageBox.warning(self, "Error", "Invalid selection for Sale/Entry.")
#             return

#         try:
#             # Log the request parameters for debugging
#             print("Request URL:", f"http://127.0.0.1:8000/auth/inventory/{endpoint}/")
#             print("Request Params:", {"month": month_number, "item": selected_item, "item_type": selected_item_type})

#             response = requests.get(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/",
#                                     params={"month": month_number, "item": selected_item, "item_type": selected_item_type})
            
#             print("Response Status Code:", response.status_code)
#             print("Response Text:", response.text)  # Debugging: Log the response text

#             if response.status_code == 200:
#                 try:
#                     data = response.json().get("items", [])
#                 except ValueError:
#                     QMessageBox.critical(self, "Error", "Server returned invalid JSON or no data.")
#                     return

#                 self.ui.tableWidget.setRowCount(0)  # Clear existing rows
#                 for row_data in data:
#                     row = self.ui.tableWidget.rowCount()
#                     self.ui.tableWidget.insertRow(row)
#                     self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(row_data["month"])))
#                     self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(row_data["item"]))
#                     self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(row_data["item_type"]))
#                     self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(f"{row_data['price']:.2f}"))
#                     self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(row_data["quantity"])))

#                 global_amount = sum(row_data["price"] * row_data["quantity"] for row_data in data)
#                 self.ui.globalamount.setText(f"Total: {global_amount:.2f} CFA")
#             else:
#                 QMessageBox.warning(self, "Error", f"Failed to retrieve data: {response.json().get('error', 'Unknown error')}")
#         except requests.exceptions.RequestException as e:
#             QMessageBox.critical(self, "Error", f"Server error: {e}")


            
            
            


    # def display_monthly_summary(self, data):
    #     """Display the monthly summary in a dock widget."""
    #     dock = QDockWidget("Monthly Summary", self)
    #     dock.setAllowedAreas(Qt.LeftDockWidgetArea | Qt.RightDockWidgetArea)

    #     table = QTableWidget()
    #     table.setColumnCount(4)
    #     table.setHorizontalHeaderLabels(["Month", "Item Type", "Total Quantity", "Total Price"])
    #     dock.setWidget(table)
    #     self.addDockWidget(Qt.RightDockWidgetArea, dock)

    #     # Populate the table with data
    #     all_data = data["frames"] + data["lenses"] + data["accessories"]
    #     table.setRowCount(len(all_data))

    #     for row, item in enumerate(all_data):
    #         table.setItem(row, 0, QTableWidgetItem(item["month"]))
    #         table.setItem(row, 1, QTableWidgetItem(item.get("frame_type") or item.get("lens_type") or item.get("name")))
    #         table.setItem(row, 2, QTableWidgetItem(str(item["total_quantity"])))
    #         table.setItem(row, 3, QTableWidgetItem(f"{item['total_price']}"))
    # def load_monthly_summary(self):
    #     """Fetch and display the monthly summary in the dock widget."""
    #     try:
    #         # Make a GET request to fetch the summary
    #         response = requests.get("http://127.0.0.1:8000/auth/inventory/monthly-summary/")
    #         if response.status_code == 200:
    #             summary_data = response.json()

    #             # Clear existing rows in the table
    #             self.dockTableWidget.setRowCount(0)

    #             # Add frame data
    #             for frame in summary_data.get("frames", []):
    #                 row = self.dockTableWidget.rowCount()
    #                 self.dockTableWidget.insertRow(row)

    #                 self.dockTableWidget.setItem(row, 0, QTableWidgetItem("Frame"))
    #                 self.dockTableWidget.setItem(row, 1, QTableWidgetItem(frame["frame_type"]))
    #                 self.dockTableWidget.setItem(row, 2, QTableWidgetItem(f"{frame['month']}/{frame['year']}"))
    #                 self.dockTableWidget.setItem(row, 3, QTableWidgetItem(str(frame["total_quantity"])))
    #                 self.dockTableWidget.setItem(row, 4, QTableWidgetItem(f"{frame['total_price']:.2f}"))

    #             # Add lens data
    #             for lens in summary_data.get("lenses", []):
    #                 row = self.dockTableWidget.rowCount()
    #                 self.dockTableWidget.insertRow(row)

    #                 self.dockTableWidget.setItem(row, 0, QTableWidgetItem("Lens"))
    #                 self.dockTableWidget.setItem(row, 1, QTableWidgetItem(lens["lens_type"]))
    #                 self.dockTableWidget.setItem(row, 2, QTableWidgetItem(f"{lens['month']}/{lens['year']}"))
    #                 self.dockTableWidget.setItem(row, 3, QTableWidgetItem(str(lens["total_quantity"])))
    #                 self.dockTableWidget.setItem(row, 4, QTableWidgetItem(f"{lens['total_price']:.2f}"))

    #             # Add accessory data
    #             for accessory in summary_data.get("accessories", []):
    #                 row = self.dockTableWidget.rowCount()
    #                 self.dockTableWidget.insertRow(row)

    #                 self.dockTableWidget.setItem(row, 0, QTableWidgetItem("Optical Accessory"))
    #                 self.dockTableWidget.setItem(row, 1, QTableWidgetItem(accessory["name"]))
    #                 self.dockTableWidget.setItem(row, 2, QTableWidgetItem(f"{accessory['month']}/{accessory['year']}"))
    #                 self.dockTableWidget.setItem(row, 3, QTableWidgetItem(str(accessory["total_quantity"])))
    #                 self.dockTableWidget.setItem(row, 4, QTableWidgetItem(f"{accessory['total_price']:.2f}"))

    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch data: {response.json().get('error', 'Unknown error')}")
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")



    # Other methods like update_item_types_and_table, add_item, delete_item, etc., remain unchanged.


    # def calculate_totals(self):
    #     """Calculate and display the total stock and price for the selected item type."""
    #     selected_item = self.itemsSelect.currentText().lower()
        
    #     # Map the selected item to the corresponding API endpoint
    #     endpoint_map = {
    #         "frame": "frames",
    #         "lens": "lenses",
    #         "optical accessory": "accessories"
    #     }
    #     endpoint = endpoint_map.get(selected_item)

    #     if not endpoint:
    #         QMessageBox.warning(self, "Error", "Invalid item type selected.")
    #         return

    #     try:
    #         # Make a GET request to the totals endpoint
    #         response = requests.get(f"http://127.0.0.1:8000/auth/inventory/{endpoint}/totals/")
    #         if response.status_code == 200:
    #             totals = response.json()
    #             total_stock = totals.get("total_stock", 0)
    #             total_price = totals.get("total_price", 0.0)

    #             # Update UI labels with totals
    #             self.label_5.setText(f"Total Stock: {total_stock}")
    #             self.totalstockLabel.setText(" hello world")
                
    #             self.label_6.setText(f"Total Price: {total_price:.2f}")
    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch totals: {response.json().get('error', 'Unknown error')}")
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")







if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventorySystem()
    window.show()
    sys.exit(app.exec())