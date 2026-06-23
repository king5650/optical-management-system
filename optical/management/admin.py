from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Patient, MedicalReport,ItemCategory, ItemType, InventoryItem, SaleEntry
class CustomUserAdmin(UserAdmin):
    # Define fields to display in the list view (in the Django admin)
    list_display = ('username', 'email', 'contact', 'role', 'date_joined', 'is_staff', 'is_active')
    # Define which fields are editable in the admin form
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal Info', {'fields': ('contact',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Role', {'fields': ('role',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'contact', 'role', 'is_staff', 'is_active'),
        }),
    )
    search_fields = ('username', 'email')
    ordering = ('date_joined',)

# Register the CustomUser model with the CustomUserAdmin
admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'contact', 'age', 'address', 'profession', 'gender', 'date_registered')  # Fields to display in the admin list view
    search_fields = ('name', 'email')  # Fields to allow search functionality
    
    
    
from django.contrib import admin
from .models import MedicalReport, Lens, Frame, OpticalAccessory,PurchaseDetail,Purchase,TransactionItem,Transaction, Sale, SoldItem
@admin.register(MedicalReport)
class MedicalReportAdmin(admin.ModelAdmin):
    list_display = ('patient','date_registered', 'pdf_file', 'date') 
    fieldsets = (
        ('Patient Information', {
            'fields': ('patient', 'age', 'sexe', 'profession',)
        }),
        ('Eye Tests (OD - Right Eye)', {
            'fields': ('sphere_od', 'cyl_od', 'axe_od', 'addition_od')
        }),
        ('Eye Tests (OG - Left Eye)', {
            'fields': ('sphere_og', 'cyl_og', 'axe_og', 'addition_og')
        }),
        ('Prescription Details', {
            'fields': (
                'ametropie', 
                'types_de_verre', 
                'teintes', 
                'foyers', 
                'port', 
                'indice'
            )
        }),
    )


@admin.register(Frame)
class FrameAdmin(admin.ModelAdmin):
    list_display = ('frame_type','unit_price', 'stock_level', 'date_added') 
    


from django.contrib import admin
from .models import Lens
# from .forms import LensAdminForm

from django.contrib import admin
from .models import Lens, PaymentHistory, MedicalReports, Refraction, PrescriptionDetail

@admin.register(Lens)
class LensAdmin(admin.ModelAdmin):
    list_display = ('lens_representation', 'unit_price', 'stock_level', 'quantity_sold', 'qtes', 'date_added')
    list_filter = ('lens_type',)
    search_fields = ('lens_type',)

    def lens_representation(self, obj):
        return str(obj)  # Uses the __str__ method
    lens_representation.short_description = "Lens"  # Custom column header in the admin table



@admin.register(OpticalAccessory)
class OpticalAccessoryAdmin(admin.ModelAdmin):
    list_display = ('name','unit_price', 'stock_level', 'date_added') 
    
    
    
@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('patient','total_without_tax', 'total_balance', 'created_at')

@admin.register( TransactionItem)
class TransactionItemAdmin(admin.ModelAdmin):
    list_display = ('transaction','item_type', 'quantity', 'unit_price', 'total_price')
    
@admin.register(Purchase)
class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('patient_name','total_amount', 'vat_total', 'date_created')
    
@admin.register(PurchaseDetail)
class PurchaseDetailyAdmin(admin.ModelAdmin):
    list_display = ('purchase','unit_price', 'quantity', 'total')
    
@admin.register(Sale)
class SaleyAdmin(admin.ModelAdmin):
    list_display = ('buyer_name','total_amount', 'total_without_tax', 'date')
    
@admin.register(SoldItem)
class SoldItemAdmin(admin.ModelAdmin):
    list_display = ('sale','unit_price', 'total_price', 'quantity')
    

    
@admin.register(SaleEntry)
class SaleEntryAdmin(admin.ModelAdmin):
    list_display = ('item', 'quantity', 'price', 'date')
    
    
@admin.register(ItemType)
class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ('category','name')
    
@admin.register(InventoryItem)
class InventoryItemAdmin(admin.ModelAdmin):
    list_display = ('category','type', 'unit_price', 'stock_level', 'date_added')
    

@admin.register(PaymentHistory)
class PaymentHistory(admin.ModelAdmin):
    list_display = ('patient','payment_date', 'total_balance', 'total_vat', 'total_amount')
    
@admin.register(MedicalReports)
class MedicalReports(admin.ModelAdmin):
    list_display = ('patient', 'reference_id', 'pdf_file', 'age_at_report', 'profession_at_report', 'date')
@admin.register(Refraction)
class Refraction(admin.ModelAdmin):
    list_display = ('sphere_od','cyl_od', 'axe_od', 'addition_od',  'sphere_og', 'cyl_og', 'axe_og', 'addition_og')
@admin.register(PrescriptionDetail)
class PrescriptionDetail(admin.ModelAdmin):
    list_display = ('ametropie','types_de_verre', 'teintes',  'foyers', 'port', 'indice')
