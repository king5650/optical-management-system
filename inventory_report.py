         
            
import sys
import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem, QWidget
from ui_ux.inventory_system.ui_monthly_entries_sales1 import Ui_Form
from PySide6.QtCore import Qt

class MonthlyEntriesSales(QWidget, Ui_Form):  # Ensure this inherits from QWidget or QMainWindow
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.populate_months()
        self.populate_items()
        self.populate_years()
        self.sale_entries.addItems(["Sales", "Entries"])

        # Connect signals
        self.items.currentTextChanged.connect(self.update_item_types_and_table)
        self.items_types.currentTextChanged.connect(self.filter_data)
        self.months.currentTextChanged.connect(self.filter_data)
        self.years.currentTextChanged.connect(self.filter_data)
        self.sale_entries.currentTextChanged.connect(self.filter_data)

        # Load initial data 
        self.update_item_types_and_table()

    def populate_months(self):
        """Populate months combobox."""
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        self.months.addItems(months)

    def populate_items(self):
        """Populate items combobox."""
        self.items.addItems(["Frame", "Lens", "Optical Accessory"])

    def populate_years(self):
        """Fetch distinct years from the backend and populate the years combobox."""
        try:
            response = requests.get("http://127.0.0.1:8000/auth/inventory/years/")
            if response.status_code == 200:
                years = response.json().get("years", [])
                self.years.addItems([str(year) for year in years])
            else:
                QMessageBox.warning(self, "Error", "Failed to fetch years.")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

    def update_item_types_and_table(self):
        """Update item types and table data dynamically based on the selected category."""
        self.update_item_types()
        self.filter_data()  # Trigger data filtering immediately after updating item types

    def update_item_types(self):
        """Update item types dynamically based on the selected item."""
        selected_item = self.items.currentText()
        self.items_types.clear()

        if selected_item == "Frame":
            self.items_types.addItems(["VIP", "VIP+", "VIP++", "CLASSIC"])
        elif selected_item == "Lens":
            self.items_types.addItems(["Simple Vision", "Progressive Stock", "Progressive Commande", "Bi-focaux"])
        else:
            self.items_types.clear()  # No types for Optical Accessory

    def filter_data(self):
        """Fetch and display filtered data based on the selected filters."""
        month = self.months.currentIndex() + 1  # Convert to 1-based index
        year = self.years.currentText()
        item = self.items.currentText()
        item_type = self.items_types.currentText()
        sale_or_entry = self.sale_entries.currentText()

        if not year or not item:
            return  # Avoid fetching data with incomplete filters

        params = {
            "month": month,
            "year": year,
            "item_type": item,
            "sale_or_entry": sale_or_entry
        }

        try:
            response = requests.get("http://127.0.0.1:8000/auth/inventory/filter/", params=params)
            if response.status_code == 200:
                data = response.json().get("data", [])
                total_global_amount = response.json().get("total_global_amount", 0.0)
                item_type_totals = response.json().get("item_type_totals", {})

                # Update the global amount label
                self.globalamount.setText(f" {total_global_amount}")

                # Update labels for item type totals
                if item == "Frame":
                    self.label_9.setText(f"VIP Total: {item_type_totals.get('VIP', 0.0)}")
                    self.label_10.setText(f"VIP+ Total: {item_type_totals.get('VIP+', 0.0)}")
                    self.label_11.setText(f"VIP++ Total: {item_type_totals.get('VIP++', 0.0)}")
                    self.label_12.setText(f"CLASSIC Total: {item_type_totals.get('CLASSIC', 0.0)}")
                elif item == "Lens":
                    self.label_9.setText(f"Simple Vision Total: {item_type_totals.get('Simple Vision', 0.0)}")
                    self.label_10.setText(f"Progressive Stock Total: {item_type_totals.get('Progressive Stock', 0.0)}")
                    self.label_11.setText(f"Progressive Commande Total: {item_type_totals.get('Progressive Commande', 0.0)}")
                    self.label_12.setText(f"Bi-focaux Total: {item_type_totals.get('Bi-focaux', 0.0)}")
                else:  # Optical Accessory
                    self.label_9.setText(f"Optical Accessory Total: {total_global_amount}")
                    self.label_10.setText("")
                    self.label_11.setText("")
                    self.label_12.setText("")

                # Populate the table
                self.tableWidget.setRowCount(0)
                for row_data in data:
                    row = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(row)
                    self.tableWidget.setItem(row, 0, QTableWidgetItem(row_data["month"]))
                    self.tableWidget.setItem(row, 1, QTableWidgetItem(row_data["item"]))
                    self.tableWidget.setItem(row, 2, QTableWidgetItem(row_data["item_type"]))
                    self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{row_data['price']}"))
                    self.tableWidget.setItem(row, 4, QTableWidgetItem(str(row_data["amount"])))
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch data: {response.json().get('error', 'Unknown error')}")
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Server error: {e}")

       
            
            
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MonthlyEntriesSales()
    window.show()
    sys.exit(app.exec())
    

    # def filter_data(self):
    #     """Fetch and display filtered data based on the selected filters."""
    #     # Gather filter values
    #     month = self.months.currentIndex() + 1  # Convert to 1-based month index
    #     year = self.years.currentText()
    #     item = self.items.currentText()
    #     item_type = self.items_types.currentText()
    #     sale_or_entry = self.sale_entries.currentText()

    #     if not year or not item:
    #         return  # Avoid fetching data with incomplete filters

    #     # Prepare request parameters
    #     params = {
    #         "month": month,
    #         "year": year,
    #         "item_type": item,
    #         "sale_or_entry": sale_or_entry
    #     }

    #     try:
    #         # Fetch data from the backend
    #         response = requests.get("http://127.0.0.1:8000/auth/inventory/filter/", params=params)
            
    #         # Ensure the response is valid JSON
    #         try:
    #             response_data = response.json()
    #         except ValueError:
    #             QMessageBox.critical(self, "Error", "Invalid response from the server.")
    #             return

    #         # Extract data
    #         data = response_data.get("data", [])
    #         total_global_amount = response_data.get("total_global_amount", 0.0)
    #         item_type_totals = response_data.get("item_type_totals", {})

    #         # Update the global amount label
    #         self.globalamount.setText(f"{total_global_amount}")

    #         # Populate the table
    #         self.tableWidget.setRowCount(0)
    #         for row_data in data:
    #             row = self.tableWidget.rowCount()
    #             self.tableWidget.insertRow(row)
    #             self.tableWidget.setItem(row, 0, QTableWidgetItem(row_data["month"]))
    #             self.tableWidget.setItem(row, 1, QTableWidgetItem(row_data["item"]))
    #             self.tableWidget.setItem(row, 2, QTableWidgetItem(row_data["item_type"]))
    #             self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{row_data['price']}"))
    #             self.tableWidget.setItem(row, 4, QTableWidgetItem(str(row_data["amount"])))

    #         # Update labels for item type totals dynamically
    #         if item == "Frame":
    #             self.label_9.setText(f"VIP Total: {float(item_type_totals.get('VIP', 0.0))}")
    #             self.label_10.setText(f"VIP+ Total: {float(item_type_totals.get('VIP+', 0.0)):.2f}")
    #             self.label_11.setText(f"VIP++ Total: {float(item_type_totals.get('VIP++', 0.0)):.2f}")
    #             self.label_12.setText(f"CLASSIC Total: {float(item_type_totals.get('CLASSIC', 0.0)):.2f}")
    #         elif item == "Lens":
    #             self.label_9.setText(f"Simple Vision Total: {float(item_type_totals.get('Simple Vision', 0.0)):.2f}")
    #             self.label_10.setText(f"Progressive Stock Total: {float(item_type_totals.get('Progressive Stock', 0.0)):.2f}")
    #             self.label_11.setText(f"Progressive Commande Total: {float(item_type_totals.get('Progressive Commande', 0.0)):.2f}")
    #             self.label_12.setText(f"Bi-focaux Total: {float(item_type_totals.get('Bi-focaux', 0.0)):.2f}")
    #         elif item == "Optical Accessory":
    #             self.label_9.setText(f"Accessory Total: {float(total_global_amount):.2f}")
    #             self.label_10.setText("")
    #             self.label_11.setText("")
    #             self.label_12.setText("")
    #         else:
    #             self.label_9.setText("")
    #             self.label_10.setText("")
    #             self.label_11.setText("")
    #             self.label_12.setText("")
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")




    # def filter_data(self):
    #     """Fetch and display filtered data based on the selected filters."""
    #     # Gather filter values
    #     month_name = self.months.currentText()
    #     month_map = {
    #         "January": 1, "February": 2, "March": 3, "April": 4,
    #         "May": 5, "June": 6, "July": 7, "August": 8,
    #         "September": 9, "October": 10, "November": 11, "December": 12
    #     }
    #     month = month_map.get(month_name, 0)  # Default to 0 if invalid
    #     year = self.years.currentText()
    #     item = self.items.currentText()
    #     item_type = self.items_types.currentText()
    #     sale_or_entry = self.sale_entries.currentText()

    #     # Log the filter values
    #     print(f"Filters: Month={month}, Year={year}, Item={item}, Item Type={item_type}, Sale/Entry={sale_or_entry}")

    #     if not year or not item:
    #         print("Invalid filters, skipping fetch.")
    #         return  # Avoid fetching data with incomplete filters

    #     # Prepare request parameters
    #     params = {
    #         "month": month,
    #         "year": year,
    #         "item_type": item,
    #         "sale_or_entry": sale_or_entry
    #     }

    #     try:
    #         # Fetch data from the backend
    #         response = requests.get("http://127.0.0.1:8000/auth/inventory/filter/", params=params)
    #         if response.status_code == 200:
    #             data = response.json().get("data", [])
    #             total_global_amount = response.json().get("total_global_amount", 0.0)

    #             # Debugging: Log the received data
    #             print("Backend Response:", data)

    #             # Update the global amount label
    #             self.globalamount.setText(f"{total_global_amount}")

    #             # Populate the table
    #             self.tableWidget.setRowCount(0)
    #             for row_data in data:
    #                 row = self.tableWidget.rowCount()
    #                 self.tableWidget.insertRow(row)
    #                 self.tableWidget.setItem(row, 0, QTableWidgetItem(row_data["month"]))
    #                 self.tableWidget.setItem(row, 1, QTableWidgetItem(row_data["item"]))
    #                 self.tableWidget.setItem(row, 2, QTableWidgetItem(row_data["item_type"]))
    #                 self.tableWidget.setItem(row, 3, QTableWidgetItem(f"{row_data['price']}"))
    #                 self.tableWidget.setItem(row, 4, QTableWidgetItem(str(row_data["amount"])))
    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch data: {response.json().get('error', 'Unknown error')}")
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")





    

    # def populate_items(self):
    #     """Fetch distinct item categories from the backend."""
    #     try:
    #         response = requests.get("http://127.0.0.1:8000/auth/inventory/items/")
    #         if response.status_code == 200:
    #             items = response.json().get("items", [])
    #             self.items.clear()
    #             self.items.addItems(items)
    #         else:
    #             QMessageBox.warning(self, "Error", "Failed to fetch item categories.")
    #     except requests.exceptions.RequestException as e:
    #         QMessageBox.critical(self, "Error", f"Server error: {e}")