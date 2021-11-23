"""DB model class for genres table"""

from film_proj import db
from film_proj.models.association_tables import films_genres


class Genres(db.Model):
    """Genres table"""

    __tablename__ = 'genres'
    genre_id = db.Column(db.Integer, primary_key=True)
    genre_name = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    film_genre = db.relationship(
        'Films', secondary=films_genres, lazy='subquery',
        backref=db.backref('genre_films', lazy=True))

    def __init__(self, genre_name: str):
        self.genre_name = genre_name

    def __repr__(self):
        return f'Genre: {self.genre_name}'
