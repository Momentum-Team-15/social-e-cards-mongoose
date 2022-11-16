from rest_framework import serializers
from .models import User, Card, Friend, Favorite

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('user', 'title', 'card_msg', 'created_at','updated_at','published', 'color', 'font_color')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'bio')

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('name', 'user')

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('card','user','created_at')