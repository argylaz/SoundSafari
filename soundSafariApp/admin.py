from django.contrib import admin
from soundSafariApp.models import Genre, Artist, Album, Song, Page, UserProfile, Review

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display=('username', 'password')

class ArtistsAdmin(admin.ModelAdmin):
    list_display=('name')

class SongAdmin(admin.ModelAdmin):
    list_display=('name', 'duration', 'album')
    prepopulated_fields={'slug':('name',)}

class GenreAdmin(admin.ModelAdmin):
    list_display=('name')

class AlbumAdmin(admin.ModelAdmin):
    list_display=('name', 'duration', 'release_date')


admin.site.register(UserProfile)
admin.site.register(Artist)
admin.site.register(Song, SongAdmin)
admin.site.register(Genre)
admin.site.register(Album)
admin.site.register(Review)
admin.site.register(Page)
