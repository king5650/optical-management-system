import sys
import os

# Go two levels up to reach the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget,
    QFileDialog, QTableWidget, QTableWidgetItem, QMessageBox, QHBoxLayout,
    QLabel, QComboBox, QHeaderView
)

from PySide6.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PySide6.QtGui import QPainter
from PySide6.QtGui import QPainter, QFont, QColor, QPen
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage
from PySide6.QtGui import QIcon, QFont, QAction, QColor
from PySide6.QtCore import QSize


# BASE_URL = "http://127.0.0.1:8000/"  # Django backend
# BASE_URL = "http://127.0.0.1:8000/"  
from config_loader import BASE_URL
response = requests.get(f'{BASE_URL}')


class InventoryReportViewer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Inventory Report")
        self.setGeometry(100, 100, 1100, 600)
        self.setStyleSheet("""

            QLabel{
                background-color: none;
            }

            
        """)
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

        self.generate_button = QPushButton(QIcon("images/stumbleupon_48px.png"), "Generate Report")
        self.generate_button.setIconSize(QSize(30, 30))
        self.generate_button.setStyleSheet("""
                QPushButton{
                background-color: rgb(255, 255, 255);
                border-radius: 5px;
                padding: 10px;
                color: rgb(0, 0, 0);
                width: 90px;
                font-weight: 900;
                spacing: 10px;
                width: auto;
            }  
                        QPushButton:hover {
                background-color: #e74c3c;
            }
                                          """)          
        self.generate_button.clicked.connect(self.fetch_inventory_data)
        filter_layout.addWidget(self.generate_button)

        layout.addLayout(filter_layout)

        # 🔹 Table Section
        self.inventory_table = QTableWidget()
        self.inventory_table.setColumnCount(5)
        self.inventory_table.setHorizontalHeaderLabels(["Type", "Category", "Stock", "Unit Price", "Expiry Date"])
        # self.inventory_table.styleSheet("")
        self.inventory_table.setStyleSheet("""color: black; font-weight: bold; background-color: white; font-size: 15px;""")
        self.inventory_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.inventory_table)

        # 🔹 Export Buttons
        button_layout = QHBoxLayout()
        # self.preview_button = QPushButton((QIcon("images/report_file_64px.png"),"Preview Report"))
        self.preview_button = QPushButton(QIcon("images/fine_print_48px.png"), "Preview Report")
        self.preview_button.setIconSize(QSize(30, 30))
        self.preview_button.setStyleSheet("""
                QPushButton{
                background-color: rgb(255, 255, 255);
                border-radius: 5px;
                padding: 10px;
                color: rgb(0, 0, 0);
                width: 90px;
                font-weight: 900;
                spacing: 10px;
                width: auto;
            }  
                        QPushButton:hover {
                background-color: #e74c3c;
            }
            QIcon{
                width: 100px;
                height: 100px;
            }            
                                          """)
        self.export_pdf_button = QPushButton(QIcon("images/pdf_48px.png"), "Export PDF Report")
        self.export_pdf_button.setIconSize(QSize(30, 30))  # Change 48 to desired size
        
        self.export_pdf_button.setStyleSheet("""
                QPushButton{
                background-color: rgb(255, 255, 255);
                border-radius: 5px;
                padding: 10px;
                color: rgb(0, 0, 0);
                width: 90px;
                font-weight: 900;
                spacing: 10px;
                width: auto;
            }  
                        QPushButton:hover {
                background-color: #e74c3c;
            }
            QIcon{
                width: 50px;
                height: 50px;
            }            
                                          """)        
        self.export_csv_button = QPushButton(QIcon("images/csv_48px.png"), "Export CSV Report")
        self.export_csv_button.setIconSize(QSize(30, 30))
        self.export_csv_button.setStyleSheet("""
                QPushButton{
                background-color: rgb(255, 255, 255);
                border-radius: 5px;
                padding: 10px;
                color: rgb(0, 0, 0);
                width: 90px;
                font-weight: 900;
                spacing: 10px;
                width: auto;
            }  
                        QPushButton:hover {
                background-color: #e74c3c;
            }
            QIcon{
                width: 50px;
                height: 50px;
            }
                                          """)   
        self.export_pdf_button.clicked.connect(self.print_report)
        self.export_csv_button.clicked.connect(self.export_csv_report)
        self.preview_button.clicked.connect(self.preview_report)

        button_layout.addWidget(self.preview_button)
        button_layout.addWidget(self.export_pdf_button)
        button_layout.addWidget(self.export_csv_button)
        
        layout.addLayout(button_layout)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
        container.setStyleSheet("""
            
                /*background-color: rgb(88, 162, 157);*/
                background-color: rgba(44, 47, 134, 200);
                color: white;
                font-size: 15px;
                font-weight: 600;

        
            QPushButton{
                background-color: rgb(255, 255, 255);
                border-radius: 5px;
                padding: 10px;
                color: rgb(0, 0, 0);
                width: 90px;
                font-weight: 900;
                spacing: 10px;
                width: auto;
            }        
            QPushButton:hover {
                background-color: #e74c3c;
            }
            QTableWidget{
                background-color: rgb(88, 162, 157);
            }                
                                
                                """)

    def fetch_categories(self):
            """Fetch categories from the backend."""
            try:
                response = requests.get(f"{BASE_URL}/categories/")
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
            response = requests.get(f"{BASE_URL}/inventory-report/", 
                                    params={"category_id": category_id, "stock": stock_filter, "expiry": expiry_filter})
            data = response.json()

            if response.status_code == 200 and data.get("inventory"):
                inventory = data["inventory"]
                self.inventory_table.setRowCount(0)
                self.inventory_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

                for row, item in enumerate(inventory):
                    self.inventory_table.insertRow(row)
                    self.inventory_table.setItem(row, 0, QTableWidgetItem(item["type__name"]))
                    self.inventory_table.setItem(row, 1, QTableWidgetItem(item["category__name"]))
                    self.inventory_table.setItem(row, 2, QTableWidgetItem(str(item["stock_level"])))

                    # ✅ Convert unit_price to float before formatting
                    unit_price = float(item["unit_price"])
                    self.inventory_table.setItem(row, 3, QTableWidgetItem(f"{unit_price:,.2f} XAF"))

                    from datetime import datetime


                    # raw_expiry = item.get("expiry_date")

                    # if raw_expiry is None:
                    #     expiry_display = "N/A"
                    # # else:
                    #     expiry_dt = datetime.strptime(raw_expiry, "%Y-%m-%d")

                    # ... inside your for loop
                    #raw_expiry = item.get("expiry_date")

                    #if raw_expiry is None:
                       # expiry_display = "N/A"
                    #else:
                        #expiry_dt = datetime.strptime(raw_expiry, "%Y-%m-%d")
                        
                        # today = datetime.today()
                        # if expiry_dt < today:
                        #     expiry_display = "Expired"
                        # else:
                        #     expiry_display = expiry_dt.strftime("%Y-%m-%d")
                    raw_expiry = item.get("expiry_date")

                    try:
                        if not raw_expiry:
                            expiry_display = "N/A"
                        else:
                            expiry_dt = datetime.strptime(raw_expiry, "%Y-%m-%d")
                            today = datetime.today()
                            expiry_display = "Expired" if expiry_dt < today else expiry_dt.strftime("%Y-%m-%d")
                    except Exception:
                        expiry_display = "Invalid Date"


                    self.inventory_table.setItem(row, 4, QTableWidgetItem(expiry_display))


            else:
                QMessageBox.information(self, "No Data", "No inventory data found.")

        except requests.RequestException as e:
            QMessageBox.critical(self, "Network Error", str(e))
    def preview_report(self):
        """Preview the inventory report before printing."""
        printer = QPrinter()
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.render_pdf)
        preview_dialog.exec()

    def render_pdf(self, printer):
        """Manually draw the table using QPainter with improved styling."""
        painter = QPainter(printer)
        # painter.setFont(QFont("Arial", 12, QFont.Weight.Bold))  # Set font style and size
        # painter.drawText(100, 100, "Inventory Report")
        # painter.setFont(QFont("Arial", 10))  # Reset to default font for the content
        # painter.drawText(100, 130, "Generated from Inventory System")
        

            # Set up logo paths and dimensions
        logo_path = "Picsart_25-03-14_16-37-11-568.png"
        logo_width = 0.7 * 72  # Convert inches to points (1 inch = 72 points)
        logo_height = 0.7 * 72
        margin = 72  # 1 inch margin
        page_width = printer.pageRect(QPrinter.Unit.Point).width()
        page_height = printer.pageRect(QPrinter.Unit.Point).height()


        # Add background color
        # painter.setBrush(QColor("#EAEAEA"))  # Light gray background
        # painter.setPen(Qt.PenStyle.NoPen)  # No border for the background
        # painter.drawRect(int(0), int(0), int(page_width), int(page_height))  # Fill the entire page background
        # # Reset pen for drawing other elements
        # painter.setPen(QPen(QColor("#062440")))

        # Add watermark
        painter.setOpacity(0.2)  # Make the watermark semi-transparent
        painter.setFont(QFont("Arial", 60))
        painter.setPen(QPen(QColor("#D3D3D3")))  # Light gray color
        painter.drawText(int(page_width / 4), int(page_height / 2), "CONFIDENTIAL")  # Watermark text

        # Reset opacity for other content
        painter.setOpacity(1.0)
            # Draw logos
        # painter.drawImage(margin, page_height - 2.2 * 72, QImage(logo_path).scaled(logo_width, logo_height))
        # painter.drawImage(int(margin), int(page_height - 2.2 * 72), QImage(logo_path).scaled(int(logo_width), int(logo_height)))
        
        painter.drawImage(int(margin), int(page_height - 10.17 * 72), QImage(logo_path).scaled(int(logo_width), int(logo_height)))
        # painter.drawImage(page_width / 1.2, page_height - 2.2 * 72, QImage(logo_path).scaled(logo_width, logo_height))

        # Set colors and fonts
        painter.setPen(QColor("#062440"))  # Set text color
        painter.setFont(QFont("Helvetica-Bold", 45))
        
        # painter.drawText(page_width / 8.0, page_height - 0.88 * 72, "NGASSAM OPTIQUE")
        painter.drawText(int(page_width / 6.0), int(page_height - 10.8 * 72), "NGASSAM OPTIQUE")
        

        painter.setFont(QFont("Helvetica-Bold", 12))
        painter.drawText(int((page_width - 8) / 2), int(page_height - 753), "CABINET OPTIQUE")
        painter.drawText(int((page_width - 480) / 2), int(page_height - 730), "Vente de matériel Ophtalmique médical-Verre ophtalmique - Montures de marque")
        painter.drawText(int((page_width - 250) / 2), int(page_height - 710), "N.I.U: P039116571318-RC/YAO/2023/A/351")
        painter.drawText(int((page_width - 500) / 2), int(page_height - 690), "Situé derrière ADAMAQUA PALACE - Tél.: (237) 699 67 50 25/620 37 69 28/651 63 06 45")

        # Add centered titles
        painter.setFont(QFont("Helvetica-Bold", 16))
        painter.drawText(int((page_width - 40) / 2), int(page_height - 660), "Inventory History Report")

        # painter.setFont(QFont("Helvetica", 12))
        # painter.drawText((page_width - 550) / 2, page_height - 225, f"Year: {self.year_combo.currentText()} | Month: {self.month_combo.currentText()}")
        
        # # Set up pagination variables
        rows_per_page = 30  # Maximum rows per page
        total_rows = self.inventory_table.rowCount()
        total_pages = (total_rows + rows_per_page - 1) // rows_per_page  # Calculate number of pages
        x_start = 20
        y_start = 150  # Start below header
        row_height = 30
        col_widths = [180, 185, 90, 180, 120]  # Column widths
        
        
        # Draw footer on every page
        painter.setFont(QFont("Helvetica-Bold", 10))
        painter.setPen(QPen(QColor("black")))
        footer_text = "copy-write software - Generated by Stark-tech - Confidential Report"
        painter.drawText(int(page_width / 2 - 100), int(page_height  + 250), footer_text)

        # Extract data from table
        data = [("Type", "Category", "Stock", "Unit Price", "Expiry Date")]
        for row in range(self.inventory_table.rowCount()):
            item_type = self.inventory_table.item(row, 0).text()
            category = self.inventory_table.item(row, 1).text()
            stock = self.inventory_table.item(row, 2).text()
            unit_price = self.inventory_table.item(row, 3).text()
            expiry_date = self.inventory_table.item(row, 4).text()
            data.append((item_type, category, stock, unit_price, expiry_date))

        x_start = 20
        y_start = 200
        row_height = 30
        col_widths = [180, 185, 90, 180, 120]

        # Draw table content with styling
        for row_idx, row in enumerate(data):
            for col_idx, cell in enumerate(row):
                cell_x = x_start + sum(col_widths[:col_idx]) + 10
                cell_y = y_start + (row_idx * row_height) + 20

                # Add background color for header row
                if row_idx == 0:
                    painter.fillRect(
                        x_start + sum(col_widths[:col_idx]),
                        y_start + (row_idx * row_height),
                        col_widths[col_idx],
                        row_height,
                        QColor(200, 200, 255)  # Light blue color
                    )

                # Set text color
                if row_idx == 0:
                    painter.setPen(QPen(QColor("white")))  # White text for header

                else:
                    painter.setPen(QPen(QColor("black")))  # White text for header


                painter.drawText(cell_x, cell_y, cell)

        # Draw table grid with enhanced borders
        painter.setPen(QPen(QColor("black"), 1))  # Thinner line for grid
        for row_idx in range(len(data) + 1):
            y_pos = y_start + (row_idx * row_height)
            painter.drawLine(x_start, y_pos, x_start + sum(col_widths), y_pos)

        for col_idx in range(len(col_widths) + 1):
            x_pos = x_start + sum(col_widths[:col_idx])
            painter.drawLine(x_pos, y_start, x_pos, y_start + (len(data) * row_height))

        # Add thicker border for the entire table
        painter.setPen(QPen(QColor("black"), 2))  # Thicker line for table border
        painter.drawRect(x_start, y_start, sum(col_widths), len(data) * row_height)

        painter.end()


    def print_report(self):
        """Save and print the report."""
        printer = QPrinter()
        file_dialog = QFileDialog(self, "Save Report", "", "PDF Files (*.pdf)")
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

        if file_dialog.exec():
            save_path = file_dialog.selectedFiles()[0]

            # Set output file format
            printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
            printer.setOutputFileName(save_path)

            # Render the PDF directly
            self.render_pdf(printer)

    def export_csv_report(self):
        """Export inventory data as CSV."""
        file_dialog = QFileDialog(self, "Save CSV Report", "", "CSV Files (*.csv)")
        file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)

        if file_dialog.exec():
            save_path = file_dialog.selectedFiles()[0]

            with open(save_path, "w") as file:
                file.write("Type,Category,Stock,Unit Price,Expiry Date\n")
                for row in range(self.inventory_table.rowCount()):
                    file.write(",".join([
                        self.inventory_table.item(row, col).text()
                        for col in range(self.inventory_table.columnCount())
                    ]) + "\n")

            QMessageBox.information(self, "Success", "CSV Report saved successfully.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InventoryReportViewer()
    window.show()
    sys.exit(app.exec())
