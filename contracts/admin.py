from django.contrib import admin
from .models import Contract
# Register your models here.
class ContractAdmin(admin.ModelAdmin):
    list_display = ['client','contractor','title','description','amount','status','start_date','end_date','created_at']
    search_fields = ['client__username', 'contractor__username']
    list_filter = ['start_date', 'end_date', 'status']
    
admin.site.register(Contract, ContractAdmin)
    