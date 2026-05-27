from django.db import models
from django.conf import settings

# Create your models here.

class Job(models.Model):
    """Job models for Africa Trust System"""
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('ASSIGNED', 'Assigned'),
        ('COMPLETED', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, related_name = 'job_postings', on_delete = models.CASCADE)
    budget =  models.DecimalField(max_digits = 10, decimal_places = 2)
    status = models.CharField(max_length=30, choices = STATUS_CHOICES, default = 'OPEN')
    class Meta:
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.title} - {self.status}"
        