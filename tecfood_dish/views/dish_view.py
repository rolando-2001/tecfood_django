from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from tecfood_dish.models import Dish
from tecfood_dish.serializers import DishSerializer
from tecfood_admin.permissions.user_permissions import IsAdminRole 
from django.shortcuts import get_object_or_404

class DishViewSet(viewsets.ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsAdminRole]
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

   #list dishes
    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

    #one dish
    def retrieve(self, request, pk=None):
        dish = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(dish)
        return Response(serializer.data)

    #create dish
    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    #update dish
    def update(self, request, pk=None):
        dish = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = self.get_serializer(dish, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    #delete dish
    def destroy(self, request, pk=None):
        dish = get_object_or_404(self.get_queryset(), pk=pk)
        self.perform_destroy(dish)
        return Response(status=status.HTTP_204_NO_CONTENT)