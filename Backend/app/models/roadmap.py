# models/roadmap.py
from app import db

class Roadmap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    career_goal = db.Column(db.String(100))
    data = db.Column(db.JSON)
