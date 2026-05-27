from django.contrib import admin
from .models import Job
# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['title','description', 'location', 'created_at', 'client', 'budget', 'status']
    search_fields = ['title', 'client__username' , 'location']
    list_filter = ['status', 'location']
    
admin.site.register(Job, JobAdmin)