from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('secretary', 'Secretary'),
        ('stockist', 'Stockist'),
        ('patient', 'Patient'),
    )
    contact = models.CharField(max_length=15, null=True, blank=True)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='patient')
    date_joined = models.DateTimeField(auto_now_add=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.username
    
from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Other'),  # Optional inclusive option
    )
    name = models.CharField(max_length=255)
    contact = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, default='Yaoundé')  # Fixed spelling from 'addresse' to 'address'
    profession = models.CharField(max_length=355, default=' ', null=True, blank=True)
    age = models.IntegerField(null=True)  # Ensure this is present
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, default='M')
    date_registered = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name





# -------------------------------
# Medical Report Table  
# -------------------------------
class MedicalReports(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_reports')
    date = models.DateField(auto_now_add=True)
    age_at_report = models.PositiveIntegerField(blank=True, null=True)
    profession_at_report = models.CharField(max_length=200, blank=True, null=True)
    reference_id = models.CharField(max_length=20, unique=True, null=True, blank=True)  # Unique reference ID for the report
    # PDF File Upload for scanned or generated prescription (optional)
    # pdf_file = models.FileField(upload_to='medical_reports/', blank=True, null=True)
    pdf_file = models.FileField(upload_to='medical_reports/%Y/%m/%d', blank=True, null=True)

    def __str__(self):
        return f"Report for {self.patient.name} - {self.date}"

# -------------------------------
# Refraction Table (Eye Measurements)
# -------------------------------
class Refraction(models.Model):
    medical_report = models.OneToOneField(MedicalReports, on_delete=models.CASCADE, related_name='refraction')

    # Right Eye (OD)
    sphere_od = models.CharField(max_length=10, blank=True)
    cyl_od = models.CharField(max_length=10, blank=True)
    axe_od = models.CharField(max_length=10, blank=True)
    addition_od = models.CharField(max_length=10, blank=True)

    # Left Eye (OG)
    sphere_og = models.CharField(max_length=10, blank=True)
    cyl_og = models.CharField(max_length=10, blank=True)
    axe_og = models.CharField(max_length=10, blank=True)
    addition_og = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return f"Refraction - {self.medical_report}"

# -------------------------------
# Prescription Detail Table
# -------------------------------
class PrescriptionDetail(models.Model):
    medical_report = models.OneToOneField(MedicalReports, on_delete=models.CASCADE, related_name='prescription')

    AMETROPIE_CHOICES = [
        ('myopie', 'Myopie'),
        ('hypermetropie', 'Hypermétropie'),
        ('astigmatisme', 'Astigmatisme'),
        ('presbytie', 'Presbytie'),
        ('emmetropie', 'Emmétropie'),
    ]
    # ametropie = models.CharField(max_length=20, choices=AMETROPIE_CHOICES, blank=True)
    ametropie = MultiSelectField(choices=AMETROPIE_CHOICES, blank=True)

    VERRE_CHOICES = [
        ('mineraux', 'Minéraux'),
        ('organiques', 'Organiques'),
        ('polycarbonates', 'Polycarbonates'),
    ]
    # types_de_verre = models.CharField(max_length=20, choices=VERRE_CHOICES, blank=True)
    types_de_verre = MultiSelectField(choices=VERRE_CHOICES, blank=True)
    
    TEINTES_CHOICES = [
        ('blanc', 'Blanc'),
        ('gris', 'Gris'),
        ('photochromique', 'Photochromique'),
        ('antireflet', 'Antireflet'),
        ('bleue_protect', 'Bleue Protect'),
    ]
    # teintes = models.CharField(max_length=20, choices=TEINTES_CHOICES, blank=True)
    teintes = MultiSelectField(choices=TEINTES_CHOICES, blank=True)

    FOYERS_CHOICES = [
        ('unifocaux', 'Unifocaux'),
        ('bifocaux', 'Bifocaux'),
        ('progressifs', 'Progressifs'),
    ]
    # foyers = models.CharField(max_length=20, choices=FOYERS_CHOICES, blank=True)
    foyers = MultiSelectField(choices=FOYERS_CHOICES, blank=True)

    PORT_CHOICES = [
        ('constant', 'Constant'),
        ('lecture', 'Lecture'),
    ]
    # port = models.CharField(max_length=10, choices=PORT_CHOICES, blank=True)
    port = MultiSelectField(choices=PORT_CHOICES, blank=True)

    INDICE_CHOICES = [
        ('normal', 'Normal'),
        ('fort_indice', 'Fort Indice'),
    ]
    # indice = models.CharField(max_length=20, choices=INDICE_CHOICES, blank=True)
    indice = MultiSelectField(choices=INDICE_CHOICES, blank=True)

    def __str__(self):
        return f"Prescription Detail - {self.medical_report}"

##############################################################################################################################3333


#whatsapp message automation

from django.db import models

# 2. ScheduledMessage Model
class ScheduledMessage(models.Model):
    message = models.TextField()
    scheduled_time = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
        ('cancelled', 'Cancelled'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')

    def __str__(self):
        return f"Message (#{self.id}) - {self.status} - Scheduled at {self.scheduled_time}"

# 3. MessageRecipient Model (Tracks which patient got which message)
class MessageRecipient(models.Model):
    message = models.ForeignKey(ScheduledMessage, on_delete=models.CASCADE, related_name='recipients')
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    DELIVERY_STATUS = [
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
    ]
    status = models.CharField(max_length=10, choices=DELIVERY_STATUS, default='pending')
    error_message = models.TextField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.patient.name} - {self.status}"




























    

from django.db import models

class MedicalReport(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_reports')
    patient = models.ForeignKey('Patient', on_delete=models.CASCADE)  # Link to Patient
    date = models.DateField(auto_now_add=True)  # Automatically sets the date
    age = models.IntegerField()  # Age of the patient
    sexe = models.CharField(max_length=10)  # Sex of the patient (Male, Female)
    profession = models.CharField(max_length=100)  # Profession of the patient
    date_registered = models.DateTimeField(auto_now_add=True, blank=True, null=True) 
    
    # OD (Right Eye), OG (Left Eye) fields for the eye tests
    sphere_od = models.CharField(max_length=10, blank=True)
    cyl_od = models.CharField(max_length=10, blank=True)
    axe_od = models.CharField(max_length=10, blank=True)
    addition_od = models.CharField(max_length=10, blank=True)

    sphere_og = models.CharField(max_length=10, blank=True)
    cyl_og = models.CharField(max_length=10, blank=True)
    axe_og = models.CharField(max_length=10, blank=True)
    addition_og = models.CharField(max_length=10, blank=True)

    ametropie_choices = [
        ('myopie', 'Myopie'),
        ('hypermetropie', 'Hypermétropie'),
        ('astigmatisme', 'Astigmatisme'),
        ('presbytie', 'Presbytie'),
        ('emmetropie', 'Emmétropie'),
    ]
    ametropie = models.CharField(max_length=20, choices=ametropie_choices, blank=True)

    verre_choices = [
        ('mineraux', 'Minéraux'),
        ('organiques', 'Organiques'),
        ('polycarbonates', 'Polycarbonates'),
    ]
    types_de_verre = models.CharField(max_length=20, choices=verre_choices, blank=True)

    teintes_choices = [
        ('blanc', 'Blanc'),
        ('gris', 'Gris'),
        ('photochromique', 'Photochromique'),
        ('antireflet', 'Antireflet'),
        ('bleue_protect', 'Bleue Protect'),
    ]
    teintes = models.CharField(max_length=20, choices=teintes_choices, blank=True)

    foyers_choices = [
        ('unifocaux', 'Unifocaux'),
        ('bifocaux', 'Bifocaux'),
        ('progressifs', 'Progressifs'),
    ]
    foyers = models.CharField(max_length=20, choices=foyers_choices, blank=True)

    port_choices = [
        ('constant', 'Constant'),
        ('lecture', 'Lecture'),
    ]
    port = models.CharField(max_length=10, choices=port_choices, blank=True)

    indice_choices = [
        ('normal', 'Normal'),
        ('fort_indice', 'Fort Indice'),
    ]
    indice = models.CharField(max_length=20, choices=indice_choices, blank=True)
    
    pdf_file = models.FileField(upload_to='medical_reports/', blank=True, null=True)
    def __str__(self):
        return f"Medical Report for {self.patient.name} on {self.date}"










































from django.db import models
from django.utils import timezone

# Model for Frames with date tracking and balance
class Frame(models.Model):
    FRAME_TYPES = [
        ('VIP', 'VIP'),
        ('VIP+', 'VIP+'),
        ('VIP++', 'VIP++'),
        ('CLASSIC', 'CLASSIC'),
    ]
    frame_type = models.CharField(max_length=10, choices=FRAME_TYPES)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_level = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)  # Date and time tracker
    quantity_sold = models.IntegerField(default=0)
    
    def total_value(self):
        return self.unit_price * self.stock_level  # Total value of this type of frame

    def __str__(self):
        return f"{self.frame_type} - {self.stock_level} items available"

# Model for Lenses with date tracking and balance
# class Lens(models.Model):
#     LENS_TYPES = [
#         ('simple vision', 'Simple Vision'),
#         ('progressive stock', 'Progressive Stock'),
#         ('progressive commande', 'Progressive Commande'),
#         ('bi-focaux', 'Bi-focaux'),
#     ]
#     lens_type = models.CharField(max_length=20, choices=LENS_TYPES)
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock_level = models.PositiveIntegerField()
#     date_added = models.DateTimeField(default=timezone.now)  # Date and time tracker
#     quantity_sold = models.IntegerField(default=0)
#     qtes = models.IntegerField(default=0)
    
#     def total_value(self):
#         return self.unit_price * self.stock_level  # Total value of this type of lens

#     def __str__(self):
#         return f"{self.lens_type} - {self.stock_level} items available"


class Lens(models.Model):
    LENS_TYPES = [
        ('simple vision', 'Simple Vision'),
        ('progressive stock', 'Progressive Stock'),
        ('progressive commande', 'Progressive Commande'),
        ('bi-focaux', 'Bi-focaux'),
    ]
    lens_type = models.CharField(max_length=20, choices=LENS_TYPES)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_level = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)  # Date and time tracker
    quantity_sold = models.IntegerField(default=0)
    qtes = models.IntegerField(default=0)
    
    def total_value(self):
        return self.unit_price * self.stock_level  # Total value of this type of lens

    def __str__(self):
        return f"{self.lens_type} - {self.stock_level} items available"

    def save(self, *args, **kwargs):
        # Ensure lens_type is set correctly before saving
        if not self.lens_type:
            raise ValueError("Lens type must be set.")
        super().save(*args, **kwargs)

# Model for Optical Accessories with date tracking and balance
class OpticalAccessory(models.Model):
    name = models.CharField(max_length=100)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_level = models.PositiveIntegerField()
    date_added = models.DateTimeField(default=timezone.now)  # Date and time tracker
    quantity_sold = models.IntegerField(default=0)
    
    def total_value(self):
        return self.unit_price * self.stock_level  # Total value of this accessory

    def __str__(self):
        return f"{self.name} - {self.stock_level} items available"
    


# from django.db import models
# from django.utils import timezone


# class Purchase(models.Model):
#     item_type = models.CharField(max_length=20)  # Frame, Lens, Optical Accessory
#     item_subtype = models.CharField(max_length=50, blank=True, null=True)  # e.g., VIP, Progressive Stock
#     quantity = models.PositiveIntegerField()
#     unit_price = models.DecimalField(max_digits=10, decimal_places=2)
#     total_price = models.DecimalField(max_digits=12, decimal_places=2)
#     date_sold = models.DateTimeField(default=timezone.now)
#     patient_name = models.CharField(max_length=100, blank=True, null=True)  # Optional patient name
#     patient_contact = models.CharField(max_length=15, blank=True, null=True)  # Optional patient contact

#     def __str__(self):
#         return f"{self.item_type} - {self.item_subtype} - {self.quantity} sold"

# class Receipt(models.Model):
#     purchases = models.ManyToManyField(Purchase, related_name="receipt_purchases")
#     total_amount = models.DecimalField(max_digits=12, decimal_places=2)
#     date_created = models.DateTimeField(default=timezone.now)  

    def __str__(self):
        return f"Receipt {self.id} - {self.total_amount} created on {self.date_created}"

from django.db import models
from django.utils import timezone

class Sale(models.Model):
    buyer_name = models.CharField(max_length=100, null=True, blank=True)  # Buyer name (can be patient or other)
    buyer_email = models.EmailField(null=True, blank=True)  # Optional buyer email
    buyer_contact = models.CharField(max_length=15, null=True, blank=True)
    buyer_address = models.TextField(null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total amount including VAT
    vat_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Total VAT
    total_without_tax = models.DecimalField(max_digits=10, decimal_places=2)  # Total before VAT
    change_to_give = models.DecimalField(max_digits=10, decimal_places=2, default=0)  # Change after payment
    date = models.DateTimeField(default=timezone.now)  # Date of sale

    def __str__(self):
        return f"Sale ID: {self.id}, Buyer: {self.buyer_name}, Total: {self.total_amount}"

class SoldItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name="items")  # Link to Sale
    item_type = models.CharField(max_length=50)  # E.g., "Frame", "Lens", "Optical Accessory"
    subtype = models.CharField(max_length=50, null=True, blank=True)  # Subtype, if applicable
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)  # Unit price of the item
    quantity = models.PositiveIntegerField()  # Quantity sold
    total_price = models.DecimalField(max_digits=10, decimal_places=2)  # Total price for this item
    vat = models.DecimalField(max_digits=10, decimal_places=2)  # VAT for this item

    def __str__(self):
        return f"{self.item_type} - {self.subtype or 'N/A'}, Quantity: {self.quantity}, Total: {self.total_price}"

from django.db import models
from .models import Frame, Lens, OpticalAccessory, Patient  # Import your existing models


class Transaction(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True)
    total_without_tax = models.DecimalField(max_digits=15, decimal_places=2)
    total_vat = models.DecimalField(max_digits=15, decimal_places=2)
    total_balance = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Transaction #{self.id} for {self.patient or 'Guest'}"


class TransactionItem(models.Model):
    TRANSACTION_ITEM_TYPES = [
        ('Frame', 'Frame'),
        ('Lens', 'Lens'),
        ('Optical Accessory', 'Optical Accessory'),
    ]

    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE, related_name="items")
    item_type = models.CharField(max_length=20, choices=TRANSACTION_ITEM_TYPES)
    frame = models.ForeignKey(Frame, null=True, blank=True, on_delete=models.SET_NULL)
    lens = models.ForeignKey(Lens, null=True, blank=True, on_delete=models.SET_NULL)
    accessory = models.ForeignKey(OpticalAccessory, null=True, blank=True, on_delete=models.SET_NULL)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)

    def __str__(self):
        if self.item_type == "Frame":
            return f"{self.frame.frame_type} ({self.quantity}) in Transaction #{self.transaction.id}"
        elif self.item_type == "Lens":
            return f"{self.lens.lens_type} ({self.quantity}) in Transaction #{self.transaction.id}"
        elif self.item_type == "Optical Accessory":
            return f"{self.accessory.name} ({self.quantity}) in Transaction #{self.transaction.id}"

class Purchase(models.Model):
    patient_name = models.CharField(max_length=255)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    vat_total = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Purchase by {self.patient_name} on {self.date_created.strftime('%Y-%m-%d')}"


class PurchaseDetail(models.Model):
    purchase = models.ForeignKey(Purchase, related_name="details", on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_type = models.CharField(max_length=50)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity}x {self.item_name} ({self.item_type})"




# inventory system

from django.db import models
from django.utils import timezone

class ItemCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Frame, Lens, Accessory
    
    def __str__(self):
        return self.name


class ItemType(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)  # VIP, Simple Vision, etc.

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class InventoryItem(models.Model):
    category = models.ForeignKey(ItemCategory, on_delete=models.CASCADE)
    type = models.ForeignKey(ItemType, null=True, blank=True, on_delete=models.SET_NULL)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_level = models.PositiveIntegerField()
    quantity_sold = models.IntegerField(default=0)
    date_added = models.DateTimeField(default=timezone.now)
    low_stock_threshold = models.PositiveIntegerField(default=5)  # Low stock alert threshold
    expiry_date = models.DateField(null=True, blank=True)  # ✅ Added expiry date field
    def total_value(self):
        return self.unit_price * self.stock_level

    def __str__(self):
        type_name = self.type.name if self.type else "Custom Item"
        return f"{type_name} - {self.stock_level} items available"

    def is_low_stock(self):
        """Check if stock is below the defined threshold."""
        return self.stock_level <= self.low_stock_threshold

# from django.db import models
# from django.utils import timezone

# class SaleRecord(models.Model):
#     inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
#     quantity_sold = models.PositiveIntegerField()
#     sale_date = models.DateTimeField(default=timezone.now)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Sale of {self.quantity_sold} {self.inventory_item.type.name} on {self.sale_date.strftime('%Y-%m-%d')}"
# from django.db import models
# from django.utils import timezone

# class SaleEntry(models.Model):
#     item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     date = models.DateTimeField(default=timezone.now)

#     def total_price(self):
#         return self.quantity * self.price

#     def __str__(self):
#         return f"Sale of {self.quantity} {self.item.type.name} on {self.date}"
from django.db import models
from django.utils import timezone
from django.db import transaction
from django.core.exceptions import ValidationError

class SaleEntry(models.Model):
    item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)

    def total_price(self):
        return self.quantity * self.price

    def __str__(self):
        return f"Sale of {self.quantity} {self.item.type.name} on {self.date}"

    def save(self, *args, **kwargs):
        """Override save to deduct stock from InventoryItem."""
        with transaction.atomic():
            inventory_item = self.item

            # Check if there's enough stock
            if inventory_item.stock_level < self.quantity:
                raise ValidationError(f"Insufficient stock for {inventory_item.type.name}. Available: {inventory_item.stock_level}, Requested: {self.quantity}")

            # Deduct the stock
            inventory_item.stock_level -= self.quantity
            inventory_item.save()

            # Proceed with saving the SaleEntry
            super().save(*args, **kwargs)


class PaymentHistory(models.Model):
    patient = models.ForeignKey("Patient", on_delete=models.SET_NULL, null=True, blank=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_vat = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_balance = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)  # Auto add timestamp

    def __str__(self):
        return f"Payment ID {self.id} - {self.total_balance} XAF"



from django.db import models
from django.contrib.auth import get_user_model
 
User = get_user_model()
 
 
class Order(models.Model):
    STATUS_CHOICES = [
        ("draft",       "Draft"),
        ("confirmed",   "Confirmed"),
        ("in_progress", "In Progress"),
        ("ready",       "Ready"),
        ("delivered",   "Delivered"),
        ("completed",   "Completed"),
        ("cancelled",   "Cancelled"),
    ]
 
    order_number = models.CharField(max_length=50, unique=True)
 
    # CASCADE on patient is aggressive — consider PROTECT so deleting a
    # patient doesn't silently wipe all their orders.
    patient = models.ForeignKey(
        "Patient",
        on_delete=models.PROTECT,           # changed from CASCADE → PROTECT
        related_name="patient_order"
    )
    prescription = models.ForeignKey(
        "MedicalReports",
        on_delete=models.PROTECT
    )
 
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )
 
    # Financial fields — calculated by OrderService.calculate_totals()
    subtotal      = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    discount      = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_amount  = models.DecimalField(max_digits=10, decimal_places=2, default=0)
 
    # FIX: These two fields now exist — required by PaymentService.update_order_balance()
    amount_paid   = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        help_text="Sum of all payments. Updated after each payment or refund."
    )
    balance       = models.DecimalField(
        max_digits=10, decimal_places=2, default=0,
        help_text="Remaining amount owed. Updated after each payment or refund."
    )
 
    created_by  = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="created_orders"
    )
    assigned_to = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="assigned_orders"
    )
 
    created_at            = models.DateTimeField(auto_now_add=True)
    expected_delivery_date = models.DateField(null=True, blank=True)
    delivered_at          = models.DateTimeField(null=True, blank=True)
 
    notes = models.TextField(blank=True)
 
    def __str__(self):
        return self.order_number








# class Order(models.Model):
#     STATUS_CHOICES = [
#         ("draft", "Draft"),
#         ("confirmed", "Confirmed"),
#         ("in_progress", "In Progress"),
#         ("ready", "Ready"),
#         ("delivered", "Delivered"),
#         ("completed", "Completed"),
#         ("cancelled", "Cancelled"),
#     ]

#     order_number = models.CharField(max_length=50, unique=True)

#     #patient = models.ForeignKey("Patient", on_delete=models.PROTECT)
#     patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='patient_order')
#     prescription = models.ForeignKey(MedicalReports, on_delete=models.PROTECT)

#     status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="draft")

#     subtotal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     created_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
#     assigned_to = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, related_name="assigned_orders")

#     created_at = models.DateTimeField(auto_now_add=True)
#     expected_delivery_date = models.DateField(null=True, blank=True)
#     delivered_at = models.DateTimeField(null=True, blank=True)

#     notes = models.TextField(blank=True)

#     def __str__(self):
#         return self.order_number
    

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(InventoryItem, on_delete=models.PROTECT)

    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    item_type = models.CharField(max_length=50)  # frame, lens, service


class Payment(models.Model):
    PAYMENT_METHODS = [
        ("cash", "Cash"),
        ("mobile_money", "Mobile Money"),
        ("card", "Card"),
    ]

    order = models.ForeignKey(Order, related_name="payments", on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)

    transaction_reference = models.CharField(max_length=100, blank=True)

    recorded_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)

    payment_date = models.DateTimeField(auto_now_add=True)
    
class OrderStatusHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="status_history")
    old_status = models.CharField(max_length=20)
    new_status = models.CharField(max_length=20)
    changed_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    changed_at = models.DateTimeField(auto_now_add=True)