"""Project init"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_restx import Api
from config import Config

app = Flask(__name__)

api = Api(app, version="1.0", title="Film Project API",
          description="Just API")

login_manager = LoginManager(app)
login_manager.init_app(app)

app.config.from_object(Config)
db = SQLAlchemy(app)

migrate = Migrate(app, db)

# import routes and modules
from film_proj import routes, models_file
from film_proj.models import auth
