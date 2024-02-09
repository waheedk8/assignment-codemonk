# models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class Paragraph(models.Model):
    text = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



class CustomUser(AbstractUser):
    dob = models.DateField(null=True, blank=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    modifiedAt = models.DateTimeField(auto_now=True)
    
    class Meta:
        # Add this to avoid clashes with the built-in User model
        swappable = 'AUTH_USER_MODEL'

# Add related_name arguments to avoid clashes with built-in User model
CustomUser._meta.get_field('groups').related_name = 'custom_user_groups'
CustomUser._meta.get_field('user_permissions').related_name = 'custom_user_permissions'