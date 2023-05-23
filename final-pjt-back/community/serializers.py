from rest_framework import serializers
from .models import Post, Comment

class PostListSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('likes_count',)


class CommentSerializer(serializers.ModelSerializer):
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
    liked = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(pk=request.user.pk).exists()
        return False

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'comment_set', 'comment_count', 'likes', 'likes_count', 'liked',)
        extra_kwargs = {
            'title': {'required': True},
            'content': {'required': True},
        }
    
    # def to_representation(self, instance):
    #     representation = super().to_representation(instance)
    #     if not representation['image']:
    #         representation['image'] =  static('default.png')  # 기본 이미지 경로를 지정
    #     return representation
    
    # def get_image(self, obj):
    #     if obj.image:
    #         return obj.image.url
    #     return self.context['request'].build_absolute_uri(DEFAULT_IMAGE)


