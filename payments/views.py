from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PaymentSerializer
from .models import Payment

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer