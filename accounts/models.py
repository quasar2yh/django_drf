from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    name = models.CharField(max_length=150)
    birthday = models.DateField()
    GENDER = [
        ("M", "male"),
        ("F", "female"),
    ]
    gender = models.CharField(choices=GENDER, max_length=1)
    first_name = None
    last_name = None

    REQUIRED_FIELDS = ['name', 'birthday', 'gender']

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    interset = models.CharField(max_length=100, null=True)
    self_introduction = models.TextField(null=True)
    following = models.ManyToManyField(
        "self", symmetrical=False, related_name="followers")

