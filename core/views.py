from django.shortcuts import render
from django.contrib.auth import login, logout
from rest_framework.generics import CreateAPIView, UpdateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView
from rest_framework.response import Response
from rest_framework import permissions
from core.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from core.serializers import CreateUserSerializer, UserSerializer, LoginSerializer, UpdatePasswordSerializer


# Create your views here.

class SignupView(CreateAPIView):
    model = User
    permission_classes = [permissions.AllowAny]
    serializer_class = CreateUserSerializer


# @method_decorator(csrf_exempt, name='dispatch')
class LoginApiView(GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        s: LoginSerializer = self.get_serializer(data=request.data)
        s.is_valid(raise_exception=True)
        user = s.validated_data["user"]
        login(request, user=user)
        user_serializer = UserSerializer(instance=user)
        return Response(user_serializer.data)


# @method_decorator(csrf_exempt, name='dispatch')
class ProfileView(RetrieveUpdateDestroyAPIView):
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        logout(request)
        return Response({})


# @method_decorator(csrf_exempt, name='dispatch')
class UpdatePasswordView(UpdateAPIView):
    model = User
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UpdatePasswordSerializer

    def get_object(self):
        return self.request.user
