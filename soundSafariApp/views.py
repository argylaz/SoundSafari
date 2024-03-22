from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from soundSafariApp.models import Artist, UserProfile, Song, Genre, Album, Review, Page
from soundSafariApp.forms import UserForm, UserProfileForm, GenreForm, EditProfileForm, AlbumForm, ArtistForm, User, ReviewForm
from django.utils import timezone

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


def add_artist_review(request, artist_name_slug):
    artist = get_object_or_404(Artist, slug=artist_name_slug)
    page = get_object_or_404(Page, artist=artist)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user_profile
            review.page = page
            review.date_added = timezone.now()  # Set the review date to now
            review.save()

            return redirect('soundSafariApp/index')
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'artist': artist,
    }
    return render(request, 'soundSafariApp/add_review_to_artist.html', context)


def add_song_review(request, song_name_slug):
    song = get_object_or_404(Song, slug=song_name_slug)
    page = get_object_or_404(Page, song=song)
    user_profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = user_profile
            review.page = page
            review.date_added = timezone.now()  # Set the review date to now
            review.save()
            return redirect('soundSafariApp:show_single', song_name_slug=song.slug)
    else:
        form = ReviewForm()

    context = {
        'form': form,
        'song':song,
    }
    return render(request, 'soundSafariApp/add_song_review.html', context=context)





def show_artist(request, artist_name_slug):
    context_dict={}
    try:
        artist = Artist.objects.get(slug=artist_name_slug)
        album=Album.objects.filter(artist=artist)
        songs=Song.objects.filter(artist=artist,  album__isnull=True)
        page=Page.objects.get(name=artist.name)
        reviews=Review.objects.filter(page=page)
        #print(reviews)
        context_dict['albums']=album
        context_dict['songs']=songs
        context_dict['artist']=artist
        context_dict['reviews']=reviews
        context_dict['page']=page
    except Artist.DoesNotExist:
        context_dict['albums']=None
        context_dict['artist']=None
        context_dict['songs']=None
        context_dict['reviews']=None
        context_dict['page']=None
    return render(request, 'soundSafariApp/artist.html', context_dict)

def show_album(request, artist_name_slug, album_name_slug):
    context_dict={}
    try:
        album = Album.objects.get(slug=album_name_slug)
        songs=Song.objects.filter(album=album)
        page=Page.objects.get(name=album.name)
        reviews=Review.objects.filter(page=page)
        context_dict['songs']=songs
        context_dict['album']=album
        context_dict['reviews']=reviews
        context_dict['page']=page
    except:
        context_dict['songs']=None
        context_dict['album']=None
        context_dict['reviews']=None
        context_dict['page']=None
    return render(request, 'soundSafariApp/album.html', context_dict)

def show_song(request, artist_name_slug, album_name_slug , song_name_slug):
    context_dict={}
    try:
        song=Song.objects.get(slug=song_name_slug)
        page=Page.objects.get(name=song.name)
        reviews=Review.objects.filter(page=page)
        context_dict['song']=song
        context_dict['reviews']=reviews
        context_dict['page']=page
    except:
        context_dict['song']=None
        context_dict['reviews']=None
        context_dict['page']=None
    return render(request, 'soundSafariApp/song.html', context_dict)

def show_single(request, artist_name_slug, song_name_slug):
    context_dict={}
    try:
        song=Song.objects.get(slug=song_name_slug)
        page=Page.objects.get(name=song.name)
        reviews=Review.objects.filter(page=page)
        context_dict['song']=song
        context_dict['reviews']=reviews
        context_dict['page']=page
    except:
        context_dict['song']=None
        context_dict['reviews']=None
        context_dict['page']=None
    return render(request, 'soundSafariApp/show_single.html', context_dict)




@login_required
def add_album(request, artist_name_slug):
    artist = get_object_or_404(Artist, slug=artist_name_slug)
    print(artist)
    form = AlbumForm(request.POST, request.FILES)
    if form.is_valid():
        album = form.save(commit=False)
        album.artist = artist
        album.save()         
        return redirect('soundSafariApp:artist_detail', artist_name_slug=artist.slug)
    else:
        print(form.errors)
    
    return render(request, 'soundSafariApp/add_album.html', {'form': form, 'artist': artist})

@login_required
def add_genre(request):
    form = GenreForm()

    if request.method == 'POST':
        form = GenreForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/soundsafari/genres/')
        else:
            print(form.errors)
    
    return render(request, 'soundSafariApp/add_genre.html', {'form': form})

@login_required
def add_artist(request):
    form = ArtistForm()

    if request.method == 'POST':
        form = ArtistForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return redirect('/soundsafari/artists/')
        else:
            print(form.errors)
    
    return render(request, 'soundSafariApp/add_artist.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('soundSafariApp:index'))

@login_required
def user_profile(request, username):
    context_dict={}
    try:
        user=User.objects.get(user=username)
        reviews=Review.objects.filter(user=user)
        #context_dict['user']=user
        context_dict['reviews']=reviews
    except:
        #context_dict['user']=None
        context_dict['reviews']=None

    return render(request, 'soundSafariApp/profile.html', context_dict)



@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user.userprofile)
        if form.is_valid():
            form.save()
            return redirect('soundSafariApp:user_profile', username=request.user.username)

    else:
        form = EditProfileForm(instance=request.user.userprofile)
    return render(request, 'soundSafariApp/edit_profile.html', {'form': form})