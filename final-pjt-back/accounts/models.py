# from django.contrib.auth.models import AbstractUser
# from django.db import models
# from django.utils.translation import gettext_lazy as _

# from .managers import UserManager

# class User(AbstractUser):
#     username = None
#     email = models.EmailField(_("이메일"), unique=True)
#     name = models.CharField(_("이름"), max_length=10)
#     nickname = models.CharField(_("닉네임"), max_length=10)

#     # profile_img = models.ImageField(_("프로필 사진"), upload_to=None, null=True, blank=True)
#     # favorite_movie = models.CharField(_("인생 영화"), max_length=100, null=True, blank=True)

#     objects = UserManager()

#     USERNAME_FIELD = 'email'
#     # REQUIRED_FIELDS: 필수로 받고 싶은 필드
#     REQUIRED_FIELDS = []

#     def __str__(self):
#         return self.email


from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=20, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []