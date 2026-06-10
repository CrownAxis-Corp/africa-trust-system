from rest_framework import serializers
from .models import TrustEvent


class TrustEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrustEvent
        fields = ['user', 'event_type', 'score_change', 'notes', 'created_at']
        read_only_fields = ['created_at', 'score_change']