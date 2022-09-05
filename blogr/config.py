import os
basedir = os.path.abspath(os.path.dirname(__file__))
class Config:
    DEBUG = os.environ.get("DEBUG") or False
    SECRET_KEY = os.environ.get("SECRET_KEY") or "blogr's-secret-key"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI") or "sqlite:///" + os.path.join(basedir, "blogr.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = True