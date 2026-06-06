from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.authentication import TokenAuthentication


from .serializers import SignUpSerializer,LoginSerializer, ProfileSerializer,\
    ProfileUpdateSerializer
    
    


class SignUpView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = SignUpSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
            "message": "Sign-Up",
            "token": token.key,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)
        
        
class LoginView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = LoginSerializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        
        user = serializer.validated_data["user"]
        
        token, created = Token.objects.get_or_create(user = user)
        
        return Response({
            "message": "Login successful",
            "token": token.key,
            "username": user.username,
            "email": user.email,
        }, status=status.HTTP_200_OK)



class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        user = request.user
        serializer = ProfileSerializer(user)
        
        return Response({
            "message": "Profile",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)
        
        
        
class ProfileUpdateView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def patch(self, request, id):
        user = request.user
        # data = request.data, instance = user bu yerda o'zgaruvchiga tenglab berganimiz uchun ham ishlaydi,
        # joyi o'zgarsa ham farq qilmaydi
        serializer = ProfileUpdateSerializer(data = request.data, instance = user, partial=True)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            "message": "Profile update",
            "data": serializer.data,
        }, status=status.HTTP_200_OK)
        
        
        
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        
        return Response({
            "message": "Logout successful"
        }, status=status.HTTP_200_OK)   
        
        
 