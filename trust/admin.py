from django.contrib import admin
from .models import TrustEvent

# Register your models here.
class TrustAdmin(admin.ModelAdmin):
    list_display = ['user', 'event_type', 'score_change', 'notes']
    search_fields = ['user__username']
    list_filter = ['event_type', 'created_at']
    
admin.site.register(TrustEvent, TrustAdmin)