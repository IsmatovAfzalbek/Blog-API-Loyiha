from rest_framework.generics import GenericAPIView 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from django.shortcuts import get_object_or_404

from .models import Post
from .serializers import PostSerializer
from app_posts.permissions import IsOwnerPermission



class ListCreatedView(GenericAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    filterset_fields = ['category']

    search_fields = ['title']

    ordering_fields = ['created_at']
    
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
    
    def get(self, request):
        posts = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(posts, many = True)
        
        return Response({
            "message": "Posts",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(author=request.user)
        
        return Response({
            "message": "Post created",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
    


class DetailUpdateDelete(GenericAPIView):
    serializer_class = PostSerializer
    lookup_field = "id"
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerPermission()]
    
    
    def get_object(self, id):
        return get_object_or_404(Post, id=id)
    
    
    def get(self, request, id):
        serializer = self.get_serializer(self.get_object(id=id))
        
        return Response({
            "message": "detail",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)
    
    
    def patch(self, request, id):
        post = self.get_object(id)
        self.check_object_permissions(request, post)
        
        serializer = self.get_serializer(self.get_object(id), partial = True, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response({
            "message": "update",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
        
    def delete(self, request, id):
        post = self.get_object(id)
        
        self.check_object_permissions(request, post)
        
        post.delete()
        
        return Response({
            "message": "deleted"
        }, status=status.HTTP_204_NO_CONTENT)