from django.db import models
from django.core.exceptions import ValidationError
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=30)
    song_count = models.IntegerField(default = 0)

    def __str__(self):
        return self.name

class Artist(models.Model):
    name = models.CharField(max_length=30)
    birthDate=models.DateField(null=True,default=None)
    picture = models.ImageField()
    slug = models.SlugField(unique=True, blank=True)


    def save(self, *args, **kwargs): #slug implemented 
        if not self.slug:
            self.slug = slugify(self.name)
        super(Artist, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Album(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=True)

    name = models.CharField(max_length=30)
    picture = models.ImageField()
    duration = models.IntegerField()
    release_date = models.DateField(null=True,default=None)
    slug = models.SlugField(null=True, unique = True)

    def save(self, *args, **kwargs): #slug implemenetd
        if not self.slug:

            self.slug = slugify(self.name)
        super(Album, self).save(*args, **kwargs)


    def __str__(self):
        return self.name

class Song(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE,null=True)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE,null=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, null=True)
    
    name = models.CharField(max_length=30)
    duration = models.IntegerField()
    release_date = models.DateField(null=True,default=None)
    slug = models.SlugField(null=True, unique = True)

    def save(self, *args, **kwargs): #slug implemented
        if not self.slug:
            self.slug = slugify(self.name)
        super(Song, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


# A page can either represent an artist page, an album page or a song page
# This is the entity that users will review.
class Page(models.Model):
    # These three foreign keys will represent the type of the page
    # 
    artist = models.OneToOneField(Artist, on_delete=models.CASCADE, null=True, blank=True)
    album = models.OneToOneField(Album, on_delete=models.CASCADE, null=True, blank=True)
    song = models.OneToOneField(Song, on_delete=models.CASCADE, null=True, blank=True)

    avg_rating = models.IntegerField()
    url = models.URLField(null=True)

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
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return  "Page with average rating: " + str(self.avg_rating)

<<<<<<< Updated upstream
=======
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateField(null=True,default=None)
    picture = models.ImageField(default="static/images/defaultUsrImg.jpg")
    bio = models.TextField(blank=True, null=True) 

    def __str__(self):
        return self.user.username
    
>>>>>>> Stashed changes
class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    page = models.ForeignKey(Page, on_delete=models.CASCADE, null=True)

    rating = models.IntegerField()
    date_added = models.DateField(null=True,default=None)
    comment = models.CharField(max_length=200, null=True) # Comment is optional 

    def __str__(self):
        return "Rating: " + str(self.rating) + '\n' + "Comment: " + str(self.comment)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date_created = models.DateField(null=True,default=None)
    picture = models.ImageField()

    def __str__(self):
        return self.user.username