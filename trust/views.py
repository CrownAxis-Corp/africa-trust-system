from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TrustEventSerializer
from .models import TrustEvent

# Create your views here.
class TrustViewSet(viewsets.ModelViewSet):
    queryset = TrustEvent.objects.all()
    serializer_class = TrustEventSerializer