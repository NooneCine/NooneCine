# from django.urls import path, include
# from . import views

# urlpatterns = [
#     path('', include('dj_rest_auth.urls')),
#     path('registration/', customSignUpView.as_view())
#     # path('registration/', include('dj_rest_auth.registration.urls')),
# ]


from django.urls import path
from .views import RegisterView, LoginView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
]