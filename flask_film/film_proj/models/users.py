"""DB model class for users table"""

from film_proj import db


class Users(db.Model):
    """Users table"""

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.VARCHAR(255), nullable=False)
    last_name = db.Column(db.VARCHAR(255), nullable=False)
    username = db.Column(db.VARCHAR(255), unique=True, nullable=False)
    user_group_id = db.Column(db.Integer, db.ForeignKey('user_groups.user_group_id'), nullable=False)
    password = db.Column(db.VARCHAR(255))

    def __init__(self, first_name: str, last_name: str, username: str, password: str, user_group_id: int = 1):
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.user_group_id = user_group_id

    def __repr__(self):
        return f'User: username: {self.username}, first name: {self.first_name},' \
               f' last name: {self.last_name}, user group id: {self.user_group_id}'

