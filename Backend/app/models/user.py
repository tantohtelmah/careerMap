from app.extensions import db 
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    career_goal = db.Column(db.String(250))  # user roadmap / dream career
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to Jobs
    jobs = db.relationship('Job', backref='user', lazy=True)

    def __repr__(self):
        return f"<User {self.full_name} ({self.email})>"
