from django.urls import path
from . import views
from .views import (
    ScheduleMessageView,
    ListScheduledMessagesView,
    CancelScheduledMessageView,
    UpdateRecipientStatusView,
)
 
# Import the new order/payment views from the separate file
from .views import (
    order_list_create,
    order_detail,
    order_summary,
    change_order_status,
    cancel_order,
    order_status_history,
    add_payment,
    payments_by_order,
    refund_payment,
)
from services.views_dropdowns import (
    item_types_by_category,
    inventory_items_by_type,
    prescriptions_by_patient,
)


urlpatterns = [
    

    path('dashboard-counts/', views.dashboard_counts, name='dashboard_counts'),

    path('login/', views.login_view, name='login'),
    path('patients/add/', views.add_patient, name='add_patient'),
    path('patients/update/<int:patient_id>/', views.update_patient, name='update_patient'),
    path('patients/delete/<int:patient_id>/', views.delete_patient, name='delete_patient'),
    path('patients/list/', views.get_patients, name='get_patients'),
    path('patients/search/', views.search_patients, name='search_patients'),
    path('patients/search/', views.search_patients, name='search_patients'),
    path('patients/list/', views.list_patients, name='list_patients'),
    # medical reports urls
    path('medical-reports/create/', views.create_medical_report, name='create_medical_report'),
    path('medical-reports/next-reference/', views.get_next_reference_id, name='get_next_reference_id'),
    #path('medical-reports/view/<int:report_id>/', views.view_medical_report, name='view_medical_report'),
    # path('medical-reports/view/<int:report_id>/', views.view_medical_report, name='view_medical_report'),
    # path('medical-reports/view/<int:report_id>/', views.get_report_details, name='get_report_details'),
    # path('medical-reports/latest/<int:patient_id>/', views.get_latest_report_for_patient, name='get_latest_report'),
    path('medical-reports/view/<int:report_id>/', views.view_medical_report, name='view_medical_report'),
    path("medical-reports/next-reference/", views.get_next_reference_id),
    path("medical-reports/view-by-ref/<str:reference_id>/", views.get_medical_report_by_reference),
    path('medical-reports/list/<int:patient_id>/', views.list_medical_reports, name='list_medical_reports'),
    
    #whatsapp automation

    path('messages/schedule/', ScheduleMessageView.as_view(), name='schedule-message'),
    path('messages/', ListScheduledMessagesView.as_view(), name='list-messages'),
    path('messages/<int:pk>/cancel/', CancelScheduledMessageView.as_view(), name='cancel-message'),
    path('recipients/<int:pk>/update/', UpdateRecipientStatusView.as_view(), name='update-recipient'),
    path('messages/create/', views.create_scheduled_message, name='create_scheduled_message'),
    
    # path('backup-db', views.backup_database, name='backup-db'),
    path("backup/", views.backup_database, name="backup"),
    path("restore/", views.restore_database, name="restore"),
    
    
    
    path('medical-reports/save/', views.save_medical_report, name='save_medical_report'),
    path('medical-reports/search/<int:patient_id>/', views.search_medical_report, name='search_medical_report'),
    # path('medical-reports/list/<int:patient_id>/', views.list_medical_reports, name='list_medical_reports'),
    path('medical-reports/delete/<int:report_id>/', views.delete_medical_report, name='delete_medical_report'),
    # path('medical-reports/view/<int:report_id>/', views.view_medical_report, name='view_medical_report'),
    
    path('inventory/add/', views.add_item, name='add_item'),
    # path('inventory/add/', views.add_item, name='add_item'),
    path("inventory/frames/list/", views.list_frames, name="list_frames"),
    path("inventory/lenses/list/", views.list_lenses, name="list_lenses"),
    path("inventory/accessories/list/", views.list_accessories, name="list_accessories"),
    
    path("inventory/<str:item_type>/delete/<int:item_id>/", views.delete_item, name="delete_item"),
    
    path("inventory/update/<int:item_id>/", views.update_item, name="update_item"),

    path('inventory/<str:item_type>/totals/', views.inventory_totals, name='inventory_totals'),
    
    path('inventory/filter/', views.filter_monthly_data, name='filter_monthly_data'),
    path('inventory/years/', views.get_years, name='get_years'),  # To fetch available years
    
    # categories section
    path('categories/', views.fetch_categories, name='fetch_categories'),  # Fetch all categories
    path('categories/add-category/', views.add_category, name='add_category'),       # Add a category
    path('categories/delete-category/<int:category_id>/', views.delete_category, name='delete_category'),  # Delete a category
    path('categories/update-category/<int:category_id>/', views.update_category, name='update_category'),  # Update a category

    # item_type section
    path('item-types/', views.fetch_item_types, name='fetch_item_types'),
    path('item-types/add/', views.add_item_type, name='add_item_type'),
    path('item-types/delete/<int:item_type_id>/', views.delete_item_type, name='delete_item_type'),
    path('item-types/update/<int:item_type_id>/', views.update_item_type, name='update_item_type'),
    

        #inventory code
    path('add-item/', views.add_item, name='add_item'),
    path('fetch-items/', views.fetch_items, name='fetch_items'),
    # path('inventory/add/', views.add_inventory_item, name='add_inventory_item'),
    # path('inventory/update/<int:item_id>/', views.update_inventory_item, name='update_inventory_item'),
    path('delete-item/<int:item_id>/', views.delete_item, name='delete_item'),
    path('update-item/<int:item_id>/', views.update_item, name='update_item'),
    path('category-stock-summary/', views.get_category_stock_summary, name='get_category_stock_summary'),
    
    path('filter-report/', views.filter_report, name='filter_report'),
    path('get-totals-by-type/', views.get_totals_by_type, name='get_totals_by_type'),
    path('export-report/', views.export_report, name='export_report'),
    
    # sales section
    path('get-unit-price/', views.get_unit_price, name='get_unit_price'),
    path('fetch-patients/', views.fetch_patients, name='fetch_patients'),
    path("search-patient/", views.search_patient, name="search_patient"),
    path('process-sale/', views.process_sale_transaction, name='process_sale_transaction'),
    path('update-item-price/', views.update_item_price, name='update_item_price'),
    path('check-low-stock/"', views.check_low_stock, name='check-low-stock'),
    path('payment-history/', views.fetch_payment_history, name='fetch_payment_history'),
    path('get-stock-level/', views.fetch_payment_history, name='fetch_payment_history'),
    path('inventory-report/', views.inventory_report, name='inventory_report'),

    # path('auth/fetch-report/', views.fetch_report, name='fetch_report'), 
    # path('export-report/', views.export_report, name='export_report'),
    # path('years-months/', views.get_years_and_months, name='get_years_and_months'),
    # path('sale-entry-types/', views.get_sale_entry_types, name='get_sale_entry_types'),
    # path('filter-inventory-entries/', views.filter_inventory_entries, name='filter_inventory_entries'),
    # path('filter-sales-entries/', views.filter_sales_entries, name='filter_sales_entries'),

    
    path('inventory/items/', views.fetch_inventory_items, name='fetch_inventory_items'),
    path('inventory/add/', views.add_inventory_item, name='add_inventory_item'),
    path('auth/item-types/', views.get_stock_level, name='get_stock_level'),
    
    # List all orders or create a new order
    path("orders/",                              order_list_create,    name="order_list_create"),
 
    # Get or partially update a specific order
    path("orders/<int:pk>/",                     order_detail,         name="order_detail"),
 
    # Financial snapshot: total, paid, balance, payment status
    path("orders/<int:pk>/summary/",             order_summary,        name="order_summary"),
 
    # Move the order to the next status (validated transition)
    path("orders/<int:pk>/change-status/",       change_order_status,  name="change_order_status"),
 
    # Cancel an order (dedicated endpoint — handles any non-terminal status)
    path("orders/<int:pk>/cancel/",              cancel_order,         name="cancel_order"),
 
    # Full audit log: who changed status, when, from/to what
    path("orders/<int:pk>/history/",             order_status_history, name="order_status_history"),
 
    # ─────────────────────────────────────────────────────────────────────
    # FIX 2: PAYMENT ENDPOINTS (completely new — were missing before)
    # ─────────────────────────────────────────────────────────────────────
 
    # Record a new payment
    path("payments/",                            add_payment,          name="add_payment"),
 
    # List all payments for a specific order
    path("payments/by-order/<int:order_id>/",    payments_by_order,    name="payments_by_order"),
 
    # Record a refund against an order
    path("payments/refund/<int:order_id>/",      refund_payment,       name="refund_payment"),
    
    path(
        "item-types/by-category/<int:category_id>/",
        item_types_by_category,
        name="item_types_by_category",
    ),
    path(
        "inventory/by-type/<int:type_id>/",
        inventory_items_by_type,
        name="inventory_items_by_type",
    ),
    path(
        "prescriptions/by-patient/<int:patient_id>/",
        prescriptions_by_patient,
        name="prescriptions_by_patient",
    ),

    
    
    
    
    # path('inventory/', views.fetch_inventory_items, name='fetch_inventory_items'),
    # path('item-types/<int:category_id>/', views.fetch_item_types_by_category, name='fetch_item_types_by_category'),
    
    
    # # Patient-related URLs
    # path('patients/', views.get_patients, name='get_patients'),  # Fetch all patients
    # # path('patients/<str:name>/details/', views.get_patient_details, name='get_patient_details'),  # Fetch patient details
    # path('patients/<int:patient_id>/details/', views.patient_details, name='patient_details'),

    # # Item-related URLs
    # path('inventory/items/<str:item_type>/types/', views.get_item_types, name='get_item_types'),  # Fetch item types (Frame, Lens, or Accessories)
    # path('inventory/items/<str:item_type>/<str:subtype_or_name>/price/', views.get_item_price, name='get_item_price'),  # Fetch price for an item

    # # Transaction-related URLs
    # # path('transactions/validate/', views.validate_transaction, name='validate_transaction'),  # Save transaction data
    # path("purchase/add/", views.validate_purchase, name="validate_purchase"),


    # path("sales/add/", views.add_sale, name="add_sale"),
    # path("sales/filter/", views.filter_sales, name="filter_sales"),
    # path("inventory/fetch-patient-details/", views.fetch_patient_details, name="fetch_patient_details"),
    # path("inventory/fetch-item-price/", views.fetch_item_price, name="fetch_item_price"),
    # path("inventory/submit-purchase/", views.submit_purchase, name="submit_purchase"),
    # path("inventory/<str:item_category>/types/", views.get_item_types),
    # path("inventory/<str:item_category>/price/", views.get_unit_price),


    # path("inventory/categories/", views.get_categories),
    # path("inventory/<str:item_category>/price/", views.get_unit_price),
    
    # path('inventory/monthly-summary/', views.monthly_summary, name='monthly_summary'),
    # path('auth/inventory/monthly/', views.get_monthly_entries_sales, name='monthly_entries_sales'),
    # path('inventory/monthly-entries-sales/', views.monthly_entries_sales, name='monthly_entries_sales'),
    # # Add routes
    # path("frames/add/", views.add_frame, name="add_frame"),/inventory/{selected_item}/list/
    # path("lenses/add/", views.add_lens, name="add_lens"),
    # path("accessories/add/", views.add_accessory, name="add_accessory"),

    # # Update routes
    # path("frames/update/<int:item_id>/", views.update_item, {"model": "frame"}, name="update_frame"),
    # path("lenses/update/<int:item_id>/", views.update_item, {"model": "lens"}, name="update_lens"),
    # path("accessories/update/<int:item_id>/", views.update_item, {"model": "accessory"}, name="update_accessory"),

    # # Delete routes
    # path("frames/delete/<int:item_id>/", views.delete_item, {"model": "frame"}, name="delete_frame"),
    # path("lenses/delete/<int:item_id>/", views.delete_item, {"model": "lens"}, name="delete_lens"),
    # path("accessories/delete/<int:item_id>/", views.delete_item, {"model": "accessory"}, name="delete_accessory"),

    # # List routes
    # path("frames/", views.list_items, {"model": "frame"}, name="list_frames"),
    # path("lenses/", views.list_items, {"model": "lens"}, name="list_lenses"),
    # path("accessories/", views.list_items, {"model": "accessory"}, name="list_accessories"),


    #  # List all items for a given type
    # path('inventory/<str:item_type>/list/', views.list_items, name='list_items'),

    # # Add a new item
    # path('inventory/<str:item_type>/add/', views.add_item, name='add_item'),

    # # Update an item by ID
    # path('inventory/<str:item_type>/update/<int:item_id>/', views.update_item, name='update_item'),

    # # Delete an item by ID
    # path('inventory/<str:item_type>/delete/<int:item_id>/', views.delete_item, name='delete_item'),


    # path('medical-reports/delete/<int:report_id>/', views.delete_medical_report, name='delete_medical_report'),


    # path('report/<int:report_id>/save-pdf/', views.save_pdf, name='save_pdf'),delete_medical_report
    # path('report/<int:report_id>/print/', views.print_pdf, name='print_pdf'),
    # path('report/<int:report_id>/download/', views.download_pdf, name='download_pdf'),
    # path('auth/medical-reports/<int:patient_id>/', views.get_medical_report, name='get_medical_report'),
    # path('auth/medical-reports/save/', views.save_medical_report, name='save_medical_report'),

    # path('medical-reports/<int:patient_id>/', views.get_medical_report, name='get_medical_report'),
    # path('medical-reports/save/', views.save_medical_report, name='save_medical_report'),
    #     path('medical_reports/<int:patient_id>/', views.list_medical_reports, name='list_medical_reports'),
    # path('medical_reports/add/', views.create_medical_report, name='create_medical_report'),
    # path('medical_reports/<int:report_id>/detail/', views.get_medical_report, name='get_medical_report'),
]
