"""DB model class for films"""

from film_proj import db
from film_proj.models.association_tables import films_directors
from film_proj.models.association_tables import films_genres


class Films(db.Model):
    """Film table"""
    __tablename__ = 'films'
    film_id = db.Column(db.Integer, primary_key=True)
    film_name = db.Column(db.VARCHAR(255), unique=False, nullable=False, index=True)
    poster = db.Column(db.Text, nullable=False)
    release_date = db.Column(db.Integer, unique=False, nullable=False, index=True)
    rating = db.Column(db.Float, unique=False, nullable=False, index=True)
    added_user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    description = db.Column(db.Text, nullable=True, index=True)

    film_genre = db.relationship(
        'Genres', secondary=films_genres, lazy='subquery',
        backref=db.backref('films_genres', lazy=True))

    film_director = db.relationship(
        'Directors', secondary=films_directors, lazy='subquery',
        backref=db.backref('films_directors', lazy=True))

    def __init__(self, film_name: str, poster: str, release_date: int,
                 rating: float, added_user_id: int, description: str = None):

        self.film_name = film_name
        self.poster = poster
        self.release_date = release_date
        self.rating = rating
        self.description = description
        self.added_user_id = added_user_id

    def __repr__(self):
        return f'film_id: {self.film_id}, film_name:{self.film_name}, ' \
               f'poster: {self.poster}, release_date: {self.release_date}, ' \
               f'rating: {self.rating}, added_user_id: {self.added_user_id}, ' \
               f'description: {self.description}'
