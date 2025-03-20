from tokenize import TokenError

from django.contrib.auth import get_user_model, authenticate
from django.template.context_processors import request
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from libraryApi.accounts.serializers import RegisterSerializer, LoginRequestSerializer, LoginResponseSerializer, \
    LogoutResponseSerializer

UserModel = get_user_model()

class RegisterApiView(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = RegisterSerializer


@extend_schema(
    tags=['accounts'],
    summary="Login endpoint",
    description="Authenticate a user and get back access and refresh tokens",
    request=LoginRequestSerializer,
    responses={
        200: LoginResponseSerializer,
        400: "Invalid username or password",
    },
)
class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(
            username=username,
            password=password,
        )

        if user is None:
            return Response(
                {
                    "error": "Invalid username or password"
                },status=status.HTTP_401_UNAUTHORIZED,)

        refresh = RefreshToken.for_user(user)

        return  Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "message": "Login successful",
        }, status=status.HTTP_200_OK)

@extend_schema(
    tags=['accounts'],
    summary="Logout endpoint",
    description="Blacklist the refresh token",
    request=LoginRequestSerializer,
    responses={
        200: LogoutResponseSerializer,
        400: "Invalid refresh token",
    },
)
class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        refresh = request.data.get('refresh')

        try:
            token = RefreshToken(refresh)
            token.blacklist()
        except TokenError:
            return Response(
                {
                    "error": "Invalid refresh token"
                }, status=status.HTTP_400_BAD_REQUEST,)

        return Response({
            "message": "Logout successful"
        }, status=status.HTTP_200_OK)