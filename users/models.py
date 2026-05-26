from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    """Custom User model for Africa Trust System"""
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=50, blank=True, null=True)
    trust_score = models.IntegerField(default=0)
    class Meta:
        verbose_name="User"
        verbose_name_plural="Users"
        
    def __str__(self):
        return self.username