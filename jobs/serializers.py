from rest_framework import serializers
from .models import Job
from users.serializers import UserSerializer

class JobSerializer(serializers.ModelSerializer):
    client = UserSerializer(read_only = True)
    class Meta:
        model = Job
        fields = ['id', 'title', 'description', 'budget', 'location', 'status', 'client']
        
        