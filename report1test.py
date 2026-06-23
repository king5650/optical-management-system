# # # # import os
# # # # import csv
# # # # import requests
# # # # from datetime import datetime
# # # # from PySide6.QtWidgets import (
# # # #     QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
# # # #     QLabel, QPushButton, QComboBox, QMessageBox
# # # # )
# # # # from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
# # # # from PySide6.QtGui import QPainter
# # # # from PySide6.QtPrintSupport import QPrinter
# # # # from reportlab.pdfgen import canvas
# # # # from reportlab.lib.pagesizes import A4
# # # # from reportlab.lib import colors
# # # # from reportlab.lib.units import inch
# # # # from PySide6.QtWidgets import QApplication
# # # # from PySide6.QtWebEngineWidgets import QWebEngineView  # ✅ PDF Viewer
# # # # from PySide6.QtCore import QUrl,  QTimer

# # # # BASE_URL = "http://127.0.0.1:8000/"  # Django backend



# # # # class InventoryPrintDialog(QDialog):
# # # #     """Dialog for Print Preview using QWebEngineView."""
    
# # # #     def __init__(self, pdf_path, parent=None):
# # # #         super().__init__(parent)
# # # #         self.setWindowTitle("Print Preview")
# # # #         self.setMinimumSize(900, 600)
# # # #         self.pdf_path = pdf_path

# # # #         layout = QVBoxLayout()

# # # #         # ✅ Embedded PDF Viewer
# # # #         self.pdf_viewer = QWebEngineView()
# # # #         layout.addWidget(self.pdf_viewer)

# # # #         # 📌 Print Button
# # # #         self.print_button = QPushButton("Print")
# # # #         self.print_button.clicked.connect(self.print_pdf)
# # # #         layout.addWidget(self.print_button)

# # # #         self.setLayout(layout)

# # # #         # ✅ Delay PDF loading to ensure file is fully generated
# # # #         QTimer.singleShot(1000, self.load_pdf_preview)  

# # # #     def load_pdf_preview(self):
# # # #         """Load the PDF file into the QWebEngineView."""
# # # #         if os.path.exists(self.pdf_path):
# # # #             self.pdf_viewer.setUrl(QUrl.fromLocalFile(self.pdf_path))
# # # #         else:
# # # #             QMessageBox.warning(self, "Error", "PDF file not found. Please try again.")

# # # #     def print_pdf(self):
# # # #         """Open system print dialog to print the PDF."""
# # # #         printer = QPrinter(QPrinter.HighResolution)
# # # #         dialog = QPrintDialog(printer, self)

# # # #         if dialog.exec() == QPrintDialog.Accepted:
# # # #             os.system(f"start {self.pdf_path}")  # ✅ Open PDF for user
# # # #             QMessageBox.information(self, "Printing", "Inventory report sent to the printer.")
# # # #             self.accept()  # Close dialog after printing


# # # # import os
# # # # import csv
# # # # import requests
# # # # from datetime import datetime
# # # # from PySide6.QtWidgets import (
# # # #     QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
# # # #     QLabel, QPushButton, QComboBox, QMessageBox
# # # # )
# # # # from PySide6.QtPrintSupport import QPrinter, QPrintDialog
# # # # from reportlab.pdfgen import canvas
# # # # from reportlab.lib.pagesizes import A4
# # # # from reportlab.lib import colors
# # # # from reportlab.lib.units import inch
# # # # from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QLabel,  QScrollArea, QVBoxLayout

# # # # BASE_URL = "http://127.0.0.1:8000/"  # Django backend

# # # # class InventoryReportsDialog(QDialog):
# # # #     """Dialog for generating and exporting inventory reports."""
    
# # # #     def __init__(self, parent=None):
# # # #         super().__init__(parent)
# # # #         self.setWindowTitle("Inventory Reports")
# # # #         self.setMinimumSize(900, 500)
        
        

# # # #         layout = QVBoxLayout()

# # # #         # 🔹 Filter Section
# # # #         filter_layout = QHBoxLayout()
# # # #         self.category_combo = QComboBox()
# # # #         self.category_combo.addItem("All Categories")
# # # #         self.fetch_categories()

# # # #         self.stock_level_combo = QComboBox()
# # # #         self.stock_level_combo.addItems(["All", "Low Stock (<10)", "Out of Stock (0)"])

# # # #         self.expiry_combo = QComboBox()
# # # #         self.expiry_combo.addItems(["All", "Expired", "Expiring Soon (<30 days)"])

# # # #         filter_layout.addWidget(QLabel("Category:"))
# # # #         filter_layout.addWidget(self.category_combo)
# # # #         filter_layout.addWidget(QLabel("Stock Level:"))
# # # #         filter_layout.addWidget(self.stock_level_combo)
# # # #         filter_layout.addWidget(QLabel("Expiry:"))
# # # #         filter_layout.addWidget(self.expiry_combo)

# # # #         self.generate_button = QPushButton("Generate Report")
# # # #         self.generate_button.clicked.connect(self.fetch_inventory_data)
# # # #         filter_layout.addWidget(self.generate_button)
# # # #         layout.addLayout(filter_layout)

# # # #         # 🔹 Table Section
# # # #         self.inventory_table = QTableWidget()
# # # #         self.inventory_table.setColumnCount(5)
# # # #         self.inventory_table.setHorizontalHeaderLabels(["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"])
# # # #         layout.addWidget(self.inventory_table)

# # # #         # 🔹 Export Buttons
# # # #         button_layout = QHBoxLayout()
# # # #         self.export_pdf_button = QPushButton("Export PDF Report")
# # # #         self.export_csv_button = QPushButton("Export CSV Report")

# # # #         # self.export_pdf_button.clicked.connect(self.export_pdf_report)
# # # #         # self.export_pdf_button.clicked.connect(self.print_inventory_report)
# # # #         self.export_csv_button.clicked.connect(self.export_csv_report)

# # # #         button_layout.addWidget(self.export_pdf_button)
# # # #         button_layout.addWidget(self.export_csv_button)
# # # #         layout.addLayout(button_layout)

# # # #         self.setLayout(layout)
        
 

# # # #         # 🔹 Print Button
# # # #         self.print_button = QPushButton("Print Inventory Report")
# # # #         self.print_button.clicked.connect(self.preview_inventory_report)
# # # #         layout.addWidget(self.print_button)

# # # #         self.setLayout(layout)

# # # #     def fetch_categories(self):
# # # #         """Fetch categories from the backend."""
# # # #         try:
# # # #             response = requests.get(f"{BASE_URL}auth/categories/")
# # # #             if response.status_code == 200:
# # # #                 categories = response.json()
# # # #                 for category in categories:
# # # #                     self.category_combo.addItem(category["name"], category["id"])
# # # #             else:
# # # #                 QMessageBox.warning(self, "Error", "Failed to fetch categories.")
# # # #         except requests.RequestException as e:
# # # #             QMessageBox.critical(self, "Network Error", str(e))

# # # #     def fetch_inventory_data(self):
# # # #         """Fetch inventory data based on filters and display in the table."""
# # # #         category_id = self.category_combo.currentData() if self.category_combo.currentIndex() > 0 else None
# # # #         stock_filter = self.stock_level_combo.currentText()
# # # #         expiry_filter = self.expiry_combo.currentText()

# # # #         try:
# # # #             response = requests.get(f"{BASE_URL}auth/inventory-report/", 
# # # #                                     params={"category_id": category_id, "stock": stock_filter, "expiry": expiry_filter})
# # # #             data = response.json()

# # # #             if response.status_code == 200 and data.get("inventory"):
# # # #                 inventory = data["inventory"]
# # # #                 self.inventory_table.setRowCount(0)

# # # #                 for row, item in enumerate(inventory):
# # # #                     self.inventory_table.insertRow(row)
# # # #                     self.inventory_table.setItem(row, 0, QTableWidgetItem(item["type__name"]))
# # # #                     self.inventory_table.setItem(row, 1, QTableWidgetItem(item["category__name"]))
# # # #                     self.inventory_table.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))

# # # #                     # ✅ Convert unit_price to float before formatting
# # # #                     unit_price = float(item["unit_price"])
# # # #                     self.inventory_table.setItem(row, 3, QTableWidgetItem(f"{unit_price:,.2f} XAF"))

# # # #                     expiry_date = item.get("expiry_date", "N/A")
# # # #                     self.inventory_table.setItem(row, 4, QTableWidgetItem(expiry_date))

# # # #             else:
# # # #                 QMessageBox.information(self, "No Data", "No inventory data found.")

# # # #         except requests.RequestException as e:
# # # #             QMessageBox.critical(self, "Network Error", str(e))

    
# # # #     def preview_inventory_report(self):
# # # #         """Generate a print preview of the inventory report."""
# # # #         printer = QPrinter(QPrinter.HighResolution)
# # # #         preview_dialog = QPrintPreviewDialog(printer, self)

# # # #         # Connect the preview rendering function
# # # #         preview_dialog.paintRequested.connect(lambda printer: self.render_pdf(printer))

# # # #         preview_dialog.exec()  # Show print preview

# # # #     def render_pdf(self, printer):
# # # #         """Render the inventory report dynamically for print preview."""
# # # #         painter = QPainter(printer)
# # # #         width = printer.pageRect().width()
# # # #         height = printer.pageRect().height()

# # # #         painter.setFont("Arial", 16)
# # # #         painter.drawText(100, 100, "Inventory Report")
# # # #         painter.setFont("Arial", 12)
# # # #         painter.drawText(100, 130, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

# # # #         # Table Headers
# # # #         headers = ["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"]
# # # #         x_positions = [100, 250, 400, 550, 700]  # Adjusted for alignment
# # # #         y_position = 180

# # # #         for i, header in enumerate(headers):
# # # #             painter.drawText(x_positions[i], y_position, header)

# # # #         # Draw table data
# # # #         y_position += 30
# # # #         for row in range(self.inventory_table.rowCount()):
# # # #             row_data = [self.inventory_table.item(row, col).text() for col in range(self.inventory_table.columnCount())]
# # # #             for i, data in enumerate(row_data):
# # # #                 painter.drawText(x_positions[i], y_position, data)
# # # #             y_position += 30

# # # #         painter.end()
# # # #     # def export_pdf_report(self):
# # # #     #     """Generate and export inventory report as a PDF."""
# # # #     #     filename = f"Inventory_Report_{datetime.now().strftime('%Y-%m-%d')}.pdf"
# # # #     #     c = canvas.Canvas(filename, pagesize=A4)
# # # #     #     width, height = A4
# # # #     #     margin = 1 * inch

# # # #     #     c.setFont("Helvetica-Bold", 16)
# # # #     #     c.drawString(margin, height - margin, "Inventory Report")
# # # #     #     c.setFont("Helvetica", 12)
# # # #     #     c.drawString(margin, height - 1.3 * inch, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

# # # #     #     table_data = [["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"]]
# # # #     #     for row in range(self.inventory_table.rowCount()):
# # # #     #         row_data = [self.inventory_table.item(row, col).text() for col in range(self.inventory_table.columnCount())]
# # # #     #         table_data.append(row_data)

# # # #     #     y_position = height - 2 * inch
# # # #     #     for row in table_data:
# # # #     #         c.drawString(margin, y_position, "  ".join(row))
# # # #     #         y_position -= 0.3 * inch
# # # #     #         if y_position < margin:
# # # #     #             c.showPage()
# # # #     #             y_position = height - 2 * inch

# # # #     #     c.save()
# # # #     #     QMessageBox.information(self, "Export Successful", f"PDF Report saved as {filename}")

# # # #     def export_csv_report(self):
# # # #         """Generate and export inventory report as a CSV file."""
# # # #         filename = f"Inventory_Report_{datetime.now().strftime('%Y-%m-%d')}.csv"
# # # #         with open(filename, mode="w", newline="") as file:
# # # #             writer = csv.writer(file)
# # # #             writer.writerow(["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"])

# # # #             for row in range(self.inventory_table.rowCount()):
# # # #                 row_data = [self.inventory_table.item(row, col).text() for col in range(self.inventory_table.columnCount())]
# # # #                 writer.writerow(row_data)

# # # #         QMessageBox.information(self, "Export Successful", f"CSV Report saved as {filename}")
# # # # if __name__ == "__main__":
# # # #     app = QApplication([])
# # # #     window = InventoryReportsDialog()
# # # #     window.show()
# # # #     app.exec()


# # # import os
# # # import csv
# # # import requests
# # # from datetime import datetime
# # # from PySide6.QtWidgets import (
# # #     QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
# # #     QLabel, QPushButton, QComboBox, QMessageBox
# # # )
# # # from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# # # from PySide6.QtGui import QPainter, QTextDocument
# # # from PySide6.QtWidgets import QApplication

# # # BASE_URL = "http://127.0.0.1:8000/"  # Django backend


# # # class InventoryReportsDialog(QDialog):
# # #     """Dialog for generating, filtering, and printing inventory reports."""
    
# # #     def __init__(self, parent=None):
# # #         super().__init__(parent)
# # #         self.setWindowTitle("Inventory Reports")
# # #         self.setMinimumSize(900, 500)

# # #         layout = QVBoxLayout()

# # #         # 🔹 Filter Section
# # #         filter_layout = QHBoxLayout()
# # #         self.category_combo = QComboBox()
# # #         self.category_combo.addItem("All Categories")
# # #         self.fetch_categories()  # Populate categories

# # #         self.stock_level_combo = QComboBox()
# # #         self.stock_level_combo.addItems(["All", "Low Stock (<10)", "Out of Stock (0)"])

# # #         self.expiry_combo = QComboBox()
# # #         self.expiry_combo.addItems(["All", "Expired", "Expiring Soon (<30 days)"])

# # #         self.filter_button = QPushButton("Apply Filters")
# # #         self.filter_button.clicked.connect(self.fetch_inventory_data)

# # #         filter_layout.addWidget(QLabel("Category:"))
# # #         filter_layout.addWidget(self.category_combo)
# # #         filter_layout.addWidget(QLabel("Stock Level:"))
# # #         filter_layout.addWidget(self.stock_level_combo)
# # #         filter_layout.addWidget(QLabel("Expiry:"))
# # #         filter_layout.addWidget(self.expiry_combo)
# # #         filter_layout.addWidget(self.filter_button)

# # #         layout.addLayout(filter_layout)

# # #         # 🔹 Table Section
# # #         self.inventory_table = QTableWidget()
# # #         self.inventory_table.setColumnCount(5)
# # #         self.inventory_table.setHorizontalHeaderLabels(["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"])
# # #         layout.addWidget(self.inventory_table)

# # #         # 🔹 Print Button
# # #         self.print_button = QPushButton("Print Inventory Report")
# # #         self.print_button.clicked.connect(self.preview_inventory_report)
# # #         layout.addWidget(self.print_button)

# # #         self.setLayout(layout)

# # #     def fetch_categories(self):
# # #         """Fetch categories from the backend."""
# # #         try:
# # #             response = requests.get(f"{BASE_URL}auth/categories/")
# # #             if response.status_code == 200:
# # #                 categories = response.json()
# # #                 for category in categories:
# # #                     self.category_combo.addItem(category["name"], category["id"])
# # #             else:
# # #                 QMessageBox.warning(self, "Error", "Failed to fetch categories.")
# # #         except requests.RequestException as e:
# # #             QMessageBox.critical(self, "Network Error", str(e))

# # #     def fetch_inventory_data(self):
# # #         """Fetch inventory data based on filters and update the table."""
# # #         category_id = self.category_combo.currentData() if self.category_combo.currentIndex() > 0 else None
# # #         stock_filter = self.stock_level_combo.currentText()
# # #         expiry_filter = self.expiry_combo.currentText()

# # #         try:
# # #             response = requests.get(
# # #                 f"{BASE_URL}auth/inventory-report/", 
# # #                 params={"category_id": category_id, "stock": stock_filter, "expiry": expiry_filter}
# # #             )
# # #             data = response.json()

# # #             if response.status_code == 200 and data.get("inventory"):
# # #                 inventory = data["inventory"]
# # #                 self.inventory_table.setRowCount(0)

# # #                 for row, item in enumerate(inventory):
# # #                     self.inventory_table.insertRow(row)
# # #                     self.inventory_table.setItem(row, 0, QTableWidgetItem(item["type__name"]))
# # #                     self.inventory_table.setItem(row, 1, QTableWidgetItem(item["category__name"]))
# # #                     self.inventory_table.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))

# # #                     # ✅ Convert unit_price to float before formatting
# # #                     unit_price = float(item["unit_price"])
# # #                     self.inventory_table.setItem(row, 3, QTableWidgetItem(f"{unit_price:,.2f} XAF"))

# # #                     expiry_date = item.get("expiry_date", "N/A")
# # #                     self.inventory_table.setItem(row, 4, QTableWidgetItem(expiry_date))

# # #             else:
# # #                 QMessageBox.information(self, "No Data", "No inventory data found.")

# # #         except requests.RequestException as e:
# # #             QMessageBox.critical(self, "Network Error", str(e))

# # #     def preview_inventory_report(self):
# # #         """Generate a print preview of the inventory report."""
# # #         printer = QPrinter(QPrinter.HighResolution)
# # #         preview_dialog = QPrintPreviewDialog(printer, self)

# # #         # ✅ Fix: Correctly pass `printer` to `render_pdf`
# # #         preview_dialog.paintRequested.connect(self.render_pdf)

# # #         preview_dialog.exec()  # Show print preview

# # #     def render_pdf(self, printer):
# # #             """Render the inventory report dynamically for print preview."""
# # #             painter = QPainter(printer)
# # #             doc = QTextDocument()

# # #             # Get the page dimensions correctly
# # #             page_rect = printer.pageRect()

# # #             # ✅ Fix: Use `self.inventory_data` instead of UI table
# # #             report_html = "<h2>Inventory Report</h2>"
# # #             report_html += f"<p><b>Date:</b> {datetime.now().strftime('%Y-%m-%d')}</p>"
# # #             report_html += "<table border='1' cellspacing='0' cellpadding='5' width='100%'>"
# # #             report_html += "<tr><th>Item Type</th><th>Category</th><th>Stock</th><th>Unit Price</th><th>Expiry Date</th></tr>"

# # #             if not self.inventory_data:
# # #                 report_html += "<tr><td colspan='5' style='text-align:center;'>No inventory data available</td></tr>"
# # #             else:
# # #                 for item in self.inventory_data:
# # #                     report_html += (
# # #                         f"<tr><td>{item['type__name']}</td>"
# # #                         f"<td>{item['category__name']}</td>"
# # #                         f"<td>{item['stock_level']}</td>"
# # #                         f"<td>{float(item['unit_price']):,.2f} XAF</td>"
# # #                         f"<td>{item.get('expiry_date', 'N/A')}</td></tr>"
# # #                     )

# # #             report_html += "</table>"

# # #             # ✅ Load HTML into QTextDocument
# # #             doc.setHtml(report_html)
# # #             doc.setPageSize(page_rect.size())

# # #             # ✅ Render document to painter
# # #             doc.drawContents(painter)

# # #             painter.end()  # Finish painting


# # # if __name__ == "__main__":
# # #     app = QApplication([])
# # #     window = InventoryReportsDialog()
# # #     window.show()
# # #     app.exec()



# # import os
# # import csv
# # from PyPDF2 import PdfReader
# # import requests
# # from datetime import datetime
# # from PySide6.QtWidgets import (
# #     QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
# #     QLabel, QPushButton, QComboBox, QMessageBox
# # )
# # from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# # from PySide6.QtGui import QPainter, QTextDocument
# # from PySide6.QtWidgets import QApplication
# # from reportlab.lib import colors
# # from reportlab.lib.pagesizes import letter
# # from reportlab.lib.units import inch
# # from reportlab.pdfgen import canvas
# # from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QPushButton, QComboBox, QMessageBox
# # from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# # from PySide6.QtWidgets import QApplication
# # import requests
# # from datetime import datetime
# # BASE_URL = "http://127.0.0.1:8000/"  # Django backend


# # # class InventoryReportsDialog(QDialog):
# # #     """Dialog for generating, filtering, and printing inventory reports."""
    
# # #     def __init__(self, parent=None):
# # #         super().__init__(parent)
# # #         self.setWindowTitle("Inventory Reports")
# # #         self.setMinimumSize(900, 500)

# # #         layout = QVBoxLayout()

# # #         # Instance variable to store inventory data
# # #         self.inventory_data = []

# # #         # 🔹 Filter Section
# # #         filter_layout = QHBoxLayout()
# # #         self.category_combo = QComboBox()
# # #         self.category_combo.addItem("All Categories")
# # #         self.fetch_categories()  # Populate categories

# # #         self.stock_level_combo = QComboBox()
# # #         self.stock_level_combo.addItems(["All", "Low Stock (<10)", "Out of Stock (0)"])

# # #         self.expiry_combo = QComboBox()
# # #         self.expiry_combo.addItems(["All", "Expired", "Expiring Soon (<30 days)"])

# # #         self.filter_button = QPushButton("Apply Filters")
# # #         self.filter_button.clicked.connect(self.fetch_inventory_data)

# # #         filter_layout.addWidget(QLabel("Category:"))
# # #         filter_layout.addWidget(self.category_combo)
# # #         filter_layout.addWidget(QLabel("Stock Level:"))
# # #         filter_layout.addWidget(self.stock_level_combo)
# # #         filter_layout.addWidget(QLabel("Expiry:"))
# # #         filter_layout.addWidget(self.expiry_combo)
# # #         filter_layout.addWidget(self.filter_button)

# # #         layout.addLayout(filter_layout)

# # #         # 🔹 Table Section
# # #         self.inventory_table = QTableWidget()
# # #         self.inventory_table.setColumnCount(5)
# # #         self.inventory_table.setHorizontalHeaderLabels(["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"])
# # #         layout.addWidget(self.inventory_table)

# # #         # 🔹 Print Button
# # #         self.print_button = QPushButton("Print Inventory Report")
# # #         self.print_button.clicked.connect(self.preview_inventory_report)
# # #         layout.addWidget(self.print_button)

# # #         self.setLayout(layout)

# # #     def fetch_categories(self):
# # #         """Fetch categories from the backend."""
# # #         try:
# # #             response = requests.get(f"{BASE_URL}auth/categories/")
# # #             if response.status_code == 200:
# # #                 categories = response.json()
# # #                 for category in categories:
# # #                     self.category_combo.addItem(category["name"], category["id"])
# # #             else:
# # #                 QMessageBox.warning(self, "Error", "Failed to fetch categories.")
# # #         except requests.RequestException as e:
# # #             QMessageBox.critical(self, "Network Error", str(e))

# # #     def fetch_inventory_data(self):
# # #         """Fetch inventory data based on filters and update the table."""
# # #         category_id = self.category_combo.currentData() if self.category_combo.currentIndex() > 0 else None
# # #         stock_filter = self.stock_level_combo.currentText()
# # #         expiry_filter = self.expiry_combo.currentText()

# # #         try:
# # #             response = requests.get(
# # #                 f"{BASE_URL}auth/inventory-report/", 
# # #                 params={"category_id": category_id, "stock": stock_filter, "expiry": expiry_filter}
# # #             )
# # #             data = response.json()

# # #             print("Response Data:", data)  # Debugging line

# # #             if response.status_code == 200 and data.get("inventory"):
# # #                 self.inventory_data = data["inventory"]  # Store the fetched data
# # #                 self.inventory_table.setRowCount(0)

# # #                 for row, item in enumerate(self.inventory_data):
# # #                     print("Item:", item)  # Debugging line
# # #                     self.inventory_table.insertRow(row)
# # #                     self.inventory_table.setItem(row, 0, QTableWidgetItem(item["type__name"]))
# # #                     self.inventory_table.setItem(row, 1, QTableWidgetItem(item["category__name"]))
# # #                     self.inventory_table.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))

# # #                     unit_price = float(item["unit_price"])
# # #                     self.inventory_table.setItem(row, 3, QTableWidgetItem(f"{unit_price:,.2f} XAF"))

# # #                     expiry_date = item.get("expiry_date", "N/A")
# # #                     self.inventory_table.setItem(row, 4, QTableWidgetItem(expiry_date))

# # #             else:
# # #                 QMessageBox.information(self, "No Data", "No inventory data found.")

# # #         except requests.RequestException as e:
# # #             QMessageBox.critical(self, "Network Error", str(e))

# # #     def preview_inventory_report(self):
# # #         """Generate a print preview of the inventory report."""
# # #         if not self.inventory_data:
# # #             QMessageBox.warning(self, "No Data", "Please fetch inventory data before printing.")
# # #             return

# # #         printer = QPrinter(QPrinter.HighResolution)
# # #         preview_dialog = QPrintPreviewDialog(printer, self)
# # #         preview_dialog.paintRequested.connect(self.render_pdf)
# # #         preview_dialog.exec()  # Show print preview

# # #     def render_pdf(self, printer):
# # #         """Render the inventory report dynamically for print preview using ReportLab."""
# # #         # Create a PDF canvas
# # #         pdf_canvas = canvas.Canvas(printer, pagesize=letter)
# # #         width, height = letter

# # #         # Title
# # #         pdf_canvas.setFont("Helvetica-Bold", 16)
# # #         pdf_canvas.drawString(1 * inch, height - 1 * inch, "Inventory Report")

# # #         # Date
# # #         pdf_canvas.setFont("Helvetica", 12)
# # #         pdf_canvas.drawString(1 * inch, height - 1.2 * inch, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

# # #         # Table Header
# # #         pdf_canvas.setFont("Helvetica-Bold", 12)
# # #         pdf_canvas.drawString(1 * inch, height - 1.5 * inch, "Item Type")
# # #         pdf_canvas.drawString(3 * inch, height - 1.5 * inch, "Category")
# # #         pdf_canvas.drawString(4 * inch, height - 1.5 * inch, "Stock")
# # #         pdf_canvas.drawString(5 * inch, height - 1.5 * inch, "Unit Price")
# # #         pdf_canvas.drawString(6 * inch, height - 1.5 * inch, "Expiry Date")

# # #         # Table Data
# # #         pdf_canvas.setFont("Helvetica", 10)
# # #         y_position = height - 1.7 * inch  # Start below the header

# # #         for item in self.inventory_data:
# # #             pdf_canvas.drawString(1 * inch, y_position, item['type__name'])
# # #             pdf_canvas.drawString(3 * inch, y_position, item['category__name'])
# # #             pdf_canvas.drawString(4 * inch, y_position, str(item['stock_level']))
# # #             pdf_canvas.drawString(5 * inch, y_position, f"{float(item['unit_price']):,.2f} XAF")
# # #             # pdf_canvas.drawString(6 * inch, y_position, item.get('expiry_date', 'N/A'))
# # #             y_position -= 0.2 * inch  # Move down for the next row

# # #         # Save the PDF
# # #         pdf_canvas.save()

# # # if __name__ == "__main__":
# # #     app = QApplication([])
# # #     window = InventoryReportsDialog()
# # #     window.show()
# # #     app.exec()


# # import os
# # import tempfile
# # import requests
# # from datetime import datetime
# # from PySide6.QtWidgets import (
# #     QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
# #     QLabel, QPushButton, QComboBox, QMessageBox
# # )
# # from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# # from PySide6.QtWidgets import QApplication
# # from reportlab.lib.pagesizes import letter
# # from reportlab.pdfgen import canvas
# # from reportlab.lib.pagesizes import A4
# # from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# # from PySide6.QtGui import QPageLayout
# # from PySide6.QtGui import QPageSize
# # from PySide6.QtCore import QMarginsF  # Correct
# # import tempfile

# # from reportlab.lib.pagesizes import A4
# # from reportlab.lib import colors
# # from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# # from PySide6.QtPrintSupport import QPrinter
# # from PySide6.QtGui import QPdfWriter
# # from PySide6.QtGui import QPageSize
# # from PySide6.QtCore import QFile


# # BASE_URL = "http://127.0.0.1:8000/"  # Django backend

# # class InventoryReportsDialog(QDialog):
# #     """Dialog for generating, filtering, and printing inventory reports."""
    
# #     def __init__(self, parent=None):
# #         super().__init__(parent)
# #         self.setWindowTitle("Inventory Reports")
# #         self.setMinimumSize(900, 500)

# #         layout = QVBoxLayout()

# #         # Instance variable to store inventory data
# #         self.inventory_data = []

# #         # 🔹 Filter Section
# #         filter_layout = QHBoxLayout()
# #         self.category_combo = QComboBox()
# #         self.category_combo.addItem("All Categories")
# #         self.fetch_categories()  # Populate categories

# #         self.stock_level_combo = QComboBox()
# #         self.stock_level_combo.addItems(["All", "Low Stock (<10)", "Out of Stock (0)"])

# #         self.expiry_combo = QComboBox()
# #         self.expiry_combo.addItems(["All", "Expired", "Expiring Soon (<30 days)"])

# #         self.filter_button = QPushButton("Apply Filters")
# #         self.filter_button.clicked.connect(self.fetch_inventory_data)

# #         filter_layout.addWidget(QLabel("Category:"))
# #         filter_layout.addWidget(self.category_combo)
# #         filter_layout.addWidget(QLabel("Stock Level:"))
# #         filter_layout.addWidget(self.stock_level_combo)
# #         filter_layout.addWidget(QLabel("Expiry:"))
# #         filter_layout.addWidget(self.expiry_combo)
# #         filter_layout.addWidget(self.filter_button)

# #         layout.addLayout(filter_layout)

# #         # 🔹 Table Section
# #         self.inventory_table = QTableWidget()
# #         self.inventory_table.setColumnCount(5)
# #         self.inventory_table.setHorizontalHeaderLabels(["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"])
# #         layout.addWidget(self.inventory_table)

# #         # 🔹 Print Button
# #         self.print_button = QPushButton("Print Inventory Report")
# #         self.print_button.clicked.connect(self.preview_inventory_report)
# #         layout.addWidget(self.print_button)

# #         self.setLayout(layout)

# #     def fetch_categories(self):
# #         """Fetch categories from the backend."""
# #         try:
# #             response = requests.get(f"{BASE_URL}auth/categories/")
# #             if response.status_code == 200:
# #                 categories = response.json()
# #                 for category in categories:
# #                     self.category_combo.addItem(category["name"], category["id"])
# #             else:
# #                 QMessageBox.warning(self, "Error", "Failed to fetch categories.")
# #         except requests.RequestException as e:
# #             QMessageBox.critical(self, "Network Error", str(e))

# #     def fetch_inventory_data(self):
# #         """Fetch inventory data based on filters and update the table."""
# #         category_id = self.category_combo.currentData() if self.category_combo.currentIndex() > 0 else None
# #         stock_filter = self.stock_level_combo.currentText()
# #         expiry_filter = self.expiry_combo.currentText()

# #         try:
# #             response = requests.get(
# #                 f"{BASE_URL}auth/inventory-report/", 
# #                 params={"category_id": category_id, "stock": stock_filter, "expiry": expiry_filter}
# #             )
# #             data = response.json()

# #             if response.status_code == 200 and data.get("inventory"):
# #                 self.inventory_data = data["inventory"]  # Store the fetched data
# #                 self.inventory_table.setRowCount(0)

# #                 for row, item in enumerate(self.inventory_data):
# #                     self.inventory_table.insertRow(row)
# #                     self.inventory_table.setItem(row, 0, QTableWidgetItem(item["type__name"]))
# #                     self.inventory_table.setItem(row, 1, QTableWidgetItem(item["category__name"]))
# #                     self.inventory_table.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))

# #                     unit_price = float(item["unit_price"])
# #                     self.inventory_table.setItem(row, 3, QTableWidgetItem(f"{unit_price:,.2f} XAF"))

# #                     expiry_date = item.get("expiry_date", "N/A")
# #                     self.inventory_table.setItem(row, 4, QTableWidgetItem(expiry_date))

# #             else:
# #                 QMessageBox.information(self, "No Data", "No inventory data found.")

# #         except requests.RequestException as e:
# #             QMessageBox.critical(self, "Network Error", str(e))

# #     def preview_inventory_report(self):
# #         """Generate a print preview of the inventory report."""
# #         if not self.inventory_data:
# #             QMessageBox.warning(self, "No Data", "Please fetch inventory data before printing.")
# #             return

# #         printer = QPrinter(QPrinter.HighResolution)
# #         preview_dialog = QPrintPreviewDialog(printer, self)
# #         preview_dialog.paintRequested.connect(self.render_pdf)
# #         preview_dialog.exec()  # Show print preview

# #     def render_pdf(self, printer=None):
# #         """Generates an inventory report PDF and prints it using QPrinter if provided."""

# #         # Step 1: Create a Temporary File
# #         with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
# #             filename = temp_pdf.name  # Get temporary file path

# #         # Step 2: Generate PDF
# #         PAGE_WIDTH, PAGE_HEIGHT = A4
# #         MARGIN = 30  # Margin from edges

# #         col_widths = [PAGE_WIDTH / 5] * 5  # Adjust column widths equally

# #         # Define sample inventory data (Replace with actual data)
# #         data = [["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"]]  # Header row
# #         for item in self.inventory_data:
# #             data.append([
# #                 item.get("type__name", "N/A"),
# #                 item.get("category__name", "N/A"),
# #                 str(item.get("stock_level", 0)),
# #                 f"{float(item.get('unit_price', 0.0)):,.2f} XAF",
# #                 item.get("expiry_date", "N/A") or "N/A"
# #             ])

# #         num_rows = len(data)
# #         row_height = (PAGE_HEIGHT - (2 * MARGIN)) / num_rows  # Scale rows

# #         table = Table(data, colWidths=col_widths, rowHeights=row_height)

# #         # Apply styling
# #         table.setStyle(TableStyle([
# #             ("BACKGROUND", (0, 0), (-1, 0), colors.grey),  # Header background color
# #             ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),  # Header text color
# #             ("ALIGN", (0, 0), (-1, -1), "CENTER"),
# #             ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
# #             ("FONTSIZE", (0, 0), (-1, -1), 10),
# #             ("BOTTOMPADDING", (0, 0), (-1, 0), 8),
# #             ("BACKGROUND", (0, 1), (-1, -1), colors.white),
# #             ("GRID", (0, 0), (-1, -1), 1, colors.black),
# #         ]))

# #         pdf = SimpleDocTemplate(filename, pagesize=A4)
# #         pdf.build([table])  # Generate PDF

# #         print(f"✅ PDF generated: {filename}")

# #         # Step 3: Print PDF using QPrinter if printer is provided
# #         if printer:
# #             printer.setDocName("Inventory Report")
# #             printer.setPageSize(QPageSize(QPageSize.A4))

# #             # Use QPainter to print the PDF
# #             painter = QPainter()
# #             if not painter.begin(printer):
# #                 print("❌ Failed to start printer")
# #                 return

# #             # Load the generated PDF and draw it on the printer
# #             pdf_reader = PdfReader(filename)
# #             page = pdf_reader.pages[0]  # Get first page
# #             page_text = page.extract_text()

# #             # Draw text content of the PDF onto the printer
# #             painter.drawText(100, 100, page_text)  

# #             painter.end()  # Close QPainter properly

# #             print("✅ PDF sent to printer.")

# #         return filename  # Return the generated PDF file path

# # if __name__ == "__main__":
# #     app = QApplication([])
# #     window = InventoryReportsDialog()
# #     window.show()
# #     app.exec()

# import os
# import tempfile
# import fitz
# import requests
# from datetime import datetime
# from PySide6.QtWidgets import (
#     QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
#     QLabel, QPushButton, QComboBox, QMessageBox
# )
# from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# from PySide6.QtWidgets import QApplication
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# from PySide6.QtGui import QPageLayout
# from PySide6.QtGui import QPageSize
# from PySide6.QtCore import QMarginsF  # Correct
# import tempfile

# from reportlab.lib.pagesizes import A4
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from PySide6.QtPrintSupport import QPrinter
# from PySide6.QtGui import QPdfWriter
# from PySide6.QtGui import QPageSize
# from PySide6.QtCore import QFile
# from PySide6.QtGui import QPainter
# from PySide6.QtCore import Qt
# from PySide6.QtGui import QImage, QFont
# from PySide6.QtGui import QPainter, QImage
# # from PyMuPDF import fitz  # PyMuPDF for rendering PDF pages

# import os
# import tempfile
# import requests
# from PySide6.QtWidgets import (
#     QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
#     QLabel, QPushButton, QComboBox, QMessageBox
# )
# from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# from PySide6.QtWidgets import QApplication
# from reportlab.lib.pagesizes import A4
# from reportlab.lib import colors
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# from PySide6.QtGui import QPainter, QImage
# from PySide6.QtCore import Qt
# # from PyMuPDF import fitz  # PyMuPDF for PDF rendering

# BASE_URL = "http://127.0.0.1:8000/"  # Django backend

# class InventoryReportsDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#         self.setWindowTitle("Inventory Reports")
#         self.setMinimumSize(900, 500)

#         layout = QVBoxLayout()
#         self.inventory_data = []

#         filter_layout = QHBoxLayout()
#         self.category_combo = QComboBox()
#         self.category_combo.addItem("All Categories")
#         self.fetch_categories()

#         self.stock_level_combo = QComboBox()
#         self.stock_level_combo.addItems(["All", "Low Stock (<10)", "Out of Stock (0)"])

#         self.expiry_combo = QComboBox()
#         self.expiry_combo.addItems(["All", "Expired", "Expiring Soon (<30 days)"])

#         self.filter_button = QPushButton("Apply Filters")
#         self.filter_button.clicked.connect(self.fetch_inventory_data)

#         filter_layout.addWidget(QLabel("Category:"))
#         filter_layout.addWidget(self.category_combo)
#         filter_layout.addWidget(QLabel("Stock Level:"))
#         filter_layout.addWidget(self.stock_level_combo)
#         filter_layout.addWidget(QLabel("Expiry:"))
#         filter_layout.addWidget(self.expiry_combo)
#         filter_layout.addWidget(self.filter_button)

#         layout.addLayout(filter_layout)

#         self.inventory_table = QTableWidget()
#         self.inventory_table.setColumnCount(5)
#         self.inventory_table.setHorizontalHeaderLabels(["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"])
#         layout.addWidget(self.inventory_table)

#         self.print_button = QPushButton("Print Inventory Report")
#         self.print_button.clicked.connect(self.preview_inventory_report)
#         layout.addWidget(self.print_button)

#         self.setLayout(layout)

#     def fetch_categories(self):
#         try:
#             response = requests.get(f"{BASE_URL}auth/categories/")
#             if response.status_code == 200:
#                 categories = response.json()
#                 for category in categories:
#                     self.category_combo.addItem(category["name"], category["id"])
#         except requests.RequestException as e:
#             QMessageBox.critical(self, "Network Error", str(e))

#     def fetch_inventory_data(self):
#         category_id = self.category_combo.currentData() if self.category_combo.currentIndex() > 0 else None
#         stock_filter = self.stock_level_combo.currentText()
#         expiry_filter = self.expiry_combo.currentText()

#         try:
#             response = requests.get(
#                 f"{BASE_URL}auth/inventory-report/", 
#                 params={"category_id": category_id, "stock": stock_filter, "expiry": expiry_filter}
#             )
#             data = response.json()

#             if response.status_code == 200 and data.get("inventory"):
#                 self.inventory_data = data["inventory"]
#                 self.inventory_table.setRowCount(0)

#                 for row, item in enumerate(self.inventory_data):
#                     self.inventory_table.insertRow(row)
#                     self.inventory_table.setItem(row, 0, QTableWidgetItem(item["type__name"]))
#                     self.inventory_table.setItem(row, 1, QTableWidgetItem(item["category__name"]))
#                     self.inventory_table.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))
#                     self.inventory_table.setItem(row, 3, QTableWidgetItem(f"{float(item['unit_price']):,.2f} XAF"))
#                     self.inventory_table.setItem(row, 4, QTableWidgetItem(item.get("expiry_date", "N/A")))
#         except requests.RequestException as e:
#             QMessageBox.critical(self, "Network Error", str(e))

#     def preview_inventory_report(self):
#         if not self.inventory_data:
#             QMessageBox.warning(self, "No Data", "Please fetch inventory data before printing.")
#             return

#         with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_pdf:
#             filename = temp_pdf.name

#         data = [[self.inventory_table.horizontalHeaderItem(i).text() for i in range(self.inventory_table.columnCount())]]
#         for row in range(self.inventory_table.rowCount()):
#             data.append([self.inventory_table.item(row, col).text() if self.inventory_table.item(row, col) else "" for col in range(self.inventory_table.columnCount())])

#         pdf = SimpleDocTemplate(filename, pagesize=A4)
#         table = Table(data)
#         table.setStyle(TableStyle([
#             ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
#             ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
#             ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#             ("GRID", (0, 0), (-1, -1), 1, colors.black)
#         ]))
#         pdf.build([table])

#         # Use QPrinter and QPrintPreviewDialog for direct PDF preview
#         printer = QPrinter(QPrinter.HighResolution)
#         preview_dialog = QPrintPreviewDialog(printer, self)
#         preview_dialog.paintRequested.connect(lambda p: self.render_pdf_directly(p, filename))
#         preview_dialog.exec()

#     def render_pdf_directly(self, painter, filename):
#         # Render the PDF content directly using QPdfWriter or QPainter
#         pdf_writer = QPdfWriter(filename)
#         pdf_writer.setPageSize(QPageSize(QPageSize.A4))
#         painter.begin(pdf_writer)
#         doc = fitz.open(filename)
#         for page_num in range(len(doc)):
#             page = doc.load_page(page_num)  # Load the page from PDF
#             # Use QPainter's drawText or drawImage methods to render content on the painter
#             # Render PDF content on the painter here
#             painter.end()


# if __name__ == "__main__":
#     app = QApplication([])
#     window = InventoryReportsDialog()
#     window.show()
#     app.exec()

import sys
import tempfile
import csv
import requests
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QLabel,
    QPushButton, QComboBox, QMessageBox, QFileDialog
)
from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PySide6.QtGui import QPainter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle

BASE_URL = "http://127.0.0.1:8000/"  # Django backend

class InventoryReportsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inventory Reports")
        self.setMinimumSize(900, 500)
        
        layout = QVBoxLayout()
        filter_layout = QHBoxLayout()
        self.category_combo = QComboBox()
        self.category_combo.addItem("All Categories")
        self.fetch_categories()

        self.stock_level_combo = QComboBox()
        self.stock_level_combo.addItems(["All", "Low Stock (<10)", "Out of Stock (0)"])

        self.expiry_combo = QComboBox()
        self.expiry_combo.addItems(["All", "Expired", "Expiring Soon (<30 days)"])

        filter_layout.addWidget(QLabel("Category:"))
        filter_layout.addWidget(self.category_combo)
        filter_layout.addWidget(QLabel("Stock Level:"))
        filter_layout.addWidget(self.stock_level_combo)
        filter_layout.addWidget(QLabel("Expiry:"))
        filter_layout.addWidget(self.expiry_combo)
        
        self.generate_button = QPushButton("Generate Report")
        self.generate_button.clicked.connect(self.fetch_inventory_data)
        filter_layout.addWidget(self.generate_button)
        layout.addLayout(filter_layout)

        self.inventory_table = QTableWidget()
        self.inventory_table.setColumnCount(5)
        self.inventory_table.setHorizontalHeaderLabels(["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"])
        layout.addWidget(self.inventory_table)

        button_layout = QHBoxLayout()
        self.preview_button = QPushButton("Preview Report")
        self.print_button = QPushButton("Print Report")

        self.preview_button.clicked.connect(self.preview_report)
        self.print_button.clicked.connect(self.print_report)

        button_layout.addWidget(self.preview_button)
        button_layout.addWidget(self.print_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)
        self.temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name

    def fetch_categories(self):
        try:
            response = requests.get(f"{BASE_URL}auth/categories/")
            if response.status_code == 200:
                for category in response.json():
                    self.category_combo.addItem(category["name"], category["id"])
        except requests.RequestException:
            QMessageBox.critical(self, "Network Error", "Failed to fetch categories.")

    def fetch_inventory_data(self):
        try:
            response = requests.get(f"{BASE_URL}auth/inventory-report/")
            data = response.json()
            if response.status_code == 200 and data.get("inventory"):
                self.inventory_table.setRowCount(0)
                for row, item in enumerate(data["inventory"]):
                    self.inventory_table.insertRow(row)
                    self.inventory_table.setItem(row, 0, QTableWidgetItem(item["type__name"]))
                    self.inventory_table.setItem(row, 1, QTableWidgetItem(item["category__name"]))
                    self.inventory_table.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))
                    self.inventory_table.setItem(row, 3, QTableWidgetItem(f"{float(item['unit_price']):,.2f} XAF"))
                    self.inventory_table.setItem(row, 4, QTableWidgetItem(item.get("expiry_date", "N/A")))
        except requests.RequestException:
            QMessageBox.critical(self, "Network Error", "Failed to fetch inventory data.")

    def generate_pdf(self, filename):
        doc = SimpleDocTemplate(filename, pagesize=A4)
        data = [["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"]]
        for row in range(self.inventory_table.rowCount()):
            row_data = [self.inventory_table.item(row, col).text() for col in range(self.inventory_table.columnCount())]
            data.append(row_data)
        table = Table(data, colWidths=[100, 100, 80, 100, 120])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
            ('GRID', (0, 0), (-1, -1), 1, colors.black)
        ]))
        doc.build([table])

    def preview_report(self):
        printer = QPrinter()
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.render_pdf)
        preview_dialog.exec()

    def render_pdf(self, printer):
        painter = QPainter(printer)
        painter.setFont(QPainter().font())
        y_position = 100
        column_headers = ["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"]
        
        for col, header in enumerate(column_headers):
            painter.drawText(100 + col * 100, y_position, header)
        y_position += 30
        
        for row in range(self.inventory_table.rowCount()):
            for col in range(self.inventory_table.columnCount()):
                text = self.inventory_table.item(row, col).text()
                painter.drawText(100 + col * 100, y_position, text)
            y_position += 30
        
        painter.end()

    def print_report(self):
        file_dialog = QFileDialog(self, "Save Report", "", "PDF Files (*.pdf)")
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
        if file_dialog.exec():
            save_path = file_dialog.selectedFiles()[0]
            self.generate_pdf(save_path)
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.OutputFormat.NativeFormat)
        painter = QPainter(printer)
        painter.end()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryReportsDialog()
    window.show()
    sys.exit(app.exec())
