from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

app_name = "accounts"
router = DefaultRouter()
router.register(r'', UserViewSet, basename='accounts')

urlpatterns = router.urls