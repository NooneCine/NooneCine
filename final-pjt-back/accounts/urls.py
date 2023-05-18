from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignUp.as_view()),
    path('activate/<str:uidb64>/<str:token>/', views.UserActivate.as_view()),
]