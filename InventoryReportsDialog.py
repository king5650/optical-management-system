import os
import csv
import requests
from datetime import datetime
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
    QLabel, QPushButton, QComboBox, QMessageBox
)
from PySide6.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog
from PySide6.QtGui import QPainter
from PySide6.QtPrintSupport import QPrinter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from PySide6.QtWidgets import QApplication

BASE_URL = "http://127.0.0.1:8000/"  # Django backend
class InventoryPrintDialog(QDialog):
    """Dialog for Print Preview before final printing."""
    
    def __init__(self, pdf_path, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Print Preview")
        self.setMinimumSize(800, 600)
        self.pdf_path = pdf_path  # Store the PDF file path

        layout = QVBoxLayout()

        # 📌 Print Button
        self.print_button = QPushButton("Print")
        self.print_button.clicked.connect(self.print_pdf)
        layout.addWidget(self.print_button)

        self.setLayout(layout)

    def load_pdf_preview(self, printer):
        """Render the actual PDF into the print preview."""
        from PySide6.QtGui import QPdfDocument
        
        pdf_doc = QPdfDocument()
        pdf_doc.load(self.pdf_path)  # Load the generated PDF file
        
        painter = QPainter(printer)
        pdf_doc.render(painter)  # Render PDF into the preview window
        painter.end()

    def print_pdf(self):
        """Open the system print dialog to print the PDF."""
        printer = QPrinter(QPrinter.HighResolution)
        preview = QPrintPreviewDialog(printer, self)
        
        preview.paintRequested.connect(self.load_pdf_preview)  # Load actual PDF
        preview.exec()  # Show preview dialog
        
        os.system(f"start {self.pdf_path}")  # Open PDF after preview
        QMessageBox.information(self, "Printing", "Inventory report sent to the printer.")
        self.accept()  # Close preview after printing

import os
import csv
import requests
from datetime import datetime
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
    QLabel, QPushButton, QComboBox, QMessageBox
)
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QWidget, QTableWidgetItem, QLabel,  QScrollArea, QVBoxLayout



from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from PySide6.QtPrintSupport import QPrintPreviewDialog, QPrinter
from PySide6.QtGui import QPainter
from PySide6.QtWidgets import QFileDialog
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from datetime import datetime
import os


BASE_URL = "http://127.0.0.1:8000/"  # Django backend

class InventoryReportsDialog(QDialog):
    """Dialog for generating and exporting inventory reports."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Inventory Reports")
        self.setMinimumSize(900, 500)
        
        

        layout = QVBoxLayout()

        # 🔹 Filter Section
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

        # 🔹 Table Section
        self.inventory_table = QTableWidget()
        self.inventory_table.setColumnCount(5)
        self.inventory_table.setHorizontalHeaderLabels(["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"])
        layout.addWidget(self.inventory_table)

        # 🔹 Export Buttons
        button_layout = QHBoxLayout()
        self.export_pdf_button = QPushButton("Export PDF Report")
        self.export_csv_button = QPushButton("Export CSV Report")

        # self.export_pdf_button.clicked.connect(self.export_pdf_report)
        self.export_pdf_button.clicked.connect(self.generate_pdf)
        self.export_csv_button.clicked.connect(self.export_csv_report)

        button_layout.addWidget(self.export_pdf_button)
        button_layout.addWidget(self.export_csv_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

    def fetch_categories(self):
        """Fetch categories from the backend."""
        try:
            response = requests.get(f"{BASE_URL}auth/categories/")
            if response.status_code == 200:
                categories = response.json()
                for category in categories:
                    self.category_combo.addItem(category["name"], category["id"])
            else:
                QMessageBox.warning(self, "Error", "Failed to fetch categories.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    def fetch_inventory_data(self):
        """Fetch inventory data based on filters and display in the table."""
        category_id = self.category_combo.currentData() if self.category_combo.currentIndex() > 0 else None
        stock_filter = self.stock_level_combo.currentText()
        expiry_filter = self.expiry_combo.currentText()

        try:
            response = requests.get(f"{BASE_URL}auth/inventory-report/", 
                                    params={"category_id": category_id, "stock": stock_filter, "expiry": expiry_filter})
            data = response.json()

            if response.status_code == 200 and data.get("inventory"):
                inventory = data["inventory"]
                self.inventory_table.setRowCount(0)

                for row, item in enumerate(inventory):
                    self.inventory_table.insertRow(row)
                    self.inventory_table.setItem(row, 0, QTableWidgetItem(item["type__name"]))
                    self.inventory_table.setItem(row, 1, QTableWidgetItem(item["category__name"]))
                    self.inventory_table.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))

                    # ✅ Convert unit_price to float before formatting
                    unit_price = float(item["unit_price"])
                    self.inventory_table.setItem(row, 3, QTableWidgetItem(f"{unit_price:,.2f} XAF"))

                    expiry_date = item.get("expiry_date", "N/A")
                    self.inventory_table.setItem(row, 4, QTableWidgetItem(expiry_date))

            else:
                QMessageBox.information(self, "No Data", "No inventory data found.")

        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))

    # def print_inventory_report(self):
    #     """Generate a detailed inventory report and show print preview."""
    #     filename = f"Inventory_Report_{datetime.now().strftime('%Y-%m-%d')}.pdf"
    #     pdf_path = os.path.join(os.getcwd(), filename)

    #     c = canvas.Canvas(pdf_path, pagesize=A4)
    #     width, height = A4
    #     margin = 1.0 * inch

    #     c.setFont("Helvetica-Bold", 16)
    #     c.drawString(margin, height - margin, "Inventory Report")
    #     c.setFont("Helvetica", 12)
    #     c.drawString(margin, height - 1.3 * inch, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

    #     table_data = [["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"]]
    #     for row in range(self.inventory_table.rowCount()):
    #         row_data = [self.inventory_table.item(row, col).text() for col in range(self.inventory_table.columnCount())]
    #         table_data.append(row_data)

    #     y_position = height - 2 * inch
    #     for row in table_data:
    #         c.drawString(margin, y_position, "  ".join(row))
    #         y_position -= 0.3 * inch
    #         if y_position < margin:
    #             c.showPage()
    #             y_position = height - 2 * inch

    #     c.save()

    #     # Show Print Preview Dialog
    #     preview_dialog = InventoryPrintDialog(pdf_path, self)
    #     preview_dialog.exec()
    


    def generate_pdf():
        save_path = "C:/Users/falco/Desktop/system_optic/reports/"
        if not os.path.exists(save_path):
            os.makedirs(save_path)  # Ensure the directory exists
        
        pdf_filename = os.path.join(save_path, "inventory_report.pdf")
        print(f"Saving PDF to: {pdf_filename}")  # Debugging print
        
        assert pdf_filename, "Error: pdf_filename is False or None!"
        
        doc = SimpleDocTemplate(pdf_filename)
        styles = getSampleStyleSheet()
        elements = [Paragraph("Inventory Report", styles['Title']), Spacer(1, 12)]
        
        # Add more content to elements as needed
        
        doc.build(elements)
        print("PDF generated successfully.")

    generate_pdf()


    def preview_report(self):
        """Preview the document in QPrintPreviewDialog."""
        printer = QPrinter()
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.render_pdf)
        preview_dialog.exec()


    def render_pdf(self, printer):
        """Render the document onto QPrintPreviewDialog using QPainter."""
        painter = QPainter(printer)

        # Header
        painter.setFont(QPainter().font())
        painter.drawText(100, 100, "Inventory Report")
        painter.drawText(100, 130, "Generated using PyQt6 & ReportLab")

        # Table Data
        data = [["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"]]
        for row in range(self.inventory_table.rowCount()):
            row_data = [self.inventory_table.item(row, col).text() for col in range(self.inventory_table.columnCount())]
            data.append(row_data)

        x_start = 100
        y_start = 200
        row_height = 30
        col_widths = [100, 100, 80, 100, 120]

        # Draw Table
        for row_idx, row in enumerate(data):
            for col_idx, cell in enumerate(row):
                painter.drawText(x_start + sum(col_widths[:col_idx]) + 10, y_start + (row_idx * row_height) + 20, cell)

        # Draw Table Grid
        for row_idx in range(len(data) + 1):  # Rows
            y_pos = y_start + (row_idx * row_height)
            painter.drawLine(x_start, y_pos, x_start + sum(col_widths), y_pos)

        for col_idx in range(len(col_widths) + 1):  # Columns
            x_pos = x_start + sum(col_widths[:col_idx])
            painter.drawLine(x_pos, y_start, x_pos, y_start + (len(data) * row_height))

        painter.end()


    def print_report(self):
        """Print the document directly."""
        printer = QPrinter()
        file_dialog = QFileDialog(self, "Print Report", "", "PDF Files (*.pdf)")
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

        if file_dialog.exec():
            save_path = file_dialog.selectedFiles()[0]
            self.generate_pdf(save_path)  # Save PDF before printing

        printer.setOutputFormat(QPrinter.OutputFormat.NativeFormat)
        painter = QPainter(printer)

        # Header
        painter.setFont(QPainter().font())
        painter.drawText(100, 100, "Inventory Report")
        painter.drawText(100, 130, "Generated using PyQt6 & ReportLab")

        # Table Data
        data = [["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"]]
        for row in range(self.inventory_table.rowCount()):
            row_data = [self.inventory_table.item(row, col).text() for col in range(self.inventory_table.columnCount())]
            data.append(row_data)

        x_start = 100
        y_start = 200
        row_height = 30
        col_widths = [100, 100, 80, 100, 120]

        # Draw Table
        for row_idx, row in enumerate(data):
            for col_idx, cell in enumerate(row):
                painter.drawText(x_start + sum(col_widths[:col_idx]) + 10, y_start + (row_idx * row_height) + 20, cell)

        # Draw Table Grid
        for row_idx in range(len(data) + 1):  # Rows
            y_pos = y_start + (row_idx * row_height)
            painter.drawLine(x_start, y_pos, x_start + sum(col_widths), y_pos)

        for col_idx in range(len(col_widths) + 1):  # Columns
            x_pos = x_start + sum(col_widths[:col_idx])
            painter.drawLine(x_pos, y_start, x_pos, y_start + (len(data) * row_height))

        painter.end()

    # def export_pdf_report(self):
    #     """Generate and export inventory report as a PDF."""
    #     filename = f"Inventory_Report_{datetime.now().strftime('%Y-%m-%d')}.pdf"
    #     c = canvas.Canvas(filename, pagesize=A4)
    #     width, height = A4
    #     margin = 1 * inch

    #     c.setFont("Helvetica-Bold", 16)
    #     c.drawString(margin, height - margin, "Inventory Report")
    #     c.setFont("Helvetica", 12)
    #     c.drawString(margin, height - 1.3 * inch, f"Date: {datetime.now().strftime('%Y-%m-%d')}")

    #     table_data = [["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"]]
    #     for row in range(self.inventory_table.rowCount()):
    #         row_data = [self.inventory_table.item(row, col).text() for col in range(self.inventory_table.columnCount())]
    #         table_data.append(row_data)

    #     y_position = height - 2 * inch
    #     for row in table_data:
    #         c.drawString(margin, y_position, "  ".join(row))
    #         y_position -= 0.3 * inch
    #         if y_position < margin:
    #             c.showPage()
    #             y_position = height - 2 * inch

    #     c.save()
    #     QMessageBox.information(self, "Export Successful", f"PDF Report saved as {filename}")

    def export_csv_report(self):
        """Generate and export inventory report as a CSV file."""
        filename = f"Inventory_Report_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Item Type", "Category", "Stock", "Unit Price", "Expiry Date"])

            for row in range(self.inventory_table.rowCount()):
                row_data = [self.inventory_table.item(row, col).text() for col in range(self.inventory_table.columnCount())]
                writer.writerow(row_data)

        QMessageBox.information(self, "Export Successful", f"CSV Report saved as {filename}")
if __name__ == "__main__":
    app = QApplication([])
    window = InventoryReportsDialog()
    window.show()
    app.exec()