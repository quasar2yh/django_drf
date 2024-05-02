from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import (UserViewSet, FollowingViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

app_name = "accounts"

# 로그인
urlpatterns = [
    path("signin/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

# 회원 가입
urlpatterns += [path('',
                     UserViewSet.as_view({'post': 'create'}), name='signup')]

# 프로필
urlpatterns += [path('<str:username>/',
                     UserViewSet.as_view({'get': 'retrieve'}), name='profile')]

# 팔로잉
urlpatterns += [path('followings/<str:username>/',
                     FollowingViewSet.as_view({'put': 'update'}), name='followings')]
