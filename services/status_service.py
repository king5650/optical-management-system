# from django.db import transaction
# from optical.management.models import OrderStatusHistory

# class OrderStatusService:
#     pass

# VALID_TRANSITIONS = {
#     "draft": ["confirmed", "cancelled"],
#     "confirmed": ["in_progress", "cancelled"],
#     "in_progress": ["ready"],
#     "ready": ["delivered"],
#     "delivered": ["completed"],
#     "completed": [],
#     "cancelled": []
# }

# @staticmethod
# @transaction.atomic
# def change_status(order, new_status, user):
#     current_status = order.status

#     # Validate transition
#     allowed = OrderStatusService.VALID_TRANSITIONS.get(current_status, [])

#     if new_status not in allowed:
#         raise ValueError(f"Cannot change status from '{current_status}' to '{new_status}'")

#     # Log history
#     OrderStatusHistory.objects.create(
#         order=order,
#         old_status=current_status,
#         new_status=new_status,
#         changed_by=user
#     )

#     # Apply change
#     order.status = new_status

#     # Optional side effects
#     if new_status == "delivered":
#         from django.utils import timezone
#         order.delivered_at = timezone.now()

#     order.save()

#     return order


# @staticmethod
# @transaction.atomic
# def cancel_order(order, user):
#     if order.status in ["completed", "cancelled"]:
#         raise ValueError("Cannot cancel this order")

#     OrderStatusHistory.objects.create(
#         order=order,
#         old_status=order.status,
#         new_status="cancelled",
#         changed_by=user
#     )

#     order.status = "cancelled"
#     order.save()

#     return order


# @staticmethod
# def validate_transition(current_status, new_status):
#     allowed = OrderStatusService.VALID_TRANSITIONS.get(current_status, [])

#     if new_status not in allowed:
#         raise ValueError(f"Invalid transition from {current_status} to {new_status}")
    
    



from django.db import transaction
from django.utils import timezone

from management.models import OrderStatusHistory


class OrderStatusService:
    """
    Controls how an order moves through its lifecycle.
    Enforces valid transitions, logs every change, and applies
    side-effects (e.g. recording the delivery timestamp).

    FIX 1 (CRITICAL): All methods and the VALID_TRANSITIONS dict are now
    INDENTED inside the class body. Previously they sat at module level
    after 'pass', so 'OrderStatusService.change_status()' would raise
    AttributeError and 'OrderStatusService.VALID_TRANSITIONS' would raise
    AttributeError as well.

    WHY CONTROL TRANSITIONS?
    Without this, a frontend bug or a bad API call could jump an order
    from 'draft' straight to 'delivered', skipping every workflow step.
    The transition map is the single source of truth for your business rules.
    """

    # FIX 2: VALID_TRANSITIONS is now INSIDE the class.
    # Each key is a current status; the list is the only statuses it may move to.
    VALID_TRANSITIONS = {
        "draft":       ["confirmed", "cancelled"],
        "confirmed":   ["in_progress", "cancelled"],
        "in_progress": ["ready"],
        "ready":       ["delivered"],
        "delivered":   ["completed"],
        "completed":   [],   # terminal — no further moves
        "cancelled":   [],   # terminal — no further moves
    }

    @staticmethod
    @transaction.atomic
    def change_status(order, new_status, user):
        """
        Moves an order to a new status if the transition is allowed.

        Steps (all inside one transaction):
          1. Look up the allowed transitions for the current status.
          2. Raise ValueError if the requested status is not in that list.
          3. Write a history row BEFORE changing the order — so if the
             order.save() later fails, the history row is rolled back too.
          4. Apply optional side effects (e.g. stamp delivered_at).
          5. Save the order.

        Returns the updated order so the view can re-serialize it.
        """
        current_status = order.status

        allowed = OrderStatusService.VALID_TRANSITIONS.get(current_status, [])

        if new_status not in allowed:
            raise ValueError(
                f"Cannot move order from '{current_status}' to '{new_status}'. "
                f"Allowed next statuses: {allowed if allowed else 'none (terminal state)'}"
            )

        # Audit log — written before the change so it's part of the same transaction
        OrderStatusHistory.objects.create(
            order=order,
            old_status=current_status,
            new_status=new_status,
            changed_by=user
        )

        order.status = new_status

        # Side effects — add more here as your workflow grows
        if new_status == "delivered":
            order.delivered_at = timezone.now()
            OrderStatusService._deduct_order_items_stock(order)

        # Future hooks (plug these in when ready):
        # if new_status == "ready":
        #     whatsapp_service.notify_patient(order)
        # if new_status == "completed":
        #     inventory_service.deduct_stock(order)

        order.save()

        return order

    @staticmethod
    def _deduct_order_items_stock(order):
        """Deduct inventory stock when an order is delivered."""
        order_items = order.items.select_related("product").all()

        for item in order_items:
            inventory_item = item.product
            if inventory_item.stock_level < item.quantity:
                raise ValueError(
                    f"Insufficient stock for '{inventory_item}' "
                    f"(required {item.quantity}, available {inventory_item.stock_level})"
                )

            inventory_item.stock_level -= item.quantity
            inventory_item.quantity_sold += item.quantity
            inventory_item.save()

    @staticmethod
    @transaction.atomic
    def cancel_order(order, user):
        """
        Cancels an order regardless of which non-terminal status it is in.

        Separate from change_status() because cancellation has its own
        rules: it bypasses the normal transition chain but still cannot
        cancel an already-completed or already-cancelled order.
        """
        if order.status in ["completed", "cancelled"]:
            raise ValueError(
                f"Cannot cancel an order that is already '{order.status}'"
            )

        OrderStatusHistory.objects.create(
            order=order,
            old_status=order.status,
            new_status="cancelled",
            changed_by=user
        )

        order.status = "cancelled"
        order.save()

        return order

    @staticmethod
    def validate_transition(current_status, new_status):
        """
        Pure validation helper — raises ValueError or returns None.
        Use this when you want to check a transition WITHOUT making any
        database changes (e.g. for a dry-run preview in the UI).
        """
        allowed = OrderStatusService.VALID_TRANSITIONS.get(current_status, [])

        if new_status not in allowed:
            raise ValueError(
                f"Invalid transition: '{current_status}' → '{new_status}'. "
                f"Allowed: {allowed}"
            )

    @staticmethod
    def get_allowed_transitions(current_status):
        """
        Returns the list of statuses this order can legally move to.
        Useful for populating a dropdown in the frontend so the user
        only sees valid next options.
        """
        return OrderStatusService.VALID_TRANSITIONS.get(current_status, [])    