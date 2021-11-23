"""Config file for migrations"""

class Config:
    """configuration for database"""
    db_name = "films_db"
    dialect = "postgresql"

    driver = "psycopg2"
    login = "postgres"
    passw = "my_password"
    host = "localhost"

    SQLALCHEMY_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = f'{dialect}+{driver}://{login}:{passw}@{host}/{db_name}'