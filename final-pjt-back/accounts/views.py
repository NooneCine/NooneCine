# # from django.shortcuts import render
# from django.contrib.auth.models import User
# # from rest_framework import viewsets
# from rest_framework import generics
# from .serializers import CustomRegisterSerializer

# # # Create your views here.

# class RegisterView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = RegisterSerializer


# class customSignUpView(RegisterView) :
#     serializer_class = CustomRegisterSerializer

from django.contrib.auth.models import AbstractUser
from rest_framework import generics, status
from rest_framework.response import Response
from .models import User
from .serializers import RegisterSerializer, LoginSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    
class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.validated_data
        return Response({"token": token.key}, status=status.HTTP_200_OK)