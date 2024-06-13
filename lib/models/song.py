from models.__init__ import CURSOR, CONN
from models.playlist import Playlist
from models.artist import Artist

class Song:
    all = {}

    def __init__(self, title, artist_name, playlist_id, id=None):
        self.id = id
        self.title = title
        self.artist_name = artist_name
        self.playlist_id = playlist_id

    def __repr__(self):
        return (
            f"<Song {self.id}: {self.title}," +
            f" Artist Name: {self.artist_name}," +
            f" Playlist ID: {self.playlist_id}>"
        )
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title)>0:
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")
        
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
        """Create a new table to persist attributes of Song instances"""
        sql = """CREATE TABLE IF NOT EXISTS songs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            artist_name TEXT NOT NULL,
            playlist_id INTEGER NOT NULL,
            FOREIGN KEY (artist_name) REFERENCES artists(name)
            FOREIGN KEY(playlist_id) REFERENCES playlists(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persist Song instances"""
        sql = """DROP TABLE IF EXISTS songs"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name, title, artist id and playlist id values of the current Song object.
        Save the object in local dictonary using table row's PK as dictonary key"""
        sql = """
            INSERT INTO songs (title, artist_name, playlist_id) 
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.title, self.artist_name, self.playlist_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update a songs table row corresponding to the current Song instance."""
        sql = """
            UPDATE songs SET title = ?, 
            artist_name = ?, playlist_id = ? WHERE id = ?
        """
        CURSOR.execute(sql, (self.title, self.artist_name, 
                             self.playlist_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete a songs table row corresponding to the current Song instance,
           delete the dictonary entry, and reassign id attribute."""
        sql = """
            DELETE FROM songs WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def create(cls, title, artist_name, playlist_id):
        """Initialize a new Song instance and save the object to the database."""
        song = cls(title, artist_name, playlist_id)
        song.save()
        return song
    
    @classmethod
    def instance_from_db(cls, row):
        """Return a Song having the attribute values from the table row."""

        song = cls.all.get(row[0])
        if song:
            song.title = row[1]
            song.artist_name = row[2]
            song.playlist_id = row[3]
        else:
            song = cls(row[1], row[2], row[3])
            song.id = row[0]
            cls.all[song.id] = song
        return song
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Song object per row in the table."""
        sql = """
            SELECT * FROM songs
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Song object corresponding to the table row matching the specified primary key."""
        sql = """
            SELECT * FROM songs WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_title(cls, title):
        """Return a Song object corresponding to the first table row matching specified title."""
        sql = """
            SELECT * FROM songs WHERE title = ?
        """
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None