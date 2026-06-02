import re

from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework import status

from django.contrib.auth import authenticate

from .models import CustomUser


class SignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required = True, write_only = True)
    confirm_password = serializers.CharField(required = True, write_only = True)
    
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email','phone_number','password','confirm_password']
        
        
    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        
        if len(password) < 7:
            raise ValidationError({
                "message": "Parol uzunligi 7 ta belgidan kam bo'lmasligi kerak"  
            })
        
        if password != confirm_password:
            raise ValidationError({
                "message": "Parollar mos emas",
            })
              
        return attrs


    def validate_username(self,value):
        
        if len(value) < 5:
            raise ValidationError({
                "message": "username 5 ta belgidan kam bo'lmasligi kerak"
            })
            
        if not re.fullmatch(r'^[a-zA-Z0-9_.]+$', value):
            raise ValidationError({
                "message": "Username faqat harf, raqam, _ va . dan tashkil topishi kerak"
        })
            
        if self.instance:
            user = CustomUser.objects.exclude(id = self.instance.id).filter(username = value)

        else:
            user = CustomUser.objects.filter(username=value)
        
        if user.exists():
            raise ValidationError({
                "message": "Bu username band"
            })

        return value
    
    
    def validate_email(self, value):

        user = CustomUser.objects.filter(email=value)

        if self.instance:
            user = user.exclude(id=self.instance.id)

        if user.exists():
            raise ValidationError({
                "message": "Bu email band"
            })

        return value
    
    
    def validate_phone_number(self, value):

        user = CustomUser.objects.filter(phone_number=value)

        if self.instance:
            user = user.exclude(id=self.instance.id)

        if user.exists():
            raise ValidationError({
                "message": "Bu telefon raqam band"
            })

        return value
                
            
    
    
    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = CustomUser.objects.create_user(**validated_data)
        
        return user
    
    
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)
    
    
    def validate(self, attrs):
        password = attrs.get("password")
        username = attrs.get("username")
        
        user = authenticate(password=password, username=username)
        
        if not user:
            raise ValidationError({
                "message": "Login yoki Parol xato",
            })
            
        attrs["user"] = user
        
        return attrs
    
    

class ProfileSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email']
        
        
        
class ProfileUpdateSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'username', 'email', 'bio', 'image', 'phone_number']   