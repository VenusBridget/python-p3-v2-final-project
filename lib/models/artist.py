from models.__init__ import CURSOR, CONN

class Artist:
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Artist {self.id}: {self.name}>"
    
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
        """Create a new table to persist attributes of Artist instances"""
        sql = """CREATE TABLE IF NOT EXISTS artists (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persist Artist instances"""
        sql = """DROP TABLE IF EXISTS artists"""
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Insert a new row with the name, title, artist id and playlist id values of the current Song object.
        Save the object in local dictonary using table row's PK as dictonary key"""
        sql = """
            INSERT INTO artists (name) 
            VALUES (?)
        """
        CURSOR.execute(sql, (self.name,))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        """Initialize a new Artist instance and save the object to the database."""
        artist = cls(name)
        artist.save()
        return artist
    
    def update(self):
        """Update a artists table row corresponding to the current Artist instance."""
        sql = """
            UPDATE artists SET name = ? WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.id))
        CONN.commit()

    def delete(self):
        """Delete a artists table row corresponding to the current Artist instance,
           delete the dictonary entry, and reassign id attribute."""
        sql = """
            DELETE FROM artists WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return an Artist having the attribute values from the table row."""

        artist = cls.all.get(row[0])
        if artist:
            artist.name = row[1]
        else:
            artist = cls(row[1])
            artist.id = row[0]
            cls.all[artist.id] = artist
        return artist
    
    @classmethod
    def get_all(cls):
        """Return a list containing an Artist object per row in the table."""
        sql = """
            SELECT * FROM artists
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    
    @classmethod
    def find_by_id(cls, id):
        """Return an Artist object corresponding to the table row matching the specified primary key."""
        sql = """
            SELECT * FROM artists WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_name(cls, name):
        """Return an Artist object corresponding to the first table row matching specified name."""
        sql = """
            SELECT * FROM artists WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    def songs(self):
        """Return a list of songs associated with current artist."""
        from models.song import Song
        sql = """
            SELECT * FROM songs 
            WHERE artist_name = ?
        """
        CURSOR.execute(sql, (self.name,),)
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
       

    