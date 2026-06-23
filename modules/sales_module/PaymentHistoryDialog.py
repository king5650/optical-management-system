import os
import requests
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QComboBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox,QHeaderView
)
from PySide6.QtCore import Slot
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
import csv
import os
import csv
import requests
from PySide6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QPushButton, 
    QTableWidget, QTableWidgetItem, QLabel, QMessageBox, QFileDialog
)
from PySide6.QtCore import Slot, Qt
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
import sys  

BASE_URL = "http://127.0.0.1:8000/"  

class PaymentHistoryDialog(QDialog):
    """Dialog for displaying payment history."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Payment History")
        self.setMinimumSize(1070, 500)  # ✅ Increased width to fit new columns
        self.setStyleSheet("""
            /* Paste the QSS stylesheet here */
            QDialog {
                background-color: rgb(88, 162, 157);
                color: rgb(255, 255, 255);
                font-family: "Segoe UI", sans-serif;
                font-size: 14px;
            }
            /* Add the rest of the stylesheet */
            /* General Styles */
            
            /* Labels */
            QLabel {
                color: #333333;
                font-weight: bold;
            }

            /* Combo Boxes */
            QComboBox {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 5px;
                min-width: 100px;
                color: black;
            }

            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 20px;
                border-left: 1px solid #cccccc;
            }

            QComboBox::down-arrow {
                image: url(/images/plus_48px); /* Add a custom arrow icon if needed */
            }

            /* Line Edit */
            QLineEdit {
                background-color: #ffffff;
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 5px;
                color: black;
            }

            QLineEdit:focus {
                border: 1px solid #0078d7;
            }

            /* Buttons 
            QPushButton {
                	background-color: rgb(0, 0, 99);
                color: #ffffff;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                font-weight: bold;
            }*/
            QPushButton{
                background-color: rgb(255, 255, 255);
                border-radius: 5px;
                padding: 10px;
                color: rgb(0, 0, 0);
                width: 90px;
                font-weight: 900;
            }

            QPushButton:hover {
                background-color: #005bb5;
            }

            QPushButton:pressed {
                background-color: #004080;
            }

            /* Table Widget */
            QTableWidget {
                background-color: rgb(88, 162, 157);
                border: 1px solid #cccccc;
                border-radius: 4px;
                gridline-color: #cccccc;
                selection-	background-color: rgb(0, 0, 99);
                selection-color: #ffffff;
                color: white;
                font-weight: 900;
                font-size: 13px;
            }

            QHeaderView::section {
                /*background-color: rgb(0, 0, 99);*/
                background-color: rgb(88, 162, 157);
                color: #ffffff;
                padding: 8px;
                border: 2px solid whitesmoke;
                font-weight: 900;
            }

            QTableWidget::item {
                padding: 5px;
            }

            QTableWidget::item:selected {
                background-color: #0078d7;
                color: #ffffff;
            }

            /* Scrollbars */
            QScrollBar:vertical {
                background-color: #f5f5f5;
                width: 12px;
                margin: 0px 0px 0px 0px;
            }

            QScrollBar::handle:vertical {
                background-color: #cccccc;
                border-radius: 6px;
                min-height: 20px;
            }

            QScrollBar::add-line:vertical,
            QScrollBar::sub-line:vertical {
                background: none;
            }

            QScrollBar::add-page:vertical,
            QScrollBar::sub-page:vertical {
                background: none;
            }

            QScrollBar:horizontal {
                background-color: #f5f5f5;
                height: 12px;
                margin: 0px 0px 0px 0px;
            }

            QScrollBar::handle:horizontal {
                background-color: #cccccc;
                border-radius: 6px;
                min-width: 20px;
            }

            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                background: none;
            }

            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background: none;
            }
        """)
        layout = QVBoxLayout()

        # 🔹 Year & Month Filters
        filter_layout = QHBoxLayout()
        
        self.year_combo = QComboBox()
        self.populate_years()  # ✅ Call method to dynamically populate years

        self.month_combo = QComboBox()
        self.month_combo.addItems(["All", "January", "February", "March", "April", "May", "June",
                                   "July", "August", "September", "October", "November", "December"])

        filter_layout.addWidget(QLabel("Year:"))
        filter_layout.addWidget(self.year_combo)
        filter_layout.addWidget(QLabel("Month:"))
        filter_layout.addWidget(self.month_combo)

        # 🔹 Search Field
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name or details...")
        filter_layout.addWidget(self.search_input)

        # 🔹 Search Button
        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.fetch_payment_history)
        filter_layout.addWidget(self.search_button)
        layout.addLayout(filter_layout)

        # 🔹 Payment Table (Now has 7 Columns!)
        self.payment_table = QTableWidget()
        self.payment_table.setColumnCount(7)  # ✅ Updated column count
        self.payment_table.setHorizontalHeaderLabels([
            "Date", "Patient Name", "Amount Paid", "Payment Method", 
            "Reference", "Total VAT", "Total Balance"  # ✅ New Columns
        ])
        layout.addWidget(self.payment_table)

        # 🔹 Buttons for PDF & CSV Export
        button_layout = QHBoxLayout()
        self.print_pdf_button = QPushButton("Print PDF Copy")
        self.export_csv_button = QPushButton("Export CSV Copy")

        self.print_pdf_button.clicked.connect(self.generate_pdf)
        self.export_csv_button.clicked.connect(self.export_to_csv)

        button_layout.addWidget(self.print_pdf_button)
        button_layout.addWidget(self.export_csv_button)
        layout.addLayout(button_layout)

        self.setLayout(layout)

        # ✅ Automatically fetch all payment history when the dialog opens
        self.fetch_payment_history()

        # ✅ Auto-refresh table when year or month is selected
        self.year_combo.currentIndexChanged.connect(self.fetch_payment_history)
        self.month_combo.currentIndexChanged.connect(self.fetch_payment_history)

    def populate_years(self):
        """Dynamically populate the year combo box from 2024 to the current year."""
        current_year = datetime.now().year  # Get the current year
        self.year_combo.addItem("All")  # ✅ Default option to show all payments
        self.year_combo.addItems([str(year) for year in range(2024, current_year + 1)])

    @Slot()
    def fetch_payment_history(self):
        """Fetch and display payment history based on selected filters."""
        year = self.year_combo.currentText()
        month = self.month_combo.currentIndex()  # 0 = All, 1 = January, etc.
        search_query = self.search_input.text().strip()
        self.payment_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # ✅ Convert "All" to empty string (backend should handle empty filters)
        year = "" if year == "All" else year
        month = "" if month == 0 else str(month)  # Convert index to string

        try:
            response = requests.get(f"{BASE_URL}auth/payment-history/",
                                    params={"year": year, "month": month, "search": search_query})
            data = response.json()
            print("API Response:", data)  # ✅ Debugging

            if response.status_code == 200:
                payments = data.get("payments", [])
                self.payment_table.setRowCount(0)  # Clear table

                if not payments:
                    QMessageBox.information(self, "No Payments", "No payments found for the selected filters.")
                    return

                for row, payment in enumerate(payments):
                    self.payment_table.insertRow(row)
                    self.payment_table.setItem(row, 0, QTableWidgetItem(payment["date"]))
                    self.payment_table.setItem(row, 1, QTableWidgetItem(payment["patient"]))
                    self.payment_table.setItem(row, 2, QTableWidgetItem(f"{payment['amount']:,.2f} XAF"))
                    self.payment_table.setItem(row, 3, QTableWidgetItem(payment["method"]))
                    self.payment_table.setItem(row, 4, QTableWidgetItem(payment["ref"]))
                    self.payment_table.setItem(row, 5, QTableWidgetItem(f"{payment['total_vat']:,.2f} XAF"))  # ✅ Total VAT
                    self.payment_table.setItem(row, 6, QTableWidgetItem(f"{payment['total_balance']:,.2f} XAF"))  # ✅ Total Balance
                
                # Resize columns and rows to fit content
                self.payment_table.resizeColumnsToContents()
                self.payment_table.resizeRowsToContents()
                # self.payment_table.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive)
                self.payment_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)                
                self.payment_table.setColumnWidth(0, 150)  # Date column
                self.payment_table.setColumnWidth(1, 250)  # Patient Name column
                self.payment_table.setColumnWidth(2, 100)  # Amount column
                self.payment_table.setColumnWidth(3, 150)  # Payment Method column
                self.payment_table.setColumnWidth(4, 150)  # Reference column
            else:
                QMessageBox.warning(self, "Error", "Failed to fetch payment history.")
        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))




    @Slot()
    def generate_pdf(self):
        """Generate a PDF file with payment history, ensuring the table fits on A4."""
        current_date = datetime.now().strftime("%B-%d-%Y")  # Example: March-12-2025
        filename, _ = QFileDialog.getSaveFileName(self, f"Save PDF ({current_date}-PH)", f"{current_date}-PH.pdf", "PDF Files (*.pdf)")
        
        if not filename:
            return

        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4  # A4 dimensions: (595.27, 841.89) points
        margin = 1.5 * inch  
        # Header
        logo_path = "Picsart_25-03-14_16-37-11-568.png"
        c.drawImage(logo_path, margin, height - 2.2 * inch, width=.7 * inch, height=.7 * inch, mask="auto")
        c.drawImage(logo_path, width / 1.2, height - 2.2 * inch, width=.7 * inch, height=.7 * inch, mask="auto")

        c.setFillColor(colors.HexColor('#062440'))
        c.setFont("Helvetica-Bold", 45)
        c.drawString(width / 8.0, height - 0.88 * inch, "NGASSAM OPTIQUE")
        c.setFont("Helvetica-Bold", 12)
        c.drawString((width - 150) / 2, height - 90, "CABINET OPTIQUE")
        c.drawString((width - 480) / 2, height - 110, "Vente de matériel Ophtalmique médical-Verre ophtalmique - Montures de marque")
        c.drawString((width - 250) / 2, height - 130, "N.I.U: P039116571318-RC/YAO/2023/A/351")
        c.drawString((width - 500) / 2, height - 150, "Situé derrière ADAMAQUA PALACE - Tél.: (237) 699 67 50 25/620 37 69 28/651 63 06 45")

        c.setFont("Helvetica-Bold", 16)
        c.drawString((width - 550) / 2, height - 200, "Payment History Report")  # Centered Title
        c.setFont("Helvetica", 12)
        c.drawString((width - 550) / 2, height - 225, f"Year: {self.year_combo.currentText()} | Month: {self.month_combo.currentText()}")  

        # Table Data
        table_data = [["Date", "Patient", "Amount", "Payment Method", "Ref.", "VAT", "Balance"]]  # Shortened headers
        for row in range(self.payment_table.rowCount()):
            table_data.append([self.payment_table.item(row, col).text() for col in range(self.payment_table.columnCount())])

        # Dynamically Adjusted Column Widths
        available_width = width - (2 * inch)  # Leave 1 inch margin on both sides
        col_widths = [available_width * 0.19,  # Date
                    available_width * 0.25,  # Patient
                    available_width * 0.16,  # Amount
                    available_width * 0.18,  # Payment Method
                    available_width * 0.15,  # Reference
                    available_width * 0.16,  # VAT
                    available_width * 0.19]  # Balance

        table = Table(table_data, colWidths=col_widths)

        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ]))

        # Calculate X position for centering
        table_x = (width - sum(col_widths)) / 2.0
        table_y = height - 350  # Position below header

        table.wrapOn(c, width, height)
        table.drawOn(c, table_x, table_y)

        # Save PDF
        c.save()
        QMessageBox.information(self, "PDF Saved", f"Payment history saved to {filename}")
        
        
    @Slot()
    def export_to_csv(self):
        """Export the payment history to a CSV file, including date in filename."""
        current_date = datetime.now().strftime("%B-%d-%Y")  # Example: March-12-2025
        filename, _ = QFileDialog.getSaveFileName(self, f"Save CSV ({current_date}-PH)", f"{current_date}-PH.csv", "CSV Files (*.csv)")

        if not filename:
            return

        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Patient Name", "Total Amount", "Payment Method", "Reference", "Total VAT", "Total Balance"])
            for row in range(self.payment_table.rowCount()):
                writer.writerow([self.payment_table.item(row, col).text() for col in range(self.payment_table.columnCount())])

        QMessageBox.information(self, "Export Successful", f"Payment history exported to {filename}")



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaymentHistoryDialog()
    window.show()
    sys.exit(app.exec())