from rest_framework import (viewsets, status, permissions, generics)
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404


class ProductPagination(PageNumberPagination):
    page_size = 10  # Number of products per page
    page_query_param = 'page'  # Query parameter to specify the page number
    page_size_query_param = 'page_size'  # Query parameter to specify the page size
    max_page_size = 20  # Maximum number of products per page


class ProductViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {
        'create': [permissions.IsAuthenticated],
        'list': [permissions.IsAuthenticatedOrReadOnly],
        'update': [permissions.IsAuthenticated],
    }
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = Product.objects.all().order_by('-id')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        if product.author != request.user:
            raise PermissionDenied(
                "You do not have permission to edit this product.")

        serializer = ProductSerializer(
            product, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        product.delete()
        data = {"pk": f"(no.{pk} article) '{product.title}' is deleted."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)
