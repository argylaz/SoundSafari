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
    path('profile/', views.profile, name='profile'),

]