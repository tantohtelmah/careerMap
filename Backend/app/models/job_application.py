from datetime import datetime
from app import db

class JobApplication(db.Model):
    __tablename__ = 'job_applications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'), nullable=False)
    status = db.Column(db.String(50), default='applied')  # applied, interviewed, accepted, rejected
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)
