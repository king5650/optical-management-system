# import sys
# import requests
# from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
# from ui_item_inventorys7 import Ui_MainWindow  # Replace with your UI file name

# BASE_URL = "http://127.0.0.1:8000/"  # Django server URL

# class InventoryApp(QMainWindow, Ui_MainWindow):
#     def __init__(self):
#         super().__init__()
#         self.setupUi(self)  # Initialize UI components
#         self.pushButton_2.clicked.connect(self.add_item)  # Connect Add button
#         self.populate_category_dropdown()  # Populate category dropdown on startup
#         self.category.currentIndexChanged.connect(self.populate_item_type_dropdown)  # Handle category selection

#     def populate_category_dropdown(self):
#         """Populate the category dropdown with data from the backend."""
#         try:
#             response = requests.get(f"{BASE_URL}auth/categories/")
#             if response.status_code == 200:
#                 categories = response.json()
#                 self.category.clear()
#                 self.category.addItem("Select Category", None)
#                 for category in categories:
#                     self.category.addItem(category["name"], category["id"])
#             else:
#                 QMessageBox.warning(self, "Error", f"Failed to fetch categories: {response.status_code}")
#         except requests.RequestException as e:
#             QMessageBox.critical(self, "Network Error", str(e))

#     def populate_item_type_dropdown(self):
#         """Populate the item type dropdown based on the selected category."""
#         category_id = self.category.currentData()
#         if not category_id:
#             self.itemtype.clear()
#             self.itemtype.addItem("Select Type", None)
#             return

#         try:
#             response = requests.get(f"{BASE_URL}auth/item-types/", params={"category_id": category_id})
#             if response.status_code == 200:
#                 item_types = response.json().get("item_types", [])
#                 self.itemtype.clear()
#                 self.itemtype.addItem("Select Type", None)
#                 for item_type in item_types:
#                     self.itemtype.addItem(item_type["name"], item_type["id"])
#             else:
#                 QMessageBox.warning(self, "Error", f"Failed to fetch item types: {response.status_code}")
#         except requests.RequestException as e:
#             QMessageBox.critical(self, "Network Error", str(e))

#     def add_item(self):
#         category = self.category.currentData()  # Get the selected category ID
#         item_type = self.itemtype.currentData()  # Get the selected type ID
#         unit_price = self.itemAmount.text()
#         stock_level = self.itemquant.text()

#         # Validate inputs
#         if not category or not unit_price or not stock_level:
#             QMessageBox.warning(self, "Input Error", "Please fill in all required fields.")
#             return

#         # Prepare data payload
#         data = {
#             "category": category,
#             "type": item_type,
#             "unit_price": float(unit_price),
#             "stock_level": int(stock_level),
#         }
#         print("Sending data to backend:", data)  # Debug print

#         try:
#             response = requests.post(f"{BASE_URL}auth/add-item/", json=data)
#             print("Response status code:", response.status_code)
#             print("Response content:", response.text)

#             if response.status_code == 201:
#                 QMessageBox.information(self, "Success", "Item added successfully!")
#                 self.load_items()  # Refresh the table
#             else:
#                 QMessageBox.warning(self, "Error", f"Failed to add item: {response.json()}")
#         except requests.RequestException as e:
#             QMessageBox.critical(self, "Network Error", str(e))

#     def load_items(self):
#         try:
#             response = requests.get(f"{BASE_URL}auth/fetch-items/")
#             if response.status_code == 200:
#                 items = response.json()  # Parse JSON data
#                 self.tableWidget.setRowCount(len(items))
#                 for row, item in enumerate(items):
#                     self.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["id"])))
#                     self.tableWidget.setItem(row, 1, QTableWidgetItem(item["type__name"]))
#                     self.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))
#                     self.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["unit_price"])))
#                     self.tableWidget.setItem(row, 4, QTableWidgetItem(item["date_added"]))
#             else:
#                 print(f"Error {response.status_code}: {response.text}")
#         except requests.exceptions.RequestException as e:
#             print("Error: Could not connect to the server:", e)
#         except ValueError:
#             print("Error: Invalid JSON response from the server.")

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = InventoryApp()
#     window.show()
#     sys.exit(app.exec())


import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import Slot
from ui_ux.inventory_system.ui_item_inventorys7 import Ui_MainWindow  # Import the analyzed UI file

BASE_URL = "http://127.0.0.1:8000/"  # Django server URL


class InventoryManager(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_connections()
        self.fetch_inventory_items()  # Populate the inventory table on startup
        self.populate_category_dropdown()  # Populate category dropdown on startup
        self.ui.category.currentIndexChanged.connect(self.filter_items_by_category)
        self.ui.tableWidget.itemSelectionChanged.connect(self.populate_item_details)
        self.ui.category.currentIndexChanged.connect(self.populate_item_type_dropdown)

    def setup_connections(self):
        """Connect buttons to their respective slots."""
        self.ui.pushButton_2.clicked.connect(self.add_inventory_item)  # Add button
        self.ui.pushButton.clicked.connect(self.delete_inventory_item)
        
        
    ### Backend Integration ###
    def fetch_inventory_items(self):
        """Fetch all inventory items from the backend and populate the table."""
        try:
            response = requests.get(f"{BASE_URL}auth/fetch-items/")
            if response.status_code == 200:
                inventory_items = response.json()
                self.populate_table(inventory_items)
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch inventory items: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    def populate_table(self, items):
        """Populate the table with inventory items."""
        self.ui.tableWidget.setRowCount(0)  # Clear existing rows
        for row, item in enumerate(items):
            self.ui.tableWidget.insertRow(row)
            self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["id"])))
            self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["type__name"]))
            self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))
            self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["unit_price"])))
            self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(item["date_added"]))

    def populate_category_dropdown(self):
        """Populate the category dropdown with data from the backend."""
        try:
            response = requests.get(f"{BASE_URL}auth/categories/")
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

    @Slot()
    def filter_items_by_category(self):
        """Filter items in the table based on the selected category."""
        category_id = self.ui.category.currentData()
        if not category_id:
            self.fetch_inventory_items()  # Show all items if no category is selected
            return

        try:
            response = requests.get(f"{BASE_URL}auth/fetch-items/", params={"category_id": category_id})
            if response.status_code == 200:
                items = response.json()
                self.populate_table(items)
            else:
                QMessageBox.warning(self, "Error", f"Failed to filter items: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
            
    def populate_item_type_dropdown(self):
        """Populate the item type dropdown based on the selected category."""
        category_id = self.ui.category.currentData()
        print(f"Selected Category ID: {category_id}")  # Debugging log

        if not category_id:
            self.ui.itemtype.clear()
            self.ui.itemtype.addItem("Select Type", None)
            return

        try:
            response = requests.get(f"{BASE_URL}auth/item-types/", params={"category_id": category_id})
            print(f"Response Status: {response.status_code}, Data: {response.json()}")  # Debugging log

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
    def populate_item_details(self):
        """Populate the details of the selected inventory item."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row != -1:
            # Get data from the selected row
            item_type_name = self.ui.tableWidget.item(selected_row, 1).text()
            stock_level = self.ui.tableWidget.item(selected_row, 2).text()
            unit_price = self.ui.tableWidget.item(selected_row, 3).text()

            # Populate the input fields
            self.ui.itemAmount.setText(unit_price)
            self.ui.itemquant.setText(stock_level)

            # Set the corresponding category in the dropdown
            item_category_id = self.get_category_id_by_item_type(item_type_name)
            category_index = self.ui.category.findData(item_category_id)
            if category_index != -1:
                self.ui.category.setCurrentIndex(category_index)

            # Populate the item type dropdown based on the category and set the selected item type
            self.populate_item_type_dropdown()
            item_type_index = self.ui.itemtype.findText(item_type_name)
            if item_type_index != -1:
                self.ui.itemtype.setCurrentIndex(item_type_index)

    def populate_item_type_dropdown(self):
        """Populate the item type dropdown based on the selected category."""
        category_id = self.ui.category.currentData()
        if not category_id:
            self.ui.itemtype.clear()
            self.ui.itemtype.addItem("Select Type", None)
            return

        try:
            response = requests.get(f"{BASE_URL}auth/item-types/", params={"category_id": category_id})
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

    def get_category_id_by_item_type(self, item_type_name):
        """Get the category ID associated with the given item type."""
        try:
            response = requests.get(f"{BASE_URL}auth/item-type-category/", params={"item_type_name": item_type_name})
            if response.status_code == 200:
                return response.json().get("category_id")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
        return None

    @Slot()
    def add_inventory_item(self):
        """Add a new inventory item."""
        category_id = self.ui.category.currentData()
        type_id = self.ui.itemtype.currentData()
        unit_price = self.ui.itemAmount.text().strip()
        stock_level = self.ui.itemquant.text().strip()

        if not category_id or not unit_price or not stock_level:
            QMessageBox.warning(self, "Input Error", "All fields are required.")
            return

        try:
            unit_price = float(unit_price)
            stock_level = int(stock_level)
        except ValueError:
            QMessageBox.warning(self, "Input Error", "Price and quantity must be valid numbers.")
            return

        payload = {"category": category_id, "type": type_id, "unit_price": unit_price, "stock_level": stock_level}

        try:
            response = requests.post(f"{BASE_URL}auth/add-item/", json=payload)
            if response.status_code == 201:
                QMessageBox.information(self, "Success", "Item added successfully!")
                self.fetch_inventory_items()
                self.clear_fields()
            else:
                error_message = response.json().get("error", "Unknown error occurred.")
                QMessageBox.warning(self, "Error", f"Failed to add item: {error_message}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
            
            
            # type__name
    @Slot()
    def delete_inventory_item(self):
        """Delete the selected inventory item."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select an item to delete.")
            return

        item_id = self.ui.tableWidget.item(selected_row, 0).text()
        item_type_name = self.ui.tableWidget.item(selected_row, 1).text()
        
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete this item (ID: {item_id}-{item_type_name})?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                response = requests.delete(f"{BASE_URL}auth/inventory/delete/", params={"item_id": item_id})
                # response = requests.delete(f"http://127.0.0.1:8000/auth/delete/{item_id}/")
                if response.status_code == 200:
                    data = response.json()
                    if data.get("success"):
                        QMessageBox.information(self, "Success", data.get("message"))
                        self.fetch_inventory_items()  # Refresh the table
                    else:
                        QMessageBox.warning(self, "Error", data.get("message"))
                else:
                    QMessageBox.warning(self, "Error", f"Failed to delete item: {response.status_code}")
            except requests.RequestException as e:
                QMessageBox.critical(self, "Network Error", str(e))



    def clear_fields(self):
        """Clear all input fields."""
        self.ui.itemAmount.clear()
        self.ui.itemquant.clear()
        self.ui.category.setCurrentIndex(0)
        self.ui.itemtype.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryManager()
    window.show()
    sys.exit(app.exec())


















# # import sys
# # import requests
# # from PySide6.QtWidgets import QApplication, QMessageBox, QTableWidgetItem, QWidget,QMainWindow
# # from PySide6.QtCore import Slot
# # from ui_item_inventorys6 import Ui_MainWindow  # Import the UI file


# # class InventorySystem(QMainWindow, Ui_MainWindow):
# #     def __init__(self):
# #         super().__init__()
# #         self.ui = Ui_MainWindow()
# #         self.ui.setupUi(self)
# #         self.setup_connections()
# #         self.fetch_categories()
# #         self.fetch_inventory_items()

# #     def setup_connections(self):
# #         """Set up button connections."""
# #         self.ui.pushButton_2.clicked.connect(self.add_inventory_item)  # Add
# #         self.ui.pushButton_8.clicked.connect(self.update_inventory_item)  # Update
# #         self.ui.pushButton.clicked.connect(self.delete_inventory_item)  # Delete
# #         self.ui.pushButton_7.clicked.connect(self.clear_fields)  # Clear
# #         self.ui.category.currentIndexChanged.connect(self.fetch_item_types)

# #     ### Backend Integration ###
# #     def fetch_categories(self):
# #         """Fetch categories and populate the category dropdown."""
# #         try:
# #             response = requests.get("http://127.0.0.1:8000/auth/categories/")
# #             if response.status_code == 200:
# #                 categories = response.json()
# #                 self.ui.category.clear()  # Clear existing entries
# #                 self.ui.category.addItem("Select Category", None)
# #                 for category in categories:
# #                     self.ui.category.addItem(category["name"], category["id"])
# #             else:
# #                 QMessageBox.warning(self, "Error", f"Failed to fetch categories: {response.status_code}")
# #         except requests.RequestException as e:
# #             QMessageBox.critical(self, "Network Error", str(e))
# #     @Slot()
# #     def fetch_item_types(self):
# #         """Fetch item types based on the selected category."""
# #         category_id = self.ui.category.currentData()
# #         if not category_id:
# #             self.ui.itemtype.clear()
# #             self.ui.itemtype.addItem("Select Item Type", None)
# #             return

# #         try:
# #             response = requests.get(f"http://127.0.0.1:8000/auth/item-types/{category_id}/")
# #             if response.status_code == 200:
# #                 item_types = response.json()
# #                 self.ui.itemtype.clear()
# #                 # self.ui.itemtype.addItem("Select Item Type", None)  # Default option
# #                 for item_type in item_types:
# #                     self.ui.itemtype.addItem(item_type["name"], item_type["id"])
# #             else:
# #                 QMessageBox.warning(self, "Error", f"Failed to fetch item types: {response.status_code}")
# #         except requests.RequestException as e:
# #             QMessageBox.critical(self, "Network Error", str(e))


# #     def fetch_inventory_items(self):
# #         """Fetch all inventory items and populate the table."""
# #         try:
# #             response = requests.get("http://127.0.0.1:8000/auth/inventory/")
# #             if response.status_code == 200:
# #                 inventory_items = response.json().get("inventory_items", [])
# #                 self.ui.tableWidget.setRowCount(0)  # Clear the table
# #                 for row, item in enumerate(inventory_items):
# #                     self.ui.tableWidget.insertRow(row)
# #                     self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["id"])))
# #                     self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["category"]["name"]))
# #                     self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(item["type"]["name"] if item["type"] else "Custom Item"))
# #                     self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["stock_level"])))
# #                     self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(f"${item['unit_price']}"))
# #                     self.ui.tableWidget.setItem(row, 5, QTableWidgetItem(item["date_added"]))
# #             else:
# #                 QMessageBox.warning(self, "Error", f"Failed to fetch inventory items: {response.status_code}")
# #         except requests.RequestException as e:
# #             QMessageBox.critical(self, "Network Error", str(e))

# #     ### CRUD Operations ###
# #     @Slot()
# #     def add_inventory_item(self):
# #         """Add a new inventory item and update the table."""
# #         item_type_id = self.ui.itemtype.currentData()
# #         quantity = self.ui.itemquant.text().strip()
# #         price = self.ui.itemAmount.text().strip()

# #         if not item_type_id:
# #             QMessageBox.warning(self, "Input Error", "Please select an item type.")
# #             return

# #         if not quantity.isdigit() or int(quantity) <= 0:
# #             QMessageBox.warning(self, "Input Error", "Quantity must be a positive integer.")
# #             return

# #         try:
# #             price = float(price)
# #         except ValueError:
# #             QMessageBox.warning(self, "Input Error", "Price must be a valid number.")
# #             return

# #         try:
# #             response = requests.post(
# #                 "http://127.0.0.1:8000/auth/inventory/add/",
# #                 json={"item_type_id": item_type_id, "quantity": quantity, "price": price}
# #             )
# #             if response.status_code == 200:
# #                 data = response.json()
# #                 if data.get("success"):
# #                     QMessageBox.information(self, "Success", data.get("message"))
# #                     self.clear_fields()
# #                     self.fetch_inventory_items()  # Refresh the table
# #                 else:
# #                     QMessageBox.warning(self, "Error", data.get("message"))
# #             else:
# #                 QMessageBox.warning(self, "Error", f"Failed to add item: {response.status_code}")
# #         except requests.RequestException as e:
# #             QMessageBox.critical(self, "Network Error", str(e))


# #     @Slot()
# #     def update_inventory_item(self):
# #         """Update the selected inventory item."""
# #         selected_row = self.ui.tableWidget.currentRow()
# #         if selected_row == -1:
# #             QMessageBox.warning(self, "Selection Error", "Please select an item to update.")
# #             return

# #         item_id = self.ui.tableWidget.item(selected_row, 0).text()
# #         quantity = self.ui.itemquant.text().strip()
# #         price = self.ui.itemAmount.text().strip()

# #         if not quantity or not price:
# #             QMessageBox.warning(self, "Input Error", "Quantity and price are required.")
# #             return

# #         try:
# #             response = requests.put(
# #                 f"http://127.0.0.1:8000/auth/inventory/update/{item_id}/",
# #                 json={"quantity": quantity, "price": price}
# #             )
# #             if response.status_code == 200:
# #                 data = response.json()
# #                 if data.get("success"):
# #                     QMessageBox.information(self, "Success", data.get("message"))
# #                     self.clear_fields()
# #                     self.fetch_inventory_items()  # Refresh the table
# #                 else:
# #                     QMessageBox.warning(self, "Error", data.get("message"))
# #             else:
# #                 QMessageBox.warning(self, "Error", f"Failed to update item: {response.status_code}")
# #         except requests.RequestException as e:
# #             QMessageBox.critical(self, "Network Error", str(e))

    @Slot()
    def delete_inventory_item(self):
        """Delete the selected inventory item."""
        selected_row = self.ui.tableWidget.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select an item to delete.")
            return

        item_id = self.ui.tableWidget.item(selected_row, 0).text()
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete this item (ID: {item_id})?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            try:
                response = requests.delete(f"http://127.0.0.1:8000/auth/inventory/delete/{item_id}/")
                if response.status_code == 200:
                    data = response.json()
                    if data.get("success"):
                        QMessageBox.information(self, "Success", data.get("message"))
                        self.fetch_inventory_items()  # Refresh the table
                    else:
                        QMessageBox.warning(self, "Error", data.get("message"))
                else:
                    QMessageBox.warning(self, "Error", f"Failed to delete item: {response.status_code}")
            except requests.RequestException as e:
                QMessageBox.critical(self, "Network Error", str(e))

# #     @Slot()
# #     def clear_fields(self):
# #         """Clear all input fields."""
# #         self.ui.itemquant.clear()
# #         self.ui.itemAmount.clear()
# #         self.ui.itemtype.setCurrentIndex(0)  # Reset dropdown


# # if __name__ == "__main__":
# #     app = QApplication(sys.argv)
# #     window = InventorySystem()
# #     window.show()
# #     sys.exit(app.exec())