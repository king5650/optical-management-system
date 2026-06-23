from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QComboBox, QVBoxLayout
from PyQt6.QtCore import QLocale, QTranslator, QCoreApplication

class LanguageChanger(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize UI elements
        self.setWindowTitle(QCoreApplication.translate("LanguageChanger", "Language Changer"))
        self.label = QLabel(QCoreApplication.translate("LanguageChanger", "Select Language:"), self)
        self.language_combo = QComboBox(self)
        self.language_combo.addItems(["English", "French"])
        self.change_button = QPushButton(QCoreApplication.translate("LanguageChanger", "Change Language"), self)
        self.translation_label = QLabel(QCoreApplication.translate("LanguageChanger", "Hello, World!"), self) 

        # Connect signals to slots
        self.language_combo.currentIndexChanged.connect(self.change_language)
        self.change_button.clicked.connect(self.change_language)

        # Layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.language_combo)
        layout.addWidget(self.change_button)
        layout.addWidget(self.translation_label) 

        # Load initial language (English)
        self.translator = QTranslator()
        self.load_translation("en") 

    def change_language(self):
        """Changes the application language based on the selected language."""
        language = self.language_combo.currentText().lower()
        self.load_translation(language)

    def load_translation(self, language):
        """Loads the translation file for the specified language."""
        if language == "french":
            if self.translator.load(":/translations/fr_FR"):  # Assuming your translation file is in the 'translations' folder
                QCoreApplication.installTranslator(self.translator)
        else:
            QCoreApplication.removeTranslator(self.translator) 

        # Re-translate UI elements
        self.setWindowTitle(QCoreApplication.translate("LanguageChanger", "Language Changer")) 
        self.label.setText(QCoreApplication.translate("LanguageChanger", "Select Language:")) 
        self.change_button.setText(QCoreApplication.translate("LanguageChanger", "Change Language"))
        self.translation_label.setText(QCoreApplication.translate("LanguageChanger", "Hello, World!"))

if __name__ == "__main__":
    app = QApplication([])
    window = LanguageChanger()
    window.show()
    app.exec()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
#     from django.db import transaction
# from django.http import JsonResponse
# from .models import Frame, Lens, OpticalAccessory, Purchase

# @csrf_exempt
# def validate_purchase(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)

#             # Debugging: Log the received data
#             print("Data received from frontend:", data)

#             patient_name = data.get('patient_name')
#             total_amount = data.get('total_amount')
#             vat_total = data.get('vat_total')
#             purchase_details = data.get('purchase_details', [])

#             if not patient_name or not purchase_details:
#                 return JsonResponse({"error": "Invalid data provided."}, status=400)

#             with transaction.atomic():
#                 # Save purchase record
#                 purchase = Purchase.objects.create(
#                     patient_name=patient_name,
#                     total_amount=total_amount,
#                     vat_total=vat_total,
#                 )

#                 # Save each purchase detail and update stock
#                 for detail in purchase_details:
#                     item_name = detail['item_name']
#                     item_type = detail['item_type']
#                     unit_price = detail['unit_price']
#                     quantity = detail['quantity']
#                     total = detail['total']

#                     # Parse the item type and subtype
#                     item_type, subtype = parse_item_type_and_subtype(item_type)

#                     # Identify item type and validate stock
#                     if item_type == "Frame":
#                         frame = Frame.objects.filter(frame_type__iexact=subtype).first()
#                         if not frame:
#                             raise ValueError(f"Frame with type '{subtype}' not found.")
#                         if frame.stock_level < quantity:
#                             raise ValueError(f"Insufficient stock for Frame type '{subtype}'. Available: {frame.stock_level}, Requested: {quantity}")
#                         frame.stock_level -= quantity
#                         frame.quantity_sold += quantity
#                         frame.save()

#                     elif item_type == "Lens":
#                         lens = Lens.objects.filter(lens_type__iexact=subtype).first()
#                         if not lens:
#                             raise ValueError(f"Lens with type '{subtype}' not found.")
#                         if lens.stock_level < quantity:
#                             raise ValueError(f"Insufficient stock for Lens type '{subtype}'. Available: {lens.stock_level}, Requested: {quantity}")
#                         lens.stock_level -= quantity
#                         lens.quantity_sold += quantity
#                         lens.save()

#                     elif item_type == "Optical Accessory":
#                         accessory = OpticalAccessory.objects.filter(name__iexact=subtype).first()
#                         if not accessory:
#                             raise ValueError(f"Optical Accessory '{subtype}' not found.")
#                         if accessory.stock_level < quantity:
#                             raise ValueError(f"Insufficient stock for Optical Accessory '{subtype}'. Available: {accessory.stock_level}, Requested: {quantity}")
#                         accessory.stock_level -= quantity
#                         accessory.quantity_sold += quantity
#                         accessory.save()

#                     else:
#                         raise ValueError(f"Invalid item type: {item_type}")

#                     # Save purchase detail
#                     purchase.details.create(
#                         item_name=subtype,
#                         item_type=item_type,
#                         unit_price=unit_price,
#                         quantity=quantity,
#                         total=total,
#                     )

#                 return JsonResponse({"message": "Purchase validated successfully!"}, status=200)

#         except ValueError as ve:
#             print("ValueError:", ve)  # Debugging
#             return JsonResponse({"error": str(ve)}, status=400)
#         except Exception as e:
#             print("Exception occurred:", e)  # Debugging
#             return JsonResponse({"error": f"An error occurred: {str(e)}"}, status=500)

#     return JsonResponse({"error": "Invalid request method."}, status=405)

# def parse_item_type_and_subtype(item_type):
#     """
#     Parse the item type string to separate the main type (Frame, Lens, etc.)
#     and its subtype (e.g., VIP, Bi-focaux).
#     """
#     if "(" in item_type and ")" in item_type:
#         # Extract main type and subtype
#         main_type, subtype = item_type.split("(", 1)
#         return main_type.strip(), subtype.strip(")")
#     return item_type, ""
