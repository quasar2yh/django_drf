from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'
        # is_valid()에서 author 정보 요구를 피하기 위해 추가
        read_only_fields = ("author",)
