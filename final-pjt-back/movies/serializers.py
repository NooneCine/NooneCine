from rest_framework import serializers
from .models import Genre, Actor, Movie, Review


class ActorListSerializer(serializers.ModelSerializer):
    fan_count = serializers.IntegerField(source='fan.count', read_only=True)
    
    class Meta:
        model = Actor
        fields = ('name', 'profile_path', 'fan_count',)
        read_only_fields = ('fan_count',)


class MovieListSerializer(serializers.ModelSerializer):
    likes_count = serializers.IntegerField(source='likes.count', read_only=True)
    noonecine_count = serializers.IntegerField(source='noonecine.count', read_only=True)
    
    class Meta:
        model = Movie
        fields = ('title', 'overview', 'poster_path', 'likes_count', 'noonecine_count',)
        read_only_fields = ('likes_count', 'noonecine_count',)


class ReviewSerializer(serializers.ModelSerializer):
    user_nickname = serializers.CharField(source='user.nickname', read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ('movie', 'user',)


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title',)


class ActorDetailSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(many=True)
    
    class Meta:
        model = Actor
        fields = '__all__'



class MovieDetailSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    review_count = serializers.IntegerField(source='review_set.count', read_only=True)
    
    likes_count = serializers.SerializerMethodField()
    liked_users = serializers.SerializerMethodField()

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_liked_users(self, obj):
        return obj.get_liked_users()

    noonecine_count = serializers.IntegerField(source='noonecine.count', read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'
        read_only_fields = ('review_set', 'review_count', 'likes_count', 'noonecine_count',)



