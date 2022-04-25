from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    edit_methods = ("PUT, PATCH")
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser and request.method not in self.edit_methods:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.owner == request.user
