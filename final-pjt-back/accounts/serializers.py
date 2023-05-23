from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User
from .validators import validate_username


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(username=attrs['email'], password=attrs['password'])

        if not user:
            raise serializers.ValidationError('Incorrect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}



class UserSerializer(serializers.ModelSerializer):
    # 기본값이 True라서 안해줘도 되는 것 같긴 함
    profile_img = serializers.ImageField(use_url=True, required=False)

    class Meta:
        model = User
        fields = (
            'id',
            'last_login',
            'email',
            'name',
            'nickname',
            'profile_img',
            'favorite_movie',
            'is_active',
            'password'
        )
        read_only_fields = ('last_login', 'is_active')
        extra_kwargs = {
            'password': {'required': True, 'write_only': True},
            'name': {'required': True},
            'nickname': {'required': True},
            # 'profile_img': {},
            # 'favorite_movie': {}
        }

    @staticmethod
    def validate_email(value):
        return validate_username(value)


    def create(self, validated_data):
        profile_img = validated_data.pop('profile_img', None)
        user = User.objects.create_user(
            validated_data.pop('email'),
            validated_data.pop('password'),
            **validated_data
        )
        return user
