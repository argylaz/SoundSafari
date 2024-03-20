from soundSafariApp.models import Album,Artist,Song,Genre,UserProfile
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), required= True)
    username = forms.CharField(required=True, max_length=30)


    class Meta:
        model=User
        fields = ('username','password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields=('date_created','picture')

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=30, help_text="Please enter the genre name")
    song_count = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Genre
        fields = ('name','song_count')
