import sys
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QComboBox, QLineEdit, QPushButton, 
    QTableWidget, QTableWidgetItem, QLabel, QMessageBox, QFileDialog, QFrame
)
import os
import requests
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QComboBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox,QHeaderView
)
from PySide6.QtGui import QIcon
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
from reportlab.platypus import Table, TableStyle, SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import sys 
BASE_URL = "http://127.0.0.1:8000/" 

class PaymentHistoryDialog(QDialog):
    """Dialog for displaying payment history with a black frame and improved design."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Payment History")
        self.setMinimumSize(1070, 500)
        icon_path = "logo1.png"
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"Warning: Icon file not found at {icon_path}")    
        self.setStyleSheet("""
            QDialog {
                background-color: rgba(44, 47, 134, 230);  /* Less transparent */
                color: white;
                font-family: "Segoe UI", sans-serif;
                font-size: 14px;
            }

            QLabel {
                color: white;
                font-weight: bold;
            }

            QComboBox, QLineEdit {
                background-color: white;
                color: black;
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 5px;
                width: 120px;
            }

            QLineEdit:focus {
                border: 1px solid #0078d7;
            }

            QPushButton {
                background-color: #ffffff;
                border-radius: 5px;
                padding: 8px 16px;
                color: #000;
                font-weight: bold;
            }

            QPushButton:hover {
                background-color: #005bb5;
                color: white;
            }

            QPushButton:pressed {
                background-color: #003f7f;
            }

            QTableWidget {
                background-color: transparent;
                border: 1px solid #ccc;
                border-radius: 4px;
                gridline-color: #ccc;
                selection-background-color: rgb(0, 0, 99);
                selection-color: #ffffff;
                color: white;
               ; 
            }

            QHeaderView::section {
                background-color: rgba(44, 47, 134, 230);
                color: white;
                padding: 8px;
                border: 1px solid white;
                font-weight: 900;
            }

            QTableWidget::item:selected {
                background-color: #0078d7;
                color: white;
                font-weight: 900;
            }

            QScrollBar:vertical, QScrollBar:horizontal {
                background: #f0f0f0;
            }

            QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
                background: #999;
                border-radius: 6px;
            }

            /* Black Frame Styling */
            QFrame#MainFrame {
                background-color: rgba(0, 0, 0, 180);
                border: 2px solid #000;
                border-radius: 10px;
                padding: 15px;
            }
        """)

        # 🟦 Outer Layout
        outer_layout = QVBoxLayout(self)

        # 🟧 Main Black Frame
        self.main_frame = QFrame()
        self.main_frame.setObjectName("MainFrame")
        frame_layout = QVBoxLayout(self.main_frame)

        # 🔹 Filter Row
        filter_layout = QHBoxLayout()

        self.year_combo = QComboBox()
        self.populate_years()

        self.month_combo = QComboBox()
        self.month_combo.addItems(["All", "January", "February", "March", "April", "May", "June",
                                   "July", "August", "September", "October", "November", "December"])

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Search by name or details...")

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.fetch_payment_history)

        filter_layout.addWidget(QLabel("Year:"))
        filter_layout.addWidget(self.year_combo)
        filter_layout.addWidget(QLabel("Month:"))
        filter_layout.addWidget(self.month_combo)
        filter_layout.addWidget(self.search_input)
        filter_layout.addWidget(self.search_button)

        # 🔹 Table
        self.payment_table = QTableWidget()
        self.payment_table.setColumnCount(7)
        self.payment_table.setHorizontalHeaderLabels([
            "Date", "Patient Name", "Amount Paid", "Payment Method",
            "Reference", "Total VAT", "Total Balance"
        ])

        # 🔹 Export Buttons
        button_layout = QHBoxLayout()
        self.print_pdf_button = QPushButton("Print PDF Copy")
        self.export_csv_button = QPushButton("Export CSV Copy")

        self.print_pdf_button.clicked.connect(self.generate_pdf)
        self.export_csv_button.clicked.connect(self.export_to_csv)

        button_layout.addStretch()
        button_layout.addWidget(self.print_pdf_button)
        button_layout.addWidget(self.export_csv_button)

        # ⬇️ Add widgets to black frame layout
        frame_layout.addLayout(filter_layout)
        frame_layout.addWidget(self.payment_table)
        frame_layout.addLayout(button_layout)

        # ⬇️ Add black frame to dialog layout
        outer_layout.addWidget(self.main_frame)

        # Connect signals
        self.year_combo.currentIndexChanged.connect(self.fetch_payment_history)
        self.month_combo.currentIndexChanged.connect(self.fetch_payment_history)

        # Auto-load payment data
        self.fetch_payment_history()

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
    # def generate_pdf(self):
    #     """Generate a professional, non-overlapping A4 PDF of payment history."""
        
    #     current_date = datetime.now().strftime("%B-%d-%Y")
    #     filename, _ = QFileDialog.getSaveFileName(
    #         self,
    #         f"Save PDF ({current_date}-PH)",
    #         f"{current_date}-PH.pdf",
    #         "PDF Files (*.pdf)"
    #     )

    #     if not filename:
    #         return

    #     doc = SimpleDocTemplate(
    #         filename,
    #         pagesize=A4,
    #         leftMargin=inch,
    #         rightMargin=inch,
    #         topMargin=inch,
    #         bottomMargin=inch
    #     )

    #     width, height = A4
    #     styles = getSampleStyleSheet()
    #     story = []

    #     # --- Header Section ---
    #     logo_path = "images/Picsart_25-03-14_16-37-11-568.png"
    #     if os.path.exists(logo_path):
    #         logo = Image(logo_path, width=0.7 * inch, height=0.7 * inch)
    #         logo.hAlign = 'LEFT'
    #         story.append(logo)
    #     else:
    #         print("Logo not found")

    #     header_style = styles["Title"]
    #     header_style.fontName = "Helvetica-Bold"
    #     header_style.fontSize = 28
    #     header_style.textColor = colors.HexColor('#062440')
    #     story.append(Paragraph("NGASSAM OPTIQUE", header_style, height=0.7 * inch))

    #     sub_header_style = styles["Normal"]
    #     sub_header_style.fontSize = 12
    #     sub_header_style.alignment = 1  # Centered

    #     story.append(Paragraph("CABINET OPTIQUE", sub_header_style))
    #     story.append(Paragraph("Vente de matériel Ophtalmique médical - Verre ophtalmique - Montures de marque", sub_header_style))
    #     story.append(Paragraph("N.I.U: P039116571318 - RC/YAO/2023/A/351", sub_header_style))
    #     story.append(Paragraph("Situé derrière ADAMAQUA PALACE - Tél.: (237) 699 67 50 25 / 620 37 69 28 / 651 63 06 45", sub_header_style))
    #     story.append(Spacer(1, 0.3 * inch))

    #     # --- Report Title ---
    #     report_title = Paragraph(
    #         f"<b>Payment History Report</b><br/>Year: {self.year_combo.currentText()} | Month: {self.month_combo.currentText()}",
    #         styles["Heading2"]
    #     )
    #     story.append(report_title)
    #     story.append(Spacer(1, 0.3 * inch))

    #     # --- Table Data ---
    #     table_data = [["Date", "Patient", "Amount", "Payment Method", "Ref.", "VAT", "Balance"]]
    #     for row in range(self.payment_table.rowCount()):
    #         table_data.append([
    #             self.payment_table.item(row, col).text() if self.payment_table.item(row, col) else ""
    #             for col in range(self.payment_table.columnCount())
    #         ])

    #     # Adjust column widths proportionally
    #     available_width = width - 2 * inch
    #     col_widths = [
    #         available_width * 0.15,  # Date
    #         available_width * 0.22,  # Patient
    #         available_width * 0.12,  # Amount
    #         available_width * 0.18,  # Payment Method
    #         available_width * 0.12,  # Ref.
    #         available_width * 0.10,  # VAT
    #         available_width * 0.11,  # Balance
    #     ]

    #     table = Table(table_data, colWidths=col_widths, hAlign='CENTER')

    #     table.setStyle(TableStyle([
    #         ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#062440")),
    #         ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
    #         ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    #         ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    #         ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    #         ("FONTSIZE", (0, 0), (-1, -1), 9),
    #         ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
    #         ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    #         ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey])
    #     ]))

    #     story.append(table)

    #     # Build the PDF
    #     doc.build(story)

    #     QMessageBox.information(self, "PDF Saved", f"Payment history saved to {filename}")
        
    def generate_pdf(self):
        current_date = datetime.now().strftime("%B-%d-%Y")
        filename, _ = QFileDialog.getSaveFileName(
            self,
            f"Save PDF ({current_date}-PH)",
            f"{current_date}-PH.pdf",
            "PDF Files (*.pdf)"
        )
        if not filename:
            return

        width, height = A4
        styles = getSampleStyleSheet()
        story = []

        # Table Data
        table_header = ["Date", "Patient", "Amount", "Payment Method", "Ref.", "VAT", "Balance"]
        table_data = [table_header]
        for row in range(self.payment_table.rowCount()):
            table_data.append([
                self.payment_table.item(row, col).text() if self.payment_table.item(row, col) else ""
                for col in range(self.payment_table.columnCount())
            ])

        # Split table data into pages of 28 rows (including header)
        rows_per_page = 20
        total_rows = len(table_data)
        pages = [table_data[i:i+rows_per_page] for i in range(0, total_rows, rows_per_page)]
        # available_width = width - 0.5 * inch
        
        # col_widths = [
        #     available_width * 0.15,  # Date
        #     available_width * 0.22,  # Patient
        #     available_width * 0.12,  # Amount
        #     available_width * 0.18,  # Payment Method
        #     available_width * 0.12,  # Ref.
        #     available_width * 0.10,  # VAT
        #     available_width * 0.11,  # Balance
        # ]
        # Dynamically Adjusted Column Widths
        available_width = width - (2 * inch)  # Leave 1 inch margin on both sides
        col_widths = [available_width * 0.19,  # Date
                    available_width * 0.25,  # Patient
                    available_width * 0.16,  # Amount
                    available_width * 0.18,  # Payment Method
                    available_width * 0.15,  # Reference
                    available_width * 0.16,  # VAT
                    available_width * 0.19]  # Balance        
        table_style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#062440")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
            ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.whitesmoke, colors.lightgrey]),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 8),  # Increase value for more height
            ("TOPPADDING", (0, 0), (-1, -1), 8),            
        ])

        # Build story: first page with header, others with just table, last with signature
        for i, page_rows in enumerate(pages):
            if i == 0:
                # --- First page: logo, header, details ---
                logo_path = "images/Picsart_25-03-14_16-37-11-568.png"
                if os.path.exists(logo_path):
                    logo = Image(logo_path, width=0.5 * inch, height=0.7 * inch)
                else:
                    logo = Spacer(0.5 * inch, 0.7 * inch)  # Empty space if logo missing

                header_style = styles["Title"]
                header_style.fontName = "Helvetica-Bold"
                header_style.fontSize = 24
                header_style.textColor = colors.HexColor('#062440')
                header_para = Paragraph("NGASSAM OPTIQUE", header_style)

                # Table with logo and header side by side
                header_table = Table(
                    [[logo, header_para]],
                    colWidths=[0.5 * inch, (width - 2.5 * inch) - 0.8 * inch],  # logo width, rest for header
                    hAlign='LEFT'
                )
                header_table.setStyle(TableStyle([
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 0),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                    ("TOPPADDING", (0, 0), (-1, -1), 0),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ]))
                story.append(header_table)

                center_style = ParagraphStyle(name="centered", parent=styles["Normal"], alignment=1, fontSize=11)
                story.append(Paragraph("CABINET OPTIQUE", center_style))
                story.append(Paragraph("Vente de matériel Ophtalmique médical - Verre ophtalmique - Montures de marque", center_style))
                story.append(Paragraph("N.I.U: P039116571318 - RC/YAO/2023/A/351", center_style))
                story.append(Paragraph("Situé derrière ADAMAQUA PALACE - Tél.: (237) 699 67 50 25/620 37 69 28/651 63 06 45", center_style))
                story.append(Spacer(1, 0.01 * inch))

                report_title = Paragraph(
                    f"<b>Payment History Report</b><br/>Year: {self.year_combo.currentText()} | Month: {self.month_combo.currentText()}",
                    styles["Heading2"]
                )
                story.append(report_title, )
                story.append(Spacer(1, 0.1 * inch))
            else:
                # Add top spacer only on second and subsequent pages
                story.append(Spacer(1, 50))  # 10 points space
                        

            # Table for this page
            table = Table(page_rows, colWidths=col_widths, hAlign='CENTER')
            table.setStyle(table_style)
            story.append(table)

            # Add signature only on the last page
            if i == len(pages) - 1:
                story.append(Spacer(1, 0.5 * inch))
                signature = Paragraph('<para align="left"><b>Digital Signature:</b> ________________________</para>', styles["Normal"])
                story.append(signature)
            if i < len(pages) - 1:
                story.append(PageBreak())

        # Build PDF
        doc = SimpleDocTemplate(
            filename,
            pagesize=A4,
            leftMargin=inch,
            rightMargin=inch,
            topMargin=0.01*inch,
            bottomMargin=1.2 * inch
        )
        doc.build(story)
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