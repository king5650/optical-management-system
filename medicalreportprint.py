# from reportlab.lib.pagesizes import A4
# from reportlab.pdfgen import canvas
# from reportlab.lib import colors
# from reportlab.lib.units import inch
# from reportlab.lib import colors
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.pdfgen import canvas


# def draw_prescription_form(pdf_path):
#     c = canvas.Canvas(pdf_path, pagesize=A4)
#     width, height = A4
#     margin = 1.5 * inch
#     elements = []
#     styles = getSampleStyleSheet()

#     # Header
#     c.setFont("Helvetica-Bold", 50)
#     c.setFillColor(colors.red)
#     c.drawString(0.75 * inch, height - 1 * inch, "NGASSAM OPTIQUE")

#     c.setFont("Helvetica", 12)
#     c.setFillColor(colors.black)
#     c.drawString(2.0 * inch, height - 1.3 * inch, "Situé à l'Avenue Kennedy derrière ADAMAOUA PALACE")
#     c.drawString(2.1 * inch, height - 1.5 * inch, "Tél.: (237) 699 67 50 25 / 620 37 69 38 / 671 16 65 27")
    
#     c.setFont("Helvetica-Oblique", 14)
#     c.setFillColor(colors.red)
#     c.drawString(2.59 * inch, height - 1.8 * inch, "Le professionnel de la santé visuelle")
    
#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(2.53 * inch, height - 2.2 * inch, "ORDONNANCE DE LUNETTES")

#     # 📌 Draw Separator Line
#     c.setStrokeColor(colors.black)
#     c.setLineWidth(2)
#     c.line(margin, height - 1.91 * inch, width - margin, height - 1.91 * inch)


#     # Patient Information
#     c.setFont("Helvetica-Bold", 12)
#     c.setFillColor(colors.black)
#     c.drawString(0.8 * inch, height - 3.0 * inch, "Noms et Prénoms :")
#     c.drawString(6.2 * inch, height - 2.7 * inch, "Date :")

#     c.drawString(0.8 * inch, height - 3.4 * inch, "Age :")
#     c.drawString(2.3 * inch, height - 3.4 * inch, "Sexe :")
#     c.drawString(4.5 * inch, height - 3.4 * inch, "Profession :")

#     # Table Headers
#     c.setFont("Helvetica-Bold", 12)
#     c.drawString(1.0 * inch, height - 3.9 * inch, "œil")
#     c.drawString(2.2 * inch, height - 3.9 * inch, "Sphère")
#     c.drawString(3.4 * inch, height - 3.9 * inch, "Cyl")
#     c.drawString(4.5 * inch, height - 3.9 * inch, "Axe")
#     c.drawString(5.8 * inch, height - 3.9 * inch, "Addition")

#     # Table Rows
#     c.setFont("Helvetica", 12)
#     c.drawString(1.0 * inch, height - 4.3 * inch, "OD")
#     c.drawString(1.0 * inch, height - 4.6 * inch, "OG")
    
    

#     # Checkboxes
#     def draw_checkbox(x, y):
#         c.rect(x, y, 10, 10, stroke=1, fill=0)

#     c.setFont("Helvetica-Bold", 12)
#     c.drawString(0.8 * inch, height - 5.0 * inch, "Amétropie:")
#     c.drawString(1.78 * inch, height - 5.0 * inch, "Myopie")
#     draw_checkbox(2.4 * inch, height - 5.0 * inch)
#     c.drawString(2.78 * inch, height - 5.0 * inch, "Hypermétropie")
#     draw_checkbox(4.0 * inch, height - 5.0 * inch)
#     c.drawString(5.4 * inch, height - 5.0 * inch, "Astigmatisme")
#     draw_checkbox(6.5 * inch, height - 5.0 * inch)
    
#     # Additional Sections for types of lenses, coatings, and prescriptions
#     c.drawString(0.8 * inch, height - 5.5 * inch, "Types de verre :")
#     c.drawString(1.2 * inch, height - 5.8 * inch, "minéraux")
#     draw_checkbox(2.2 * inch, height - 5.85 * inch)
#     c.drawString(3.0 * inch, height - 5.8 * inch, "organiques")
#     draw_checkbox(4.3 * inch, height - 5.85 * inch)
#     c.drawString(5.4 * inch, height - 5.8 * inch, "polycarbonates")
#     draw_checkbox(6.5 * inch, height - 5.85 * inch)

#     # Footer
#     c.setFont("Helvetica-Bold", 12)
#     c.setFillColor(colors.red)
#     c.drawString(1.0 * inch, height - 10.5 * inch, "N.B.: Rapporter toujours vos lunettes après l'achat pour le contrôle")

#     # Save PDF
#     c.save()

# # Generate PDF
# draw_prescription_form("prescription_form.pdf")



from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from reportlab.lib.units import inch
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def draw_prescription_form(pdf_path):
    c = canvas.Canvas(pdf_path, pagesize=A4)
    width, height = A4
    margin = 1.5 * inch
    elements = []
    styles = getSampleStyleSheet()

    # Header
    c.setFont("Helvetica-Bold", 50)
    c.setFillColor(colors.red)
    c.drawString(0.75 * inch, height - 1 * inch, "NGASSAM OPTIQUE")

    c.setFont("Helvetica", 12)
    c.setFillColor(colors.black)
    c.drawString(2.0 * inch, height - 1.3 * inch, "Situé à l'Avenue Kennedy derrière ADAMAOUA PALACE")
    c.drawString(2.1 * inch, height - 1.5 * inch, "Tél.: (237) 699 67 50 25 / 620 37 69 38 / 671 16 65 27")
    
    c.setFont("Helvetica-Oblique", 14)
    c.setFillColor(colors.red)
    c.drawString(2.59 * inch, height - 1.8 * inch, "Le professionnel de la santé visuelle")
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(2.53 * inch, height - 2.2 * inch, "ORDONNANCE DE LUNETTES")

    # Separator Line
    c.setStrokeColor(colors.black)
    c.setLineWidth(2)
    c.line(margin, height - 1.91 * inch, width - margin, height - 1.91 * inch)

    # Patient Information
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.black)
    c.drawString(0.8 * inch, height - 3.0 * inch, "Noms et Prénoms :")
    c.drawString(6.2 * inch, height - 2.7 * inch, "Date :")

    c.drawString(0.8 * inch, height - 3.4 * inch, "Age :")
    c.drawString(2.3 * inch, height - 3.4 * inch, "Sexe :")
    c.drawString(4.5 * inch, height - 3.4 * inch, "Profession :")

    # Table Data
    table_data = [
        ["œil", "Sphère", "Cyl", "Axe", "Addition"],
        ["OD", "", "", "", ""],
        ["OG", "", "", "", ""]
    ]
    
    table = Table(table_data, colWidths=[1.4 * inch] * 5)
    table.setStyle(TableStyle([
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ('FONTNAME', (0, 0), (-1, 0), "Helvetica-Bold"),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER')
    ]))
    
    table.wrapOn(c, width, height)
    table.drawOn(c, 0.8 * inch, height - 4.48 * inch)
    
    
        # Checkboxes with Shadows
    def draw_checkbox(x, y):
        c.setFillColor(colors.lightgrey)  # Shadow effect
        c.rect(x + 1, y - 1, 10, 10, fill=1, stroke=0)
        c.setFillColor(colors.black)  # Main checkbox
        c.rect(x, y, 10, 10, stroke=1, fill=0)

    c.setFont("Helvetica-Bold", 12)
    c.drawString(0.8 * inch, height - 6.0 * inch, "Amétropie:")
    c.drawString(1.78 * inch, height - 6.0 * inch, "Myopie")
    draw_checkbox(2.4 * inch, height - 6.0 * inch)
    c.drawString(2.78 * inch, height - 6.0 * inch, "Hypermétropie")
    draw_checkbox(4.0 * inch, height - 6.0 * inch)
    c.drawString(4.5 * inch, height - 6.0 * inch, "Astigmatisme")
    draw_checkbox(5.64 * inch, height - 6.0 * inch)
    
    c.drawString(6.1 * inch, height - 6.0 * inch, "Presbytie")
    draw_checkbox(6.91 * inch, height - 6.0 * inch)
    
    c.drawString(1.78 * inch, height - 6.4 * inch, "Emmetropie")
    draw_checkbox(2.78 * inch, height - 6.4 * inch)
    
    # Additional Sections for types of lenses
    c.drawString(0.8 * inch, height - 6.74 * inch, "Types de verre :")
    c.drawString(2.2 * inch, height - 6.74 * inch, "minéraux")
    draw_checkbox(3.0 * inch, height - 6.74 * inch)
    c.drawString(3.4 * inch, height - 6.74 * inch, "organiques")
    draw_checkbox(4.35 * inch, height - 6.74 * inch)
    c.drawString(4.9 * inch, height - 6.74 * inch, "polycarbonates")
    draw_checkbox(6.2 * inch, height - 6.74 * inch)


    c.drawString(0.8 * inch, height - 7.3 * inch, "Tientes :")
    c.drawString(1.61 * inch, height - 7.3 * inch, "Blac")
    draw_checkbox(2.03 * inch, height - 7.3 * inch)
    c.drawString(2.45 * inch, height - 7.3 * inch, "Grise")
    draw_checkbox(2.95 * inch, height - 7.3 * inch)
    c.drawString(3.3 * inch, height - 7.3 * inch, "Photochromique")
    draw_checkbox(4.67 * inch, height - 7.3 * inch)
    c.drawString(5.13 * inch, height - 7.3 * inch, "Antireflet")
    draw_checkbox(5.96 * inch, height - 7.3 * inch)
    c.drawString(6.5 * inch, height - 7.3 * inch, "Blue Portect")
    draw_checkbox(7.6 * inch, height - 7.3 * inch)
    
    
    c.drawString(0.8 * inch, height - 7.84* inch, "Foyer :")
    c.drawString(1.46 * inch, height - 7.84* inch, "Unifocaux")
    draw_checkbox(2.33 * inch, height - 7.84* inch)
    c.drawString(2.9 * inch, height - 7.84* inch, "Bifocaux")
    draw_checkbox(3.67 * inch, height - 7.84* inch)
    c.drawString(4.3 * inch, height - 7.84* inch, "Progressifs")
    draw_checkbox(5.27 * inch, height - 7.84* inch)


    c.drawString(0.8 * inch, height - 8.5* inch, "Port :")
    c.drawString(1.46 * inch, height - 8.5* inch, "Constant")
    draw_checkbox(2.33 * inch, height - 8.5* inch)
    c.drawString(2.9 * inch, height - 8.5* inch, "Lecture")
    draw_checkbox(3.67 * inch, height - 8.5* inch)

    

    c.drawString(0.8 * inch, height - 9.0* inch, "Indice :")
    c.drawString(1.46 * inch, height - 9.0* inch, "Normal")
    draw_checkbox(2.33 * inch, height - 9.0* inch)
    c.drawString(2.9 * inch, height - 9.0* inch, "For Indice")
    draw_checkbox(3.67 * inch, height - 9.0* inch)

    
    


    # Footer
    c.setFont("Helvetica-Bold", 12)
    c.setFillColor(colors.red)
    c.drawString(1.0 * inch, height - 10.5 * inch, "N.B.: Rapporter toujours vos lunettes après l'achat pour le contrôle")

    # Save PDF
    c.save()

# Generate PDF
draw_prescription_form("prescription_form1.pdf")


# from reportlab.lib import colors
# from reportlab.lib.pagesizes import A4
# from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
# from reportlab.lib.styles import getSampleStyleSheet
# from reportlab.pdfgen import canvas

# def generate_prescription_form(filename):
#     doc = SimpleDocTemplate(filename, pagesize=A4)
#     elements = []
#     styles = getSampleStyleSheet()
    
#     # Header Section
#     title = Paragraph("<b>NGASSAM OPTIQUE</b>", styles['Title'])
#     subtitle = Paragraph("Situé à l’Avenue Kennedy derrière ADAMAOUA PALACE", styles['Normal'])
#     contact = Paragraph("Tél.: (237) 699 67 50 25 / 620 37 69 38 / 671 16 65 27", styles['Normal'])
#     elements.extend([title, subtitle, contact, Spacer(1, 12)])
    
#     # Prescription Title
#     prescription_title = Paragraph("<b>ORDONNANCE DE LUNETTES</b>", styles['Heading2'])
#     elements.append(prescription_title)
    
#     # Patient Details
#     patient_info = [
#         ["Noms et Prénoms :", ""],
#         ["Age :", "", "Sexe :", "", "Profession :", ""],
#         ["Date :", ""]
#     ]
#     patient_table = Table(patient_info, colWidths=[100, 200, 50, 50, 80, 150])
#     patient_table.setStyle(TableStyle([
#         ('GRID', (0,0), (-1,-1), 1, colors.black),
#         ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
#         ('ALIGN', (0,0), (-1,-1), 'LEFT')
#     ]))
#     elements.append(patient_table)
#     elements.append(Spacer(1, 12))
    
#     # Prescription Table
#     data = [
#         ["Oeil", "Sphère", "Cyl", "Axe", "Addition"],
#         ["OD", "", "", "", ""],
#         ["OG", "", "", "", ""]
#     ]
#     table = Table(data, colWidths=[60, 60, 60, 60, 60])
#     table.setStyle(TableStyle([
#         ('GRID', (0,0), (-1,-1), 1, colors.black),  # Add border around all cells
#         ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),  # Header background
#         ('ALIGN', (0,0), (-1,-1), 'CENTER'),
#         ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
#         ('BOTTOMPADDING', (0,0), (-1,0), 8),
#     ]))
#     elements.append(table)
    
#     # Additional Sections (Check Boxes)
#     conditions = [
#         ["Amétropie:", "Myopie", "☐", "Hypermétropie", "☐", "Astigmatisme", "☐"],
#         ["", "Presbytie", "☐", "Emmétropie", "☐", "", ""]
#     ]
#     conditions_table = Table(conditions, colWidths=[80, 80, 30, 80, 30, 80, 30])
#     conditions_table.setStyle(TableStyle([
#         ('GRID', (0,0), (-1,-1), 1, colors.black),
#         ('FONTNAME', (0,0), (-1,-1), 'Helvetica'),
#         ('ALIGN', (0,0), (-1,-1), 'LEFT')
#     ]))
#     elements.append(conditions_table)
    
#     # Footer Note
#     footer_note = Paragraph("<b>N.B.:</b> Rappoter toujours vos lunettes après l'achat pour le contrôle", styles['Italic'])
#     elements.append(Spacer(1, 12))
#     elements.append(footer_note)
    
#     # Generate PDF
#     doc.build(elements)

# # Generate the form
# generate_prescription_form("prescription_form.pdf")
