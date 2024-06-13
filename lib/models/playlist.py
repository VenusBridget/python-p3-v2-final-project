from models.__init__ import CURSOR, CONN

class Playlist:
    all = {}
    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Playlist {self.id}: {self.name}>"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")
        
    @classmethod
    def create_table(cls):
        """Create a new table to persist attributes of Playlist instances"""
        sql = """CREATE TABLE IF NOT EXISTS playlists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persist attributes of Playlist instances"""
        sql = """DROP TABLE IF EXISTS playlists"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Save a Playlist instance to the database.
        Save the object in local dictonary using table row's PK as dictonary key"""
        sql = """
            INSERT INTO playlists (name) VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """Create a new Playlist instance and save it to the database."""
        playlist = cls(name)
        playlist.save()
        return playlist
    
    def update(self):
        """Update a playlists table row corresponding to the current Playlist instance."""
        sql = """
            UPDATE playlists SET name = ? WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete a playlists table row corresponding to the current Playlist instance,
           delete the dictonary entry, and reassign id attribute."""
        sql = """
            DELETE FROM playlists WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a Playlist having the attribute values from the table row."""

        playlist = cls.all.get(row[0])
        if playlist:
            playlist.name = row[1]
        else:
            playlist = cls(row[1])
            playlist.id = row[0]
            cls.all[playlist.id] = playlist
        return playlist
    
    @classmethod
    def get_all(cls):
        """Return a list containing a Playlist object per row in the table."""
        sql = """
            SELECT * FROM playlists
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return a Playlist object corresponding to the table row matching the specified primary key."""
        sql = """
            SELECT * FROM playlists WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return a Playlist object corresponding to the first table row matching specified name."""
        sql = """
            SELECT * FROM playlists WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def songs(self):
        """Return a list of songs associated with current playlist."""
        from models.song import Song
        sql = """
            SELECT * FROM songs WHERE playlist_id = ?
        """
        CURSOR.execute(sql, (self.id,),)
        rows = CURSOR.fetchall()
        # return [Song.instance_from_db(row) for row in rows]
        formatted_songs = ""
        for row in rows:
            song_info = [
                f"Song {row[0]}: {row[1]}",
                f"Artist name: {row[2]}",
                f"Playlist ID: {row[3]}"  
            ]
            formatted_songs += "\n".join(song_info) + "\n\n" 
        
        return formatted_songs.strip()