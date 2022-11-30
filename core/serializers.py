from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from .models import User, Card, Friend, Favorite, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name','bio', 'username')

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = ('title','user','font_color', 'color', 'card_msg','created_at','updated_at','published', 'text_alignment', 'comments')

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friend
        fields = ('friend',)

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = ('card','created_at', 'user')


class CommentSerializer(serializers.ModelSerializer):
    comment_owner = UserSerializer(read_only=True)
    
    class Meta:
        model = Comment
        fields = ('pk', 'comment_owner', 'card', 'text')

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ("name", "password", "username", "bio")