from app.extensions import db 

# Linking table for Jobs and Milestones (Many-to-Many)
job_milestones = db.Table(
    'job_milestones',
    db.Column('job_id', db.Integer, db.ForeignKey('jobs.job_id'), primary_key=True),
    db.Column('milestone_id', db.Integer, db.ForeignKey('milestones.milestone_id'), primary_key=True)
)
