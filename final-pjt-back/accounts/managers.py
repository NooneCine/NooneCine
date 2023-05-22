from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, name, nickname, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        if not name:
            raise ValueError('The Name must be set')
        if not nickname:
            raise ValueError('The Nickname must be set')
            
        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email),
            name=name,
            nickname=nickname,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=True,
            last_login=now,
            joined_at=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


    def get_by_natural_key(self, username):
        return self.get(**{'{}__iexact'.format(self.model.USERNAME_FIELD): username})


    def create_user(self, email, password, name, nickname, **extra_fields):
        return self._create_user(email, password, name, nickname, False, False, **extra_fields)
    

    def create_superuser(self, email, password, name, nickname):
        return self._create_user(email, password, name, nickname, True, True, **extra_fields)

