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
    image = serializers.ImageField(use_url=True, required=False)
    # 해당 포스터에 요청한 사용자가 좋아요를 눌렀는지 여부를 나타냄
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'comment_set', 'comment_count')
        extra_kwargs = {
            'title': {'required': True},
            'content': {'required': True},
        }
    
    def get_is_liked(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            return obj.is_liked_by(user)
        return False




