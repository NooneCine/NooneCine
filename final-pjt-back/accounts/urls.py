from django.conf.urls import url
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^register/$', views.RegisterView.as_view(), name='user-register'),
    url(r'^login/$', views.LoginView.as_view(), name='user-login'),
    url(r'^logout/$', views.LogoutView.as_view(), name='user-logout'),
    url(r'^profile/$', views.UserProfileView.as_view(), name='user-profile'),
]