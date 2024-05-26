from django.contrib import admin

# Register your models here.
from tecfood_dish.models.dish_category import DishCategory
from tecfood_dish.models.dish import Dish

admin.site.register(DishCategory)
admin.site.register(Dish)