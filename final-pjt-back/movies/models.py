from django.db import models
from django.conf import settings

# # Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=50)


class Actor(models.Model):
    name = models.CharField(max_length=100, null=True)
    original_name = models.CharField(max_length=300, null=True)
    profile_path = models.CharField(max_length=300, null=True)
    gender = models.IntegerField()
    birth = models.DateField()
    fan = models.ManyToManyField(settings.AUTH_USER_MODEL)
    

class Movie(models.Model):
    title = models.CharField(max_length=300, default='None')
    original_title = models.CharField(max_length=300, default='None')
    overview = models.TextField()
    poster_path = models.CharField(max_length=300, null=True)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_count = models.IntegerField()
    vote_average = models.FloatField()
    runtime = models.IntegerField()
    director = models.CharField(max_length=100) # Director model 만들어서 fk?

    genres = models.ManyToManyField(Genre, related_name='movies')
    actors = models.ManyToManyField(Actor, related_name='movies')
    
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='likes_movies')
    watched = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='watched_movies')
    noonecine = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='noone_movies')


class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    noone_score = models.IntegerField(default=0)