from rest_framework import serializers
from .models import User, Card, Friend, Favorite

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','bio')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('title','user','font_color', 'color', 'card_msg','created_at','updated_at','published', 'text_alignment')

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('friend',)

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('card','created_at', 'user')
