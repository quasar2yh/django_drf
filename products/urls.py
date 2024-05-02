from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

app_name = "products"

# ViewSet을 Router에 등록
router = DefaultRouter()
router.register("", views.ProductViewSet, basename='product')
urlpatterns = router.urls