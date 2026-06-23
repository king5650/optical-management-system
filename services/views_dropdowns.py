"""
views_dropdowns.py  —  NEW FILE

Provides lightweight read-only endpoints that power the three cascaded
dropdowns in the Create Order form:

  1.  GET /api/categories/
        → All ItemCategory rows  (already exists — no change needed)

  2.  GET /api/item-types/by-category/<category_id>/    ← NEW
        → All ItemType rows belonging to that category

  3.  GET /api/inventory/by-type/<type_id>/             ← NEW
        → All InventoryItem rows of that ItemType (usually 1 or 2)
        → Includes unit_price and stock_level so the form can
          auto-fill the price and warn about low stock

  4.  GET /api/prescriptions/by-patient/<patient_id>/   ← NEW
        → All MedicalReports for that patient, newest first
        → Used to populate the prescription dropdown after
          a patient is selected

WHY A SEPARATE FILE?
  These views are pure lookups (no business logic, no service calls).
  Mixing them into views_orders.py or the giant views.py would make
  those files even harder to navigate.

HOW TO WIRE THESE IN:
  In urls.py add:

    from .views_dropdowns import (
        item_types_by_category,
        inventory_items_by_type,
        prescriptions_by_patient,
    )

    path("item-types/by-category/<int:category_id>/", item_types_by_category, name="item_types_by_category"),
    path("inventory/by-type/<int:type_id>/",          inventory_items_by_type,  name="inventory_items_by_type"),
    path("prescriptions/by-patient/<int:patient_id>/", prescriptions_by_patient, name="prescriptions_by_patient"),
"""

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from management.models import ItemType, InventoryItem, MedicalReports


# ─────────────────────────────────────────────────────────────────────────────
# 1. Item types filtered by category
# ─────────────────────────────────────────────────────────────────────────────

def item_types_by_category(request, category_id):
    """
    GET /api/item-types/by-category/<category_id>/

    Returns all ItemType rows that belong to the given ItemCategory.

    WHEN CALLED:
      The user selects a category (e.g. "Lenses") in the Create Order form.
      This endpoint immediately fires and populates the "Item type" dropdown
      with only the types that live inside that category.

    RESPONSE EXAMPLE:
      {
        "item_types": [
          {"id": 3, "name": "VIP"},
          {"id": 4, "name": "Simple Vision"},
          {"id": 5, "name": "Progressif"}
        ]
      }
    """
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    types = (
        ItemType.objects
        .filter(category_id=category_id)
        .order_by("name")
        .values("id", "name")
    )

    return JsonResponse({"item_types": list(types)})


# ─────────────────────────────────────────────────────────────────────────────
# 2. Inventory items filtered by item type
# ─────────────────────────────────────────────────────────────────────────────

def inventory_items_by_type(request, type_id):
    """
    GET /api/inventory/by-type/<type_id>/

    Returns all InventoryItem rows whose 'type' FK matches type_id.

    WHY MULTIPLE ITEMS PER TYPE?
      The same ItemType (e.g. "VIP lens") might have multiple InventoryItem
      rows at different price points or from different stock batches.
      The form shows them all so the user can pick the right one.

    WHEN CALLED:
      After the user picks an item type from the second dropdown.
      The third dropdown (product) is populated with these results,
      and selecting one auto-fills the unit price field.

    RESPONSE EXAMPLE:
      {
        "items": [
          {
            "id": 12,
            "type_id": 4,
            "type_name": "VIP",
            "category_name": "Lenses",
            "unit_price": "45000.00",
            "stock_level": 8,
            "is_low_stock": false
          }
        ]
      }
    """
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    items = (
        InventoryItem.objects
        .filter(type_id=type_id)
        .select_related("type", "category")
        .order_by("unit_price")
    )

    data = []
    for item in items:
        data.append({
            "id": item.id,
            "type_id": item.type_id,
            "type_name": item.type.name if item.type else "",
            "category_name": item.category.name if item.category else "",
            "unit_price": str(item.unit_price),
            "stock_level": item.stock_level,
            "is_low_stock": item.is_low_stock(),
        })

    return JsonResponse({"items": data})


# ─────────────────────────────────────────────────────────────────────────────
# 3. Prescriptions (MedicalReports) filtered by patient
# ─────────────────────────────────────────────────────────────────────────────

def prescriptions_by_patient(request, patient_id):
    """
    GET /api/prescriptions/by-patient/<patient_id>/

    Returns all MedicalReports for the given patient, newest first.

    WHEN CALLED:
      The user selects a patient in the Create Order form.
      This endpoint fires immediately and populates the "Prescription"
      dropdown so the user can pick which visit/report this order
      is linked to.

    WHY IS THIS NEEDED?
      Without it, staff would have to type a raw prescription ID number,
      which they don't know by heart. This makes the form usable.

    RESPONSE EXAMPLE:
      {
        "prescriptions": [
          {"id": 7,  "reference_id": "REF-2025-007", "date": "2025-11-03"},
          {"id": 3,  "reference_id": "REF-2025-003", "date": "2025-08-15"}
        ]
      }

    NOTE:
      If a patient has no reports yet, the list is empty and the form
      should show a warning: "No prescriptions found for this patient."
    """
    if request.method != "GET":
        return JsonResponse({"error": "Method not allowed"}, status=405)

    reports = (
        MedicalReports.objects
        .filter(patient_id=patient_id)
        .order_by("-date")
        .values("id", "reference_id", "date")
    )

    prescriptions = []
    for r in reports:
        prescriptions.append({
            "id": r["id"],
            "reference_id": r["reference_id"] or f"Report #{r['id']}",
            "date": str(r["date"]),
        })

    return JsonResponse({"prescriptions": prescriptions})
