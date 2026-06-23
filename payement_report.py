from PySide6.QtWidgets import (
    QApplication, QDialog, QVBoxLayout, QHBoxLayout, QPushButton, QComboBox, QTableWidget, QTableWidgetItem, QMessageBox, QFileDialog
)
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
import os
import sys

class PaymentHistoryDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Test Payment PDF")
        layout = QVBoxLayout(self)

        # Year and Month ComboBoxes
        self.year_combo = QComboBox()
        self.year_combo.addItems(["2023", "2024", "2025"])
        self.month_combo = QComboBox()
        self.month_combo.addItems(["All", "January", "February", "March"])

        # Table
        self.payment_table = QTableWidget(60, 7)
        self.payment_table.setHorizontalHeaderLabels(
            ["Date", "Patient", "Amount", "Payment Method", "Ref.", "VAT", "Balance"]
        )
        # Fill with dummy data
        for row in range(60):
            for col in range(7):
                self.payment_table.setItem(row, col, QTableWidgetItem(f"Data {row+1}-{col+1}"))

        # Button
        btn = QPushButton("Generate PDF")
        btn.clicked.connect(self.generate_pdf)

        # Layout
        top = QHBoxLayout()
        top.addWidget(self.year_combo)
        top.addWidget(self.month_combo)
        layout.addLayout(top)
        layout.addWidget(self.payment_table)
        layout.addWidget(btn)

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
        available_width = width - 0.5 * inch
        
        col_widths = [
            available_width * 0.15,  # Date
            available_width * 0.22,  # Patient
            available_width * 0.12,  # Amount
            available_width * 0.18,  # Payment Method
            available_width * 0.12,  # Ref.
            available_width * 0.10,  # VAT
            available_width * 0.11,  # Balance
        ]
        table_style = TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#062440")),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
            ("FONTSIZE", (0, 0), (-1, -1), 11),
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlg = PaymentHistoryDialog()
    dlg.show()
    sys.exit(app.exec())