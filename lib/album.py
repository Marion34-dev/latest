class Album:
    def __init__(self, id, title, release_year, artist_id, artist_name=None):
        self.id = id
        self.title = title
        self.release_year = release_year
        self.artist_id = artist_id
        self.artist_name = artist_name  # New attribute for artist name

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __str__(self):
        return f"Album({self.id}, {self.title}, {self.release_year}, {self.artist_id}, {self.artist_name})"
