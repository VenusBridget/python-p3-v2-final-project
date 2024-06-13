# lib/helpers.py
from models.playlist import Playlist
from models.song import Song
from models.artist import Artist
from models.collab import Collab


def exit_program():
    print("Goodbye!")
    exit()

#Playlist functions
def list_playlists():
    playlists = Playlist.get_all()
    for playlist in playlists:
        print(playlist)


def find_playlist_by_name():
    name = input("Enter the playlist's name: ")
    playlist = Playlist.find_by_name(name)
    print(playlist) if playlist else print(
        f'playlist {name} not found')


def find_playlist_by_id():
    id_ = input("Enter the playlist's id: ")
    playlist = Playlist.find_by_id(id_)
    print(playlist) if playlist else print(f'Playlist {id_} not found')


def create_playlist():
    name = input("Enter the playlist's name: ")
    try:
        playlist = Playlist.create(name)
        print(f'Success: {playlist}')
    except Exception as exc:
        print("Error creating playlist: ", exc)


def update_playlist():
    id_ = input("Enter the playlist's id: ")
    if playlist := Playlist.find_by_id(id_):
        try:
            name = input("Enter the playlist's new name: ")
            playlist.name = name

            playlist.update()
            print(f'Success: {playlist}')
        except Exception as exc:
            print("Error updating playlist: ", exc)
    else:
        print(f'playlist {id_} not found')


def delete_playlist():
    id_ = input("Enter the playlist's id: ")
    if playlist := Playlist.find_by_id(id_):
        playlist.delete()
        print(f'Playlist {id_} deleted')
    else:
        print(f'Playlist {id_} not found')

# Artist functions
def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        print(artist)


def find_artist_by_name():
    name = input("Enter the artist's name: ")
    artist = Artist.find_by_name(name)
    print(artist) if artist else print(
        f'Artist {name} not found')


def find_artist_by_id():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    print(artist) if artist else print(f'artist {id_} not found')


def create_artist():
    name = input("Enter the artist's name: ")
    try:
        artist = Artist.create(name)
        print(f'Success: {artist}')
    except Exception as exc:
        print("Error creating artist: ", exc)


def update_artist():
    id_ = input("Enter the artist's id: ")
    if artist := Artist.find_by_id(id_):
        try:
            name = input("Enter the artist's new name: ")
            artist.name = name

            artist.update()
            print(f'Success: {artist}')
        except Exception as exc:
            print("Error updating artist: ", exc)
    else:
        print(f'Artist {id_} not found')


def delete_artist():
    id_ = input("Enter the artist's id: ")
    if artist := Artist.find_by_id(id_):
        artist.delete()
        print(f'Artist {id_} deleted')
    else:
        print(f'Artist {id_} not found')

# Song functions
def list_songs():
    songs = Song.get_all()
    for song in songs:
        print(song)


def find_song_by_title():
    title=input("Enter the song's title: ")
    song = Song.find_by_title(title)
    print(song) if song else print(
        f'song {title} not found')
    pass


def find_song_by_id():
    id_=input("Enter the song's id: ")
    song=Song.find_by_id(id_)
    print(song) if song else print(
        f'song {id_} not found')
    pass


def create_song():
    title=input("Enter the song's title: ")
    artist_name=input("Enter the song's artist name: ")
    playlist_id =input("Enter the song's playlist id: ")
    try:
        song = Song.create(title, artist_name, playlist_id)
        print(f'Success: {song}')
    except Exception as exc:
        print("Error creating song: ", exc)


def update_song():
    id_=input("Enter the song's id: ")
    if song:= Song.find_by_id(id_):
        try:
            title=input("Enter the song's new title: ")
            song.title=title
            artist_name=input("Enter the new artist's name: ")
            song.artist_name = artist_name
            playlist_name=input("Enter the song's new playlist name: ")
            song.playlist_name=playlist_name

            song.update()
            print(f'Success: {song}')
        except Exception as exc:
            print("Error updating song: ", exc)
    pass


def delete_song():
    id_=input("Enter the song's id: ")
    if song:=Song.find_by_id(id_):
        song.delete()
        print(f'Song {id_} deleted')
    pass


def list_playlist_songs():
    id_=input("Enter the playlist's id: ")
    playlist=Playlist.find_by_id(id_)
    if playlist:
        print(playlist.songs())
    else:
        print(f'Playlist {id_} not found')

def list_artist_songs():
    name_=input("Enter the artist's name: ")
    artist=Artist.find_by_name(name_)
    if artist:
        print(artist.songs())
    else:
        print(f'Artist {name_} not found')


#Collab functions
def list_collabs():
   collabs = Collab.get_all()
   for collab in collabs:
       print(collab)


def find_collab_by_title():
    song_title=input("Enter the collab's title: ")
    collab = Collab.find_by_title(song_title)
    print(collab) if collab else print(
        f'collab {song_title} not found')


def find_collab_by_id():
    song_id_=input("Enter the collab's id: ")
    collab= Collab.find_by_id(song_id_)
    print(collab) if collab else print(
        f'Collab {song_id_} not found')
    pass


def create_collab():
    song_title=input("Enter the collab's title: ")
    artist_name=input("Enter the collab's artist name: ")
    playlist_id=input("Enter the collab's playlist id: ")
    try:
        collab=Collab.create(song_title, artist_name, playlist_id)
        print(f'Success: {collab}')
    except Exception as exc:
        print("Error creating collab: ", exc)
    pass


def update_collab():
    song_id_=input("Enter the collab's id: ")
    if collab:=Collab.find_by_id(song_id_):
        try:
            song_title=input("Enter the collab's new title: ")
            collab.song_title=song_title
            artist_name=input("Enter the collab's new artist name: ")
            collab.artist_name=artist_name
            playlist_name=input("Enter the collab's new playlist name: ")
            collab.playlist_name=playlist_name

            collab.update()
            print(f'Success: {collab}')
        except Exception as exc:
            print("Error updating collab: ", exc)
    pass


def delete_collab():
    song_id_=input("Enter the collab's id: ")
    if collab:= Collab.find_by_id(song_id_):
        collab.delete()
        print(f'collab {song_id_} deleted')
    pass