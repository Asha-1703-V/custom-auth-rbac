from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from .serializers import RegisterSerializer, UserSerializer
from core.permissions import CustomRBACPermission
from rest_framework.permissions import AllowAny


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Пользователь зарегистрирован'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            if not user.is_active:
                return Response({'error': 'Аккаунт деактивирован'}, status=status.HTTP_400_BAD_REQUEST)
            login(request, user)
            return Response({'message': 'Успешный вход!', 'user': UserSerializer(user).data})
        return Response({'error': 'Неверные данные'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [CustomRBACPermission]

    def post(self, request):
        logout(request)
        return Response({'message': 'Выход выполнен'})


class ProfileView(APIView):
    permission_classes = [CustomRBACPermission]

    def get(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        request.user.is_active = False
        request.user.save()
        logout(request)
        return Response({'message': 'Аккаунт деактивирован'}, status=status.HTTP_204_NO_CONTENT)

