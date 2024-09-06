import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist import Artist
from lib.artist_repository import ArtistRepository

app = Flask(__name__)

@app.route('/')
def welcome_page():
    return render_template("welcome.html")

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html",albums=albums)

@app.route('/albums/<int:id>', methods=['GET'])
def get_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    if album is None:
        return "Album not found", 404 
    return render_template('albums/show.html', album=album)


@app.route('/albums/new', methods=['GET'])
def get_new_album():
    connection = get_flask_database_connection(app)
    artist_repository = ArtistRepository(connection)
    artists = artist_repository.all()
    return render_template('albums/new.html', artists=artists)


@app.route('/albums', methods=['POST'])
def post_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    
    # Ensure we are retrieving the correct form data
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']

    # Debugging statements to verify form data
    print(f"Title: {title}, Release Year: {release_year}, Artist ID: {artist_id}")

    if not title or not release_year or not artist_id:
        return "You need to submit a title, release_year, and artist_id", 400

    # Create the Album object with the correct data
    album = Album(None, title, release_year, artist_id)
    repository.create(album)
    
    return redirect("/albums")


def has_invalid_album_parameters(form):
    return 'title' not in form or 'release_year' not in form or 'artist_id' not in form

@app.route('/albums/<id>/edit', methods=['GET'])
def edit_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template('albums/edit.html', album=album)

@app.route('/albums/<id>', methods=['POST'])
def update_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    repository.update(id, title, release_year, artist_id)
    return redirect('/albums')

@app.route('/albums/<id>/delete', methods=['POST'])
def delete_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return redirect('/albums')



###### ###### ###### ###### ###### 

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artists = repository.all()
    return render_template("artists/index.html",artists=artists)

@app.route('/artists/<id>', methods=['GET'])
def get_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)

    artist = repository.find(id)
    return render_template('artists/show_artist.html', artist=artist)

@app.route('/artists', methods=['POST'])
def post_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = Artist(None, 
                request.form['name'],
                request.form['genre'])
    repository.create(artist)
    return redirect(f"/artists")

@app.route('/artists/new', methods=['GET'])
def get_new_artist():
    return render_template('artists/new.html')

@app.route('/artists/<id>/delete', methods=['POST'])
def delete_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    repository.delete(id)
    return redirect('/artists')

@app.route('/artists/<id>/edit', methods=['GET'])
def edit_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    artist = repository.find(id)
    return render_template('artists/edit.html', artist=artist)

@app.route('/artists/<id>', methods=['POST'])
def update_artist(id):
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    name = request.form['name']
    genre = request.form['genre']
    repository.update(id, name, genre)
    return redirect('/artists')


if __name__ == '__main__':
    app.run(
    debug=True,
    host="0.0.0.0" # Listen for connections _to_ any server
    )
