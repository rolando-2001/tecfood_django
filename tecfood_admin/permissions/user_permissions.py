# En un archivo como permissions.py dentro de tu aplicación

from rest_framework import permissions

class IsAdminRole(permissions.BasePermission):


    def has_permission(self, request, view):
        # Verificar si el usuario está autenticado y tiene el rol adecuado
        return request.user.is_authenticated and request.user.role.name == 'ROLE_ADMIN'
