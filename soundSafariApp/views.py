from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404
from .models import Artist

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
                return redirect(reverse('rango:index'))
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'soundSafariApp/login.html')
    
def about(request):
    return render(request, 'soundSafariApp/about.html')

def artists(request):
    return render(request, 'soundSafariApp/artists.html')

def genres(request):
    return render(request, 'soundSafariApp/genres.html')

def guide(request):
    return render(request, 'soundSafariApp/guide.html')

def artist_detail_view(request, slug):
    artist = get_object_or_404(Artist, slug=slug)
    return render(request, 'artist_detail.html', {'artist': artist})