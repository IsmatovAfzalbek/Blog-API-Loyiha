from django.db import models
from django.contrib.auth.models import AbstractUser





class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=13, unique=True, null=True, blank=True)
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    
    
    class Meta:
        verbose_name = "Foydalanuvchi"
        verbose_name_plural = "Foydalanuvchilar"
        ordering = ['-date_joined']
        
        
    def __str__(self):
        return self.username


