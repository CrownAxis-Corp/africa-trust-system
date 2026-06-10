from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PaymentSerializer
from .models import Payment

# Create your views here.
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer