from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    path('', views.post_list),
    path('<int:post_pk>/', views.post_detail),
    # path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('posts/<int:post_pk>/comments/', views.comment_create),
    # path('posts/<int:post_pk>/like/', views.PostLikeView.as_view(), name='post-like'),
    # path('posts/<int:post_pk>/unlike/', views.PostLikeView.as_view(), name='post-unlike'),
]

# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import PostViewSet

# router = DefaultRouter()
# router.register('post', PostViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]