from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import PostListSerializer, PostSerializer, CommentSerializer
from .models import Post, Comment


# Create your views here.
@api_view(['GET', 'POST'])
def post_list(request):
    pass


@api_view(['GET', 'DELETE', 'PUT'])
def post_detail(request):
    pass


# @api_view(['POST'])
# def comment_create(request, post_pk):
#     pass