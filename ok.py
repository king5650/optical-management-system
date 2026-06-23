from PySide6.QtPrintSupport import QPrinter
from PySide6.QtGui import QPainter, QFont
from PySide6.QtCore import QRectF, QPointF, Qt

def render_pdf():
    printer = QPrinter(QPrinter.HighResolution)
    printer.setOutputFormat(QPrinter.PdfFormat)
    printer.setOutputFileName("prescription_output.pdf")
    printer.setPageSize(QPrinter.A4)

    painter = QPainter()
    if not painter.begin(printer):
        print("Failed to open file for writing")
        return

    # Setup fonts
    title_font = QFont("Arial", 10, QFont.Bold)
    normal_font = QFont("Arial", 9)

    x_start = 30
    y = 40
    checkbox_size = 10
    spacing_x = 70
    spacing_y = 25

    def draw_section(title):
        nonlocal y
        painter.setFont(title_font)
        painter.drawText(x_start, y, title)
        y += spacing_y
        painter.setFont(normal_font)

    def draw_checkboxes(items, items_per_row=3):
        nonlocal y
        x = x_start
        count = 0
        for label in items:
            painter.drawText(x, y, label)
            painter.drawRect(x + 60, y - 10, checkbox_size, checkbox_size)
            x += spacing_x
            count += 1
            if count % items_per_row == 0:
                y += spacing_y
                x = x_start
        if count % items_per_row != 0:
            y += spacing_y

    # Draw layout
    draw_section("Amétropie :")
    draw_checkboxes(["Myopie", "Hypermétropie", "Astigmatisme", "Presbytie", "Emmétropie"], 3)

    draw_section("Types de verre :")
    draw_checkboxes(["minéraux", "organiques", "polycarbonates"], 3)

    draw_section("Teintes :")
    draw_checkboxes(["blanc", "gris", "photochromique", "antireflet", "bleue protect"], 3)

    draw_section("Foyers :")
    draw_checkboxes(["unifocaux", "bifocaux", "progressifs"], 3)

    draw_section("Port :")
    draw_checkboxes(["constant", "lecture"], 2)

    draw_section("Indice :")
    draw_checkboxes(["normal", "fort indice"], 2)

    painter.end()
    print("PDF generated successfully.")
