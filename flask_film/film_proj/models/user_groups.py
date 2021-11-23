"""DB model class for User Groups"""

from film_proj import db


class UserGroups(db.Model):
    """UserGroups table"""
    user_group_id = db.Column(db.Integer, primary_key=True)
    user_group_name = db.Column(db.VARCHAR(255), unique=True, nullable=False)

    def __init__(self, user_group_name):
        self.user_group_name = user_group_name

    def __repr__(self):
        return f'User group: {self.user_group_name}'
