from django.urls import path
from soundSafariApp import views

app_name = 'soundSafariApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('guide/', views.guide, name='guide'),

    #URLS for genre things
    path('genres/', views.genres, name='genres'),
    path('genres/add/', views.add_genre, name='add_genre'),
    #Forms
    path('genres/<slug:artist_name_slug>/<slug:song_name_slug>/', views.show_single, name='show_single_genre'),
    path('genres/<slug:song_name_slug>/add_review/', views.add_song_review, name='add_song_review'),

    #URLS for Account Things
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/<str:username>', views.user_profile, name='user_profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    #URLS for all artist things
    path('artists/', views.artists, name='artists'), 
    path('artists/<slug:artist_name_slug>/', views.show_artist, name='show_artist'),
    path('artists/<slug:artist_name_slug>/<slug:album_name_slug>/', views.show_album, name='show_album'),
    path('artists/<slug:artist_name_slug>/<slug:album_name_slug>/<slug:song_name_slug>/', views.show_song, name='show_song'),
    path('genres/<slug:artist_name_slug>/<slug:song_name_slug>/', views.show_single, name='show_single_genre'),
    #Forms
    path('artists/<slug:artist_name_slug>/add_album/', views.add_album, name='add_album'),
    path('artists/add_artist/', views.add_artist, name='add_artist'),
    path('artist/<slug:artist_name_slug>/add_song/', views.add_song, name='add_song'),





    path('artists/<slug:artist_name_slug>/add_review_artist/', views.add_artist_review, name='add_artist_review')

]