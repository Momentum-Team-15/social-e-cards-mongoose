from django.db import models
from django.contrib.auth.models import AbstractUser

# Basic models for now, we can add stuff later

COLOR_CHOICES = {
('GRAY', 'GRAY'),
('RED', 'RED'),
('ORANGE', 'ORANGE'),
('YELLOW', 'YELLOW'),
('BLUE', 'BLUE'),
('GREEN', 'GREEN'),
('PURPLE', 'PURPLE'),
('BLACK', 'BLACK'),
('GOLD', 'GOLD'),
('DARKRED', 'DARKRED')
}


class User(AbstractUser):
    bio = models.TextField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)

class Card(models.Model): 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    card_msg = models.TextField(max_length=500, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='WHITE')
    font_color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='BLACK')
    
    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='favorites')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, )

    def __str__(self):
        return self.user.name

