from django.db import models

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    country = models.CharField(max_length=100)

class Scenario(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    movie = models.OneToOneField('Movie', on_delete=models.CASCADE, null=True, related_name='scenario')

class Film(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    duration_minutes = models.IntegerField()
    genre = models.CharField(max_length=100)
    director = models.ForeignKey('Director', on_delete=models.CASCADE, related_name='films')
    scenario = models.ForeignKey('Scenario', on_delete=models.CASCADE, null=True, related_name='films')

class Actor(models.Model):
    last_name = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    age = models.IntegerField()
    movies = models.ManyToManyField('Movie', related_name='actors')

class Movie(models.Model):
    film = models.OneToOneField('Film', on_delete=models.CASCADE, related_name='movie')

class Play(models.Model):
    movie = models.ForeignKey(Film, on_delete=models.CASCADE)
    actor = models.ForeignKey(Actor, on_delete=models.CASCADE)