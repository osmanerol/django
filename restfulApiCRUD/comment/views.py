from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from comment.models import Comment
from comment.serializers import CommentCreateSerializer, CommentListSerializer, CommentDeleteUpdateSerializer
from comment.permissions import IsOwner
from comment.paginations import CommentPagination
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

class CommentCreateAPIView(CreateAPIView):
    queryset= Comment.objects.all()
    serializer_class= CommentCreateSerializer

    def perform_create(self, serializer):
        return serializer.save(user= self.request.user)

class CommentListAPIView(ListAPIView):
    serializer_class= CommentListSerializer
    pagination_class= CommentPagination

    def get_queryset(self):
        queryset= Comment.objects.filter(parent=None)
        query= self.request.GET.get('q') # http://localhost:8000/api/comment/list?q=7 ile 7 id'li posta ait commentler
        if query:
            queryset= queryset.filter(post=query)
        return queryset

class CommentUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset= Comment.objects.all()
    serializer_class= CommentDeleteUpdateSerializer
    lookup_field= 'pk'

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class CommentDeleteAPIView(DestroyAPIView, UpdateModelMixin, RetrieveModelMixin):
    queryset= Comment.objects.all()
    serializer_class= CommentDeleteUpdateSerializer
    lookup_field= 'pk'
    permission_classes= [IsOwner]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)  

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)    