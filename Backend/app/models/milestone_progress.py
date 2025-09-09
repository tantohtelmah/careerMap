from app.extensions import db 
from datetime import datetime

class MilestoneProgress(db.Model):
    __tablename__ = 'milestone_progress'

    progress_id = db.Column(db.Integer, primary_key=True)
    milestone_id = db.Column(db.Integer, db.ForeignKey('milestones.milestone_id'), nullable=False)
    status = db.Column(db.String(50), default='pending')  # pending, in_progress, completed
    progress_date = db.Column(db.DateTime, default=datetime.utcnow)
    note = db.Column(db.String(500))

    milestone = db.relationship('Milestone', backref=db.backref('progress', lazy=True))

    def __repr__(self):
        return f"<MilestoneProgress milestone={self.milestone_id} status={self.status}>"

