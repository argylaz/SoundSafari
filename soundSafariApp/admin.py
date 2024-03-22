from django.contrib import admin
from soundSafariApp.models import Genre, Artist, Album, Song, Page, UserProfile, Review

admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Album)
admin.site.register(Song)
admin.site.register(Page)
admin.site.register(UserProfile)
admin.site.register(Review)


from soundSafariApp.models import UserProfile, Artist, Song, Genre, Album
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
