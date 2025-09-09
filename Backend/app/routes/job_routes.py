from flask import Blueprint, request, jsonify

job_bp = Blueprint('job_bp', __name__)

from app.extensions import db
from app.models.jobs import Job

# Create
@job_bp.route('/', methods=['POST'])
def create_job():
    data = request.json
    job = Job(**data)
    db.session.add(job)
    db.session.commit()
    return jsonify({'message': 'Job created', 'job': data}), 201

# Read
@job_bp.route('/<int:user_id>', methods=['GET'])
def get_jobs(user_id):
    jobs = Job.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'job_id': j.job_id,
        'title': j.title,
        'company': j.company,
        'status': j.status
    } for j in jobs])

# Update
@job_bp.route('/<int:job_id>', methods=['PUT'])
def update_job(job_id):
    job = Job.query.get_or_404(job_id)
    data = request.json
    job.status = data.get('status', job.status)
    job.notes = data.get('notes', job.notes)
    db.session.commit()
    return jsonify({'message': 'Job updated'})

# Delete
@job_bp.route('/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = Job.query.get_or_404(job_id)
    db.session.delete(job)
    db.session.commit()
    return jsonify({'message': 'Job deleted'})
