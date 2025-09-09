from app.extensions import db 

class Tag(db.Model):
    __tablename__ = 'tags'

    tag_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
 
    def __repr__(self):
        return f"<Tag {self.name}>"
    
#Optional Many-to-Many linking table for Jobs and Tags:
job_tags = db.Table(
	'job_tags',
	db.Column('job_id', db.Integer, db.ForeignKey('jobs.job_id'), primary_key=True),
	db.Column('tag_id', db.Integer, db.ForeignKey('tags.tag_id'), primary_key=True)
)