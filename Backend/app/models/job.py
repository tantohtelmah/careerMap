from datetime import datetime
from app import db

# Association table for AI recommended jobs (many-to-many)
ai_job_assoc = db.Table(
    'ai_recommended_jobs',
    db.Column('ai_id', db.Integer, db.ForeignKey('ai_recommendations.id'), primary_key=True),
    db.Column('job_id', db.Integer, db.ForeignKey('jobs.id'), primary_key=True)
)

class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    company = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=True)
    requirements = db.Column(db.JSON, default=[])
    location = db.Column(db.String(150), nullable=True)
    link = db.Column(db.String(300), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    job_applications = db.relationship('JobApplication', backref='job', lazy=True)
    ai_recommendations = db.relationship('AIRecommendation', secondary=ai_job_assoc,
                                         back_populates='recommended_jobs')
