from models.__init__ import CURSOR, CONN
from models.song import Song
from models.artist import Artist
from models.playlist import Playlist

class Collab:
    all = {}

    def __init__(self, song_title, artist_name, playlist_id, song_id = None):
        self.song_id = song_id
        self.song_title = song_title
        self.artist_name = artist_name
        self.playlist_id = playlist_id

    def __repr__(self):
        return (
            f"<Collab: {self.song_title}, " +
            f" By: {self.artist_name}, " +
            f"Playlist: {self.playlist_id}>"
        )
    
    @property
    def song_title(self):
        return self._song_title
    
    @song_title.setter
    def song_title(self, song_title):
        if type(song_title) is str and Song.find_by_title(song_title):
            self._song_title = song_title
        else:
            raise ValueError("song_title must reference a song in the database")
        
    @property
    def artist_name(self):
        return self._artist_name
    
    @artist_name.setter
    def artist_name(self, artist_name):
        if type(artist_name) is str and Artist.find_by_name(artist_name):
            self._artist_name = artist_name
        else:
            raise ValueError("artist_name must reference an artist in the database")
        
    @property
    def playlist_id(self):
        return self._playlist_id
    
    @playlist_id.setter
    def playlist_id(self, playlist_id):
        if type(playlist_id) is int and Playlist.find_by_id(playlist_id):
            self._playlist_id = playlist_id
        else:
            raise ValueError("playlist_id must reference a playlist in the database")
        
    @classmethod
    def create_table(cls):
        """Create a new table to persist attributes of Collab instances"""
        sql = """CREATE TABLE IF NOT EXISTS collabs (
            song_id INTEGER PRIMARY KEY AUTOINCREMENT,
            song_title TEXT NOT NULL,
            artist_name TEXT NOT NULL,
            playlist_id INTEGER NOT NULL,
            FOREIGN KEY(song_id) REFERENCES songs(id)
            FOREIGN KEY(song_title) REFERENCES songs(title)
            FOREIGN KEY(artist_name) REFERENCES artists(name)
            FOREIGN KEY(playlist_id) REFERENCES playlists(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persist Collab instances"""
        sql = """DROP TABLE IF EXISTS collabs"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the title, artist id and playlist id values."""
        sql = """
            INSERT INTO collabs (song_title, artist_name, playlist_id) 
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.song_title, self.artist_name, self.playlist_id))
        CONN.commit()
        self.song_id = CURSOR.lastrowid
        type(self).all[self.song_id] = self

    def update(self):
        """Update a collabs table row corresponding to the current Collab instance."""
        sql = """
            UPDATE collabs SET song_title = ?, 
            artist_name = ?, playlist_id = ? WHERE song_id = ?
        """
        CURSOR.execute(sql, (self.song_title, self.artist_name, 
                             self.playlist_id))
        CONN.commit()

    def delete(self):
        """Delete a collabs table row corresponding to the current Collab instance,
           delete the dictonary entry, and reassign id attribute."""
        sql = """
            DELETE FROM collabs WHERE song_id = ?
        """
        CURSOR.execute(sql, (self.song_id,))
        CONN.commit()
        del type(self).all[self.song_id]
        self.song_id = None

    @classmethod
    def create(cls, song_title, artist_name, playlist_id):
        """Initialize a new Collab instance and save the object to the database."""
        collab = cls(song_title, artist_name, playlist_id)
        collab.save()
        return collab
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Collab having the attribute values from the table row."""

        collab = cls.all.get(row[0])
        if collab:
            collab.song_title = row[1]
            collab.artist_name = row[2]
            collab.playlist_id = row[3]
        else:
            collab = cls(row[1], row[2], row[3])
            collab.song_id = row[0]
            cls.all[collab.song_id] = collab
        return collab
    
    @classmethod
    def get_all(cls):
        """Return a list of all Collab instances."""
        sql = """
            SELECT * FROM collabs
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, song_id):
        """Return a Collab object corresponding to the table row matching the specified id."""
        sql = """
            SELECT * FROM collabs WHERE song_id = ?
        """
        row = CURSOR.execute(sql, (song_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_title(cls, song_title):
        """Return a Collab object corresponding to the first table row matching specified title."""
        sql = """
            SELECT * FROM collabs WHERE song_title = ?
        """
        row = CURSOR.execute(sql, (song_title,)).fetchone()
        return cls.instance_from_db(row) if row else None