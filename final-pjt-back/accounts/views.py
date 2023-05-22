from django.conf import settings
from django.contrib.auth import login, logout
from rest_framework import views, generics, response, permissions, authentication
from rest_framework.authtoken.models import Token
from .models import User
from .serializers import UserSerializer, LoginSerializer


class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return response.Response({'token': token.key, 'user': UserSerializer(user).data})


class LogoutView(views.APIView):
    def post(self, request):
        logout(request)
        return response.Response()


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        user.backend = settings.AUTHENTICATION_BACKENDS[0]
        login(self.request, user)
        token, _ = Token.objects.get_or_create(user=user)
        return response.Response({'token': token.key, 'user': UserSerializer(user).data})


class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'

    def get_object(self, *args, **kwargs):
        return self.request.user

