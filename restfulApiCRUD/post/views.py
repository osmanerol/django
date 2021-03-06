from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from post.models import Post
from post.serializers import PostSerializer, PostCreateUpdateSerializer
from rest_framework.permissions import IsAuthenticated
from post.permissions import IsOwner
from post.paginations import PostPagination
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import CreateModelMixin, ListModelMixin, DestroyModelMixin

class PostListAPIView(ListAPIView, CreateModelMixin):
    serializer_class= PostSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    search_fields= ['title', 'content']
    throttle_scope = 'user'

    def get_queryset(self):
        queryset= Post.objects.filter(draft= False)
        return queryset
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user= self.request.user)

class PostDetailAPIView(RetrieveAPIView):
    queryset= Post.objects.all()
    serializer_class= PostSerializer
    lookup_field= 'slug'

class PostCrateAPIView(CreateAPIView, ListModelMixin):
    queryset= Post.objects.all()
    serializer_class= PostCreateUpdateSerializer
    permission_classes= [IsAuthenticated]
    
    def perform_create(self, serializer):
        return serializer.save(user= self.request.user)

    '''
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    '''

class PostUpdateAPIView(RetrieveUpdateAPIView, DestroyModelMixin):
    queryset= Post.objects.all()
    serializer_class= PostCreateUpdateSerializer
    lookup_field= 'slug'
    permission_classes= [IsOwner]

    def perform_update(self, serializer):
        return serializer.save(modifiedBy= self.request.user)

    def delete(request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class PostDeleteAPIView(DestroyAPIView):
    queryset= Post.objects.all()
    serializer_class= PostSerializer
    lookup_field= 'slug'
    permission_classes= [IsOwner]