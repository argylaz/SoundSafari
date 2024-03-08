from django.urls import path
from soundSafariApp import views

app_name = 'SoundSafari'

urlpatterns = [
    path('', views.index, name='index'),

]