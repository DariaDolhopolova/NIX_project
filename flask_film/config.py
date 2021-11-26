"""Config file for migrations"""

class Config:
    """configuration for database"""
    db_name = "films_db"
    dialect = "postgresql"

    # or pg8000
    driver = "psycopg2"
    login = "postgres"
    passw = "tomato12"
    host = "localhost"

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'{dialect}+{driver}://{login}:{passw}@{host}/{db_name}'
