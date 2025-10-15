from datetime import datetime
from app import db

class CareerGoal(db.Model):
    __tablename__ = 'career_goals'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    goal = db.Column(db.String(200), nullable=False)
    ai_recommendations = db.Column(db.JSON, default={})  # AI suggestions for this goal
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
