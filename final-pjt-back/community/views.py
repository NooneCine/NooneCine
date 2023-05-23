from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import PostListSerializer, PostSerializer, CommentSerializer
from .models import Post, Comment


# Create your views here.
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def post_list(request):
    if request.method == 'GET':
        posts = get_list_or_404(Post)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PostListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# class PostViewSet(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        if comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)

        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        if comment.user != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(post=post, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class PostLikeView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        post.like(request.user)
        return Response({'message': 'Post liked'})

    def delete(self, request, post_pk):
        post = get_object_or_404(Post, pk=post_pk)
        post.unlike(request.user)
        return Response({'message': 'Post unliked'})