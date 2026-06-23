# import sys
# import tempfile
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
# from PyQt6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# from PyQt6.QtGui import QPainter
# from reportlab.pdfgen import canvas


# # from PySide6.QtWidgets import (
# #     QDialog, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, 
# #     QLabel, QPushButton, QComboBox, QMessageBox,QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
# # )
# class PrintPreviewExample(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Print Preview Example")
#         self.setGeometry(100, 100, 500, 300)

#         # Create UI
#         layout = QVBoxLayout()
#         self.preview_button = QPushButton("Preview Report")
#         self.print_button = QPushButton("Print Report")

#         layout.addWidget(self.preview_button)
#         layout.addWidget(self.print_button)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#         # Connect buttons to actions
#         self.preview_button.clicked.connect(self.preview_report)
#         self.print_button.clicked.connect(self.print_report)

#         # Temporary file to store the PDF
#         self.temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name

#     def generate_pdf(self, filename):
#         """Generate a PDF using reportlab."""
#         c = canvas.Canvas(filename)
#         c.drawString(100, 750, "Inventory Report")
#         c.drawString(100, 730, "Generated using PyQt6 & ReportLab")
#         c.drawString(100, 700, "Item 1: 10 units")
#         c.drawString(100, 680, "Item 2: 5 units")
#         c.drawString(100, 660, "Item 3: 20 units")
#         c.save()

#     def preview_report(self):
#         """Preview the generated PDF in QPrintPreviewDialog."""
#         self.generate_pdf(self.temp_pdf)  # Generate the PDF first
#         printer = QPrinter()
        
#         preview_dialog = QPrintPreviewDialog(printer, self)
#         preview_dialog.paintRequested.connect(self.render_pdf)
#         preview_dialog.exec()

#     def render_pdf(self, printer):
#         """Render the generated PDF onto the QPrintPreviewDialog using QPainter."""
#         painter = QPainter(printer)
#         painter.drawText(100, 100, "Rendering PDF Preview...")  # Placeholder
#         painter.drawText(100, 730, "Generated using PyQt6 & ReportLab")
#         painter.drawText(100, 700, "Item 1: 10 units")
#         painter.drawText(100, 680, "Item 2: 5 units")
#         painter.drawText(100, 660, "Item 3: 20 units")
#         painter.end()

#     def print_report(self):
#         """Print the generated PDF directly."""
#         printer = QPrinter()
        
#         file_dialog = QFileDialog(self, "Print Report", "", "PDF Files (*.pdf)")
#         file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
#         if file_dialog.exec():
#             save_path = file_dialog.selectedFiles()[0]
#             self.generate_pdf(save_path)  # Save PDF before printing

#         printer.setOutputFormat(QPrinter.OutputFormat.NativeFormat)
#         painter = QPainter(printer)
#         painter.drawText(100, 100, "Printing PDF...")  # Placeholder
#         painter.end()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PrintPreviewExample()
#     window.show()
#     sys.exit(app.exec())

# import sys
# import tempfile
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
# from PyQt6.QtPrintSupport import QPrinter
# from PyQt6.QtGui import QPainter
# from reportlab.pdfgen import canvas
# import sys
# import tempfile
# from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
# from PyQt6.QtPrintSupport import QPrinter, QPrintPreviewDialog
# from PyQt6.QtGui import QPainter
# from reportlab.pdfgen import canvas
# from PyQt6.QtPdf import QPdfDocument
# from PyQt6.QtPdf import QPdfDocument, QPdfPageRenderer

# class PrintPreviewExample(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.setWindowTitle("Print Preview Example")
#         self.setGeometry(100, 100, 500, 300)

#         # Create UI
#         layout = QVBoxLayout()
#         self.preview_button = QPushButton("Preview Report")
#         self.print_button = QPushButton("Print Report")

#         layout.addWidget(self.preview_button)
#         layout.addWidget(self.print_button)

#         container = QWidget()
#         container.setLayout(layout)
#         self.setCentralWidget(container)

#         # Connect buttons to actions
#         self.preview_button.clicked.connect(self.preview_report)
#         self.print_button.clicked.connect(self.print_report)

#         # Temporary file to store the PDF
#         self.temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name

#     def generate_pdf(self, filename):
#         """Generate a PDF using reportlab."""
#         c = canvas.Canvas(filename)
#         c.drawString(100, 750, "Inventory Report")
#         c.drawString(100, 730, "Generated using PyQt6 & ReportLab")
#         c.drawString(100, 700, "Item 1: 10 units")
#         c.drawString(100, 680, "Item 2: 5 units")
#         c.drawString(100, 660, "Item 3: 20 units")
#         c.save()

#     def preview_report(self):
#         """Preview the generated PDF in QPrintPreviewDialog."""
#         self.generate_pdf(self.temp_pdf)  # Generate the PDF first
#         printer = QPrinter()
        
#         preview_dialog = QPrintPreviewDialog(printer, self)
#         preview_dialog.paintRequested.connect(self.render_pdf)
#         preview_dialog.exec()

#     def render_pdf(self, printer):
#         """Render the actual PDF file onto the QPrintPreviewDialog using QPdfDocument."""
#         pdf_doc = QPdfDocument(self)
#         pdf_doc.load(self.temp_pdf)

#         if pdf_doc.pageCount() > 0:
#             painter = QPainter(printer)
#             pdf_doc.paint(painter, printer.pageRect())  # Render PDF content
#             painter.end()

#     def print_report(self):
#         """Print the generated PDF directly."""
#         printer = QPrinter()
        
#         file_dialog = QFileDialog(self, "Print Report", "", "PDF Files (*.pdf)")
#         file_dialog.setAcceptMode(QFileDialog.AcceptMode.AcceptSave)
#         if file_dialog.exec():
#             save_path = file_dialog.selectedFiles()[0]
#             self.generate_pdf(save_path)  # Save PDF before printing

#         printer.setOutputFormat(QPrinter.OutputFormat.NativeFormat)
#         painter = QPainter(printer)
#         painter.drawText(100, 100, "Printing PDF...")  # Placeholder
#         painter.end()

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = PrintPreviewExample()
#     window.show()
#     sys.exit(app.exec())
import sys
import tempfile
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
)
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QPainter
from reportlab.pdfgen import canvas
import sys
import tempfile
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtGui import QPainter
from reportlab.pdfgen import canvas
import sys
import tempfile
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QFileDialog
from PyQt6.QtPrintSupport import QPrinter, QPrintPreviewDialog
from PyQt6.QtGui import QPainter
from reportlab.pdfgen import canvas
from PyQt6.QtPdf import QPdfDocument
from PyQt6.QtPdf import QPdfDocument, QPdfPageRenderer
from reportlab.lib.pagesizes import letter

class PrintPreviewExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Print Preview Example")
        self.setGeometry(100, 100, 500, 300)

        # Create UI
        layout = QVBoxLayout()
        self.preview_button = QPushButton("Preview Report")
        self.print_button = QPushButton("Print Report")

        layout.addWidget(self.preview_button)
        layout.addWidget(self.print_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Connect buttons to actions
        self.preview_button.clicked.connect(self.preview_report)
        self.print_button.clicked.connect(self.print_report)

        # Temporary file to store the PDF
        self.temp_pdf = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf").name

    def generate_pdf(self, filename):
        """Generate a PDF using ReportLab, including a table."""
        c = canvas.Canvas(filename, pagesize=letter)
        width, height = letter

        c.setFont("Helvetica-Bold", 14)
        c.drawString(100, height - 50, "Inventory Report")

        c.setFont("Helvetica", 12)
        c.drawString(100, height - 70, "Generated using PyQt6 & ReportLab")

        # Table Data
        data = [("Item", "Quantity", "Price"),
                ("Item 1", "10", "$50"),
                ("Item 2", "5", "$25"),
                ("Item 3", "20", "$100")]

        x_start = 100
        y_start = height - 120
        row_height = 20
        col_widths = [100, 100, 100]  # Width for columns

        # Draw Table
        for row_idx, row in enumerate(data):
            for col_idx, cell in enumerate(row):
                c.drawString(x_start + sum(col_widths[:col_idx]), y_start - (row_idx * row_height), cell)

        # Draw Table Grid
        for row_idx in range(len(data) + 1):  # Rows
            y_pos = y_start - (row_idx * row_height)
            c.line(x_start, y_pos, x_start + sum(col_widths), y_pos)

        for col_idx in range(len(col_widths) + 1):  # Columns
            x_pos = x_start + sum(col_widths[:col_idx])
            c.line(x_pos, y_start, x_pos, y_start - (len(data) * row_height))

        c.save()

    def preview_report(self):
        """Preview the document in QPrintPreviewDialog."""
        printer = QPrinter()
        preview_dialog = QPrintPreviewDialog(printer, self)
        preview_dialog.paintRequested.connect(self.render_pdf)
        preview_dialog.exec()

    def render_pdf(self, printer):
        """Render the document onto QPrintPreviewDialog using QPainter."""
        painter = QPainter(printer)

        painter.setFont(QPainter().font())
        painter.drawText(100, 100, "Inventory Report")
        painter.drawText(100, 130, "Generated using PyQt6 & ReportLab")

        # Table Data
        data = [("Item", "Quantity", "Price"),
                ("Item 1", "10", "$50"),
                ("Item 2", "5", "$25"),
                ("Item 3", "20", "$100")]

        x_start = 100
        y_start = 200
        row_height = 30
        col_widths = [100, 100, 100]

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

        # Draw content (same as preview)
        painter.setFont(QPainter().font())
        painter.drawText(100, 100, "Inventory Report")
        painter.drawText(100, 130, "Generated using PyQt6 & ReportLab")

        # Table Data
        data = [("Item", "Quantity", "Price"),
                ("Item 1", "10", "$50"),
                ("Item 2", "5", "$25"),
                ("Item 3", "20", "$100")]

        x_start = 100
        y_start = 200
        row_height = 30
        col_widths = [100, 100, 100]

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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PrintPreviewExample()
    window.show()
    sys.exit(app.exec())
