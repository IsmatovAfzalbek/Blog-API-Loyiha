from rest_framework import serializers

from .models import Post




class PostSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    
    likes_count = serializers.SerializerMethodField()

    comments_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'description', 'image', 'author', 
                  'category', 'created_at', 'updated_at','likes_count','comments_count',]
        
        
        read_only_fields = ['id', 'slug', 'author']
        
        
    
    def get_likes_count(self, obj):
        return obj.likes_set.count()


    def get_comments_count(self, obj):
        return obj.comment_set.count()


    def validate_title(self, value):

        if len(value.strip()) < 3:
            raise serializers.ValidationError({
                "message":"Title kamida 3 ta belgidan iborat bo'lishi kerak"
            })

        return value


    def validate_description(self, value):

        if len(value.strip()) < 5:
            raise serializers.ValidationError({
                "message": "Description kamida 5 ta belgidan iborat bo'lishi kerak"
            })

        return value








