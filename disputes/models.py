from django.db import models
from django.conf import settings
from contracts.models import Contract
# Create your models here.
class Dispute(models.Model):
    STATUS_CHOICES = [
        ("OPEN", "Open"),
        ("UNDER_REVIEW", "Under_review"),
        ("RESOLVED", "Resolved"),
    
    ]
    RESOLUTION_CHOICES = [
        ('CLIENT_WON', 'Client_won'),
        ('CONTRACTOR_WON', 'Contractor_won'),
        ('DISMISSED', 'Dismissed')
    ]
    filed_by = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="filed_by", on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, related_name="Contract_Dispute", on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices = STATUS_CHOICES, default = "OPEN")
    resolution = models.CharField(max_length = 50, choices = RESOLUTION_CHOICES, blank = True, null=True)
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    resolved_at = models.DateTimeField(blank = True, null = True)

    class Meta:
        verbose_name = "Dispute"
        verbose_name_plural = "Disputes"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.filed_by} - {self.status}"

