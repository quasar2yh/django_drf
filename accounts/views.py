from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
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
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
