from django.contrib.auth.models import AbstractUser
from django.db import models
from tecfood_admin.models.role import Role
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone_number = models.CharField(max_length=9)  
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=250)
    dni = models.CharField(max_length=8, unique=True)  
    img_url = CloudinaryField('image',null=True, blank=True)
    is_google_account = models.BooleanField(default=False)
    is_verified_email = models.BooleanField(default=False)

    # Foreign key
    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)
    

    # Django default fields
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    username = models.CharField(max_length=150, unique=True, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    