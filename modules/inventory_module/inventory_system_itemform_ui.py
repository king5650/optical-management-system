import sys
import os
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)


import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget, QHeaderView
from PySide6.QtCore import Slot
# from ui_ux.inventory_system.ui_item_type_form2 import Ui_Form 
from ui_ux.inventory_system.ui_add_item_type_form_ok1 import Ui_Form 

from config_loader import BASE_URL
response = requests.get(f'{BASE_URL}')
#"http://127.0.0.1:8000/"  

class ItemTypeForm(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_connections()
        self.fetch_categories()  # Populate the category dropdown and table on launch
        self.fetch_item_types()  # Populate the item types table on launch
        self.enable_sorting()  # Enable sorting for tables        
        self.ui.categor_table_display.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.table_item_type_display.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #table_item_type_display
        
       
        
    def setup_connections(self):
        # Category Section
        self.ui.add_categoty.clicked.connect(self.add_category)
        self.ui.delete_category.clicked.connect(self.delete_category)
        self.ui.edit_category.clicked.connect(self.update_category)
        self.ui.categor_table_display.itemSelectionChanged.connect(self.populate_category_name)
        self.ui.search_category_bar.textChanged.connect(self.search_categories)
        
        # Item Type Section        
        self.ui.add_item_type.clicked.connect(self.add_item_type)
        self.ui.delete_item_type.clicked.connect(self.delete_item_type)
        self.ui.edit_item_type.clicked.connect(self.update_item_type)
        self.ui.select_category.currentIndexChanged.connect(self.filter_item_types_by_category)
        self.ui.table_item_type_display.itemSelectionChanged.connect(self.populate_item_type_details)
        self.ui.search_item_type_bar.textChanged.connect(self.search_item_types)

    def retranslate_ui(self):
        """
        Called when the app language changes.
        It re-applies the translated strings to this form.
        """
        self.ui.retranslateUi(self) 
        
    ## Category Section ###
    def fetch_categories(self):
        """Fetch categories from the backend and populate the dropdown and table."""
        try:
            response = requests.get(f"{BASE_URL}/categories/")
            if response.status_code == 200:
                categories = response.json()
                self.ui.select_category.clear()  # Clear existing dropdown entries
                self.ui.select_category.addItem("All Categories", None)  # Default option
                self.ui.categor_table_display.setRowCount(0)  # Clear existing table rows

                for row, category in enumerate(categories):
                    self.ui.categor_table_display.insertRow(row)
                    self.ui.categor_table_display.setItem(row, 0, QTableWidgetItem(str(category["id"])))
                    self.ui.categor_table_display.setItem(row, 1, QTableWidgetItem(category["name"]))

                    # Add to category dropdown
                    self.ui.select_category.addItem(category["name"], category["id"])
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch categories: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
    ### Category Section ###
    # def fetch_categories(self):
    #     """Fetch categories from the backend and populate the dropdown and table."""
    #     try:
    #         response = requests.get("http://127.0.0.1:8000/auth/categories/")
    #         if response.status_code == 200:
    #             categories = response.json()
    #             self.ui.select_category.clear()  # Clear existing dropdown entries
    #             self.ui.select_category.addItem("All Categories", None)  # Default option
    #             self.ui.categor_table_display.setRowCount(0)  # Clear existing table rows

    #             for row, category in enumerate(categories):
    #                 self.ui.categor_table_display.insertRow(row)
    #                 self.ui.categor_table_display.setItem(row, 0, QTableWidgetItem(str(category["id"])))
    #                 self.ui.categor_table_display.setItem(row, 1, QTableWidgetItem(category["name"]))

    #                 # Add to category dropdown
    #                 self.ui.select_category.addItem(category["name"], category["id"])
    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch categories: {response.status_code}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))

    @Slot()
    def search_categories(self):
        """Filter categories based on the search bar input."""
        search_text = self.ui.search_category_bar.text().strip().lower()
        for row in range(self.ui.categor_table_display.rowCount()):
            item_name = self.ui.categor_table_display.item(row, 1).text().lower()
            self.ui.categor_table_display.setRowHidden(row, search_text not in item_name)


    @Slot()
    def populate_category_name(self):
        """Populate the category_name QLineEdit with the selected table row."""
        selected_row = self.ui.categor_table_display.currentRow()
        if selected_row != -1:
            category_name = self.ui.categor_table_display.item(selected_row, 1).text()
            self.ui.category_name.setText(category_name)

    @Slot()
    def add_category(self):
        """Add a new category."""
        category_name = self.ui.category_name.text().strip()
        if not category_name:
            QMessageBox.warning(self, "Input Error", "Category name cannot be empty.")
            return

        try:
            response = requests.post(f"{BASE_URL}/categories/add-category/", json={"name": category_name})
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    QMessageBox.information(self, "Success", data.get("message"))
                    self.ui.category_name.clear()
                    self.fetch_categories()  # Refresh table and dropdown
                else:
                    QMessageBox.warning(self, "Error", data.get("message"))
            else:
                QMessageBox.warning(self, "Error", f"Failed to add category: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    # @Slot()
    # def delete_category(self):
    #     """Delete the selected category."""
    #     selected_row = self.ui.categor_table_display.currentRow()
    #     if selected_row == -1:
    #         QMessageBox.warning(self, "Selection Error", "Please select a category to delete.")
    #         return

    #     category_id = self.ui.categor_table_display.item(selected_row, 0).text()
    #     try:
    #         response = requests.delete(f"http://127.0.0.1:8000/auth/categories/delete-category/{category_id}/")
    #         if response.status_code == 200:
    #             data = response.json()
    #             if data.get("success"):
    #                 QMessageBox.information(self, "Success", data.get("message"))
    #                 self.fetch_categories()  # Refresh table and dropdown
    #             else:
    #                 QMessageBox.warning(self, "Error", data.get("message"))
    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to delete category: {response.status_code}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))


    @Slot()
    def delete_category(self):
        """Delete the selected category with a confirmation dialog."""
        selected_row = self.ui.categor_table_display.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a category to delete.")
            return

        category_id = self.ui.categor_table_display.item(selected_row, 0).text()
        category_name = self.ui.categor_table_display.item(selected_row, 1).text()

        # Confirmation dialog
        confirm_dialog = QMessageBox(self)
        confirm_dialog.setWindowTitle("Confirm Deletion")
        confirm_dialog.setText(f"Are you sure you want to delete the category '{category_name}'?")
        confirm_dialog.setIcon(QMessageBox.Warning)
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)

        response = confirm_dialog.exec()

        if response == QMessageBox.Yes:
            try:
                response = requests.delete(f"{BASE_URL}/categories/delete-category/{category_id}/")
                if response.status_code == 200:
                    data = response.json()
                    if data.get("success"):
                        QMessageBox.information(self, "Success", data.get("message"))
                        self.fetch_categories()  # Refresh table and dropdown
                    else:
                        QMessageBox.warning(self, "Error", data.get("message"))
                else:
                    QMessageBox.warning(self, "Error", f"Failed to delete category: {response.status_code}")
            except requests.RequestException as e:
                QMessageBox.critical(self, "Network Error", str(e))



    @Slot()
    def update_category(self):
        """Update the selected category."""
        selected_row = self.ui.categor_table_display.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select a category to update.")
            return

        category_id = self.ui.categor_table_display.item(selected_row, 0).text()
        new_name = self.ui.category_name.text().strip()
        if not new_name:
            QMessageBox.warning(self, "Input Error", "Category name cannot be empty.")
            return

        try:
            response = requests.put(
                f"{BASE_URL}/categories/update-category/{category_id}/", json={"name": new_name}
            )
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    QMessageBox.information(self, "Success", data.get("message"))
                    self.fetch_categories()  # Refresh table and dropdown
                else:
                    QMessageBox.warning(self, "Error", data.get("message"))
            else:
                QMessageBox.warning(self, "Error", f"Failed to update category: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
            


    ### Item Type Section ###
    def fetch_item_types(self, category_id=None):
        """Fetch item types from the backend and populate the table."""
        try:
            params = {"category_id": category_id} if category_id else {}
            response = requests.get(f"{BASE_URL}/item-types/", params=params)
            if response.status_code == 200:
                item_types = response.json().get("item_types", [])
                self.ui.table_item_type_display.setRowCount(0)  # Clear existing rows
                for row, item_type in enumerate(item_types):
                    self.ui.table_item_type_display.insertRow(row)
                    self.ui.table_item_type_display.setItem(row, 0, QTableWidgetItem(str(item_type["id"])))
                    self.ui.table_item_type_display.setItem(row, 1, QTableWidgetItem(item_type["name"]))
                    self.ui.table_item_type_display.setItem(row, 2, QTableWidgetItem(item_type["category__name"]))
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch item types: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    @Slot()
    @Slot()
    def search_item_types(self):
        """Filter item types based on the search bar input."""
        search_text = self.ui.search_item_type_bar.text().strip().lower()
        for row in range(self.ui.table_item_type_display.rowCount()):
            item_name_item = self.ui.table_item_type_display.item(row, 1)  # Column 1: Item Name
            if item_name_item:
                item_name = item_name_item.text().lower()
                self.ui.table_item_type_display.setRowHidden(row, search_text not in item_name)
            else:
                self.ui.table_item_type_display.setRowHidden(row, True)  # Hide if no item name


    @Slot()
    def filter_item_types_by_category(self):
        """Filter item types by the selected category."""
        category_id = self.ui.select_category.currentData()
        self.fetch_item_types(category_id)
        


    # @Slot()
    # def populate_item_type_details(self):
    #     """Populate the details of the selected item type for editing."""
    #     selected_row = self.ui.table_item_type_display.currentRow()
    #     if selected_row != -1:
    #         item_name = self.ui.table_item_type_display.item(selected_row, 1).text()
    #         category_id = self.ui.table_item_type_display.item(selected_row, 2).text()
    #         self.ui.category_type_name.setText(item_name)
    #         self.ui.select_category.setCurrentIndex(
    #             self.ui.select_category.findData(int(category_id))
    #         )
    @Slot()
    def populate_item_type_details(self):
        """Populate the details of the selected item type for editing."""
        selected_row = self.ui.table_item_type_display.currentRow()
        if selected_row != -1:
            # Get item type name and category name from the table
            item_name = self.ui.table_item_type_display.item(selected_row, 1).text()
            category_name = self.ui.table_item_type_display.item(selected_row, 2).text()

            # Populate the QLineEdit with the item type name
            self.ui.category_type_name.setText(item_name)

            # Find and set the corresponding category in the QComboBox
            index = self.ui.select_category.findText(category_name)
            if index != -1:
                self.ui.select_category.setCurrentIndex(index)
            else:
                QMessageBox.warning(self, "Error", "Category not found in the dropdown.")


    @Slot()
    def add_item_type(self):
        """Add a new item type."""
        item_name = self.ui.category_type_name.text().strip()
        category_id = self.ui.select_category.currentData()
        if not item_name or not category_id:
            QMessageBox.warning(self, "Input Error", "Item type name and category are required.")
            return

        try:
            response = requests.post(
                f"{BASE_URL}/item-types/add/", json={"name": item_name, "category_id": category_id}
            )
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    QMessageBox.information(self, "Success", data.get("message"))
                    self.ui.category_type_name.clear()
                    self.fetch_item_types()
                else:
                    QMessageBox.warning(self, "Error", data.get("message"))
            else:
                QMessageBox.warning(self, "Error", f"Failed to add item type: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
            
            

        


    # @Slot()
    # def delete_item_type(self):
    #     """Delete the selected item type."""
    #     selected_row = self.ui.table_item_type_display.currentRow()
    #     if selected_row == -1:
    #         QMessageBox.warning(self, "Selection Error", "Please select an item type to delete.")
    #         return

    #     item_type_id = self.ui.table_item_type_display.item(selected_row, 0).text()
    #     try:
    #         response = requests.delete(f"http://127.0.0.1:8000/auth/item-types/delete/{item_type_id}/")
    #         if response.status_code == 200:
    #             data = response.json()
    #             if data.get("success"):
    #                 QMessageBox.information(self, "Success", data.get("message"))
    #                 self.fetch_item_types()
    #             else:
    #                 QMessageBox.warning(self, "Error", data.get("message"))
    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to delete item type: {response.status_code}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))
    
    
    @Slot()
    def delete_item_type(self):
        """Delete the selected item type with a confirmation dialog."""
        selected_row = self.ui.table_item_type_display.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select an item type to delete.")
            return

        item_type_id = self.ui.table_item_type_display.item(selected_row, 0).text()
        item_type_name = self.ui.table_item_type_display.item(selected_row, 1).text()

        # Confirmation dialog
        confirm_dialog = QMessageBox(self)
        confirm_dialog.setWindowTitle("Confirm Deletion")
        confirm_dialog.setText(f"Are you sure you want to delete the item type '{item_type_name}'?")
        confirm_dialog.setIcon(QMessageBox.Warning)
        confirm_dialog.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm_dialog.setDefaultButton(QMessageBox.No)

        response = confirm_dialog.exec()

        if response == QMessageBox.Yes:
            try:
                response = requests.delete(f"{BASE_URL}/item-types/delete/{item_type_id}/")
                if response.status_code == 200:
                    data = response.json()
                    if data.get("success"):
                        QMessageBox.information(self, "Success", data.get("message"))
                        self.fetch_item_types()  # Refresh the item type table
                    else:
                        QMessageBox.warning(self, "Error", data.get("message"))
                else:
                    QMessageBox.warning(self, "Error", f"Failed to delete item type: {response.status_code}")
            except requests.RequestException as e:
                QMessageBox.critical(self, "Network Error", str(e))


    @Slot()
    def update_item_type(self):
        """Update the selected item type."""
        selected_row = self.ui.table_item_type_display.currentRow()
        if selected_row == -1:
            QMessageBox.warning(self, "Selection Error", "Please select an item type to update.")
            return

        item_type_id = self.ui.table_item_type_display.item(selected_row, 0).text()
        new_name = self.ui.category_type_name.text().strip()
        new_category_id = self.ui.select_category.currentData()

        if not new_name or not new_category_id:
            QMessageBox.warning(self, "Input Error", "Item type name and category are required.")
            return

        try:
            response = requests.put(
                f"{BASE_URL}/item-types/update/{item_type_id}/",
                json={"name": new_name, "category_id": new_category_id},
            )
            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    QMessageBox.information(self, "Success", data.get("message"))
                    self.fetch_item_types()
                else:
                    QMessageBox.warning(self, "Error", data.get("message"))
            else:
                QMessageBox.warning(self, "Error", f"Failed to update item type: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

        

    

    ### Confirmation Dialogs ###
    def confirm_delete(self, item_name):
        """Show a confirmation dialog before deletion."""
        reply = QMessageBox.question(
            self,
            "Confirm Delete",
            f"Are you sure you want to delete '{item_name}'?",
            QMessageBox.Yes | QMessageBox.No
        )
        return reply == QMessageBox.Yes

    ### Sorting ###
    def enable_sorting(self):
        """Enable column sorting for tables."""
        self.ui.categor_table_display.setSortingEnabled(True)
        self.ui.table_item_type_display.setSortingEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ItemTypeForm()
    window.show()
    sys.exit(app.exec())
