import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, String, Integer

database_path = os.environ['DATABASE_URL']

db = SQLAlchemy()

def setup_db(app, database_path=database_path):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)

class Player(db.Model):
    __tablename__ = 'player'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    skill = Column(Integer)

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def insert(self):
        db.session.add(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def format(self):
        return {
            'name': self.name,
            'skill': self.skill
        }