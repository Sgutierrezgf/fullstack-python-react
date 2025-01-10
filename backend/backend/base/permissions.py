from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        # Verifica si el usuario tiene el rol 'admin'
        return request.user.rol == 'admin' 