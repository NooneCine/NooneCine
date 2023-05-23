from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from .managers import UserManager
from django.utils import timezone


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20, unique=True)

    profile_img = models.ImageField(upload_to='%Y/%m/%d/', null=True, blank=True)
    favorite_movie = models.CharField(max_length=100, null=True, blank=True)

    is_staff = models.BooleanField('Is staff', default=False)
    is_active = models.BooleanField('Is active', default=True)
    is_superuser = models.BooleanField('Is superuser', default=True)
    joined_at = models.DateTimeField('Joined at', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    # AbstractUser 모델에서 username이 필수적이라 REQUIRED_FIELDS에 username을 포함하지 않으면
    # superuser를 만들 때 username이 없어서 typeerror가 발생
    REQUIRED_FIELDS = ['username']
