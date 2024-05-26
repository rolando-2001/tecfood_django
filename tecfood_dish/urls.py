from django.urls import path, include
from rest_framework.routers import DefaultRouter
from tecfood_dish.views import DishCategoryViewSet
from tecfood_dish.views import DishViewSet

router = DefaultRouter()
router.register(r'dish-categories', DishCategoryViewSet)

router.register(r'dishes', DishViewSet, basename='dish')

urlpatterns = [
    path('', include(router.urls)),
]