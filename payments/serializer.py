from .models import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['status', 'amount', 'contract', 'created_at', 'completed_at']
        read_only_fields = ['created_at', 'completed_at']