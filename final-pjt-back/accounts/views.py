from django.shortcuts import render
from .models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import UserSerializer
from rest_framework.views import APIView
import traceback
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_text
from rest_framework import permissions
from .tokens import account_activation_token

# Create your views here.
class SignUp(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# user가 email 누르면 작동하는 부분
class UserActivate(APIView):
  permission_classes = (permissions.AllowAny,)

  def get(self, request, uidb64, token):
      try:
          uid = force_text(urlsafe_base64_decode(uidb64.encode('utf-8')))
          user = User.objects.get(pk=uid)
      except(TypeError, ValueError, OverflowError, User.DoesNotExist):
          user = None

      try:
          if user is not None and account_activation_token.check_token(user, token):
              user.is_active = True
              user.save()
              return Response(user.email + '계정이 활성화 되었습니다', status=status.HTTP_200_OK)
          else:
              return Response('만료된 링크입니다', status=status.HTTP_400_BAD_REQUEST)

      except Exception as e:
          print(traceback.format_exc())