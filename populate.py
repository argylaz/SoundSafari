import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soundSafari.settings')

import django
django.setup()
from django.utils import timezone
from soundSafariApp.models import Genre, Artist, Album, Song, Page, UserProfile, Review
from django.contrib.auth.models import User

def create_genres():
    genres = ['Pop', 'Rock', 'Heavy Metal', 'Hip-Hop', 'Electronic', 'Jazz', 'R&B']
    for genre_name in genres:
        Genre.objects.get_or_create(name=genre_name)

def create_artists():
    artists_data = [
        {
            'name': 'The Weeknd',
            'birthDate': timezone.datetime(1990, 2, 16),
            'picture': 'images/TheWeeknd.jpg',
        },
        {
            'name': 'Taylor Swift',
            'birthDate': timezone.datetime(1989, 12, 13),
            'picture': 'images/TaylorSwift.jpg',
        },
        {
            'name': 'Eminem', 
            'birthDate': timezone.datetime(1972, 10, 17),
            'picture': 'images/Eminem.jpg',
        },
        {
            'name' : 'ACDC',
            'birthDate' : timezone.datetime(1973, 1, 1),
            'picture' : 'images/ACDC.jpg',
        },
        {
            'name' : 'Hittman',
            'birthDate' : timezone.datetime(1985, 1, 1),
            'picture' : 'images/Hittman.jpg',
        },
        {
            'name' : 'Ed Sheeran',
            'birthDate' : timezone.datetime(1991, 2, 17),
            'picture' : 'images/EdSheeran.jpg',
        },
        {
            'name' : 'Beyonce',
            'birthDate' : timezone.datetime(1981, 9, 4),
            'picture' : 'images/Beyonce.jpg',
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
            'picture': 'images/AfterHours.jpg',
        },
        {
            'name': '1989 (Taylor\'s Version)',
            'genre': Genre.objects.get(name='Pop'),
            'artist': Artist.objects.get(name='Taylor Swift'),
            'release_date': timezone.datetime(2021, 11, 12),
            'picture': 'images/1989.jpg',
        },
        {
            'name': 'The Eminem Show',
            'genre': Genre.objects.get(name='Hip-Hop'),
            'artist': Artist.objects.get(name='Eminem'),
            'release_date': timezone.datetime(200, 5, 26),
            'picture': 'images/TheEminemShow.jpg',
        },
        {
            'name' : 'Highway to Hell (Album)',
            'genre' : Genre.objects.get(name='Rock'),
            'artist' : Artist.objects.get(name='ACDC'),
            'release_date' : timezone.datetime(1979, 7, 27),
            'picture' : 'images/HighwayToHell.jpg',
        },
        {
            'name' : 'Hittman (1984)',
            'genre' : Genre.objects.get(name='Heavy Metal'),
            'artist' : Artist.objects.get(name='Hittman'),
            'release_date' : timezone.datetime(1984, 1, 1),
            'picture' : 'images/HittmanAlbum.jpg',
        },
        {
            'name' : 'Divide',
            'genre' : Genre.objects.get(name='Pop'),
            'artist' : Artist.objects.get(name='Ed Sheeran'),
            'release_date' : timezone.datetime(1984, 1, 1),
            'picture' : 'images/%.jpg',
        },
        {
            'name' : 'Lemonade',
            'genre' : Genre.objects.get(name='Pop'),
            'artist' : Artist.objects.get(name='Beyonce'),
            'release_date' : timezone.datetime(1984, 1, 1),
            'picture' : 'images/Lemonade.jpg',
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

        # AC/DC Album Songs
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Highway to Hell', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 208, 'release_date': timezone.datetime(1979, 7, 27)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Girls Got Rhythm', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 189, 'release_date': timezone.datetime(1979, 7, 27)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Walk All Over You', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 310, 'release_date': timezone.datetime(1979, 7, 27)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Touch Too Much', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 272, 'release_date': timezone.datetime(1979, 7, 27)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Beating Around the Bush', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 223, 'release_date': timezone.datetime(1979, 7, 27)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Shot Down in Flames', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 183, 'release_date': timezone.datetime(1979, 7, 27)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Get It Hot', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 185, 'release_date': timezone.datetime(1979, 7, 27)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'If You Want Blood (You\'ve Got It)', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 280, 'release_date': timezone.datetime(1979, 7, 27)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Love Hungry Man', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 245, 'release_date': timezone.datetime(1979, 7, 27)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Night Prowler', 'album' : Album.objects.get(name='Highway to Hell'), 'genre' : Genre.objects.get(name='Rock'), 'duration': 276, 'release_date': timezone.datetime(1979, 7, 27)},

        # AC/DC Singles
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Back in Black', 'genre' : Genre.objects.get(name='Rock'), 'duration': 255, 'release_date': timezone.datetime(1980, 7, 21)},
        {'artist' : Artist.objects.get(name='ACDC'), 'name': 'Thunderstruck', 'genre' : Genre.objects.get(name='Rock'), 'duration': 292, 'release_date': timezone.datetime(1990, 9, 10)},

        # Hittman Album songs
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Metal Sport', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 211, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Breakout', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 215, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Backstreet Rebels', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 279, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Caught in the Crossfire', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 249, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Secret Agent Man', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 282, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Behind the Lines', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 233, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'The Test of Time', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 222, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Kick in the Teeth', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 230, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Battleground', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 230, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Dead on Arrival', 'album' : Album.objects.get(name='Hittman (1984)'), 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 224, 'release_date': timezone.datetime(1988, 1, 1)},

        # Hittman Singles
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Back Street Rebels', 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 279, 'release_date': timezone.datetime(1988, 1, 1)},
        {'artist' : Artist.objects.get(name='Hittman'), 'name': 'Dead on Arrival', 'genre' : Genre.objects.get(name='Heavy Metal'), 'duration': 224, 'release_date': timezone.datetime(1988, 1, 1)},

        # Ed Sheeran Divide Album Songs
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Eraser', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 204, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Castle on the Hill', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 261, 'release_date': timezone.datetime(2017, 1, 6)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Dive', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 229, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Shape of You', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 233, 'release_date': timezone.datetime(2017, 1, 6)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Perfect', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 263, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Galway Girl', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 170, 'release_date': timezone.datetime(2017, 3, 17)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Happier', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 207, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'New Man', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 189, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Hearts Don\'t Break Around Here', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 235, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'What Do I Know?', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 237, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'How Would You Feel (Paean)', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 280, 'release_date': timezone.datetime(2017, 2, 17)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Supermarket Flowers', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 221, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Barcelona', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 176, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Bibia Be Ye Ye', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 157, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Nancy Mulligan', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 186, 'release_date': timezone.datetime(2017, 3, 3)},
        {'artist' : Artist.objects.get(name='Ed Sheeran'), 'name': 'Save Myself', 'album' : Album.objects.get(name='Divide'), 'genre' : Genre.objects.get(name='Pop'), 'duration': 258, 'release_date': timezone.datetime(2017, 3, 3)},

        # Beyoncé's "Lemonade" Album Songs
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Pray You Catch Me', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 224, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Hold Up', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 223, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Don\'t Hurt Yourself', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 222, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Sorry', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 234, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': '6 Inch', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 225, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Daddy Lessons', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 266, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Love Drought', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 223, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Sandcastles', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 233, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Forward', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 66, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Freedom', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 288, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'All Night', 'album' : Album.objects.get(name='Lemonade'), 'genre' : Genre.objects.get(name='R&B'), 'duration': 336, 'release_date': timezone.datetime(2016, 4, 23)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Formation', 'genre' : Genre.objects.get(name='R&B'), 'duration': 262, 'release_date': timezone.datetime(2016, 2, 6)},

        # Other Popular Beyoncé Singles
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Halo', 'genre' : Genre.objects.get(name='R&B'), 'duration': 256, 'release_date': timezone.datetime(2008, 1, 20)},
        {'artist' : Artist.objects.get(name='Beyonce'), 'name': 'Irreplaceable', 'genre' : Genre.objects.get(name='R&B'), 'duration': 220, 'release_date': timezone.datetime(2006, 10, 23)},
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
        },
        {
            'username': 'BurgerKing123',
            'password': 'cheeseburger',
            'email': 'burgerlover@gmail.com',
            'date_joined': timezone.now(),
        },
        {
            'username': 'PizzaManiac22',
            'password': 'pizzaparty',
            'email': 'pizzalover@gmail.com',
            'date_joined': timezone.now(),
        },
        {
            'username': 'DancingPotato',
            'password': 'potatodance',
            'email': 'potatolover@gmail.com',
            'date_joined': timezone.now(),
        },
    ]

    images = ['images/Maria.jpg', 'images/John.jpg']

    for i, user_data in enumerate(users_data):
        user = User.objects.create_user(**user_data)
        if i < 2:
            UserProfile.objects.create(user=user, picture=images[i])
        else:
            UserProfile.objects.create(user=user)

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
        },
        {
            'user': UserProfile.objects.get(user__username='BurgerKing123'),
            'page': Page.objects.get(name="The Eminem Show"),
            'rating': 4,
            'date_added': timezone.now(),
            'comment': 'Classic album, never gets old!'
        },
        {
            'user': UserProfile.objects.get(user__username='PizzaManiac22'),
            'page': Page.objects.get(name='After Hours'),
            'rating': 4,
            'date_added': timezone.now(),
            'comment': 'Great vibe, perfect for chilling!'
        },
        {
            'user': UserProfile.objects.get(user__username='DancingPotato'),
            'page': Page.objects.get(name='1989 (Taylor\'s Version)'),
            'rating': 5,
            'date_added': timezone.now(),
            'comment': 'Feeling nostalgic, Taylor Swift never disappoints!'
        },
        {
            'user': UserProfile.objects.get(user__username='BurgerKing123'),
            'page': Page.objects.get(name="Love Story"),
            'rating': 5,
            'date_added': timezone.now(),
            'comment': 'One of the best love songs ever written!'
        },
        {
            'user': UserProfile.objects.get(user__username='PizzaManiac22'),
            'page': Page.objects.get(name='Lose Yourself'),
            'rating': 5,
            'date_added': timezone.now(),
            'comment': 'A true motivational anthem!'
        },
        {
            'user': UserProfile.objects.get(user__username='DancingPotato'),
            'page': Page.objects.get(name='Lemonade'),
            'rating': 4,
            'date_added': timezone.now(),
            'comment': 'Powerful and empowering!'
        },
        {
            'user': UserProfile.objects.get(user__username='DancingPotato'),
            'page': Page.objects.get(name='Hittman'),
            'rating': 5,
            'date_added': timezone.now(),
            'comment': 'Best Metal band ever!'
        },
        {
            'user': UserProfile.objects.get(user__username='PizzaManiac22'),
            'page': Page.objects.get(name='Hittman'),
            'rating': 4,
            'date_added': timezone.now(),
            'comment': 'Extremely Underrated!'
        },
        {
            'user': UserProfile.objects.get(user__username='DancingPotato'),
            'page': Page.objects.get(name='Back in Black'),
            'rating': 4,
            'date_added': timezone.now(),
        },
        {
            'user': UserProfile.objects.get(user__username='DancingPotato'),
            'page': Page.objects.get(name='Thunderstruck'),
            'rating': 3,
            'date_added': timezone.now(),
        },
        {
            'user': UserProfile.objects.get(user__username='BurgerKing123'),
            'page': Page.objects.get(name='I Know Places'),
            'rating': 2,
            'date_added': timezone.now(),
        },
        {
            'user': UserProfile.objects.get(user__username='DancingPotato'),
            'page': Page.objects.get(name='Back in Black'),
            'rating': 4,
            'date_added': timezone.now(),
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