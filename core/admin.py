from django.contrib import admin
from .models import User, Card, Friend, Favorite

# Register your models here.
admin.site.register(User)
admin.site.register(Card)
admin.site.register(Friend)
admin.site.register(Favorite)