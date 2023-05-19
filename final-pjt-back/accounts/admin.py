# from django.contrib import admin
# from .models import User
# from django.contrib.auth.admin import UserAdmin
# # # from django.utils.translation import gettext_lazy as _

# # Register your models here.
# # class MyUserAdmin(UserAdmin):
# #     model = User
# #     list_display = ("email", "name", "nickname")
# #     # search_fields = ("email", "nickname",)
# #     ordering = ("email",)

# #     fieldsets = UserAdmin.fieldsets + (("Custom fields", {"fields": ("name", "nickname",)}),)

# admin.site.register(User, UserAdmin)
# UserAdmin.fieldsets += (("Custom fields", {"fields": ("nickname",)}),)