from django.db.models.query import EmptyQuerySet
from rest_framework import generics, request
from django.shortcuts import render
from .serializers import CardSerializer, UserSerializer, FavoriteSerializer, FriendSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Card, User, Favorite, Friend

# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'card_list': reverse('card_list', request=request, format=format),
    })

class CardUser(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)


class CardList(generics.ListCreateAPIView): 
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CardSerializer
        return self.serializer_class


class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(user=self.request.user.pk)
        return queryset



class FavoriteList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()

    def get_queryset(self):
        queryset = Favorite.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class FriendList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FriendSerializer
    queryset = Friend.objects.all()

    def get_queryset(self):
        queryset = Friend.objects.filter(user=self.request.user)
        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FriendCardList(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CardSerializer

    def get_queryset(self):
        queryset = Card.objects.none()
        friends = Friend.objects.filter(user=self.request.user).values_list('friend')
        for friend in friends:
            IndivCards = Card.objects.filter(user=friend)
            queryset = queryset | IndivCards
        
        queryset.order_by('created_at')
        return queryset


        

    

class CardUser(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)
