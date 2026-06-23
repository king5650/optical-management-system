# # # # from reportlab.lib.pagesizes import letter, A3
# # # # from reportlab.pdfgen import canvas

# # # # def create_pdf_with_image(output_filename, image_path):
# # # #     c = canvas.Canvas(output_filename, pagesize=A3)
# # # #     width, height = letter

# # # #     # Set the coordinates where the image will be drawn
# # # #     x = 100
# # # #     y = height - 200  # from the top

# # # #     # Draw the image
# # # #     c.drawImage(image_path, x, y, width=400, height=300)

# # # #     # Add some text
# # # #     c.drawString(100, height - 50, "Hello, this is a PDF with an image!")

# # # #     # Save the PDF file
# # # #     c.save()

# # # # # Specify the output PDF file and the image file
# # # # output_filename = "example.pdf"
# # # # image_path = "add_shopping_cart_16px.png"
# # # # # optical/management/static/add_shopping_cart_16px.png
# # # # # Create the PDF with the image
# # # # create_pdf_with_image(output_filename, image_path)



# # # from reportlab.pdfgen import canvas

# # # def hello(c):
# # #     c.drawString(100,100,"hello world")
# # # c = canvas.Canvas("p1.pdf")
# # # hello(c)
# # # c.showPage()
# # # c.save()

# # from reportlab.lib.pagesizes import letter
# # from reportlab.pdfgen import canvas
# # from reportlab.lib.units import inch
# # from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
# # from reportlab.lib import colors

# # def create_receipt(filename, company_details, buyer_details, items, subtotal, tax, total):
# #     doc = SimpleDocTemplate(filename, pagesize=letter)
# #     elements = []

# #     # Company Details
# #     c_details = f"Company Name: {company_details['name']}\nAddress: {company_details['address']}\nPhone: {company_details['phone']}\nEmail: {company_details['email']}"
# #     elements.append(canvas.StringCanvas)
    
# #     # Buyer Details
# #     b_details = f"Buyer Name: {buyer_details['name']}\nAddress: {buyer_details['address']}\nPhone: {buyer_details['phone']}\nEmail: {buyer_details['email']}"
# #     elements.append(canvas.StringCanvas)

# #     # Items Table
# #     data = [['Item', 'Price']] + [[item, f"${price:.2f}"] for item, price in items.items()]
# #     table = Table(data)
# #     table.setStyle(TableStyle([
# #         ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
# #         ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
# #         ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
# #         ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
# #         ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
# #         ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
# #         ('GRID', (0, 0), (-1, -1), 1, colors.black),
# #     ]))
# #     elements.append(table)

# #     # Subtotal, Tax, and Total
# #     elements.append(canvas.StringCanvas)
# #     elements.append(canvas.StringCanvas)

# #     doc.build(elements)

# # # Example usage
# # company_details = {
# #     "name": "ABC Corp",
# #     "address": "123 Business Road, Business City, BC 12345",
# #     "phone": "123-456-7890",
# #     "email": "contact@abccorp.com"
# # }

# # buyer_details = {
# #     "name": "John Doe",
# #     "address": "456 Customer St, Customer City, CC 67890",
# #     "phone": "098-765-4321",
# #     "email": "johndoe@example.com"
# # }

# # items = {
# #     "Item A": 29.99,
# #     "Item B": 9.99,
# #     "Item C": 4.99
# # }
# # subtotal = sum(items.values())
# # tax = subtotal * 0.07
# # total = subtotal + tax

# # create_receipt("detailed_receipt.pdf", company_details, buyer_details, items, subtotal, tax, total)





#  from reportlab.lib.pagesizes import A3
# from reportlab.lib import colors
# from reportlab.lib.units import inch
# from reportlab.pdfgen import canvas
# from reportlab.platypus import Table, TableStyle


# def generate_receipt_pdf(filename="receipt.pdf"):
#     c = canvas.Canvas(filename, pagesize=A3)
#     width, height = A3

#     # Set Logo
#     logo_path = "add_shopping_cart_16px.png"  # Update with actual path
#     c.drawImage(logo_path, inch, height - 2 * inch, width=3 * inch, height=1.5 * inch, mask="auto")

#     # Business Header
#     c.setFont("Helvetica-Bold", 48)
#     c.drawString(3.5 * inch, height - 1.5 * inch, "NGASSAM OPTIQUE")
    
#     c.setFont("Helvetica", 16)
#     c.drawString(3.5 * inch, height - 2 * inch, "CABINET OPTIQUE")
#     c.setFont("Helvetica", 14)
#     c.drawString(3.5 * inch, height - 2.5 * inch, "Vente de matériel - Ophtalmique médical - Verre ophtalmique")
#     c.drawString(3.5 * inch, height - 3 * inch, "Situé derrière ADAMAOUA PALACE - Tél: (237) 699 67 50 25")

#     # Receipt Title
#     c.setFont("Helvetica-Bold", 20)
#     c.drawString(3.5 * inch, height - 4 * inch, "FACTURE PROFORMA")

#     # Invoice Details
#     c.setFont("Helvetica", 14)
#     c.drawString(inch, height - 4.8 * inch, "Doit:")
#     c.drawString(width / 2, height - 4.8 * inch, "Date:")
#     c.drawString(inch, height - 5.3 * inch, "N.I.U:")

#     # Table Header
#     table_data = [
#         ["Qté", "Désignation", "Prix Unitaire", "Prix Total"],
#         ["I - Verre (H.T.)", "", "", ""],
#         ["II - Montures (H.T.)", "", "", ""],
#         ["III - Accessoires (H.T.)", "", "", ""],
#     ]

#     # Table Styling
#     table = Table(table_data, colWidths=[1 * inch, 4 * inch, 2 * inch, 2 * inch])
#     table.setStyle(TableStyle([
#         ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
#         ("TEXTCOLOR", (0, 0), (-1, 0), colors.black),
#         ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#         ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
#         ("FONTSIZE", (0, 0), (-1, -1), 14),
#         ("GRID", (0, 0), (-1, -1), 1, colors.black),
#     ]))

#     # Draw Table
#     table.wrapOn(c, width, height)
#     table.drawOn(c, inch, height - 8 * inch)

#     # Summary Section
#     y_summary = height - 10 * inch
#     c.setFont("Helvetica-Bold", 14)
#     c.drawString(3 * inch, y_summary, "Total hors taxes:")
#     c.drawString(7 * inch, y_summary, "XAF")

#     c.drawString(3 * inch, y_summary - 0.5 * inch, "TVA sur Monture (19.25%):")
#     c.drawString(7 * inch, y_summary - 0.5 * inch, "XAF")

#     c.drawString(3 * inch, y_summary - 1 * inch, "TVA sur Accessoires (19.25%):")
#     c.drawString(7 * inch, y_summary - 1 * inch, "XAF")

#     c.drawString(3 * inch, y_summary - 1.5 * inch, "TVA sur Frais montage (19.25%):")
#     c.drawString(7 * inch, y_summary - 1.5 * inch, "XAF")

#     c.drawString(3 * inch, y_summary - 2.5 * inch, "Total TVA:")
#     c.drawString(7 * inch, y_summary - 2.5 * inch, "XAF")

#     c.drawString(3 * inch, y_summary - 4 * inch, "Arrêté la présente facture proforma à la somme de :")
#     c.drawString(7 * inch, y_summary - 4 * inch, "XAF")

#     # Save PDF
#     c.save()

#     return filename


# # Test generate receipt
# generate_receipt_pdf()


######################################################################

# original version
# from reportlab.lib.pagesizes import A3
# from reportlab.lib import colors
# from reportlab.lib.units import inch
# from reportlab.pdfgen import canvas
# from reportlab.platypus import Table, TableStyle, Image


# def generate_receipt_pdf(transaction_data, filename="receipt_test1.pdf"):
#     """
#     Generate a receipt PDF with the given transaction data.
    
#     :param transaction_data: Dictionary containing sale details
#     :param filename: Output PDF filename
#     """
    
#     c = canvas.Canvas(filename, pagesize=A3)
#     width, height = A3
#     margin = 1.5 * inch  # Added margin for better alignment
    
#         # Draw border frame
#     c.setStrokeColor(colors.black)
#     c.setLineWidth(3)
#     c.rect(margin / 2, margin / 2, width - margin, height - margin)

#     # 🏷️ Logo Placement
#     logo_path = "add_shopping_cart_16px.png"  # Update this with your actual logo path
#     c.drawImage(logo_path, margin, height - 2.5 * inch, width=.4 * inch, height=.4 * inch, mask="auto")
    
#     #left icon
#     logo_path = "add_shopping_cart_16px.png"  # Update this with your actual logo path
#     c.drawImage(logo_path, width / 1.2, height - 2.6 * inch, width=.4 * inch, height=.4 * inch, mask="auto")


#     # 🏢 Business Info 
#     c.setFillColor(colors.HexColor('#062440'))
#     c.setFont("Helvetica-Bold", 64)
#     c.drawString(width / 8.0, height - 1.5 * inch, "NGASSAM OPTIQUE")
#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(width / 2.34, height - 1.87 * inch, "CABINET OPTIQUE")
#     c.drawString(margin + 0.59 * inch, height - 2.1 * inch, "Vente de matériel Ophtalmique médical-Verre ophtalmique - Montures de marque")
#     c.drawString(margin + 2.5 * inch, height - 2.5 * inch, "N.I.U: P039116571318-RC/YAO/2023/A/351")
#     c.drawString(margin + 0.1 * inch, height - 2.9 * inch, "Situé derrière ADAMAQUA PALACE - Tél.: (237) 699 67 50 25/620 37 69 28/651 63 06 45")

#     # 📌 Draw Separator Line
#     c.setStrokeColor(colors.black)
#     c.setLineWidth(2)
#     c.line(margin, height - 3.15 * inch, width - margin, height - 3.15 * inch)

#     c.setFont("Helvetica-Bold", 17)
#     c.drawString(margin + 2.67 * inch, height - 3.6 * inch, "Le professionnel de la santé visuelle")
    
    
#         # 🧾 Receipt date
#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(width / 1.2, height - 4 * inch, "Date:")
    

#     # 🧾 Receipt Title
#     c.setFont("Helvetica-Bold", 22)
#     c.drawString(width / 2.6, height - 4.5 * inch, "SALES RECEIPT")


#     # 📜 Transaction Details
#     c.setFont("Helvetica-Bold", 14)
#     y_position = height - 5.5 * inch
#     c.drawString(margin, y_position, f"Doit: {transaction_data['date']}")
#     # c.drawString(width / 2, y_position, f"Transaction ID: {transaction_data['transaction_id']}")
#     c.drawString(margin, y_position - 0.5 * inch, f"N.U.I: {transaction_data['cashier']}")
#     # c.drawString(width / 2, y_position - 0.5 * inch, f"Patient: {transaction_data['patient_name']}")

#     # 📋 Table Headers
#     table_data = [["Qty", "Item", "Unit Price (XAF)", "Total (XAF)"]]
#     for item in transaction_data["items"]:
#         table_data.append([item["quantity"], item["item_name"], f"{item['unit_price']:,.2f}", f"{item['total']:,.2f}"])

#     # 🏷️ Create Table with Enhanced Styling
#     table = Table(table_data, colWidths=[1 * inch, 4 * inch, 2 * inch, 2 * inch])
#     table.setStyle(TableStyle([
#         ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),  # Header background
#         ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
#         ("ALIGN", (0, 0), (-1, -1), "CENTER"),
#         ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
#         ("FONTSIZE", (0, 0), (-1, -1), 14),
#         ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
#         ("GRID", (0, 0), (-1, -1), 1, colors.black),
#     ]))

#     # 📌 Draw Table
#     table.wrapOn(c, width, height, )
#     table.drawOn(c, margin, height - 11.0 * inch)

#     # 📊 Summary Section
#     y_summary = height - 11.8 * inch
#     c.setFont("Helvetica-Bold", 16)
#     c.drawString(margin + .11 * inch, y_summary, "Total hors taxes:")
#     c.drawString(margin + 6.5 * inch, y_summary, f"{transaction_data['total_without_vat']:,.2f} XAF")
    
#     c.drawString(margin + .11 * inch, y_summary - 0.5 * inch, "TVA sur Monture (19.25%):")
#     c.drawString(margin + 6.5 * inch, y_summary - 0.5 * inch, f"{transaction_data['vat_on_frame']:,.2f} XAF")

#     c.drawString(margin + .11 * inch, y_summary - 1 * inch, "TVA sur Accessories (19.25%):")
#     c.drawString(margin + 6.5 * inch, y_summary - 1 * inch, f"{transaction_data['vat_on_accessory']:,.2f} XAF")

#     c.drawString(margin + .11 * inch, y_summary - 1.5 * inch, "TVA sur Frais montage (19.25%):")
#     c.drawString(margin + 6.5 * inch, y_summary - 1.5 * inch, f"{transaction_data['vat_on_mounting']:,.2f} XAF")

#     c.drawString(margin + .11 * inch, y_summary - 2 * inch, "Total TVA:")
#     c.drawString(margin + 6.5 * inch, y_summary - 2 * inch, f"{transaction_data['total_vat']:,.2f} XAF")

#     # c.drawString(margin + .11 * inch, y_summary - 2 * inch, "Change Due:")
#     # c.drawString(margin + 6.5 * inch, y_summary - 2 * inch, f"{transaction_data['change']:,.2f} XAF")

#     # 📌 Footer Section
#     c.setFont("Helvetica-Bold", 14)
#     c.setFillColor(colors.darkblue)
#     c.drawString(width / 6.7, y_summary - 3 * inch, "Arrêté la présente facture proforma à la somme de")
#     c.drawString(width / 1.45, y_summary - 3 * inch, f"{transaction_data['total_amount']:,.2f} XAF")
    
#     # 💾 Save PDF
#     c.save()

#     return filename


# # 🛠 Test the PDF Generation
# if __name__ == "__main__":
#     test_transaction = {
#         "date": "2025-02-06",
#         "transaction_id": "TRX123456",
#         "cashier": "John Doe",
#         "patient_name": "Jane Smith",
#         "items": [
#             {"quantity": 2, "item_name": "VIP Frame", "unit_price": 25000, "total": 50000},
#             {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
#             {"quantity": 2, "item_name": "VIP Frame", "unit_price": 25000, "total": 50000},
#             {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
#             {"quantity": 2, "item_name": "VIP Frame", "unit_price": 25000, "total": 50000},
#             {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
#             {"quantity": 2, "item_name": "VIP Frame", "unit_price": 25000, "total": 50000},
#             {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
#             {"quantity": 2, "item_name": "VIP Frame", "unit_price": 25000, "total": 50000},
#             {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
#             {"quantity": 2, "item_name": "VIP Frame", "unit_price": 25000, "total": 50000},
#             {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
#             {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
#             {"quantity": 2, "item_name": "VIP Frame", "unit_price": 25000, "total": 50000},
#             {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
#             {"quantity": 2, "item_name": "VIP Frame", "unit_price": 25000, "total": 50000},
#             {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
         
#         ],
#         "total_without_vat": 200000,
#         "vat_on_frame": 65000,
#         "vat_on_accessory": 12512.5,
#         "vat_on_mounting": 77512.5,
#         "total_vat": 80000,
#         "total_amount": 2487.5
#     }

#     pdf_file = generate_receipt_pdf(test_transaction)
#     print(f"PDF generated: {pdf_file}")
########################################################################







from reportlab.lib.pagesizes import A3
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import Table, TableStyle, Image


def generate_receipt_pdf(transaction_data, filename="receipt_test1.pdf"):
    """
    Generate a receipt PDF with the given transaction data.
    
    :param transaction_data: Dictionary containing sale details
    :param filename: Output PDF filename
    """
    
    c = canvas.Canvas(filename, pagesize=A3)
    width, height = A3
    margin = 1.5 * inch  # Added margin for better alignment
    
        # Draw border frame
    c.setStrokeColor(colors.black)
    c.setLineWidth(3)
    c.rect(margin / 2, margin / 2, width - margin, height - margin)

    def header_section():
        

        # 🏷️ Logo Placement
        logo_path = "add_shopping_cart_16px.png"  # Update this with your actual logo path
        c.drawImage(logo_path, margin, height - 2.5 * inch, width=.4 * inch, height=.4 * inch, mask="auto")
        
        #left icon
        logo_path = "add_shopping_cart_16px.png"  # Update this with your actual logo path
        c.drawImage(logo_path, width / 1.2, height - 2.6 * inch, width=.4 * inch, height=.4 * inch, mask="auto")


        # 🏢 Business Info 
        c.setFillColor(colors.HexColor('#062440'))
        c.setFont("Helvetica-Bold", 64)
        c.drawString(width / 8.0, height - 1.5 * inch, "NGASSAM OPTIQUE")
        c.setFont("Helvetica-Bold", 16)
        c.drawString(width / 2.34, height - 1.87 * inch, "CABINET OPTIQUE")
        c.drawString(margin + 0.59 * inch, height - 2.1 * inch, "Vente de matériel Ophtalmique médical-Verre ophtalmique - Montures de marque")
        c.drawString(margin + 2.5 * inch, height - 2.5 * inch, "N.I.U: P039116571318-RC/YAO/2023/A/351")
        c.drawString(margin + 0.1 * inch, height - 2.9 * inch, "Situé derrière ADAMAQUA PALACE - Tél.: (237) 699 67 50 25/620 37 69 28/651 63 06 45")

        # 📌 Draw Separator Line
        c.setStrokeColor(colors.black)
        c.setLineWidth(2)
        c.line(margin, height - 3.15 * inch, width - margin, height - 3.15 * inch)

        c.setFont("Helvetica-Bold", 17)
        c.drawString(margin + 2.67 * inch, height - 3.6 * inch, "Le professionnel de la santé visuelle")
    
    header_section()
    
    def informations_section():
        # 🧾 Receipt date
        c.setFont("Helvetica-Bold", 16)
        c.drawString(width / 1.2, height - 4 * inch, "Date:")
        

        # 🧾 Receipt Title
        c.setFont("Helvetica-Bold", 22)
        c.drawString(width / 2.6, height - 4.5 * inch, "SALES RECEIPT")


        # 📜 Transaction Details
        c.setFont("Helvetica-Bold", 14)
        y_position = height - 5.5 * inch
        c.drawString(margin, y_position, f"Doit: {transaction_data['date']}")
        # c.drawString(width / 2, y_position, f"Transaction ID: {transaction_data['transaction_id']}")
        c.drawString(margin, y_position - 0.5 * inch, f"N.U.I: {transaction_data['cashier']}")
        # c.drawString(width / 2, y_position - 0.5 * inch, f"Patient: {transaction_data['patient_name']}")
    informations_section()
    
    # 📋 Table Headers
    table_data = [["Qty", "Item", "Unit Price (XAF)", "Total (XAF)"]]
    for item in transaction_data["items"]:
        table_data.append([item["quantity"], item["item_name"], f"{item['unit_price']:,.2f}", f"{item['total']:,.2f}"])

    max_rows_per_page = 35
    rows = table_data[1:]
    y_position = height - 15.5 * inch
    first_page = True
    
    while rows:
        table_slice = [table_data[0]] + rows[:max_rows_per_page]
        rows = rows[max_rows_per_page:]
        
    # 🏷️ Create Table with Enhanced Styling
        table = Table(table_slice, colWidths=[1 * inch, 4 * inch, 2 * inch, 2 * inch])
        table.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),  # Header background
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 14),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 10),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]))

        # 📌 Draw Table
        table.wrapOn(c, width, height, )
        #table.drawOn(c, margin, height - 11.0 * inch)
        table.drawOn(c, margin, y_position)
            
        if rows:
            c.showPage()
            #header_section()
            first_page = False
            y_position = height - 10.0 * inch  # Adjust for subsequent pages

    # 📊 Summary Section
    y_summary = height - 11.8 * inch
    c.setFont("Helvetica-Bold", 16)
    c.drawString(margin + .11 * inch, y_summary, "Total hors taxes:")
    c.drawString(margin + 6.5 * inch, y_summary, f"{transaction_data['total_without_vat']:,.2f} XAF")
    
    c.drawString(margin + .11 * inch, y_summary - 0.5 * inch, "TVA sur Monture (19.25%):")
    c.drawString(margin + 6.5 * inch, y_summary - 0.5 * inch, f"{transaction_data['vat_on_frame']:,.2f} XAF")

    c.drawString(margin + .11 * inch, y_summary - 1 * inch, "TVA sur Accessories (19.25%):")
    c.drawString(margin + 6.5 * inch, y_summary - 1 * inch, f"{transaction_data['vat_on_accessory']:,.2f} XAF")

    c.drawString(margin + .11 * inch, y_summary - 1.5 * inch, "TVA sur Frais montage (19.25%):")
    c.drawString(margin + 6.5 * inch, y_summary - 1.5 * inch, f"{transaction_data['vat_on_mounting']:,.2f} XAF")

    c.drawString(margin + .11 * inch, y_summary - 2 * inch, "Total TVA:")
    c.drawString(margin + 6.5 * inch, y_summary - 2 * inch, f"{transaction_data['total_vat']:,.2f} XAF")

    # c.drawString(margin + .11 * inch, y_summary - 2 * inch, "Change Due:")
    # c.drawString(margin + 6.5 * inch, y_summary - 2 * inch, f"{transaction_data['change']:,.2f} XAF")

    # 📌 Footer Section
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.darkblue)
    c.drawString(width / 6.7, y_summary - 3 * inch, "Arrêté la présente facture proforma à la somme de")
    c.drawString(width / 1.45, y_summary - 3 * inch, f"{transaction_data['total_amount']:,.2f} XAF")
    
    # 💾 Save PDF
    c.save()

    return filename


# 🛠 Test the PDF Generation
if __name__ == "__main__":
    test_transaction = {
        "date": "2025-02-06",
        "transaction_id": "TRX123456",
        "cashier": "John Doe",
        "patient_name": "Jane Smith",
        "items": [
            {"quantity": 2, "item_name": "VIP Frame", "unit_price": 25000, "total": 50000},
            {"quantity": 1, "item_name": "Lens", "unit_price": 15000, "total": 15000},
        ] * 20,
        "total_without_vat": 200000,
        "vat_on_frame": 65000,
        "vat_on_accessory": 12512.5,
        "vat_on_mounting": 77512.5,
        "total_vat": 80000,
        "total_amount": 2487.5
    }

    pdf_file = generate_receipt_pdf(test_transaction)
    print(f"PDF generated: {pdf_file}")


#