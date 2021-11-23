"""Association tables for directors and genres tables"""

from film_proj import db

films_directors = db.Table(
    'films_directors',
    db.Column('film_id', db.Integer, db.ForeignKey('films.film_id')),
    db.Column('director_id', db.Integer, db.ForeignKey('directors.director_id')))

films_genres = db.Table(
    'films_genres',
    db.Column('film_id', db.Integer, db.ForeignKey('films.film_id')),
    db.Column('genre_id', db.Integer, db.ForeignKey('genres.genre_id')))
