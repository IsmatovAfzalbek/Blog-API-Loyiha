from rest_framework.permissions import BasePermission



class IsSuperUserOnly(BasePermission):
    message = "Kirish taqiqlangan! Bu amalni bajarish uchun siz tizimda 'Superuser' bo'lishingiz shart."
    
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False
        
        return bool(request.user.is_superuser)




class IsOwnerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        if hasattr(obj, 'author'):
            return obj.author == request.user

        elif hasattr(obj, 'user'):
            return obj.user == request.user

        return False