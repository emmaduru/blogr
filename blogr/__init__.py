from blogr.config import Config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = "login"

from blogr.views.auth import auth
from blogr.views.post import post

app.register_blueprint(auth, url_prefix="/auth")
app.register_blueprint(post, url_prefix="/posts")

from blogr.views import views