from soundSafariApp.models import Album,Artist,Song,Genre,User,UserProfile, Page, Review
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
        fields=('picture',)

class GenreForm(forms.ModelForm):
    name = forms.CharField(max_length=30, help_text="Please enter the genre name")
    song_count = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Genre
        fields = ('name','song_count')

class ArtistForm(forms.ModelForm):
    name = forms.CharField(max_length=30, help_text="Please enter the Artist name")
    birthDate = forms.DateField(required=False, initial=None)
    picture = forms.ImageField()

    class Meta:
        model = Artist
        fields = ('name','birthDate','picture')

class AlbumForm(forms.ModelForm):
    name = forms.CharField(max_length=30, help_text="Please enter the album name")
    picture = forms.ImageField()
    duration = forms.IntegerField()
    release_date = forms.DateField(required=False, initial=None)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)
    
    class Meta:
        model = Album
        fields = ('name','picture','duration','release_date','genre','artist')

class SongForm(forms.ModelForm):
    name = forms.CharField(max_length=30, help_text="Please enter the song name")
    duration = forms.IntegerField()
    release_date = forms.DateField(required=False, initial=None)
    genre = forms.ModelChoiceField(queryset=Genre.objects.all())
    artist = forms.ModelChoiceField(queryset=Artist.objects.all())
    album = forms.ModelChoiceField(queryset=Album.objects.all(), required= False)
    slug = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Song
        fields = ('name','duration','release_date','genre','artist','album')

class ReviewForm(forms.ModelForm):
    rating = forms.IntegerField()
    date_added = forms.DateField(required=False, initial=None)
    comment= forms.CharField(max_length=200,required=False)
    user = forms.ModelChoiceField(queryset=User.objects.all())
    page= forms.ModelChoiceField(queryset=Page.objects.all())

    class Meta:
        model= Review
        fields=('rating','date_added','user','page','comment')



class EditProfileForm(forms.ModelForm):
    username = forms.CharField(required=False)  

    class Meta:
        model = UserProfile
        fields = ['picture', 'username', 'bio'] 
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}), 
            'picture': forms.FileInput(attrs={'class': 'form-control'}),
        }

        