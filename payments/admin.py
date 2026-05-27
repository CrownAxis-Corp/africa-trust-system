from django.contrib import admin
from .models import Payment
# Register your models here.
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['contract', 'amount', 'status', 'completed_at']
    search_fields = ['contract__title']
    list_filter = ['status', 'created_at', 'completed_at']
    
admin.site.register(Payment, PaymentAdmin)