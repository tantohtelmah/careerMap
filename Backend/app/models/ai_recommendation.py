from datetime import datetime
from app import db

class AIRecommendation(db.Model):
    __tablename__ = 'ai_recommendations'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # career, job, learning
    content = db.Column(db.JSON, nullable=False)  # AI output as JSON
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Many-to-many relationship for recommended jobs
    recommended_jobs = db.relationship('Job', secondary='ai_recommended_jobs',
                                       back_populates='ai_recommendations')
