import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soundSafari.settings')

import django
django.setup()
from django.utils import timezone
from soundSafariApp.models import Genre, Artist, Album, Song, Page, UserProfile, Review
from django.contrib.auth.models import User

def create_genres():
    genres = ['Pop', 'Rock', 'Hip-Hop', 'Electronic', 'Jazz']
    for genre_name in genres:
        Genre.objects.get_or_create(name=genre_name)

def create_artists():
    artists_data = [
        {
            'name': 'The Weeknd',
            'birthDate': timezone.datetime(1990, 2, 16),
            'picture': 'static/images/TheWeeknd.jpg',
        },
        {
            'name': 'Taylor Swift',
            'birthDate': timezone.datetime(1989, 12, 13),
            'picture': 'static/images/TaylorSwift.jpg',
        },
        {
            'name': 'Eminem', 
            'birthDate': timezone.datetime(1972, 10, 17),
            'picture': 'static/images/Eminem.jpg',
        }
    ]
    for artist_data in artists_data:
        Artist.objects.get_or_create(**artist_data)

def create_albums():
    albums_data = [
        {
            'name': 'After Hours',
            'genre': Genre.objects.get(name='Pop'),
            'artist': Artist.objects.get(name='The Weeknd'),
            'release_date': timezone.datetime(2020, 3, 20),
            'picture': 'static/images/AfterHours.jpg',
        },
        {
            'name': '1989 (Taylor\'s Version)',
            'genre': Genre.objects.get(name='Pop'),
            'artist': Artist.objects.get(name='Taylor Swift'),
            'release_date': timezone.datetime(2021, 11, 12),
            'picture': 'static/images/1989.jpg',
        },
        {
            'name': 'The Eminem Show',
            'genre': Genre.objects.get(name='Hip-Hop'),
            'artist': Artist.objects.get(name='Eminem'),
            'release_date': timezone.datetime(200, 5, 26),
            'picture': 'static/images/TheEminemShow.jpg',
        }
    ]
    for album_data in albums_data:
        Album.objects.get_or_create(**album_data)

def create_songs():
    songs_data = [
        # The Weeknd After Hours Album Songs
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Alone Again', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 240, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Too Late', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 224, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Hardest to Love', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 219, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Scared to Live', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 221, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Snowchild', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 258, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Escape from LA', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 308, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Heartless', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 213, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Faith', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 228, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Blinding Lights', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 201, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'In Your Eyes', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 225, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Save Your Tears', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 212, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Repeat After Me (Interlude)', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 193, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'After Hours (S)', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 355, 'release_date': timezone.datetime(2020, 3, 20)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Until I Bleed Out', 'album' : Album.objects.get(name='After Hours'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 222, 'release_date': timezone.datetime(2020, 3, 20)},
       
        # Other The Weeknd Songs
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Starboy', 'genre' : Genre.objects.get(name='Pop'), 'duration': 230, 'release_date': timezone.datetime(2016, 9, 22)},
        {'artist' : Artist.objects.get(name='The Weeknd'), 'name': 'Blinding Lights (Remix)', 'genre' : Genre.objects.get(name='Pop'), 'duration': 208, 'release_date': timezone.datetime(2020, 3, 20)},


        # Taylor Swift 1989 songs
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'Welcome to New York', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 212, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'Blank Space', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 231, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'Style', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 231, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'Out of the Woods', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 281, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'All You Had to Do Was Stay', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 203, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'Shake It Off', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 219, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'I Wish You Would', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 208, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'Wildest Dreams (Taylor\'s Version)', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 220, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'Bad Blood', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 213, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'How You Get the Girl', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 241, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'This Love', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 245, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'I Know Places', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 214, 'release_date': timezone.datetime(2021, 11, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'Clean', 'album' : Album.objects.get(name='1989 (Taylor\'s Version)'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 280, 'release_date': timezone.datetime(2021, 11, 12)},

        # Other Taylor Swift songs
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'Love Story', 'genre' : Genre.objects.get(name='Pop'), 'duration': 235, 'release_date': timezone.datetime(2008, 9, 12)},
        {'artist' : Artist.objects.get(name='Taylor Swift'), 'name': 'You Belong with Me', 'genre' : Genre.objects.get(name='Pop'), 'duration': 231, 'release_date': timezone.datetime(2009, 4, 18)},


        # Eminem's The Eminem Show album Songs
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Curtains Up', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 34, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'White America', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 299, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Business', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 257, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Cleanin Out My Closet', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 288, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Square Dance', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 258, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'The Kiss (Skit)', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 51, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Soldier', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 210, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Say Goodbye Hollywood', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 258, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Drips', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 258, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Without Me', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 290, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Paul Rosenberg (Skit)', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 23, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Sing for the Moment', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 339, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Superman', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 319, 'release_date': timezone.datetime(2002, 5, 26)},
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Hailie\'s Song', 'album' : Album.objects.get(name='The Eminem Show'), 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 313, 'release_date': timezone.datetime(2002, 5, 26)},
        
        # Add more songs as needed
        {'artist' : Artist.objects.get(name='Eminem'), 'name': 'Lose Yourself', 'genre' : Genre.objects.get(name='Hip-Hop'), 'duration': 326, 'release_date': timezone.datetime(2002, 10, 28)},
    ]

    for song_data in songs_data:
        Song.objects.get_or_create(**song_data)

def create_user_profiles():
    users_data = [
        {
            'username': 'Maria123',
            'password': 'password1',
            'email': 'maria@gmail.com',
            'date_joined': timezone.now(),
        },
        {
            'username': 'John69',
            'password': 'password2',
            'email': 'john@gmail.com',
            'date_joined': timezone.now(),
        },
        {
            'username': 'MusicLover3',
            'password': 'password3',
            'email': 'MusicLover@gmail.com',
            'date_joined': timezone.now()
        }
    ]

    images = ['static/images/John.jpg', 'static/images/Maria.jpg', None]

    for i, user_data in enumerate(users_data):
        try:
            user = User.objects.get(username=user_data['username'])
        except User.DoesNotExist:
            user = User.objects.create_user(**user_data)
        UserProfile.objects.create(user=user, picture=images[i] if images[i] else None)

        
def create_reviews():
    reviews_data = [
        {
            'user': UserProfile.objects.get(user__username='Maria123'),
            'page': Page.objects.get(name="Eminem"),
            'rating': 4,
            'date_added': timezone.now(),
            'comment': 'Old but Gold!'
        },
        {
            'user': UserProfile.objects.get(user__username='John69'),
            'page': Page.objects.get(name='After Hours'),
            'rating': 3,
            'date_added': timezone.now(),
            'comment': 'Nice album! Binding Lights is my favourite, the rest of the songs could be better though.'
        },
        {
            'user': UserProfile.objects.get(user__username='MusicLover3'),
            'page': Page.objects.get(name='Love Story'),
            'rating': 5,
            'date_added': timezone.now(),
            'comment': 'This song is a masterpiece! I\'ve been playing it on repeat.'
        }
    ]
    for review_data in reviews_data:
        Review.objects.create(**review_data)

if __name__ == '__main__':
    create_genres()
    create_artists()
    create_albums()
    create_songs()
    create_user_profiles()
    create_reviews()