-- Drop all existing tables and sequences
DROP TABLE IF EXISTS albums;
DROP SEQUENCE IF EXISTS albums_id_seq;
DROP TABLE IF EXISTS artists;
DROP SEQUENCE IF EXISTS artists_id_seq;

-- Create sequences
CREATE SEQUENCE IF NOT EXISTS albums_id_seq;
CREATE SEQUENCE IF NOT EXISTS artists_id_seq;

-- Create the artists table
CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    name TEXT,
    genre TEXT
);

-- Insert records into the artists table
INSERT INTO artists (name, genre) VALUES ('Pixies', 'indie');
INSERT INTO artists (name, genre) VALUES ('ABBA', 'pop');
INSERT INTO artists (name, genre) VALUES ('Taylor Swift', 'pop');
INSERT INTO artists (name, genre) VALUES ('Nina Simone', 'jazz');

-- Create the albums table with a foreign key reference to artists
CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    title TEXT,
    release_year INT,
    artist_id INT,
    CONSTRAINT fk_artist FOREIGN KEY (artist_id) REFERENCES artists(id) ON DELETE CASCADE
);

-- Insert records into the albums table
INSERT INTO albums (title, release_year, artist_id) VALUES ('The Cold Nose', 2008, 1);
INSERT INTO albums (title, release_year, artist_id) VALUES ('Nikita', 1998, 1);
