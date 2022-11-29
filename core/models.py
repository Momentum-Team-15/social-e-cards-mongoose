from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    bio = models.TextField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=30, null=True, blank=True)

class Card(models.Model): 


    COLOR_CHOICES = [
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
    ]


    TEXT_ALIGNMENT_CHOICES =[
        
        ('CENTER', 'CENTER'),
        ('RIGHT', 'RIGHT'),
        ('LEFT', 'LEFT')
    
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=50)
    card_msg = models.TextField(max_length=500, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='WHITE')
    font_color = models.CharField(max_length=50, choices=COLOR_CHOICES, default='BLACK')
    text_alignment = models.CharField(max_length=50,choices=TEXT_ALIGNMENT_CHOICES)

    
    
    def __str__(self):
        return self.title

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='favorites')
    card = models.ForeignKey(Card, on_delete=models.CASCADE, related_name='favorites')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.card

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,  related_name='friends')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, )

    def __str__(self):
        return self.user.name

