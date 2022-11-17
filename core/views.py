from rest_framework import generics
from django.shortcuts import render
from .serializers import CardSerializer, CardCreateSerializer, UserSerializer, FavoriteSerializer, FriendsSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Card, User, Favorite, Friends


# Create your views here.
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'card_list': reverse('card_list', request=request, format=format),
    })


class CardList(generics.ListCreateAPIView): 
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return CardCreateSerializer
        return self.serializer_class


class UserList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(owner=self.request.user.pk)
        return queryset



class FavoriteList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def get_queryset(self):
        queryset = Favorite.objects.filter(follower=self.request.user.pk)
        return queryset

    def perform_create(self, serializer):
        serializer.save(favorite=self.request.user)



class FriendsCardList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer

    def get_queryset(self):
        queryset = Friends.objects.filter(friends=self.request.user.pk)
        return queryset

    def perform_create(self, serializer):
        serializer.save(friends=self.request.user)

