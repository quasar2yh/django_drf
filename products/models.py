from accounts.models import User
from django.db import models
import sys
sys.path.append("..")


class Product(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField(null=True)
    price = models.PositiveBigIntegerField()
    image = models.ImageField(upload_to='images/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
