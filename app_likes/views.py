from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.shortcuts import get_object_or_404


from .models import Likes
from .serializers import LikesSerializer
from app_posts.permissions import IsOwnerPermission



class CreateListView(GenericAPIView):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()
    
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
    
    
    def get(self, request):
        serializer = self.get_serializer(self.get_queryset(), many = True)
        
        return Response({
            "message": "Likes",
            "data": serializer.data
        }, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(user = request.user)
        
        return Response({
            "message": "Post liked",
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)


class DetailDeleteView(GenericAPIView):
    serializer_class = LikesSerializer
    queryset = Likes.objects.all()
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated(), IsOwnerPermission()]
    
    
    def get_object(self, id):
        return get_object_or_404(Likes, id=id)
    
    
    def get(self, request, id):
        serializer = self.get_serializer(self.get_object(id=id))
        
        return Response({
            "message": "Detail",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    
    
    def delete(self, request, id):
        like = self.get_object(id)
        
        self.check_object_permissions(request, like)

        like.delete()
        
        return Response({
            "message": "Like removed"
            
        }, status=status.HTTP_204_NO_CONTENT)