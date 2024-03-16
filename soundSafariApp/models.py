from django.db import models

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=30)
    song_count = models.IntegerField()

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=30)
    birthDate=models.DateTimeField()
    picture = models.ImageField()

    def __str__(self):
        return self.name

class Album(models.Model):
    name = models.CharField(max_length=30)
    picture = models.ImageField()
    duation = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.name

class Song(models.Model):
    name = models.CharField(max_length=30)
    duration = models.IntegerField()
    release_date = models.DateField()

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    date_created = models.DateField()
    picture = models.ImageField()

    def __str__(self):
        return self.username

class Page(models.Model):
    avg_rating = models.IntegerField()
    # MIGHT NEED TO REMOVE THIS. NOT IN DESIGN SPECIFICATION BUT I THINK IT'S NEEDED
    url = models.URLField

class Review(models.Model):
    rating = models.IntegerField()
    date_added = models.DateField()
    comment = models.CharField(max_length=200)

    def __str__(self):
        return "Rating: " + str(self.rating) + '\n' + "Comment: " + str(self.comment)