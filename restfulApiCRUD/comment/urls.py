from django.urls import path
from comment.views import CommentCreateAPIView, CommentListAPIView, CommentUpdateAPIView, CommentDeleteAPIView

urlpatterns = [
    path('list', CommentListAPIView.as_view(), name= 'list'),
    path('create', CommentCreateAPIView.as_view(), name= 'create'),
    path('update/<pk>', CommentUpdateAPIView.as_view(), name= 'update'),
    path('delete/<pk>', CommentDeleteAPIView.as_view(), name= 'delete'),
] 
