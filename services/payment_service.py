# from decimal import Decimal
# from django.db import transaction

# from optical.management.models import Payment, Order

# class PaymentService:
#     pass


# @staticmethod
# @transaction.atomic
# def add_payment(validated_data, user):
#     order = validated_data["order"]
#     amount = Decimal(validated_data["amount"])

#     # Validate payment
#     PaymentService.validate_payment(order, amount)

#     # Create payment
#     payment = Payment.objects.create(
#         order=order,
#         amount=amount,
#         payment_method=validated_data["payment_method"],
#         transaction_reference=validated_data.get("transaction_reference", ""),
#         recorded_by=user
#     )

#     # Update order financials
#     PaymentService.update_order_balance(order)

#     return payment

# @staticmethod
# def validate_payment(order, amount):
#     if amount <= 0:
#         raise ValueError("Payment amount must be greater than zero")

#     total_paid = sum(p.amount for p in order.payments.all())
#     total_paid = Decimal(total_paid)

#     if total_paid + amount > order.total_amount:
#         raise ValueError("Payment exceeds total order amount")
    
# @staticmethod
# def update_order_balance(order):
#     total_paid = sum(p.amount for p in order.payments.all())
#     total_paid = Decimal(total_paid)

#     balance = order.total_amount - total_paid

#     # Optional: store for performance
#     order.amount_paid = total_paid
#     order.balance = balance

#     order.save()
    
    
# @staticmethod
# def get_payment_status(order):
#     total_paid = sum(p.amount for p in order.payments.all())
#     total_paid = Decimal(total_paid)

#     if total_paid == 0:
#         return "unpaid"
#     elif total_paid < order.total_amount:
#         return "partial"
#     else:
#         return "paid"
    
    
# @staticmethod
# @transaction.atomic
# def refund_payment(order, amount, user):
#     amount = Decimal(amount)

#     if amount <= 0:
#         raise ValueError("Refund amount must be greater than zero")

#     total_paid = sum(p.amount for p in order.payments.all())
#     total_paid = Decimal(total_paid)

#     if amount > total_paid:
#         raise ValueError("Refund exceeds total paid amount")

#     # Create negative payment (audit-safe)
#     payment = Payment.objects.create(
#         order=order,
#         amount=-amount,
#         payment_method="refund",
#         recorded_by=user
#     )

#     PaymentService.update_order_balance(order)

#     return payment



from decimal import Decimal
from django.db import transaction

from management.models import Payment, Order


class PaymentService:
    """
    Handles all financial operations: adding payments, preventing overpayment,
    keeping order balances accurate, and recording refunds.

    FIX (CRITICAL): Every method is now INDENTED inside the class body.
    Previously all methods sat outside the class (after 'pass') so they were
    plain module-level functions — calling PaymentService.add_payment()
    would have raised AttributeError at runtime.

    APPEND-ONLY DESIGN:
    Payments are never edited or deleted. Refunds are recorded as negative
    payments. This gives a full audit trail: you can always replay the
    payment ledger and arrive at the correct balance.
    """

    @staticmethod
    @transaction.atomic
    def add_payment(validated_data, user):
        """
        Records a new payment against an order.

        Steps (all inside one transaction — if any step fails, nothing is saved):
          1. Pull the order and amount from validated data.
          2. Validate the amount is positive and won't cause overpayment.
          3. Create the Payment row.
          4. Recalculate and persist the order's balance fields.
        """
        order = validated_data["order"]
        amount = Decimal(str(validated_data["amount"]))

        PaymentService.validate_payment(order, amount)

        payment = Payment.objects.create(
            order=order,
            amount=amount,
            payment_method=validated_data["payment_method"],
            transaction_reference=validated_data.get("transaction_reference", ""),
            recorded_by=user
        )

        PaymentService.update_order_balance(order)

        return payment

    @staticmethod
    def validate_payment(order, amount):
        """
        Business rules that must pass before any payment is recorded:
          - Amount must be positive.
          - The new total paid must not exceed the order total.

        Raises ValueError (caught by the view and returned as a 400 response)
        so the database is never touched with invalid data.
        """
        if amount <= 0:
            raise ValueError("Payment amount must be greater than zero")

        total_paid = sum(
            Decimal(str(p.amount)) for p in order.payments.all()
        )

        if total_paid + amount > order.total_amount:
            overage = (total_paid + amount) - order.total_amount
            raise ValueError(
                f"Payment would exceed the order total by {overage}. "
                f"Maximum accepted: {order.total_amount - total_paid}"
            )

    @staticmethod
    def update_order_balance(order):
        """
        Recalculates the order's paid amount and remaining balance,
        then persists both to the Order row.

        FIX: The Order model must have 'amount_paid' and 'balance' fields.
        These fields did not exist before — see the corrected models note.
        Without them this method crashes with AttributeError on order.save().

        Call this after every payment or refund so the Order always reflects
        the current financial state without requerying all payments.
        """
        total_paid = sum(
            Decimal(str(p.amount)) for p in order.payments.all()
        )

        balance = order.total_amount - total_paid

        order.amount_paid = total_paid
        order.balance = balance
        order.save()

    @staticmethod
    def get_payment_status(order):
        """
        Returns a single string describing where this order stands
        in terms of payment: 'unpaid', 'partial', or 'paid'.

        Useful for quick status checks without loading the full summary.
        """
        total_paid = sum(
            Decimal(str(p.amount)) for p in order.payments.all()
        )

        if total_paid <= 0:
            return "unpaid"
        elif total_paid < order.total_amount:
            return "partial"
        else:
            return "paid"

    @staticmethod
    @transaction.atomic
    def refund_payment(order, amount, user):
        """
        Records a refund as a NEGATIVE payment row.

        Why negative and not a delete?
        Deleting a payment row loses the audit trail — you can no longer
        tell how much was paid or when. A negative row keeps the full history
        and the ledger still balances: sum(payments) = net amount paid.

        Validates:
          - Refund amount is positive.
          - Refund does not exceed total amount already paid.
        """
        amount = Decimal(str(amount))

        if amount <= 0:
            raise ValueError("Refund amount must be greater than zero")

        total_paid = sum(
            Decimal(str(p.amount)) for p in order.payments.all()
        )

        if amount > total_paid:
            raise ValueError(
                f"Cannot refund {amount} — only {total_paid} has been paid"
            )

        # Negative amount = money going out (refund)
        payment = Payment.objects.create(
            order=order,
            amount=-amount,
            payment_method="refund",
            transaction_reference="",
            recorded_by=user
        )

        PaymentService.update_order_balance(order)

        return payment