from rest_framework import serializers
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'current_year', 'school']
        extra_kwargs = {
            'password': {'write_only': True}
        }

