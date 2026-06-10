from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DisputeSerializer
from .models import Dispute
# Create your views here.

class DisputeViewset(viewsets.ModelViewSet):
    queryset = Dispute.objects.all()
    serializer_class = DisputeSerializer
