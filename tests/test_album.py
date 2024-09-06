from lib.album import Album


"""
Construst with an id, title, release date and artist id
"""

def test_constructs():
    album = Album(1, "Test title", 2000, 2)
    assert album.id == 1
    assert album.title == "Test title"
    assert album.release_year == 2000
    assert album.artist_id == 2


"""
Albums with equal contents are equal
"""
def test_compares():
    album1 = Album(1, "Test title", 2000, 2)
    album2 = Album(1, "Test title", 2000, 2)
    assert album1 == album2


"""
Albums can be represented as strings
"""
def test_stringifying():
    album = Album(1, "Test title", 2000, 2)
    assert str(album) == "Album(1, Test title, 2000, 2)"

