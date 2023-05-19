# from django.contrib.auth.base_user import BaseUserManager
# from django.utils.translation import gettext_lazy as _

# class UserManager(BaseUserManager):
#     use_in_migrations = True
    
#     def create_user(self, email, name, nickname, password, **extra_fields):
#     # def create_user(self, email, password, **extra_fields):
#         if not email:
#             raise ValueError(_('The Email must be set'))
#         if not name:
#             raise ValueError(_('The Name must be set'))
#         if not nickname:
#             raise ValueError(_('The Nickname must be set'))
            
#         user = self.model(
#             email=self.normalize_email(email),
#             name=name,
#             nickname=nickname,
#             **extra_fields
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user


#     def create_superuser(self, email, password):
#         user = self.create_user(
#             email=self.normalize_email(email),
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user
#     # # def create_superuser(self, email, name, nickname, password, **extra_fields):
#     # def create_superuser(self, email, password, **extra_fields):
#     #     extra_fields.setdefault('is_staff', True)
#     #     extra_fields.setdefault('is_superuser', True)
#     #     extra_fields.setdefault('is_active', True)

#     #     if extra_fields.get('is_staff') is not True:
#     #         raise ValueError(_('Superuser must have is_staff=True.'))
#     #     if extra_fields.get('is_superuser') is not True:
#     #         raise ValueError(_('Superuser must have is_superuser=True.'))
#     #     return self.create_user(email, name, nickname, password, **extra_fields)
#     #     # return self.create_user(email, password, **extra_fields)