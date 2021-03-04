from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView, RetrieveUpdateDestroyAPIView
from favourite.models import Favourite
from favourite.serializers import FavouriteListCreateAPISerializer, FavouriteAPISerializer
from favourite.paginations import FavouritePagination
from favourite.permissions import IsOwner

class FavouriteListCreateAPIView(ListCreateAPIView):
    queryset= Favourite.objects.all()
    serializer_class= FavouriteListCreateAPISerializer
    pagination_class= FavouritePagination

    def get_queryset(self):
        return Favourite.objects.filter(user= self.request.user)
    
    def perform_create(self, serializer):
        return serializer.save(user= self.request.user)

class FavouriteAPIView(RetrieveUpdateDestroyAPIView):
    queryset= Favourite.objects.all()
    serializer_class= FavouriteAPISerializer
    lookup_field= 'pk'
    permission_classes= [IsOwner]