from django.shortcuts import render
from .models import Card

# Create your views here.
class CardList(generics.ListCreateAPIView): 
    pass

class MyCardList(generics.ListCreateAPIView):
    pass

class FriendsCardList(generics.ListCreateAPIView):
    pass

