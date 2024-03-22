from django.urls import path
from soundSafariApp import views

app_name = 'soundSafariApp'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('about/', views.about, name='about'),
    path('guide/', views.guide, name='guide'),
    path('artists/', views.artists, name='artists'),
    path('genres/', views.genres, name='genres'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name='logout'),
    path('genres/add/', views.add_genre, name='add_genre'),
    path('artists/<slug:artist_name_slug>/', views.show_artist, name='show_artist'),
    path('artists/<slug:artist_name_slug>/<slug:album_name_slug>/', views.show_album, name='show_album'),

]