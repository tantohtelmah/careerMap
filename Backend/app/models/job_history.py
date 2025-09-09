from app.extensions import db 
from datetime import datetime

class JobHistory(db.Model):
    __tablename__ = 'job_history'

    history_id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.job_id'), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow)
    note = db.Column(db.String(500))  # Optional note for follow-ups

    # Relationship to Job
    job = db.relationship('Job', backref=db.backref('history', lazy=True))

    def __repr__(self):
        return f"<JobHistory job_id={self.job_id} status={self.status} updated_at={self.updated_at}>"
