from rest_framework import serializers

from .models import Comment




class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only = True)
    
    class Meta:
        model = Comment
        fields = ['id', 'text', 'user', 'post', 'created_at']
        read_only_fields = ['id', 'user', 'created_at']


    def validate_text(self, value):
        if len(value.strip()) < 2:
            raise serializers.ValidationError({
                "message": "Comment juda qisqa"
            })

        return value




