from django.db import models
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=30)
    song_count = models.IntegerField(default = 0)

    # Method to calculate sng count
    def count_songs(self):
        self.song_count = Song.objects.filter(genre=self).count()
        self.save()

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=30)
    birthDate=models.DateField(null=True,default=None)
    picture = models.ImageField()
    slug = models.SlugField(unique=True, blank=True)

    # Creating a page for the artist
    def create_page(self):
        page = {
            "artist" : self,
            "url" : "artist/" + self.slug,
            "name" : self.name
        }

        Page.objects.create(**page)

    def save(self, *args, **kwargs):
        # Implementing slug
        if not self.slug:
            self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

        # Whenever an artist page is created, an equivalent page should also be created
        self.create_page()

    def __str__(self):
        return self.name

class Album(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=30)
    picture = models.ImageField()
    duration = models.IntegerField(default = 0)
    release_date = models.DateField(null=True,default=None)
    slug = models.SlugField(null=True, unique = True)

    # Method to calculate duration of album by summing durations of songs in it
    def calc_duration(self):
        songs = Song.objects.filter(album=self)
        self.duration = sum([s.duration for s in songs])

    # Creating a page for the album
    def create_page(self):
        page = {
            "album" : self,
            "url" : "album/" + self.slug,
            "name" : self.name
        }

        Page.objects.create(**page)


    def save(self, *args, **kwargs): #slug implemenetd
        # Calculate duration
        self.calc_duration()

        # Define slug
        if not self.slug:

            self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)

        # Whenever an album is created an equivalent page must also be created
        self.create_page()


    def __str__(self):
        return self.name

class Song(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,null=True, default=None)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,null=True, default=None)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True, default=None)
    
    name = models.CharField(max_length=30)
    duration = models.IntegerField()
    release_date = models.DateField(null=True,default=None)
    slug = models.SlugField(unique=True)

    # Creating a page for the song
    def create_page(self):
        page = {
            "song" : self,
            "url" : "song/" + self.slug,
            "name" : self.name
        }

        Page.objects.create(**page)

    def save(self, *args, **kwargs): #slug implemented
        if not self.slug:
            self.slug = slugify(self.name)
        super(Song, self).save(*args, **kwargs)

        # Whenever a Song is created, an associated page should be created too
        self.create_page()

        # Whenever a song is created we need to update the genre song_coun
        self.genre.count_songs()

    def __str__(self):
        return self.name


# A page can either represent an artist page, an album page or a song page
# This is the entity that users will review.
class Page(models.Model):
    # These three foreign keys will represent the type of the page
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE, null=True, blank=True)
    album = models.OneToOneField(Album, on_delete=models.CASCADE, null=True, blank=True)
    song = models.OneToOneField(Song, on_delete=models.CASCADE, null=True, blank=True)


    name = models.CharField(max_length=30, default='page') # Name of album/Song/Artist associated with the page for use in Page.objects.get()
    avg_rating = models.IntegerField(default=0)            # Just a starting value of 0 when there are no reviews
    url = models.URLField(null=True)

    # Calculates the average rating of the page 
    def calc_avg(self):
        reviews = Review.objects.filter(page=self)

        count = reviews.count()
        if count != 0:
            self.avg_rating = sum([r.rating for r in reviews]) / count

        self.save() 


    # Overriding the clean method to also ensure that two of the foreign keys are null
    # and exactly one of them is not null
    def clean(self):
        super().clean()

        foreign_keys_count = sum(
            1 for field in [self.artist, self.album, self.song] if field
        )
        if foreign_keys_count != 1:
            raise ValidationError("Exactly one foreign key must be not null.")
        
    # Overriding save method to call full_clean method
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return  self.name + " page with average rating: " + str(self.avg_rating)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateField(null=True,default=None)
    picture = models.ImageField(default="static/images/defaultUsrImg.jpg")

    def __str__(self):
        return self.user.username
    
class Review(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True)

    rating = models.IntegerField()
    date_added = models.DateField(null=True,default=None)
    comment = models.CharField(max_length=200, null=True) # Comment is optional 

    # Overriding save method to call the method that calculates the average rating for the page
    def save(self, *args, **kwargs):
        self.page.calc_avg()
        
        super().save(*args, **kwargs)

    def __str__(self):
        return "Rating: " + str(self.rating) + '\n' + "Comment: " + str(self.comment)
    