import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QPainter, QFont, QColor, QPen
from PyQt6.QtPrintSupport import QPrinter

def draw_prescription_form_with_qpainter(output_path="prescription_form_qpainter.pdf"):
    app = QApplication(sys.argv)  # Required for any Qt app

    printer = QPrinter(QPrinter.PrinterMode.HighResolution)
    printer.setOutputFormat(QPrinter.OutputFormat.PdfFormat)
    printer.setOutputFileName(output_path)

    painter = QPainter()
    if not painter.begin(printer):
        print("Failed to open printer for painting.")
        return

    # Header
    painter.setFont(QFont("Helvetica", 40, QFont.Weight.Bold))
    painter.setPen(QColor("red"))
    painter.drawText(1400, 390, "NGASSAM OPTIQUE")

    painter.setFont(QFont("Helvetica-Bold", 13, QFont.Weight.Bold))
    painter.setPen(QColor("black"))
    painter.drawText(1900, 700, "Situé à l'Avenue Kennedy derrière ADAMAOUA PALACE")
    painter.drawText(1990, 900, "Tél.: (237) 699 67 50 25 / 620 37 69 38 / 671 16 65 27")

    painter.setFont(QFont("Helvetica-Bold", 13, italic=True))
    painter.setPen(QColor("red"))
    painter.drawText(3000, 1100, "Le professionnel de la santé visuelle")

    # Separator Line
    # painter.setPen(QColor("black"))
    painter.setPen(QPen(QColor("black"), 8))
    painter.drawLine(700, 1150, 9000, 1150)

    painter.setFont(QFont("Helvetica-Bold", 13, QFont.Weight.Bold))
    painter.setPen(QColor("red"))
    painter.drawText(3000, 1400, "ORDONNANCE DE LUNETTES")

    painter.setPen(QColor("black"))
    painter.setFont(QFont("Helvetica", 10, QFont.Weight.Bold))
    painter.drawText(7500, 1920, "Date: ")

    # Patient Info
    painter.setPen(QColor("black"))
    painter.setFont(QFont("Helvetica", 11, QFont.Weight.Bold))
    painter.drawText(500, 2220, "Noms et Prénoms :")
    # painter.drawText(500, 2300, "Date :")
    painter.drawText(500, 2690, "Age :")
    painter.drawText(2000, 2690, "Sexe :")
    painter.drawText(5000, 2690, "Profession :")
    # painter.drawText(500, 2990, "Sexe :")
    # painter.drawText(500, 3290, "Profession :")

    # Table
    table_x = 500
    table_y = 3300
    col_width = 1700
    row_height = 600
    headers = ["œil", "Sphère", "Cyl", "Axe", "Addition"]
    rows = [["OD", "", "", "", ""], ["OG", "", "", "", ""]]

    painter.setFont(QFont("Helvetica", 10, QFont.Weight.Bold))
    for col_index, header in enumerate(headers):
        painter.drawText(table_x + col_index * col_width + 400, table_y + 400, header)

    painter.setFont(QFont("Helvetica", 10))
    for row_index, row in enumerate(rows):
        for col_index, cell in enumerate(row):
            painter.drawText(table_x + col_index * col_width + 400,
                             table_y + (row_index + 1) * row_height + 400, cell)

    # Draw table grid
    for r in range(len(rows) + 1 + 1):
        painter.drawLine(table_x, table_y + r * row_height,
                         table_x + len(headers) * col_width, table_y + r * row_height)
    for c in range(len(headers) + 1):
        painter.drawLine(table_x + c * col_width, table_y,
                         table_x + c * col_width, table_y + (len(rows) + 1) * row_height)


 # --- Checkboxes Section ---
    def draw_checkbox(x, y):
        painter.setBrush(QColor("red"))  # Shadow effect
        painter.drawRect(x + 5, y + 5, 30, 30)
        painter.setBrush(QColor("blue"))
        painter.drawRect(x, y, 250, 250)
        painter.setPen(QPen(QColor("black"), 15))
        painter.drawRect(x, y, 250, 250)

    painter.setFont(QFont("Helvetica", 11))

    base_y = 5900
    spacing_y = 200
    x_start = 500

    painter.drawText(x_start, base_y, "Amétropie:")
    painter.drawText(x_start + 1000, base_y, "Myopie")
    draw_checkbox(x_start + 1660, base_y - 160)
    painter.drawText(x_start + 2100, base_y, "Hypermétropie")
    draw_checkbox(x_start + 3320, base_y - 160)
    painter.drawText(x_start + 3900, base_y, "Astigmatisme")
    draw_checkbox(x_start + 5030, base_y - 160)
    painter.drawText(x_start + 5600, base_y, "Presbytie")
    draw_checkbox(x_start + 6400, base_y - 160)
    painter.drawText(x_start + 6999, base_y, "Emmetropie")
    draw_checkbox(x_start + 8020, base_y - 160)
    # painter.drawText(x_start + 6999, base_y + spacing_y, "Emmetropie")
    # draw_checkbox(x_start + 7600, base_y + spacing_y - 30)

    base_y += 3 * spacing_y
    painter.drawText(x_start, base_y, "Types de verre :")
    painter.drawText(x_start + 1500, base_y, "minéraux")
    draw_checkbox(x_start + 2300, base_y - 190)
    painter.drawText(x_start + 2700, base_y, "organiques")
    draw_checkbox(x_start + 3638, base_y - 190)
    painter.drawText(x_start + 4200, base_y, "polycarbonates")
    draw_checkbox(x_start + 5500, base_y - 190)

    base_y += spacing_y + 330
    painter.drawText(x_start, base_y, "Tientes :")
    painter.drawText(x_start + 800, base_y, "Blac")
    draw_checkbox(x_start + 1200, base_y - 191)
    painter.drawText(x_start + 1599, base_y, "Grise")
    draw_checkbox(x_start + 2080, base_y - 191)
    painter.drawText(x_start + 2500, base_y, "Photochromique")
    draw_checkbox(x_start + 3865, base_y - 191)
    painter.drawText(x_start + 4390, base_y, "Antireflet")
    draw_checkbox(x_start + 5160, base_y - 191)
    painter.drawText(x_start + 5900, base_y, "Blue Portect")
    draw_checkbox(x_start + 6990, base_y - 191)

    base_y += spacing_y + 330
    painter.drawText(x_start, base_y, "Foyer :")
    painter.drawText(x_start + 700, base_y, "Unifocaux")
    draw_checkbox(x_start + 1540, base_y - 190)
    painter.drawText(x_start + 1999, base_y, "Bifocaux")
    draw_checkbox(x_start + 2750, base_y - 190)
    painter.drawText(x_start + 3200, base_y, "Progressifs")
    draw_checkbox(x_start + 4150, base_y - 190)

    base_y += spacing_y + 330
    painter.drawText(x_start, base_y, "Port :")
    painter.drawText(x_start + 700, base_y, "Constant")
    draw_checkbox(x_start + 1500, base_y - 190)
    painter.drawText(x_start + 2000, base_y, "Lecture")
    draw_checkbox(x_start + 2750, base_y - 190)

    base_y += spacing_y + 330
    painter.drawText(x_start, base_y, "Indice :")
    painter.drawText(x_start + 700, base_y, "Normal")
    draw_checkbox(x_start + 1500, base_y - 190)
    painter.drawText(x_start + 2000, base_y, "For Indice")
    draw_checkbox(x_start + 2899, base_y - 190)


    #  Footer
        # Separator Line
    painter.setPen(QPen(QColor("black"), 30))
    painter.drawLine(700, 9000, 9000, 9000)
    painter.setPen(QPen(QColor("black"), 30))
    painter.drawLine(700, 9500, 9000, 9500)
    # painter.setFont("Helvetica-Bold", 12)
    # painter.setFont(QColor('red'))
    painter.setPen(QColor("red"))
    painter.setFont(QFont("Helvetica-Bold", 12, QFont.Weight.Bold))
    painter.drawText(1500, 9300, "N.B.: Rapporter toujours vos lunettes après l'achat pour le contrôle")

    painter.end()
    print(f"Prescription form saved to {output_path}")

    # Close the app
    sys.exit(app.exec())



# Run it
draw_prescription_form_with_qpainter("prescription_form_qpainter.pdf")




