from lib.artist import Artist


"""
Construst with an id, title, release date and artist id
"""

def test_constructs():
    artist = Artist(1, "Blue", "pop")
    assert artist.id == 1
    assert artist.name == "Blue"
    assert artist.genre == "pop"


"""
artists with equal contents are equal
"""
def test_compares():
    artist1 = Artist(1, "Blue", "pop")
    artist2 = Artist(1, "Blue", "pop")
    assert artist1 == artist2


"""
artists can be reprenseted as strings
"""
def test_stringifying():
    artist = Artist(1, "Blue", "pop")
    assert str(artist) == "Artist(1, Blue, pop)"

