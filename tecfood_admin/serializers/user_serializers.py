from rest_framework import serializers
from tecfood_admin.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'user_id',
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'password',
            'dni',   
            'role_id',
        ]


