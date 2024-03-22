from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from soundSafariApp.models import Artist, UserProfile, Song, Genre, Album, Review
from soundSafariApp.forms import UserForm, UserProfileForm, GenreForm

# Create your views here.

def index(request):
    return render(request, 'soundSafariApp/index.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('soundSafariApp:index'))
            else:
                return HttpResponse("Your account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'soundSafariApp/login.html')
    
def about(request):
    return render(request, 'soundSafariApp/about.html')

def artists(request):
    artists_list=Artist.objects.all()
    contextdict={'artists': artists_list}
    return render(request, 'soundSafariApp/artists.html', contextdict)

def genres(request):
    genreslist=Genre.objects.all()
    songsdict={}
    genre_form = GenreForm()
    for genre in genreslist:
        songsdict[genre]=Song.objects.filter(genre=genre)
    return render(request, 'soundSafariApp/genres.html', {'genres':genreslist, 'songspergenre':songsdict, 'genre_form':genre_form})

def guide(request):
    return render(request, 'soundSafariApp/guide.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request,
                  'soundSafariApp/register.html',
                  context = {'user_form':user_form,
                             'profile_form': profile_form,
                             'registered': registered})

def show_artist(request, artist_name_slug):
    context_dict={}
    try:
        artist = Artist.objects.get(slug=artist_name_slug)
        album=Album.objects.filter(artist=artist)
        songs=Song.objects.filter(artist=artist)
        #reviews=Review.objects.filter(artist=artist)
        #avg_rating = sum([r.rating for r in reviews]) / reviews.count()
        context_dict['albums']=album
        context_dict['songs']=songs
        context_dict['artist']=artist
        #context_dict['reviews']=reviews
        #context_dict['rating']=avg_rating
    except Artist.DoesNotExist:
        context_dict['albums']=None
        context_dict['artist']=None
        context_dict['songs']=None
    return render(request, 'soundSafariApp/artist.html', context_dict)

def show_album(request, artist_name_slug, album_name_slug):
    context_dict={}
    try:
        album = Album.objects.get(slug=album_name_slug)
        songs=Song.objects.filter(album=album)
        context_dict['songs']=songs
        context_dict['album']=album
    except:
        context_dict['songs']=None
        context_dict['album']=None
    return render(request, 'soundSafariApp/album.html', context_dict)






@login_required
def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            new_genre = form.save()
            # Redirect to a 'genre_detail' view, or wherever you wish
            return redirect(reverse('genres', args=[new_genre.id]))
    else:
        form = GenreForm()

    return render(request, 'soundSafariApp/genres.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('soundSafariApp:index'))
