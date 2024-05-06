from rest_framework import (viewsets, status, permissions)
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .models import (User, Profile)
from .serializers import UserSerializer, ProfileSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404


class UserViewSet(viewsets.ViewSet):

    # 회원가입
    def create(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            # username이 고윳값인지 검사
            if User.objects.filter(
                    username=serializer.validated_data['username']).exists():
                return Response(
                    {'error': '이미 존재하는 username 입니다.'},
                    status=status.HTTP_400_BAD_REQUEST)
            # email이 고윳값인지 검사
            if User.objects.filter(
                    email=serializer.validated_data['email']).exists():
                return Response(
                    {'error': '이미 존재하는 이메일 입니다.'},
                    status=status.HTTP_400_BAD_REQUEST)
            user = serializer.save()  # 유저 생성시, 프로필 내용도 생성 할 수 있도록
            Profile.objects.create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 로그아웃
    # TODO 클라이언트의 access token 삭제
    @action(detail=False, methods=['post'])
    def logout(self, request):
        """
        access token은 유효기간이 짧기 때문에 우선 refresh token을 폐기하는 방식으로 진행함.
        """
        try:
            # 클라이언트로부터 'refresh' 토큰을 받아서 삭제
            refresh_token = request.data.get('refresh')
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(
                {'success': '로그아웃이 성공적으로 완료되었습니다.'},
                status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(
                {'error': f'잘못된 요청입니다. ({e})'},
                status=status.HTTP_400_BAD_REQUEST)

    # 유저 프로필
    def retrieve(self, request, username=None):
        permission_classes = [permissions.IsAuthenticated]
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.all()
        user_profile = Profile.objects.get(user=user.pk)
        serializer = ProfileSerializer(user_profile)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowingViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, username=None):
        get_follow = get_object_or_404(User, username=username)
        print(f'#############{get_follow=}')
        get_follow_profile = Profile.objects.get(user=get_follow)
        if request.user != get_follow:
            if request.user in get_follow_profile.followers.all():
                get_follow_profile.followers.remove(request.user)
            else:
                get_follow_profile.followers.add(request.user)
