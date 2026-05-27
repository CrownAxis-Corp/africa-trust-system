from django.contrib import admin
from .models import Dispute
# Register your models here.
class DisputeAdmin(admin.ModelAdmin):
    list_display = ['filed_by', 'contract', 'status', 'reason']
    search_fields = ['contract__title', 'filed_by__username']
    list_filter = ['status', 'created_at', 'resolved_at']
    
admin.site.register(Dispute, DisputeAdmin)