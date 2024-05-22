import json
from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Usuarios(UserMixin, db.Model):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email=db.Column(db.String(50), unique=True, nullable=False)
    password_ = db.Column(db.String(128), nullable=False)
    roles = db.Column(db.String(50), nullable=False)

    def __init__(self, username, password,email, roles):
        self.username = username
        self.email=email
        self.roles = roles
        self.password_hash = generate_password_hash(password)
    def save(self):
        db.session.add(self)
        db.session.commit()
        