# from decimal import Decimal
# from django.db import transaction

# from optical.management.models import Order, OrderItem, Product


# class OrderService:
#     pass

# @staticmethod
# @transaction.atomic
# def create_order(validated_data, user):
#     items_data = validated_data.pop("items")

#     # Create order
#     order = Order.objects.create(
#         created_by=user,
#         **validated_data
#     )

#     # Create items
#     for item in items_data:
#         product = item["product"]

#         OrderItem.objects.create(
#             order=order,
#             product=product,
#             product_name=product.name,  # snapshot
#             quantity=item["quantity"],
#             unit_price=item["unit_price"],
#             total_price=Decimal(item["quantity"]) * Decimal(item["unit_price"]),
#             item_type=item.get("item_type", "product")
#         )

#     # Calculate totals
#     OrderService.calculate_totals(order)

#     return order


# @staticmethod
# def calculate_totals(order):
#     items = order.items.all()

#     subtotal = sum(item.total_price for item in items)
#     subtotal = Decimal(subtotal)

#     discount = order.discount or Decimal("0.00")

#     total = subtotal - discount

#     order.subtotal = subtotal
#     order.total_amount = total

#     order.save()
    
# @staticmethod
# @transaction.atomic
# def update_order(order, validated_data):
#     # Only allow update in draft state
#     if order.status != "draft":
#         raise ValueError("Only draft orders can be updated")

#     # Update basic fields
#     for attr, value in validated_data.items():
#         if attr != "items":
#             setattr(order, attr, value)

#     order.save()

#     # Update items if provided
#     if "items" in validated_data:
#         order.items.all().delete()

#         items_data = validated_data["items"]

#         for item in items_data:
#             product = item["product"]

#             OrderItem.objects.create(
#                 order=order,
#                 product=product,
#                 product_name=product.name,
#                 quantity=item["quantity"],
#                 unit_price=item["unit_price"],
#                 total_price=Decimal(item["quantity"]) * Decimal(item["unit_price"]),
#                 item_type=item.get("item_type", "product")
#             )

#     # Recalculate totals
#     OrderService.calculate_totals(order)

#     return order

# @staticmethod
# def get_order_summary(order):
#     total_paid = sum(p.amount for p in order.payments.all())
#     total_paid = Decimal(total_paid)

#     balance = order.total_amount - total_paid

#     if total_paid == 0:
#         payment_status = "unpaid"
#     elif total_paid < order.total_amount:
#         payment_status = "partial"
#     else:
#         payment_status = "paid"

#     return {
#         "order_id": order.id,
#         "total_amount": order.total_amount,
#         "paid": total_paid,
#         "balance": balance,
#         "payment_status": payment_status,
#         "status": order.status
#     }
    
# @staticmethod
# def validate_items(items_data):
#     if not items_data:
#         raise ValueError("Order must contain at least one item")

#     for item in items_data:
#         if item["quantity"] <= 0:
#             raise ValueError("Quantity must be greater than zero")
       
 



from decimal import Decimal
from django.db import transaction
from django.utils import timezone
from management.models import Order, OrderItem

# class OrderService:
#     """
#     Handles all business logic related to creating, updating,
#     and summarising orders. All methods are static — no instance needed.

#     FIX 2 (CRITICAL): Every method is now INDENTED inside the class.
#     Previously all methods were outside the class body (after 'pass'),
#     making them plain module-level functions. Calling
#     OrderService.create_order() would have raised AttributeError. 
#     """

#     @staticmethod
#     @transaction.atomic
#     def create_order(validated_data, user):
#         """
#         Creates an order and its items inside a single database transaction.
#         If anything fails, the whole operation is rolled back — no partial data.
#         """
#         items_data = validated_data.pop("items")

#         # FIX 3: validate_items is now called before anything is saved.
#         # Previously this method existed but was never called, so empty
#         # orders or zero-quantity items would slip through silently.
#         OrderService.validate_items(items_data)

#         # Create the order header
#         order = Order.objects.create(
#             created_by=user,
#             **validated_data
#         )

#         # Create each line item, snapshotting the product name at sale time
#         # so renaming a product later does not corrupt historical orders.
#         for item in items_data:
#             product = item["product"]

#             OrderItem.objects.create(
#                 order=order,
#                 product=product,
#                 product_name=product.type.name if product.type else str(product),  # snapshot
#                 quantity=item["quantity"],
#                 unit_price=item["unit_price"],
#                 total_price=Decimal(str(item["quantity"])) * Decimal(str(item["unit_price"])),
#                 item_type=item.get("item_type", "product")
#             )

#         # Recalculate subtotal, discount and total on the saved order
#         OrderService.calculate_totals(order)

#         return order

#     @staticmethod
#     def calculate_totals(order):
#         """
#         Sums all line items and applies the order-level discount.
#         Always called after items are created or updated so the order
#         header stays in sync with the line items.
#         """
#         items = order.items.all()

#         # Use str() before Decimal to avoid floating-point rounding issues
#         subtotal = sum(Decimal(str(item.total_price)) for item in items)

#         discount = Decimal(str(order.discount)) if order.discount else Decimal("0.00")

#         total = subtotal - discount

#         order.subtotal = subtotal
#         order.total_amount = total

#         order.save()

#     @staticmethod
#     @transaction.atomic
#     def update_order(order, validated_data):
#         """
#         Replaces all line items and recalculates totals.
#         Only allowed while the order is still in 'draft' status —
#         confirmed or in-progress orders cannot be edited.
#         """
#         if order.status != "draft":
#             raise ValueError("Only draft orders can be updated")

#         # Update scalar fields (skip 'items' — handled separately below)
#         for attr, value in validated_data.items():
#             if attr != "items":
#                 setattr(order, attr, value)

#         order.save()

#         # If new items were provided, wipe the old ones and recreate
#         if "items" in validated_data:
#             order.items.all().delete()

#             for item in validated_data["items"]:
#                 product = item["product"]

#                 OrderItem.objects.create(
#                     order=order,
#                     product=product,
#                     product_name=product.type.name if product.type else str(product),
#                     quantity=item["quantity"],
#                     unit_price=item["unit_price"],
#                     total_price=Decimal(str(item["quantity"])) * Decimal(str(item["unit_price"])),
#                     item_type=item.get("item_type", "product")
#                 )

#         OrderService.calculate_totals(order)

#         return order

#     @staticmethod
#     def get_order_summary(order):
#         """
#         Returns a dict with the complete financial picture of an order:
#         total amount, how much has been paid, the remaining balance,
#         and a human-readable payment status.
#         """
#         total_paid = sum(
#             Decimal(str(p.amount)) for p in order.payments.all()
#         )

#         balance = order.total_amount - total_paid

#         if total_paid == 0:
#             payment_status = "unpaid"
#         elif total_paid < order.total_amount:
#             payment_status = "partial"
#         else:
#             payment_status = "paid"

#         return {
#             "order_id": order.id,
#             "order_number": order.order_number,
#             "status": order.status,
#             "total_amount": str(order.total_amount),
#             "paid": str(total_paid),
#             "balance": str(balance),
#             "payment_status": payment_status,
#         }

#     @staticmethod
#     def validate_items(items_data):
#         """
#         Raises ValueError if the item list is empty or contains invalid quantities.
#         Called at the start of create_order so bad data never touches the database.
#         """
#         if not items_data:
#             raise ValueError("Order must contain at least one item")

#         for item in items_data:
#             if item["quantity"] <= 0:
#                 raise ValueError("Each item quantity must be greater than zero")

#             if Decimal(str(item["unit_price"])) <= 0:
#                 raise ValueError("Each item unit price must be greater than zero")
class OrderService:
 
    # ──────────────────────────────────────────────────────────────────────
    # ORDER NUMBER AUTO-GENERATION
    # ──────────────────────────────────────────────────────────────────────
 
    @staticmethod
    def generate_order_number():
        """
        Builds a unique order number in the format  ORD-YYYY-NNNN.
 
        HOW IT WORKS:
          1. Get the current year.
          2. Find the last order whose number starts with "ORD-{year}-".
          3. Parse its trailing sequence number and add 1.
          4. Zero-pad to 4 digits so numbers sort correctly as strings.
 
        Example sequence:  ORD-2025-0001, ORD-2025-0002, … ORD-2025-0999
 
        WHY NOT USE auto-increment?
          Because the visible order number must embed the year so staff
          can instantly know when an order was created from the number alone.
          Django's auto PK is internal; this is the human-readable reference.
 
        RACE CONDITIONS:
          In a single-location optical cabinet (low concurrency) this is safe.
          For multi-location high-concurrency use, wrap the whole create_order()
          call in select_for_update() on a lock row, or use a database sequence.
        """
        year = timezone.now().year
        prefix = f"ORD-{year}-"
 
        last_order = (
            Order.objects
            .filter(order_number__startswith=prefix)
            .order_by("-order_number")
            .first()
        )
 
        if last_order:
            try:
                # "ORD-2025-0042" → split on "-" → ["ORD","2025","0042"] → last part
                last_seq = int(last_order.order_number.split("-")[-1])
            except (ValueError, IndexError):
                last_seq = 0
        else:
            last_seq = 0
 
        return f"{prefix}{str(last_seq + 1).zfill(4)}"
 
    # ──────────────────────────────────────────────────────────────────────
    # CREATE ORDER
    # ──────────────────────────────────────────────────────────────────────
 
    @staticmethod
    @transaction.atomic
    def create_order(validated_data, user):
        """
        Creates a complete order with line items inside one transaction.
 
        CHANGE FROM PREVIOUS VERSION:
          order_number is now generated here, not accepted from the frontend.
          This prevents duplicates, typos, and manual-numbering inconsistency.
          The frontend no longer sends an order_number field.
 
        STEPS (all atomic — any failure rolls back everything):
          1. Pop items from validated_data (they're handled separately).
          2. Validate items (raises ValueError on bad data → 400 response).
          3. Generate a unique order number.
          4. Create the Order header row.
          5. Create one OrderItem row per item.
          6. Calculate and save totals.
        """
        items_data = validated_data.pop("items")
 
        OrderService.validate_items(items_data)
 
        # Auto-generate — frontend does NOT send this field
        order_number = OrderService.generate_order_number()
 
        order = Order.objects.create(
            order_number=order_number,
            created_by=user,
            **validated_data
        )
 
        for item in items_data:
            product = item["product"]      # InventoryItem instance
 
            # Snapshot the product type name at order time.
            # If the ItemType is renamed later, the order still shows
            # what the item was called when it was sold.
            product_name = (
                product.type.name if product.type else f"Item #{product.id}"
            )
 
            OrderItem.objects.create(
                order=order,
                product=product,
                product_name=product_name,
                quantity=item["quantity"],
                unit_price=item["unit_price"],
                total_price=(
                    Decimal(str(item["quantity"])) *
                    Decimal(str(item["unit_price"]))
                ),
                item_type=item.get("item_type", "product")
            )
 
        OrderService.calculate_totals(order)
        return order
 
    # ──────────────────────────────────────────────────────────────────────
    # CALCULATE TOTALS
    # ──────────────────────────────────────────────────────────────────────
 
    @staticmethod
    def calculate_totals(order):
        """
        Sums all line item totals, applies the order-level discount,
        and saves subtotal + total_amount to the Order row.
 
        Always called after items are created or replaced so the header
        row is never stale.
 
        Uses Decimal(str(...)) to avoid floating-point rounding errors
        (e.g. 0.1 + 0.2 = 0.30000000000004 in plain float arithmetic).
        """
        items = order.items.all()
        subtotal = sum(Decimal(str(item.total_price)) for item in items)
        discount = Decimal(str(order.discount)) if order.discount else Decimal("0.00")
        total = subtotal - discount
 
        order.subtotal = subtotal
        order.total_amount = total
        order.save()
 
    # ──────────────────────────────────────────────────────────────────────
    # UPDATE ORDER
    # ──────────────────────────────────────────────────────────────────────
 
    @staticmethod
    @transaction.atomic
    def update_order(order, validated_data):
        """
        Replaces items and recalculates totals.
        Only allowed while status is 'draft'.
        order_number is never changed on update.
        """
        if order.status != "draft":
            raise ValueError("Only draft orders can be updated")
 
        for attr, value in validated_data.items():
            if attr != "items":
                setattr(order, attr, value)
        order.save()
 
        if "items" in validated_data:
            order.items.all().delete()
            for item in validated_data["items"]:
                product = item["product"]
                product_name = (
                    product.type.name if product.type else f"Item #{product.id}"
                )
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    product_name=product_name,
                    quantity=item["quantity"],
                    unit_price=item["unit_price"],
                    total_price=(
                        Decimal(str(item["quantity"])) *
                        Decimal(str(item["unit_price"]))
                    ),
                    item_type=item.get("item_type", "product")
                )
 
        OrderService.calculate_totals(order)
        return order
 
    # ──────────────────────────────────────────────────────────────────────
    # GET ORDER SUMMARY
    # ──────────────────────────────────────────────────────────────────────
 
    @staticmethod
    def get_order_summary(order):
        """
        Returns the complete financial snapshot for an order as a plain dict.
        Used by the order_summary view and the frontend summary panel.
        """
        total_paid = sum(
            Decimal(str(p.amount)) for p in order.payments.all()
        )
        balance = order.total_amount - total_paid
 
        if total_paid <= 0:
            payment_status = "unpaid"
        elif total_paid < order.total_amount:
            payment_status = "partial"
        else:
            payment_status = "paid"
 
        return {
            "order_id": order.id,
            "order_number": order.order_number,
            "status": order.status,
            "total_amount": str(order.total_amount),
            "paid": str(total_paid),
            "balance": str(balance),
            "payment_status": payment_status,
        }
 
    # ──────────────────────────────────────────────────────────────────────
    # VALIDATE ITEMS
    # ──────────────────────────────────────────────────────────────────────
 
    @staticmethod
    def validate_items(items_data):
        """
        Called before any DB write so bad data never reaches the database.
        Raises ValueError (caught by the view → 400 response) on:
          - Empty items list
          - Any item with quantity ≤ 0
          - Any item with unit_price ≤ 0
        """
        if not items_data:
            raise ValueError("Order must contain at least one item")
 
        for item in items_data:
            if item["quantity"] <= 0:
                raise ValueError("Each item quantity must be greater than zero")
            if Decimal(str(item["unit_price"])) <= 0:
                raise ValueError("Each item unit price must be greater than zero")
