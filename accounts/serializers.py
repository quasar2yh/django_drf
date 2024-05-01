from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password


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

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)
