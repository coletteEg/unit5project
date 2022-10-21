"""Models for movie ratings app."""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    email = db.Column(db.String(), unique = True, nullable = False)
    password = db.Column(db.String(30), nullable = False)


    def __repr__(self):
      return f'<User user_id={self.user_id} email={self.email}>'


class Movie(db.Model):

    __tablename__ = 'movies'

    movie_id = db.Column(db.Integer, primary_key =True, autoincrement = True)
    title = db.Column(db.String, unique = True, nullable = False)
    overview = db.Column(db.Text, nullable = False)
    release_date = db.Column(db.DateTime, nullable = False)
    poster_path = db.Column(db.String, nullable = False, unique = True)


    def __repr__(self):
        return (f"Movie: {self.title}\nSynopsis: {self.overview}\nRelease Date: {self.release_date}")


class Rating(db.Model):
    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    score = db.Column(db.Integer)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.movie_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))

    movie = db.relationship('Movie', backref = 'ratings')
    user = db.relationship('User', backref = 'ratings')
 
    def __repr__(self):
        return (f"Rating ID: {self.rating_id}\nScore: {self.score}")

def connect_to_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from flask import Flask
    app = Flask(__name__)
    connect_to_db(app)
    print("Connected to db...")
