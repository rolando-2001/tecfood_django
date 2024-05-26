from rest_framework import viewsets
from tecfood_admin.models import Role
from tecfood_admin.serializers import RoleSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from tecfood_admin.permissions.user_permissions import IsAdminRole


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminRole]