# from django.db import models

# # Create your models here.
# class Genre(models.Model):
#     name = models.CharField(max_length=50)


# class Movie(models.Model):
#     title = models.CharField(max_length=100)
#     release_date = models.DateField()
#     popularity = models.FloatField()
#     vote_count = models.IntegerField()
#     vote_average = models.FloatField()
#     overview = models.TextField()
#     poster_path = models.CharField(max_length=200)
#     genres = models.ManyToManyField(Genre)
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     likes = models.ManyToManyField(settings.AUTH_USER_MODEL)
#     watched = models.ManyToManyField(settings.AUTH_USER_MODEL)


# class Celebrity(models.Model):
#     name = models.CharField(max_length=100)
#     image = models.ImageField()
#     gender = models.models.IntegerField()
#     birth = models.DateField()
#     fan = models.ManyToManyField(settings.AUTH_USER_MODEL)
#     # filmography = 
#     # known_for_department =


# class Review(models.Model):
#     user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
#     movie = models.ForeignKey()
#     context = models.TextField()
#     # noone = 