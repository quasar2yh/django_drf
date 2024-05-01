from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name',
                  'birthday', 'gender', 'self_introduction']
        extra_kwargs = {
            'username': {'required': True},
            'name': {'required': True},
            'birthday': {'required': True},
            'password': {'write_only': True,
                         'required': True,
                         },
            'email': {'required': True},
            'self_introduction': {'required': False},
        }
