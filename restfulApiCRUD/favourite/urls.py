from django.urls import path
from favourite.views import FavouriteListCreateAPIView, FavouriteAPIView

urlpatterns = [
    path('list-create', FavouriteListCreateAPIView.as_view(), name='list-create'),
    path('update-delete/<pk>', FavouriteAPIView.as_view(), name='update-delete'),
]
