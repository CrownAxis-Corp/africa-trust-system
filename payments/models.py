from django.db import models
from contracts.models import Contract
# Create your models here.
class Payment(models.Model):
    """Payment fields for Africa Trust System"""
    STATUS_CHOICES = [('PENDING','Pending'),
            ('COMPLETED','Completed'),
            ('FAILED', 'Failed'),
            ('REFUNDED', 'Refunded'),
            ]
    contract = models.ForeignKey(Contract, related_name='payments', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits= 10, decimal_places = 2)
    status = models.CharField(max_length=20, choices = STATUS_CHOICES, default = 'PENDING')
    created_at = models.DateTimeField(auto_now_add = True)
    completed_at = models.DateTimeField(blank = True, null = True)
    
    class Meta:
        verbose_name = "Payment"
        verbose_name_plural = "Payments"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.contract} - {self.amount}"