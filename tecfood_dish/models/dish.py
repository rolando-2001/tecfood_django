from django.db import models
from cloudinary.models import CloudinaryField
from tecfood_dish.models import DishCategory


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    ima_url = CloudinaryField('image')
    stock = models.IntegerField()
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    dish_category_id = models.ForeignKey(DishCategory, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    class Meta:
          db_table = 'dish'