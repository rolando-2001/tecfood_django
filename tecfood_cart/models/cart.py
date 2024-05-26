from django.db import models
from tecfood_dish.models.dish import Dish
from tecfood_admin.models.user import User


class Cart(models.Model):
    cart_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    class Meta:
          db_table = 'cart'