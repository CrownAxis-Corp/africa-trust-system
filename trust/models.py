from django.db import models
from django.conf import settings
# Create your models here.

class TrustEvent(models.Model):
    """TrustEvent fields for Africa Trust System"""
    EVENT_CHOICES=[
        ("DISPUTE_LOST","Dispute_lost"),
        ("NO_SHOW", "No_show"),
        ("EARLY_COMPLETION", "Early_completion"),
        ("PAYMENT_ON_TIME", "Payment_on_time"),
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='User_Trust', on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, choices = EVENT_CHOICES, default = "NO_SHOW")
    score_change = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "TrustEvent"
        verbose_name_plural = "TrustEvents"
        ordering = ['-created_at']
        
    def __str__(self):
        return f"{self.user} - {self.event_type}"