from app.extensions import db 
from datetime import datetime

class CareerGoal(db.Model):
    __tablename__ = 'career_goals'

    goal_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('career_goals', lazy=True))

    def __repr__(self):
        return f"<CareerGoal {self.title}>"
