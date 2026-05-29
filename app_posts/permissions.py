from rest_framework.permissions import BasePermission


class IsOwnerPermission(BasePermission):

    def has_object_permission(self, request, view, obj):

        if hasattr(obj, 'author'):
            return obj.author == request.user

        elif hasattr(obj, 'user'):
            return obj.user == request.user

        return False