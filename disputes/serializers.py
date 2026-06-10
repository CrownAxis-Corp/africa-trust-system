from rest_framework import serializers
from .models import Dispute

class DisputeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispute
        fields = ['contract','status', 'resolution', 'reason', 'created_at', 'resolved_at', 'filed_by']

        