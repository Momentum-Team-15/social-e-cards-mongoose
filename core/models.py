from django.db import models
from django.contrib.auth.models import AbstractUser

# Basic models for now, we can add stuff later
class User(AbstractUser):
    bio = models.TextField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)

class Card(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    pass

class Favorite(models.Model):
    pass

class Friend(models.Model):
    pass

