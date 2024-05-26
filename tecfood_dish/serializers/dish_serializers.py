from rest_framework import serializers
from tecfood_dish.models import Dish

class DishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dish
        fields = [
            'dish_id',
            'name',
            'price',
            'stock',
            'description',
            'created_at',
            'updated_at',
            'dish_category_id',
            
        ]