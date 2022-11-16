from django.shortcuts import render
from .models import Card


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


class MyCardList(generics.ListCreateAPIView):
    pass

class FriendsCardList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Friends.objects.all()
    serializer_class = FriendsSerializer

    def get_queryset(self):
        queryset = Friends.objects.filter(follower=self.request.user.pk)
        return queryset

    def perform_create(self, serializer):
        serializer.save(follower=self.request.user)

