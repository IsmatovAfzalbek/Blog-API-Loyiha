from rest_framework import serializers

from .models import Category


class CategorySerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
    
    class Meta:
        model = Category
        fields = ["id", "name", "slug", "created_at"]





