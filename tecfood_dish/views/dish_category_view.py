from rest_framework import viewsets
from tecfood_dish.models import DishCategory
from tecfood_dish.serializers import DishCategorySerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from tecfood_admin.permissions.user_permissions import IsAdminRole

class DishCategoryViewSet(viewsets.ModelViewSet):
    queryset = DishCategory.objects.all()
    serializer_class = DishCategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminRole]