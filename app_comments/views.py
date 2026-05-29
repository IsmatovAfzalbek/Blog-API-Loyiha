from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404


from .models import Comment
from .serializers import CommentSerializer
from app_posts.permissions import IsOwnerPermission



class CommentListCreateView(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
    
    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many = True)
        
        return Response({
            "message": "comments",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(user = request.user)   
        
        return Response({
            "message": "Commnet created",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED) 



class DetailUpdateDelete(GenericAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerPermission()]
    
    
    def get_object(self, id):
        return get_object_or_404(Comment, id=id)
    
    
    def get(self, request, id):
        serializer = self.get_serializer(self.get_object(id=id))
        
        return Response({
            "message": "Detail",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    
    def patch(self, request, id):
        comment = self.get_object(id)
        
        self.check_object_permissions(request, comment)
        
        serializer = self.get_serializer(instance = self.get_object(id), data = request.data, partial = True )
        serializer.is_valid(raise_exception = True)
        serializer.save()
        
        return Response({
            "message": "Comment update",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
        
        
    def delete(self, request, id):
        commnet = self.get_object(id=id)
        
        self.check_object_permissions(request, commnet)
        
        commnet.delete()
        
        return Response({
            "message": "Comment Deleted"
        }, status=status.HTTP_204_NO_CONTENT)




