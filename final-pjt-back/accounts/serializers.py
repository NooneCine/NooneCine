# from rest_framework_simplejwt.serializers import TokenObtainSerializer
# from .models import User
# from rest_framework import serializers
# from rest_auth.registration.serializers import RegisterSerializer
# from allauth.account import app_settings as allauth_settings
# from allauth.utils import email_address_exists
# from allauth.account.adapter import get_adapter
# from allauth.account.utils import setup_user_email
# from django.utils.translation import ugettext_lazy as _

# class CustomRegisterSerializer(RegisterSerializer):
#     nickname = serializers.CharField(required=True)
#     name = serializers.CharField(required=True)

#     def validate_email(self, email):
#         email = get_adapter().clean_email(email)
#         if allauth_settings.UNIQUE_EMAIL:
#             if email and email_address_exists(email):
#                 raise serializers.ValidationError(
#                     _("A user is already registered with this e-mail address."))
#         return email

#     def validate_password1(self, password):
#         return get_adapter().clean_password(password)

#     def get_cleaned_data(self):
#         return {
#             'email': self.validated_data.get('email', ''),
#             'password': self.validated_data.get('password', ''),
#             'nickname': self.validated_data.get('nickname', ''),
#             'name': self.validated_data.get('name', ''),
#         }

#     def save(self, request):
#         adapter = get_adapter()
#         user = adapter.new_user(request)
#         self.cleaned_data = self.get_cleaned_data()
#         adapter.save_user(request, user, self)
#         setup_user_email(request, user, [])
#         user.save()
#         return user

# class userSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('email', 'password', 'nickname', 'name')


from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator
from .models import User

# 회원가입
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
    )
    password2 = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('email', 'password', 'password2', 'name', 'nickname')
        
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})
        return data
    
    def create(self, validated_data):
        user = User.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            username=validated_data['email'].split('@')[0],
            nickname=validated_data['nickname'],
        )
        user.set_password(validated_data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return {user, token}
        
# 로그인
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
    
    def validate(self, data):
        user = authenticate(**data)
        if user:
            token = Token.objects.get(user=user)
            return token
        raise serializers.ValidationError(
            {"error": "Unable to log in with provided credentials."})