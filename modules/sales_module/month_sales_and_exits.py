import sys
import os

# Go two levels up to reach the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import requests
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidgetItem,QWidget, QFileDialog, QProgressBar, QLabel, QScrollArea,QVBoxLayout, QSizePolicy,QHeaderView
from PySide6.QtCore import Slot, Qt
from ui_ux.inventory_system.ui_monthly_entries_sales9 import Ui_Form  
from PySide6.QtWidgets import QProgressDialog

# BASE_URL = "http://127.0.0.1:8000/"  
from config_loader import BASE_URL
response = requests.get(f'{BASE_URL}')


class MonthlyReportManager(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setup_connections()
        self.populate_month_combobox()
        self.populate_year_combobox()
        self.populate_category_combobox()
        self.populate_sale_entry_combobox()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def setup_connections(self):
        """Connect buttons to their respective slots."""
        self.ui.filter_button.clicked.connect(self.filter_report)  # Filter button
        self.ui.export_button.clicked.connect(self.export_report) 
        self.ui.category.currentIndexChanged.connect(self.populate_item_type_combobox)    
        self.ui.category.currentIndexChanged.connect(self.update_totals_by_type)

            
    def populate_month_combobox(self):
        """Populate the month combobox with month names."""
        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        self.ui.months.addItems(months)


    def populate_year_combobox(self):
        """Populate the year combobox with a range of years."""
        import datetime
        current_year = datetime.datetime.now().year
        years = [str(year) for year in range(current_year - 2, current_year + 1)]
        self.ui.years.addItems(years)


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
        """Fetch and populate the item type combobox based on selected category."""
        category_id = self.ui.category.currentData()
        if not category_id:
            self.ui.items_types.clear()
            self.ui.items_types.addItem("Select Item Type", None)
            return

        try:
            response = requests.get(f"{BASE_URL}/item-types/", params={"category_id": category_id})
            if response.status_code == 200:
                item_types = response.json().get("item_types", [])
                self.ui.items_types.clear()
                self.ui.items_types.addItem("Select Item Type", None)
                for item_type in item_types:
                    self.ui.items_types.addItem(item_type["name"], item_type["id"])
            else:
                QMessageBox.warning(self, "Error", f"Failed to fetch item types: {response.status_code}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))


    def populate_sale_entry_combobox(self):
        """Populate the sale/entry combobox with predefined options."""
        self.ui.sale_entries.addItems(["Sales", "Entries"])

    # @Slot()
    # def filter_report(self):
    #     """Fetch and display the report based on selected filters."""
    #     # Get selected filters
    #     month = self.ui.months.currentText()
    #     year = self.ui.years.currentText()
    #     category_id = self.ui.category.currentData()
    #     item_type_id = self.ui.items_types.currentData()
    #     report_type = self.ui.sale_entries.currentText().lower()  # "sales" or "entries"

    #     # Validate filters
    #     if not month or not year or not report_type:
    #         QMessageBox.warning(self, "Input Error", "Month, year, and report type are required.")
    #         return

    #     try:
    #         # Prepare request parameters
    #         params = {
    #             "month": month,
    #             "year": year,
    #             "category_id": category_id,
    #             "item_type_id": item_type_id,
    #             "report_type": report_type,
    #         }

    #         # Send request to the backend
    #         response = requests.get(f"{BASE_URL}/filter-report/", params=params)

    #         if response.status_code == 200:
    #             # Parse response data
    #             data = response.json()
    #             report_data = data.get('data', [])
    #             total_amount = data.get('total_amount', 0)

    #             # Update the table
    #             self.update_table(report_data)

    #             # Update global amount label
    #             self.ui.globalamount.setText(f"Total Amount: {total_amount:.2f}")

    #         else:
    #             # Display backend error message
    #             error_message = response.json().get('error', 'Unknown error occurred.')
    #             QMessageBox.warning(self, "Error", f"Failed to fetch report: {error_message}")

    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))
    
    
    @Slot()
    @Slot()
    def filter_report(self):
        """Filter the report based on selected values."""
        # Retrieve the selected values
        month_index = self.ui.months.currentIndex() + 1  # Convert to numeric month (1-12)
        year = self.ui.years.currentText()
        category_id = self.ui.category.currentData()
        item_type_id = self.ui.items_types.currentData()
        sale_entry_type = self.ui.sale_entries.currentText().lower()  # Convert to lowercase

        # Validate inputs
        if not year or not month_index or not sale_entry_type : #or not category_id or not item_type_id
            QMessageBox.warning(self, "Input Error", "Please select all required fields.")
            return

        # Prepare payload
        params = {
            "month": month_index,
            "year": year,
            "category_id": category_id,
            "item_type_id": item_type_id,
            "report_type": sale_entry_type  # "sales" or "entries"
        }

        try:
            # Backend request
            response = requests.get(f"{BASE_URL}/filter-report/", params=params)
            if response.status_code == 200:
                data = response.json()
                report_data = data.get("data", [])
                total_amount = data.get("total_amount", 0.0)

                # Update the table
                self.update_table(report_data)

                # Update global amount label
                # self.ui.globalamount.setText(f"Total Amount: {total_amount:,.2f}")
                self.ui.globalamount.setText(f"{total_amount:,.2f}")
            else:
                error_message = response.json().get('error', 'Unknown error occurred.')
                QMessageBox.warning(self, "Error", f"Failed to fetch report: {error_message}")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    # @Slot()
    # def filter_report(self):
    #     """Filter the report based on selected values."""
    #     # Retrieve the selected values
    #     month_index = self.ui.months.currentIndex() + 1  # Convert to numeric month (1-12)
    #     year = self.ui.years.currentText()
    #     category_id = self.ui.category.currentData()
    #     item_type_id = self.ui.items_types.currentData()
    #     sale_entry_type = self.ui.sale_entries.currentText().lower()  # Convert to lowercase if required

    #     # Validate inputs
    #     if not year or not month_index or not sale_entry_type:
    #         QMessageBox.warning(self, "Input Error", "Please select all required fields.")
    #         return

    #     # Prepare payload
    #     params = {
    #         "month": month_index,  # Numeric month
    #         "year": year,
    #         "category_id": category_id,
    #         "item_type_id": item_type_id,
    #         "report_type": sale_entry_type  # "sales" or "entries"
    #     }

    #     # Debugging log
    #     print(f"Filter Params: {params}")

    #     # Make the backend request
    #     try:
    #         response = requests.get(f"{BASE_URL}/filter-report/", params=params)
    #         if response.status_code == 200:
    #             report_data = response.json().get("data", [])
    #             self.update_table(report_data)
    #             total_amount = response.json().get("total_amount", 0.0)
    #             self.ui.globalamount.setText(f"Total Amount: {total_amount:.2f}")
    #         else:
    #             error_message = response.json().get('error', 'Unknown error occurred.')
    #             QMessageBox.warning(self, "Error", f"Failed to fetch report: {error_message}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))

    # def update_table(self, report_data):
    #     """Update the table with the fetched report data."""
    #     self.ui.tableWidget.setRowCount(0)  # Clear existing rows

    #     for row, item in enumerate(report_data):
    #         self.ui.tableWidget.insertRow(row)
    #         self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["date_added"])))
    #         self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["type__name"]))
    #         self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["unit_price"])))
    #         self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["stock_level"])))
    #         self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(item["total_value"])))

    def update_table(self, report_data):
        """Update the table with the fetched report data."""
        self.ui.tableWidget.setRowCount(0)  # Clear existing rows

        # Determine the report type based on data structure
        if report_data and 'price' in report_data[0]:
            # Sales data
            for row, item in enumerate(report_data):
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["date"])))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["item__type__name"]))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["price"])))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["quantity"])))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(item["total_value"])))
        elif report_data and 'unit_price' in report_data[0]:
            # Entries data
            for row, item in enumerate(report_data):
                self.ui.tableWidget.insertRow(row)
                self.ui.tableWidget.setItem(row, 0, QTableWidgetItem(str(item["date_added"])))
                self.ui.tableWidget.setItem(row, 1, QTableWidgetItem(item["type__name"]))
                self.ui.tableWidget.setItem(row, 2, QTableWidgetItem(str(item["unit_price"])))
                self.ui.tableWidget.setItem(row, 3, QTableWidgetItem(str(item["stock_level"])))
                self.ui.tableWidget.setItem(row, 4, QTableWidgetItem(str(item["total_value"])))







    @Slot()
    def update_totals_by_type(self):
        """Fetch and display the totals for each item type in the selected category."""
        category_id = self.ui.category.currentData()

        if not category_id:
            self.reset_labels()  # Clear layout if no category is selected
            return

        try:
            response = requests.get(f"{BASE_URL}/get-totals-by-type/", params={"category_id": category_id})

            if response.status_code == 200:
                totals = response.json().get("totals", [])
                self.reset_labels()  # Clear existing labels from the layout

                # Create a scrollable container for the labels
                scroll_area = QScrollArea(self.ui.frame_5)
                scroll_area.setWidgetResizable(True)
                scroll_area.setStyleSheet("border: none; background-color: transparent;")

                # Set size policy
                scroll_area.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

                content_widget = QWidget()
                scroll_area.setWidget(content_widget)
                content_layout = QVBoxLayout(content_widget)

                # Add the scroll area to the layout
                self.ui.gridLayout_2.addWidget(scroll_area, 0, 0)

                # Dynamically create a label for each item type
                for item in totals:
                    label = QLabel(content_widget)
                    label.setText(f"{item['type_name']}: {item['total_amount']:,.2f}")
                    label.setStyleSheet("font-size: 14px; font-weight: bold; color: #ffffff;")
                    content_layout.addWidget(label)

                # Add the scroll area to the frame
                self.ui.gridLayout_2.addWidget(scroll_area, 0, 0)

            else:
                self.reset_labels()  # Clear labels if no data is returned
                QMessageBox.warning(self, "Error", f"Failed to fetch totals: {response.json().get('error', 'Unknown error occurred.')}")
        
        except requests.RequestException as e:
            self.reset_labels()
            QMessageBox.critical(self, "Network Error", str(e))

    # @Slot()
    # def update_totals_by_type(self):
    #     """Fetch and display the totals for each item type in the selected category."""
    #     category_id = self.ui.category.currentData()

    #     if not category_id:
    #         # Reset the layout if no category is selected
    #         self.reset_labels()
    #         return

    #     try:
    #         response = requests.get(f"{BASE_URL}/get-totals-by-type/", params={"category_id": category_id})

    #         if response.status_code == 200:
    #             totals = response.json().get("totals", [])
    #             self.reset_labels()  # Clear existing labels from the layout

    #             scroll_area = QScrollArea(self.ui.frame_2)
    #             scroll_area.setWidgetResizable(True)
    #             content_widget = QWidget()
    #             scroll_area.setWidget(content_widget)
    #             content_layout = QVBoxLayout(content_widget)
    #             self.ui.gridLayout_2.addWidget(scroll_area)  # Add scroll area to the layout

    #             for i, item in enumerate(totals):
    #                 # Dynamically create a new label for each item type
    #                 label = QLabel(self.ui.frame_2)  # Adjust parent container as per your layout
    #                 label.setText(f"{item['type_name']}: {item['total_amount']:,.2f}")
    #                 label.setStyleSheet("font-size: 14px; font-weight: bold; color: #ffffff;")  # Styling for labels

    #                 # Add the label to the grid layout
    #                 self.ui.gridLayout_2.addWidget(label, i, 0)  # Add the label in the first column of the layout

    #         else:
    #             QMessageBox.warning(self, "Error", f"Failed to fetch totals: {response.json().get('error', 'Unknown error occurred.')}")
        
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))


    def reset_labels(self):
        """Remove all dynamically added labels from the layout."""
        while self.ui.gridLayout_2.count():
            widget = self.ui.gridLayout_2.takeAt(0).widget()
            if widget:
                widget.deleteLater()



    @Slot()
    def export_report(self):
        """Export the report in the selected format (CSV or PDF)."""
        # Get the selected filters
        month_index = self.ui.months.currentIndex() + 1  # Convert to numeric month (1-12)
        year = self.ui.years.currentText()
        category_id = self.ui.category.currentData()
        item_type_id = self.ui.items_types.currentData()
        sale_entry_type = self.ui.sale_entries.currentText().lower()  # Convert to lowercase
        file_format = "csv" if self.ui.radio_csv.isChecked() else "pdf"

        # Validate inputs
        if not year or not month_index or not sale_entry_type:
            QMessageBox.warning(self, "Input Error", "Please select all required fields.")
            return

        # Prepare payload
        params = {
            "month": month_index,
            "year": year,
            "category_id": category_id,
            "item_type_id": item_type_id,
            "report_type": sale_entry_type,
            "format": file_format
        }

        try:
            # Initialize the progress dialog
            progress_dialog = QProgressDialog("Exporting report...", "Cancel", 0, 0, self)
            progress_dialog.setWindowModality(Qt.WindowModal)
            progress_dialog.setMinimumDuration(0)
            progress_dialog.setValue(0)
            progress_dialog.show()

            # Backend request
            response = requests.get(f"{BASE_URL}/export-report/", params=params, stream=True)
            progress_dialog.setValue(50)  # Simulate progress

            if response.status_code == 200:
                # Save the file locally
                file_name, _ = QFileDialog.getSaveFileName(self, "Save File", f"report.{file_format}")
                if file_name:
                    with open(file_name, "wb") as file:
                        file.write(response.content)
                    progress_dialog.setValue(100)  # Complete progress
                    QMessageBox.information(self, "Success", f"Report saved as {file_name}.")
                else:
                    QMessageBox.warning(self, "Cancelled", "Export operation was cancelled.")
            else:
                error_message = response.json().get('error', 'Unknown error occurred.')
                # QMessageBox.warning(self, "Error", f"Failed to export report: {error_message}")
                QMessageBox.warning(self, "Error", f"Failed to export report: {error_message}. Please check your network connection or try again later.")


        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
        finally:
            progress_dialog.close()  # Ensure the progress dialog is closed


    # @Slot()
    # def export_report(self):
    #     """Export the report in the selected format (CSV or PDF)."""
    #     # Get the selected filters
    #     month_index = self.ui.months.currentIndex() + 1  # Convert to numeric month (1-12)
    #     year = self.ui.years.currentText()
    #     category_id = self.ui.category.currentData()
    #     item_type_id = self.ui.items_types.currentData()
    #     sale_entry_type = self.ui.sale_entries.currentText().lower()  # Convert to lowercase
    #     file_format = "csv" if self.ui.radio_csv.isChecked() else "pdf"

    #     # Validate inputs
    #     if not year or not month_index or not sale_entry_type:
    #         QMessageBox.warning(self, "Input Error", "Please select all required fields.")
    #         return

    #     # Prepare payload
    #     params = {
    #         "month": month_index,
    #         "year": year,
    #         "category_id": category_id,
    #         "item_type_id": item_type_id,
    #         "report_type": sale_entry_type,
    #         "format": file_format
    #     }

    #     try:
    #         # Backend request
    #         response = requests.get(f"{BASE_URL}/export-report/", params=params, stream=True)
    #         if response.status_code == 200:
    #             file_name, _ = QFileDialog.getSaveFileName(self, "Save File", f"report.{file_format}")
    #             if file_name:
    #                 with open(file_name, "wb") as file:
    #                     file.write(response.content)
    #                 QMessageBox.information(self, "Success", f"Report saved as {file_name}.")
    #         else:
    #             error_message = response.json().get('error', 'Unknown error occurred.')
    #             QMessageBox.warning(self, "Error", f"Failed to export report: {error_message}")
    #     except requests.RequestException as e:
    #         QMessageBox.critical(self, "Network Error", str(e))

if __name__ == "__main__":
    app = QApplication([])
    window = MonthlyReportManager()
    window.show()
    app.exec()
