# payment_history.py
import sys
import csv
import requests
from datetime import datetime
from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QLabel,
    QComboBox, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem,
    QMessageBox, QFileDialog, QGraphicsOpacityEffect, QHeaderView
)
from PySide6.QtCore import Qt, QPropertyAnimation, QTimer, Slot
from PySide6.QtPrintSupport import QPrinter, QPrintDialog
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle
from PySide6.QtCore import QEasingCurve


BASE_URL = "http://127.0.0.1:8000/"  # Change this to your actual Django backend


class PaymentHistoryDialog1(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Payment History")
        self.setMinimumSize(1070, 500)
        self.setStyleSheet("QDialog { background-color: rgb(88, 162, 157); }")
        
        layout = QVBoxLayout()

        # Filters
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

        layout.addLayout(filter_layout)

        # Table
        self.payment_table = QTableWidget()
        self.payment_table.setColumnCount(7)
        self.payment_table.setHorizontalHeaderLabels([
            "Date", "Patient Name", "Amount Paid", "Payment Method",
            "Reference", "Total VAT", "Total Balance"
        ])
        layout.addWidget(self.payment_table)

        # Export Buttons
        export_layout = QHBoxLayout()
        self.print_pdf_button = QPushButton("Print PDF Copy")
        self.export_csv_button = QPushButton("Export CSV Copy")
        export_layout.addWidget(self.print_pdf_button)
        export_layout.addWidget(self.export_csv_button)

        self.print_pdf_button.clicked.connect(self.generate_pdf)
        self.export_csv_button.clicked.connect(self.export_to_csv)

        layout.addLayout(export_layout)
        self.setLayout(layout)

        # Dialog fade-in animation
        self.effect = QGraphicsOpacityEffect(self)
        self.setGraphicsEffect(self.effect)
        self.anim = QPropertyAnimation(self.effect, b"opacity")
        self.anim.setDuration(800)
        self.anim.setStartValue(0)
        self.anim.setEndValue(1)
        self.anim.start()

        # Widget fade-in
        self.fade_widget(self.year_combo)
        self.fade_widget(self.month_combo, delay=100)
        self.fade_widget(self.search_input, delay=200)
        self.fade_widget(self.search_button, delay=300)

        self.year_combo.currentIndexChanged.connect(self.fetch_payment_history)
        self.month_combo.currentIndexChanged.connect(self.fetch_payment_history)

        self.fetch_payment_history()


    def fade_widget(self, widget, delay=0):
        effect = QGraphicsOpacityEffect(widget)
        widget.setGraphicsEffect(effect)
        anim = QPropertyAnimation(effect, b"opacity")
        anim.setDuration(700)
        anim.setStartValue(0)
        anim.setEndValue(1)
        anim.setEasingCurve(QEasingCurve.InOutCubic)
        QTimer.singleShot(delay, anim.start)
            
    def populate_years(self):
        current_year = datetime.now().year
        self.year_combo.addItem("All")
        self.year_combo.addItems([str(y) for y in range(2024, current_year + 1)])

    @Slot()
    def fetch_payment_history(self):
        year = self.year_combo.currentText()
        month = self.month_combo.currentIndex()
        search = self.search_input.text().strip()

        year = "" if year == "All" else year
        month = "" if month == 0 else str(month)

        try:
            response = requests.get(f"{BASE_URL}auth/payment-history/",
                                    params={"year": year, "month": month, "search": search})
            data = response.json()

            self.payment_table.setRowCount(0)
            for row, payment in enumerate(data.get("payments", [])):
                self.payment_table.insertRow(row)
                self.payment_table.setItem(row, 0, QTableWidgetItem(payment["date"]))
                self.payment_table.setItem(row, 1, QTableWidgetItem(payment["patient"]))
                self.payment_table.setItem(row, 2, QTableWidgetItem(f"{payment['amount']:,.2f} XAF"))
                self.payment_table.setItem(row, 3, QTableWidgetItem(payment["method"]))
                self.payment_table.setItem(row, 4, QTableWidgetItem(payment["ref"]))
                self.payment_table.setItem(row, 5, QTableWidgetItem(f"{payment['total_vat']:,.2f} XAF"))
                self.payment_table.setItem(row, 6, QTableWidgetItem(f"{payment['total_balance']:,.2f} XAF"))

            QTimer.singleShot(100, self.animate_table_rows)

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def animate_table_rows(self):
        for row in range(self.payment_table.rowCount()):
            for col in range(self.payment_table.columnCount()):
                item = self.payment_table.item(row, col)
                if item:
                    effect = QGraphicsOpacityEffect()
                    item.setData(Qt.UserRole, effect)
                    self.payment_table.viewport().update()

                    animation = QPropertyAnimation(effect, b"opacity", self)
                    animation.setDuration(300)
                    animation.setStartValue(0)
                    animation.setEndValue(1)
                    animation.setEasingCurve(Qt.EaseInOutCubic)
                    animation.start(QPropertyAnimation.DeleteWhenStopped)

    @Slot()
    def generate_pdf(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save PDF", "payment_history.pdf", "PDF Files (*.pdf)")
        if not filename:
            return

        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4
        margin = 1.5 * inch

        c.setFont("Helvetica-Bold", 16)
        c.drawString(margin, height - inch, "Payment History Report")

        table_data = [["Date", "Patient", "Amount", "Method", "Ref.", "VAT", "Balance"]]
        for row in range(self.payment_table.rowCount()):
            table_data.append([self.payment_table.item(row, col).text() for col in range(self.payment_table.columnCount())])

        col_widths = [70, 100, 80, 80, 60, 60, 80]
        table = Table(table_data, colWidths=col_widths)
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))
        table.wrapOn(c, width, height)
        table.drawOn(c, margin, height - 200)
        c.save()
        QMessageBox.information(self, "Saved", "PDF has been saved.")

    @Slot()
    def export_to_csv(self):
        filename, _ = QFileDialog.getSaveFileName(self, "Save CSV", "payment_history.csv", "CSV Files (*.csv)")
        if not filename:
            return

        with open(filename, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Patient", "Amount", "Method", "Reference", "VAT", "Balance"])
            for row in range(self.payment_table.rowCount()):
                writer.writerow([self.payment_table.item(row, col).text() for col in range(self.payment_table.columnCount())])
        QMessageBox.information(self, "Exported", "CSV has been saved.")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PaymentHistoryDialog1()
    window.show()
    sys.exit(app.exec())
