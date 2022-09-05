from blogr import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    bio = db.Column(db.Text)
    password_hash = db.Column(db.String(128))
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    comments = db.relationship("Comment", backref="user", lazy=True)
    posts = db.relationship("Post", backref="user", lazy=True)

    def __repr__(self):
        return "<User {} {}>".format(self.first_name, self.last_name)

    def full_name(self):
        return "{} {}".format(self.first_name, self.last_name)
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)