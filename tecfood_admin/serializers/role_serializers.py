from rest_framework import serializers
from tecfood_admin.models import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = [
            'role_id',
            'name',
            'created_at',
            'updated_at'
        ]