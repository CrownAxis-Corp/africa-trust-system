from django.contrib import admin
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','phone_number','country','trust_score','date_joined']
    search_fields = ['username','email','phone_number']
    list_filter = ['country', 'is_staff','is_active']
    ordering=['-date_joined']
    
admin.site.register(User, UserAdmin)
