from django.contrib import admin
from soundSafariApp.models import UserProfile, Artist, Song, Genre
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'password')

class ArtistsAdmin(admin.ModelAdmin):
    list_display=('name')

class SongAdmin(admin.ModelAdmin):
    list_display=('name', 'duration', 'album')

class GenreAdmin(admin.ModelAdmin):
    list_display=('name')


admin.site.register(UserProfile)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Genre)
