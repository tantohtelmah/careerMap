from app.extensions import db 
from datetime import datetime
from app.models.job_milestones import job_milestones 

class Job(db.Model):
    __tablename__ = 'jobs'

    job_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    location = db.Column(db.String(150))
    url = db.Column(db.Text)
    source = db.Column(db.String(100))
    status = db.Column(db.String(50), default='applied')
    applied_date = db.Column(db.Date)
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    milestones = db.relationship('Milestone', secondary=job_milestones, backref=db.backref('jobs', lazy='dynamic'))

