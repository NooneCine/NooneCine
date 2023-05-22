from rest_framework import serializers
from .models import Post, Comment

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        # read_only_fields = ()


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'user',)


class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:
        model = Post
        fields = ('id', 'user_nickname', 'title', 'content', 'image')
        # read_only_fields = ('user',)




