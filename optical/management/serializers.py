from rest_framework import serializers
from .models import MedicalReport
from  .models import *
from services.order_service import OrderService

class MedicalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalReports
        fields = '__all__'  # Serialize all fields in the MedicalReport model


from rest_framework import serializers
from .models import ScheduledMessage, MessageRecipient, Patient

# For displaying or selecting patients
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ['id', 'name', 'contact', 'email']

# For creating a scheduled message
class ScheduledMessageSerializer(serializers.ModelSerializer):
    recipients = serializers.ListField(
        child=serializers.IntegerField(), write_only=True
    )

    class Meta:
        model = ScheduledMessage
        fields = ['id', 'message', 'scheduled_time', 'status', 'recipients']
        read_only_fields = ['id', 'status']

    def create(self, validated_data):
        recipient_ids = validated_data.pop('recipients', [])
        message = ScheduledMessage.objects.create(**validated_data)
        for patient_id in recipient_ids:
            patient = Patient.objects.get(id=patient_id)
            MessageRecipient.objects.create(message=message, patient=patient)
        return message


# For listing messages and their recipients
class MessageRecipientSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = MessageRecipient
        fields = ['id', 'patient', 'status', 'error_message', 'sent_at']


class ScheduledMessageDetailSerializer(serializers.ModelSerializer):
    recipients = MessageRecipientSerializer(many=True)

    class Meta:
        model = ScheduledMessage
        fields = ['id', 'message', 'scheduled_time', 'status', 'recipients']


# ─────────────────────────────────────────────────────────────────────────────
# Orders
# ─────────────────────────────────────────────────────────────────────────────
 
class OrderItemSerializer(serializers.ModelSerializer):
    """
    Used for both reading order items and accepting them on creation.
    product_name, total_price are read-only — calculated server-side.
    """
    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "product_name",
            "quantity",
            "unit_price",
            "total_price",
            "item_type",
        ]
        read_only_fields = ["product_name", "total_price"]
 
 
class OrderSerializer(serializers.ModelSerializer):
    """
    Read serializer: returns an order with its nested items and payments.
    'items' and 'payments' are declared here (inside the class) — not
    floating at module level as they were before (FIX 5).
    """
    items = OrderItemSerializer(many=True, read_only=True)       # FIX 5
    payments = serializers.SerializerMethodField()               # FIX 5
    patient_name = serializers.CharField(source="patient.name", read_only=True)
    payment_status = serializers.SerializerMethodField()
 
    class Meta:
        model = Order
        fields = [
            "id",
            "order_number",
            "patient",
            "patient_name",
            "prescription",
            "status",
            "subtotal",
            "discount",
            "total_amount",
            "amount_paid",   # requires the new field in models.py
            "balance",       # requires the new field in models.py
            "payment_status",
            "created_by",
            "assigned_to",
            "created_at",
            "expected_delivery_date",
            "delivered_at",
            "notes",
            "items",
            "payments",
        ]
        read_only_fields = [
            "subtotal", "total_amount", "amount_paid", "balance",
            "payment_status", "created_at", "delivered_at",
        ]
 
    def get_payments(self, obj):
        return PaymentSerializer(obj.payments.all(), many=True).data

    def get_payment_status(self, obj):
        try:
            amount_paid = float(obj.amount_paid or 0)
            balance = float(obj.balance or 0)
        except (TypeError, ValueError):
            amount_paid = 0.0
            balance = float(obj.total_amount or 0)

        if amount_paid <= 0:
            return "unpaid"
        if balance > 0:
            return "partial"
        return "paid"


class OrderCreateSerializer(serializers.ModelSerializer):
    """
    Write serializer: accepts nested items on creation.
    Delegates to OrderService.create_order() so business logic
    (validation, total calculation) is always applied — FIX 4.
    """
    items = OrderItemSerializer(many=True)
 
    class Meta:
        model = Order
        fields = [
            "order_number",
            "patient",
            "prescription",
            "discount",
            "expected_delivery_date",
            "assigned_to",
            "notes",
            "items",
        ]
        read_only_fields = ["order_number"]  # Auto-generated by OrderService
 
    def create(self, validated_data):
        # FIX 4: delegate to the service — totals are calculated there,
        # stock is validated there, and the transaction is managed there.
        # The old code called Order.objects.create() directly, skipping all of that.
        user = self.context["request"].user
        return OrderService.create_order(validated_data, user)
 
 
# ─────────────────────────────────────────────────────────────────────────────
# Payments
# ─────────────────────────────────────────────────────────────────────────────
 
class PaymentSerializer(serializers.ModelSerializer):
    """Read serializer — returned after a payment is recorded."""
    class Meta:
        model = Payment
        fields = [
            "id",
            "order",
            "amount",
            "payment_method",
            "transaction_reference",
            "recorded_by",
            "payment_date",
        ]
        read_only_fields = ["recorded_by", "payment_date"]
 
 
class PaymentCreateSerializer(serializers.ModelSerializer):
    """
    Write serializer — validates incoming payment data.
    Amount and payment_method are required; transaction_reference is optional.
    Note: business validation (overpayment check) happens in PaymentService,
    not here — serializers only validate data shape, not business rules.
    """
    class Meta:
        model = Payment
        fields = ["order", "amount", "payment_method", "transaction_reference"]
 
    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Payment amount must be greater than zero"
            )
        return value
 
 
# ─────────────────────────────────────────────────────────────────────────────
# Order status history
# ─────────────────────────────────────────────────────────────────────────────
 
class OrderStatusHistorySerializer(serializers.ModelSerializer):
    """
    FIX 6: This serializer was missing entirely.
    It is needed by the order detail view to show the status audit log.
    """
    changed_by_username = serializers.CharField(
        source="changed_by.username", read_only=True
    )
 
    class Meta:
        model = OrderStatusHistory
        fields = [
            "id",
            "old_status",
            "new_status",
            "changed_by",
            "changed_by_username",
            "changed_at",
        ]
        read_only_fields = ["changed_at"]
 





# class OrderItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OrderItem
#         fields = "__all__"

# class OrderSerializer(serializers.ModelSerializer):
#     items = OrderItemSerializer(many=True)

#     class Meta:
#         model = Order
#         fields = "__all__"

#     def create(self, validated_data):
#         items_data = validated_data.pop("items")
#         order = Order.objects.create(**validated_data)

#         for item in items_data:
#             OrderItem.objects.create(order=order, **item)

#         return order
 
# class PaymentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Payment
#         fields = "__all__"
        
      
# #

# def create(self, validated_data):
#     items_data = validated_data.pop("items")
#     order = OrderService.create_order(validated_data, self.context["request"].user)
#     return order    
    
# items = OrderItemSerializer(many=True, read_only=True)
# payments = PaymentSerializer(many=True, read_only=True)    
    
    
    
    
    
    
    