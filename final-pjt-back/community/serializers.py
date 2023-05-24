from rest_framework import serializers
from .models import Post, Comment

class PostListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comment_set.count()
        
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('likes_count', 'comments_count',)


class CommentSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('post', 'user',)



class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    image = serializers.ImageField(use_url=True, required=False)
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    
    likes_count = serializers.SerializerMethodField()
    liked_users = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_liked_users(self, obj):
        return obj.get_liked_users()


    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'comment_set', 'comment_count', 'likes', 'likes_count', 'liked_users',)
        extra_kwargs = {
            'title': {'required': True},
            'content': {'required': True},
            'image': {'required': True},
        }
    
