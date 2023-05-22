from django.urls import path
from . import views

app_name = 'posts'
urlpatterns = [
    path('', views.post_list),
    path('<int:post_pk>/', views.post_detail),
    # path('<int:post_pk>/comments/', views.comment_create),
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import PostViewSet

# router = DefaultRouter()
# router.register('post', PostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]