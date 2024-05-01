from rest_framework import serializers
from .models import User, Profile
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'name',
                  'birthday', 'gender']
        extra_kwargs = {
            'username': {'required': True},
            'name': {'required': True},
            'birthday': {'required': True},
            'password': {'write_only': True,
                         'required': True,
                         },
            'email': {'required': True},
        }

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    name = serializers.SerializerMethodField()
    gender = serializers.SerializerMethodField()
    birthday = serializers.SerializerMethodField()
    email = serializers.SerializerMethodField()
    date_joined = serializers.SerializerMethodField()
    last_login = serializers.SerializerMethodField()
    follower_count = serializers.IntegerField(
        source="followers.count", read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'

    def get_username(self, obj):
        return obj.user.username

    def get_name(self, obj):
        return obj.user.name

    def get_gender(self, obj):
        return obj.user.gender

    def get_birthday(self, obj):
        return obj.user.birthday

    def get_email(self, obj):
        return obj.user.email

    def get_date_joined(self, obj):
        return obj.user.date_joined

    def get_last_login(self, obj):
        return obj.user.last_login

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret.pop("user")
        return ret
