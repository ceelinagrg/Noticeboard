from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.user.is_superuser:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True
            
        return obj.owner == request.user

        

# class IsOwnerOrReadOnly(permissions.BasePermission):

#     edit_methods = ("DELETE")

#     def has_permission(self, request, view):
#         if request.user.is_authenticated:
#             return True

#     def has_object_permission(self, request, view, obj):
#         if request.user.is_superuser:
#             return True

#         if request.method in permissions.SAFE_METHODS:
#             return True

#         if obj.owner == request.user:
#             return True

#         if request.user.is_staff and request.method not in self.edit_methods:
#             return True

#         return False