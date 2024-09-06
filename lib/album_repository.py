from lib.album import Album 

class AlbumRepository():
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute("""
            SELECT albums.id AS album_id, albums.title, albums.release_year, albums.artist_id, artists.name 
            FROM albums 
            JOIN artists ON albums.artist_id = artists.id
        """)
        return [
            Album(row["album_id"], row["title"], row["release_year"], row["artist_id"], row["name"])
            for row in rows
        ]

    
    def create(self, album):
        result = self._connection.execute(
            "INSERT INTO albums (title, release_year, artist_id) VALUES (%s, %s, %s) RETURNING id", 
            [album.title, album.release_year, album.artist_id]
        )
        return result[0]["id"]  # Corrected line

    
    def find(self, album_id):
        rows = self._connection.execute(
            'SELECT * from albums WHERE id = %s', [album_id])
        row = rows[0]
        return Album(row["id"], row["title"], row["release_year"], row["artist_id"])


    def delete(self, album_id):
        self._connection.execute("DELETE FROM albums WHERE id = %s", [album_id])
        return None
    
    def update(self, album_id, title, release_year, artist_id):
        self._connection.execute(
            "UPDATE albums SET title = %s, release_year = %s, artist_id = %s WHERE id = %s",
            [title, release_year, artist_id, album_id]
        )
        return None

    

    