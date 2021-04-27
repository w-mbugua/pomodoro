from . import db
from datetime import datetime
from werkzeug.security import generate_password_hash,check_password_hash


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(20))
    password_hash = db.Column(db.String(255))
    timer = db.relationship('Timer', backref ='user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return f'User {self.username}'

class Timer(db.Model):
    __tablename__ = 'timers'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    timer_length = db.Column(db.Integer)
    break_length = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'User {self.name}'