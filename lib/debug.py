#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.playlist import Playlist
from models.song import Song
from models.artist import Artist
from models.collab import Collab
import ipdb

def reset_database():
    Song.drop_table()
    Playlist.drop_table()
    Artist.drop_table()
    Collab.drop_table()
    Playlist.create_table()
    Song.create_table()
    Artist.create_table()
    Collab.create_table()

    # Create seed data
    kenyan_old_skul = Playlist.create("Kenyan old skul")
    rnb_old_skul = Playlist.create("RnB old skul")

    nameless = Artist.create("Nameless")
    tattu = Artist.create("Tattu")
    kleptomaniax = Artist.create("Kleptomaniax")
    wahu = Artist.create("Wahu")
    usher = Artist.create("Usher")
    boys_ii_men = Artist.create("Boyz II Men")
    ashanti = Artist.create("Ashanti")
    mariah = Artist.create("Mariah Carey")

    Song.create("Boomba Train", nameless.name, kenyan_old_skul.id)
    Song.create("Sinzia", nameless.name, kenyan_old_skul.id)
    Song.create("Teso", tattu.name, kenyan_old_skul.id)
    Song.create("Jua La Nyesha", tattu.name, kenyan_old_skul.id)
    Song.create("Tuendele", kleptomaniax.name, kenyan_old_skul.id)
    Song.create("Swing", kleptomaniax.name, kenyan_old_skul.id)
    Song.create("Sitishiki", wahu.name, kenyan_old_skul.id)
    Song.create("Confessions", usher.name, rnb_old_skul.id)
    Song.create("Burn", usher.name, rnb_old_skul.id)
    Song.create("End of The Road", boys_ii_men.name, rnb_old_skul.id)
    Song.create("On Bended Knee", boys_ii_men.name, rnb_old_skul.id)
    Song.create("Foolish", ashanti.name, rnb_old_skul.id)
    Song.create("Always On Time", ashanti.name, rnb_old_skul.id)
    Song.create("The Mz", wahu.name, kenyan_old_skul.id)
    Song.create("One Sweet Day", mariah.name, rnb_old_skul.id)

    Collab.create("The Mz", nameless.name, kenyan_old_skul.id)
    Collab.create("The Mz", wahu.name, kenyan_old_skul.id)
    Collab.create("One Sweet Day", mariah.name, rnb_old_skul.id)
    Collab.create("One Sweet Day", boys_ii_men.name, rnb_old_skul.id)


reset_database()
ipdb.set_trace()
