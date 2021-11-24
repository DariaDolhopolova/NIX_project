"""DB model classes for directors table"""

from film_proj import db
from film_proj.models.association_tables import films_directors


class Directors(db.Model):
    """Directors table"""
    __tablename__ = 'directors'
    director_id = db.Column(db.Integer, primary_key=True)
    director_full_name = db.Column(db.VARCHAR(255), nullable=False)
    film_director = db.relationship(
        'Films', secondary=films_directors, lazy='subquery',
        backref=db.backref('dir_films', lazy=True))

    def __init__(self, director_full_name: str):
        self.director_full_name = director_full_name

    def __repr__(self):
        return f'Director: name: {self.director_full_name}'
