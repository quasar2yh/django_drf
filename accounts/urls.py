from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (UserViewSet, FollowingViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)

app_name = "accounts"

# 로그인
urlpatterns = [
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path('signup/', UserViewSet.as_view({'post': 'create'}), name='signup'),
    path('logout/', UserViewSet.as_view({'post': 'logout'}), name='logout'),
    path('<str:username>/',
         UserViewSet.as_view({'get': 'retrieve'}), name='profile'),
    path('followings/<str:username>/',
         FollowingViewSet.as_view({'put': 'update'}), name='followings'),
]
