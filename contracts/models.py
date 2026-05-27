from django.db import models
from django.conf import settings

# Create your models here.
class Contract(models.Model):
    """Contract fields for Africa Trust System"""
    STATUS_CHOICES = [('PENDING','Pending'),
               ('ACTIVE', 'Active'),
               ('COMPLETED','Completed'),
               ]
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="client_contracts", on_delete=models.CASCADE)
    contractor = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="contractor_contracts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    amount = models.DecimalField(max_digits= 10, decimal_places = 2)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices = STATUS_CHOICES, default = "PENDING")
    
    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.status}"