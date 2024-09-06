from playwright.sync_api import Page, expect

"""
When I call GET /albums
I get a list of albums back
"""
def test_get_albums(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")
    p_tag = page.locator("p")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        "The Cold Nose",
        "Nikita"
    ])
    expect(p_tag).to_have_text([
        "Released: 2008",
        "Released: 1998"
    ])


"""
We can retrieve a single album
"""
def test_get_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums/2") 

    h2_tag = page.locator("h2") 
    p_tag = page.locator("p")   

    expect(h2_tag).to_have_text("Nikita")
    expect(p_tag).to_have_text("Released: 1998")


"""
We can create a new album
And see it reflected in the list of albums
"""
def test_create_album(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/albums")

    page.click("text='Add new album'")
    page.fill("input[name='title']", "Test Album")
    page.fill("input[name='release_year']", "2000")
    page.fill("input[name='artist_id']", "1")  
    page.click("text=Add Album")
    page.goto(f"http://{test_web_address}/albums")
    p_tag = page.locator("p")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        "The Cold Nose",
        "Nikita",
        "Test Album"
    ])
    expect(p_tag).to_have_text([
        "Released: 2008",
        "Released: 1998",
        "Released: 2000"
    ])


####### ####### ####### ####### ####### 
"""
When I call GET /artists
I get a list of artists back
"""
def test_get_artists(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")
    p_tag = page.locator("p")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone"
    ])
    expect(p_tag).to_have_text([
        "Genre: indie",
        "Genre: pop",
        "Genre: pop",
        "Genre: jazz"
    ])


"""
We can retrieve a single artist
"""
def test_get_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists/3")  

    h2_tag = page.locator("h2")  # Locate the h2 element for album title
    p_tag = page.locator("p")    # Locate the p element for release year

    expect(h2_tag).to_have_text("Taylor Swift")
    expect(p_tag).to_have_text("Genre: pop")


"""
We can create a new artist
And see it reflected in the list of artists
"""
def test_create_artist(page, test_web_address, db_connection):
    db_connection.seed("seeds/record_store.sql")
    page.goto(f"http://{test_web_address}/artists")

    page.click("text='Add new artist'")
    page.fill("input[name='name']", "Queens")
    page.fill("input[name='genre']", "rock")
    page.click("text=Add Artist")
    page.goto(f"http://{test_web_address}/artists")
    p_tag = page.locator("p")
    h2_tag = page.locator("h2")
    expect(h2_tag).to_have_text([
        "Pixies",
        "ABBA",
        "Taylor Swift",
        "Nina Simone",
        "Queens"
    ])
    expect(p_tag).to_have_text([
        "Genre: indie",
        "Genre: pop",
        "Genre: pop",
        "Genre: jazz",
        "Genre: rock"
    ])
