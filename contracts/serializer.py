from rest_framework import serializers
from .models import Contract
from users.serializers import UserSerializer
from users.models import User
class ContractSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only=True)
    contractor_id = serializers.PrimaryKeyRelatedField(source='contractor',queryset=User.objects.all())
    contractor = UserSerializer(read_only=True)
    class Meta:
        model = Contract
        fields = ['title','status','description', 'amount', 'start_date', 'end_date', 'client', 'contractor', 'contractor_id']