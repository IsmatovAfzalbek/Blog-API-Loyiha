from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.exceptions import ValidationError
from django.shortcuts import get_object_or_404


from .models import Category
from .serializers import CategorySerializer


class CategoryListView(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request):
        
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many = True)
        
        return Response({
            "message": "Categories",
            "data": serializer.data
        })



class CategoryCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CategorySerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            "message": "Category created successfully",
            "data": serializer.data,
            
        }, status=status.HTTP_201_CREATED)
        
        

class CategoryDetailView(APIView):
    
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        
        return [IsAuthenticated()]


    
    def get(self, request, id):
        category = get_object_or_404(Category, id=id)
        serializer = CategorySerializer(category)
        
        return Response({
            "message": "Detail",
            "data": serializer.data
        })



    def patch(self, request, id):
        category = get_object_or_404(Category, id=id)
        
        seralizer = CategorySerializer(data = request.data, instance = category, partial = True)
        seralizer.is_valid(raise_exception=True)
        seralizer.save()
        
        return Response({
        "message": "Category updated successfully",
        "data": seralizer.data
    }, status=status.HTTP_200_OK)
            
        
        
    def delete(self, request, id):
        category = get_object_or_404(Category, id=id)

        category.delete()

        return Response({
            "message": "Category deleted successfully"
        }, status=status.HTTP_200_OK)    
        