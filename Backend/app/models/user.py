from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    skills = db.Column(db.JSON, default=[])
    education = db.Column(db.JSON, default=[])
    experience = db.Column(db.JSON, default=[])
    preferences = db.Column(db.JSON, default={})
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    profile_image = db.Column(db.String(255), nullable=True)  # Cloud file URL path (NEW)
    career_goals = db.relationship('CareerGoal', backref='user', lazy=True)
    job_applications = db.relationship('JobApplication', backref='user', lazy=True)
    notifications = db.relationship('Notification', backref='user', lazy=True)
    ai_recommendations = db.relationship('AIRecommendation', backref='user', lazy=True)
    resume_url = db.Column(db.String(255), nullable=True)  # Cloud file URL path(new)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
