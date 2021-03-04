from django.urls import path
from post.views import PostListAPIView, PostDetailAPIView, PostCrateAPIView, PostUpdateAPIView, PostDeleteAPIView

urlpatterns = [
    path('list', PostListAPIView.as_view(), name='list'),
    path('detail/<slug>', PostDetailAPIView.as_view(), name='detail'),
    path('create', PostCrateAPIView.as_view(), name='create'),
    path('update/<slug>', PostUpdateAPIView.as_view(), name='update'),
    path('delete/<slug>', PostDeleteAPIView.as_view(), name='delete'),
]
