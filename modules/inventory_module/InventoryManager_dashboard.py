import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem,QVBoxLayout, QLabel, QProgressDialog, QHeaderView
from PySide6.QtCore import Slot, Qt, QTimer
# from ui_ux.inventory_system.ui_item_inventorys9 import Ui_MainWindow  #
from ui_ux.inventory_system.ui_item_inventorys_ok2 import Ui_MainWindow
from modules.sales_module.month_sales_and_exits import MonthlyReportManager

from shiboken6 import isValid
from PySide6.QtCore import QCoreApplication
#BASE_URL = "http://127.0.0.1:8000/"  
from config_loader import BASE_URL
response = requests.get(f'{BASE_URL}')


class InventoryManager(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        
        
        self.loading_spinner = QProgressDialog("Loading...", "Cancel", 0, 0, self)
        self.loading_spinner.setWindowModality(Qt.WindowModal)
        self.loading_spinner.setAutoClose(True)
        self.loading_spinner.setAutoReset(True)
        self.loading_spinner.setCancelButton(None)

        
        
        self.ui.setupUi(self)
        self.setup_connections()
        self.selected_item_id = None  # Track the selected item's ID for updates error_label
        
               # Show the spinner for a fixed duration before fetching data
        self.show_loading_spinner(2000)  # 2000 milliseconds (2 seconds)
        QTimer.singleShot(2000, self.fetch_initial_data)  # Fetch data after 2 seconds

        self.fetch_inventory_items()  # Populate the inventory table on startup
        self.populate_category_dropdown()  # Populate category dropdown on startup
        self.ui.category.currentIndexChanged.connect(self.populate_item_type_dropdown)

    def setup_connections(self):
        """Connect buttons to their respective slots."""
        self.ui.pushButton_2.clicked.connect(self.add_inventory_item)  # Add button
        self.ui.pushButton.clicked.connect(self.delete_inventory_item)
        self.ui.pushButton_8.clicked.connect(self.update_inventory_item)  # Update button
        self.ui.tableWidget.itemSelectionChanged.connect(self.populate_fields_for_update)  # Table selection
        self.ui.pushButton_7.clicked.connect(self.clear_fields)  # Clear
        self.ui.category.currentIndexChanged.connect(self.filter_inventory_by_category)
        self.ui.category.currentIndexChanged.connect(lambda: self.highlight_combobox_selection(self.ui.category))
        self.ui.itemtype.currentIndexChanged.connect(lambda: self.highlight_combobox_selection(self.ui.itemtype))
        self.ui.sale_entery_report.clicked.connect(self.show_monthly_entries_sales)


    def retranslate_ui(self):
        """Safely retranslate static and dynamic UI elements."""
        if not isValid(self.ui):
            print("⚠️ UI deleted, skipping retranslation")
            return

        try:
            # Retranslate static UI
            self.ui.retranslateUi(self)

            # Retranslate dynamic labels (if any)
            for type_name, label in self.dynamic_labels.items():
                if isValid(label):
                    current_text = label.text().split(":")[-1].strip()  # preserve the number
                    label.setText(QCoreApplication.translate("MainWindow", f"{type_name}: {current_text}"))

        except RuntimeError as err:
            print(f"⚠️ Some widgets deleted before retranslation: {err}")
            
            
    def show_monthly_entries_sales(self):
        """Open the Monthly Entries/Sales window."""
        self.monthly_entries_sales_window = MonthlyReportManager()
        self.monthly_entries_sales_window.show()

    ### Loading Spinner ###
    def show_loading_spinner(self, duration_ms=2000, message="Loading system, please wait..."):
        """Show the loading spinner for a specific duration."""        
        self.loading_spinner.setLabelText(message)
        self.loading_spinner.setStyleSheet("color: white; font-weight: bold; width: 300px; font-size: 15px;")
        self.loading_spinner.show()
        QTimer.singleShot(duration_ms, self.hide_loading_spinner)

    def hide_loading_spinner(self):
        """Hide the loading spinner."""
        self.loading_spinner.hide()

    ### Error Feedback ###
    def display_error(self, error_message):
        """Display backend error messages in the error label."""
        self.ui.error_label.setText(error_message)
        self.ui.error_label.setStyleSheet("color: red; font-weight: bold;")

    def clear_error(self):
        """Clear the error label."""
        self.ui.error_label.setText("")
        ### Fetch Initial Data ###
    def fetch_initial_data(self):
        """Fetch initial data after the loading spinner completes."""
        self.fetch_inventory_items()
        self.populate_category_dropdown()

    ### Highlight Combobox ###
    def highlight_combobox_selection(self, combobox):
        """Highlight the selected item in a combobox."""
        selected_text = combobox.currentText()
        if selected_text in ["Select Category", "Select Type"]:
            combobox.setStyleSheet("background-color: rgb(255, 255, 255); color: black;")
        else:
            combobox.setStyleSheet("background-color: rgb(255, 255, 255); color: black;")        
    
    ### Backend Integration ###
    def fetch_inventory_items(self):
        """Fetch inventory items from the backend and populate the table."""
        self.show_loading_spinner()
        self.clear_error()        
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        try:
            response = requests.get(f"{BASE_URL}/fetch-items/")
            if response.status_code == 200:
                inventory_items = response.json()
                self.ui.tableWidget.setRowCount(0)  # Clear existing rows
                for row, item in enumerate(inventory_items):
                    self.ui.tableWidget.insertRow(row)
                    self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["id"])))
                    self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["type__name"]))
                    self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["unit_price"])))
                    self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(item["date_added"]))
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch inventory items: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
            
    @Slot()
    def populate_fields_for_update(self):
        """Populate input fields and dropdowns with the selected item's data."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            return  # No row selected

        # Retrieve item details from the table
        self.selected_item_id = self.ui.tableWidget.item(selected_row, 0).text()
        item_type_name = self.ui.tableWidget.item(selected_row, 1).text()
        stock_level = self.ui.tableWidget.item(selected_row, 2).text()
        unit_price = self.ui.tableWidget.item(selected_row, 3).text()

        # Populate input fields
        self.ui.itemAmount.setText(unit_price)
        self.ui.itemquant.setText(stock_level)

        # Fetch category and type details from the backend
        try:
            response = requests.get(f"{BASE_URL}/item-types/", params={"type_name": item_type_name})
            if response.status_code == 200:
                item_types = response.json().get("item_types", [])
                if item_types:
                    type_data = item_types[0]
                    category_id = type_data.get("category_id")
                    type_id = type_data.get("id")

                    # Set category dropdown
                    category_index = self.ui.category.findData(category_id)
                    self.ui.category.setCurrentIndex(category_index)

                    # Populate and set the item type dropdown
                    self.populate_item_type_dropdown()  # Refresh item types based on category
                    type_index = self.ui.itemtype.findData(type_id)
                    self.ui.itemtype.setCurrentIndex(type_index)
            else:
                QMessageBox.warning(self, "Error", "Failed to fetch item type details.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))



    def get_category_id_for_type(self, type_name):
        """Fetch the category ID associated with a given type name."""
        try:
            response = requests.get(f"{BASE_URL}/item-types/", params={"type_name": type_name})
            if response.status_code == 200:
                type_data = response.json()
                return type_data.get("category_id")
        except requests.RequestException:
            return None

    def populate_category_dropdown(self):
        """Populate the category dropdown with data from the backend."""
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

    def populate_item_type_dropdown(self):
        """Populate the item type dropdown based on the selected category."""
        category_id = self.ui.category.currentData()
        if not category_id:
            self.ui.itemtype.clear()
            self.ui.itemtype.addItem("Select Type", None)
            return

        try:
            response = requests.get(f"{BASE_URL}/item-types/", params={"category_id": category_id})
            if response.status_code == 200:
                item_types = response.json().get("item_types", [])
                self.ui.itemtype.clear()
                self.ui.itemtype.addItem("Select Type", None)
                for item_type in item_types:
                    self.ui.itemtype.addItem(item_type["name"], item_type["id"])
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch item types: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))


    @Slot()
    def add_inventory_item(self):
        """Add a new inventory item."""
        # Get data from input fields
        category_id = self.ui.category.currentData()
        type_id = self.ui.itemtype.currentData()
        unit_price = self.ui.itemAmount.text().strip()
        stock_level = self.ui.itemquant.text().strip()

        # Validate input
        if not category_id or not unit_price or not stock_level:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return

        # Validate numeric fields
        try:
            unit_price = float(unit_price)
            stock_level = int(stock_level)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Price and quantity must be valid numbers.")
            return

        # Prepare payload
        payload = {
            "category": category_id,
            "type": type_id,
            "unit_price": unit_price,
            "stock_level": stock_level,
        }
        print(f"Sending data to backend: {payload}")  # Debugging log

        try:
            # Disable the Add button while the request is in progress
            self.ui.pushButton_2.setEnabled(False)

            # Send data to backend
            response = requests.post(f"{BASE_URL}/add-item/", json=payload)
            print(f"Response: {response.status_code}, {response.text}")  # Debugging log

            # Handle backend response
            if response.status_code == 201:
                response_data = response.json()
                QMessageBox.information(self, "Success", "Item added successfully!")
                self.fetch_inventory_items()  # Refresh inventory table
                self.clear_fields()  # Clear input fields
            else:
                error_message = response.json().get("error", "Unknown error occurred.")
                QMessageBox.warning(self, "Error", f"Failed to add item: {error_message}")

        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
        finally:
            # Re-enable the Add button after the request
            self.ui.pushButton_2.setEnabled(True)
            
    @Slot()
    def delete_inventory_item(self):
        """Delete the selected inventory item."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select an item to delete.")
            return

        # Get the item ID from the table
        item_id = self.ui.tableWidget.item(selected_row, 0).text()
        item_type_name = self.ui.tableWidget.item(selected_row, 1).text()
        # Show confirmation dialog
        reply = QMessageBox.question(
            self,
            "Confirm Deletion",
            f"Do you want to delete this {item_type_name} ?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            try:
                response = requests.delete(f"{BASE_URL}/delete-item/{item_id}/")
                if response.status_code == 200:
                    QMessageBox.information(self, "Success", "Item deleted successfully!")
                    self.fetch_inventory_items()  # Refresh table
                else:
                    QMessageBox.warning(self, "Error", f"Failed to delete item: {response.status_code}")
            except requests.RequestException as e:
                QMessageBox.critical(self, "Network Error", str(e))

    

    @Slot()
    def update_inventory_item(self):
        """Update the selected inventory item."""
        if not self.selected_item_id:
            QMessageBox.warning(self, "Selection Error", "No item selected for update.")
            return

        # Get data from input fields
        category_id = self.ui.category.currentData()
        type_id = self.ui.itemtype.currentData()
        unit_price = self.ui.itemAmount.text().strip()
        stock_level = self.ui.itemquant.text().strip()

        # Validate input
        if not category_id or not unit_price or not stock_level:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return

        # Validate numeric fields
        try:
            unit_price = float(unit_price)
            stock_level = int(stock_level)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Price and quantity must be valid numbers.")
            return

        # Prepare payload
        payload = {
            "category": category_id,
            "type": type_id,
            "unit_price": unit_price,
            "stock_level": stock_level,
        }

        try:
            # Send update request to backend
            response = requests.put(f"{BASE_URL}/update-item/{self.selected_item_id}/", json=payload)
            if response.status_code == 200:
                QMessageBox.information(self, "Success", "Item updated successfully!")
                self.fetch_inventory_items()  # Refresh table
                self.clear_fields()  # Clear input fields
                self.selected_item_id = None  # Reset selection
            else:
                error_message = response.json().get("error", "Unknown error occurred.")
                QMessageBox.warning(self, "Error", f"Failed to update item: {error_message}")

        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))


    def clear_fields(self):
        """Clear all input fields."""
        self.ui.itemAmount.clear()
        self.ui.itemquant.clear()
        self.ui.category.setCurrentIndex(0)
        self.ui.itemtype.setCurrentIndex(0)




    @Slot()
    def filter_inventory_by_category(self):
        """Filter inventory items by the selected category and update stock labels."""
        category_id = self.ui.category.currentData()

        if not category_id:
            # No category selected; fetch all items and reset labels
            self.fetch_inventory_items()
            self.reset_stock_labels()
            return

        # Fetch filtered items for the selected category
        try:
            response = requests.get(f"{BASE_URL}/fetch-items/", params={"category_id": category_id})
            if response.status_code == 200:
                inventory_items = response.json()
                self.ui.tableWidget.setRowCount(0)  # Clear existing rows
                for row, item in enumerate(inventory_items):
                    self.ui.tableWidget.insertRow(row)
                    self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["id"])))
                    self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["type__name"]))
                    self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))
                    self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["unit_price"])))
                    self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(item["date_added"]))

                # Fetch and update stock summary
                self.update_stock_labels(category_id)
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch filtered items: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
    # @Slot()
    # def filter_inventory_by_category(self):
    #     """Filter inventory items by the selected category."""
    #     category_id = self.ui.category.currentData()

    #     if not category_id:
    #         # No category selected; fetch all items
    #         self.fetch_inventory_items()
    #         return

    #     try:
    #         response = requests.get(f"{BASE_URL}/fetch-items/", params={"category_id": category_id})
    #         if response.status_code == 200:
    #             inventory_items = response.json()
    #             self.ui.tableWidget.setRowCount(0)  # Clear existing rows
    #             for row, item in enumerate(inventory_items):
    #                 self.ui.tableWidget.insertRow(row)
    #                 self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["id"])))
    #                 self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["type__name"]))
    #                 self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))
    #                 self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["unit_price"])))
    #                 self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(item["date_added"]))
    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch filtered items: {response.status_code}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))

    


    # def update_stock_labels(self, category_id):
    #     """Fetch and display the stock summary for the selected category."""
    #     try:
    #         response = requests.get(f"{BASE_URL}/category-stock-summary/", params={"category_id": category_id})
    #         print(f"Request URL: {response.url}")  # Debug: Verify the request URL
    #         if response.status_code == 200:
    #             stock_summary = response.json().get('stock_summary', {})
                
    #             # Update labels
    #             self.ui.label_9.setText(f"Lens: {stock_summary.get('Lens', 0)}")
    #             self.ui.label_11.setText(f"Frame: {stock_summary.get('Frame', 0)}")
    #             self.ui.label_13.setText(f"Optical Accessory: {stock_summary.get('Optical Accessory', 0)}")
    #             self.ui.label_15.setText(f"Custom Item: {stock_summary.get('Custom Item', 0)}")
    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch stock summary. Status code: {response.status_code}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))



    def update_stock_labels(self, category_id=None):
        """Fetch and display the stock summary for the selected category."""
        try:
            # Determine the URL parameters based on whether a category is selected
            params = {"category_id": category_id} if category_id else {}
            response = requests.get(f"{BASE_URL}/category-stock-summary/", params=params)

            if response.status_code == 200:
                stock_summary = response.json().get('stock_summary', {})
                total_stock = response.json().get('total_stock', 0)
                total_amount = response.json().get('total_amount', 0)

                # Debugging logs
                print(f"Stock Summary: {stock_summary}")
                print(f"Total Stock: {total_stock}")
                print(f"Total Amount: {total_amount}")

                # Update total stock and amount labels
                self.ui.total_stock.setText(f"Total Stock: {total_stock}")
                self.ui.total_amount.setText(f"Total Amount: {total_amount:.2f}")

                # Remove all dynamic labels from the QFrame except total_stock and total_amount
                for i in reversed(range(self.ui.frame_3.layout().count())):
                    widget = self.ui.frame_3.layout().itemAt(i).widget()
                    if widget and widget not in [self.ui.total_stock, self.ui.total_amount]:
                        widget.deleteLater()

                # Dynamically create labels for each item type
                for type_name, stock in stock_summary.items():
                    label = QLabel(f"{type_name}: {stock}")
                    label.setStyleSheet("font-size: 14px; color: #ffffff; font-weight: 900;")
                    self.ui.frame_3.layout().addWidget(label)

            else:
                error_message = response.json().get('error', 'Unknown error occurred.')
                QMessageBox.warning(self, "Error", f"Failed to fetch stock summary: {error_message}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

#######################################################################

    # def update_stock_labels(self, category_id=None):
    #     """Fetch and display the stock summary for the selected category."""
    #     try:
    #         # Determine the URL parameters based on whether a category is selected
    #         params = {"category_id": category_id} if category_id else {}
    #         response = requests.get(f"{BASE_URL}/category-stock-summary/", params=params)

    #         if response.status_code == 200:
    #             stock_summary = response.json().get('stock_summary', {})
    #             total_stock = response.json().get('total_stock', 0)
    #             total_amount = response.json().get('total_amount', 0)

    #             # Preserve the total_amount and total_stock labels
    #             self.ui.total_stock.setText(f"Total Stock: {total_stock}")
    #             self.ui.total_amount.setText(f"Total Amount: {total_amount:.2f}")

    #             # Remove all dynamic labels from the QFrame
    #             for i in reversed(range(self.ui.frame_3.layout().count())):
    #                 widget = self.ui.frame_3.layout().itemAt(i).widget()
    #                 if widget and widget not in [self.ui.total_stock, self.ui.total_amount]:
    #                     widget.deleteLater()

    #             # Dynamically create labels for each item type
    #             for type_name, stock in stock_summary.items():
    #                 label = QLabel(f"{type_name}: {stock}")
    #                 label.setStyleSheet("font-size: 14px; color: #ffffff; font-weight: 900;")  # Optional styling
    #                 self.ui.frame_3.layout().addWidget(label)

    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch stock summary. Status code: {response.status_code}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))
################################################################################################
    # the best of all
    
    # def update_stock_labels(self, category_id):
    #     """Fetch and display the stock summary for the selected category."""
    #     try:
    #         response = requests.get(f"{BASE_URL}/category-stock-summary/", params={"category_id": category_id})
    #         if response.status_code == 200:
    #             stock_summary = response.json().get('stock_summary', {})
                
    #             # Remove all child widgets from the QFrame
    #             for i in reversed(range(self.ui.frame_3.layout().count())):
    #                 widget = self.ui.frame_3.layout().itemAt(i).widget()
    #                 if widget:
    #                     widget.deleteLater()

    #             # Create a layout for the frame if not already set
    #             if self.ui.frame_3.layout() is None:
    #                 layout = QVBoxLayout()
    #                 self.ui.frame_3.setLayout(layout)
    #             else:
    #                 layout = self.ui.frame_3.layout()

    #             # Dynamically create labels for each item type
    #             for type_name, stock in stock_summary.items():
    #                 label = QLabel(f"{type_name}: {stock}")
    #                 label.setStyleSheet("font-size: 14px; color: #ffffff;")  # Optional styling
    #                 layout.addWidget(label)

    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch stock summary. Status code: {response.status_code}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))

    # def update_stock_labels(self, category_id):
    #     """Fetch and display the stock summary for the selected category."""
    #     try:
    #         response = requests.get(f"{BASE_URL}/category-stock-summary/", params={"category_id": category_id})
    #         if response.status_code == 200:
    #             stock_summary = response.json().get('stock_summary', {})
                
    #             # Update labels dynamically based on item types
    #             labels = [self.ui.label_9, self.ui.label_11, self.ui.label_13, self.ui.label_15]
    #             for label, (type_name, stock) in zip(labels, stock_summary.items()):
    #                 label.setText(f"{type_name}: {stock}")
                
    #             # Clear remaining labels if there are fewer than 4 types
    #             for i in range(len(stock_summary), 4):
    #                 labels[i].setText("")
    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch stock summary. Status code: {response.status_code}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))


            
    # def reset_stock_labels(self):
    #     """Reset stock labels to their default values."""
    #     self.ui.label_9.setText("Lens: 0")
    #     self.ui.label_11.setText("Frame: 0")
    #     self.ui.label_13.setText("Optical Accessory: 0")
    #     self.ui.label_15.setText("Custom Item: 0")

    def reset_stock_labels(self):
        """Reset stock labels to their default values."""
        # Ensure total_amount and total_stock remain
        self.ui.total_stock.setText("Total Stock: 0")
        self.ui.total_amount.setText("Total Amount: 0.00")

        # Remove all dynamic labels except total_stock and total_amount
        for i in reversed(range(self.ui.frame_3.layout().count())):
            widget = self.ui.frame_3.layout().itemAt(i).widget()
            if widget and widget not in [self.ui.total_stock, self.ui.total_amount]:
                widget.deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryManager()
    window.show()
    sys.exit(app.exec())
