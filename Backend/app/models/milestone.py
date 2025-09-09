from app.extensions import db 
from datetime import datetime

class Milestone(db.Model):
    __tablename__ = 'milestones'

    milestone_id = db.Column(db.Integer, primary_key=True)
    goal_id = db.Column(db.Integer, db.ForeignKey('career_goals.goal_id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500))
    target_date = db.Column(db.Date)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    goal = db.relationship('CareerGoal', backref=db.backref('milestones', lazy=True))

    def __repr__(self):
        return f"<Milestone {self.title}>"
