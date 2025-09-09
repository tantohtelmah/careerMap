from flask import Blueprint, request, jsonify

job_history_bp = Blueprint('job_history_bp', __name__)

from app.extensions import db
from app.models.job_history import JobHistory

# Create
@job_history_bp.route('/', methods=['POST'])
def add_job_history():
    data = request.json
    history = JobHistory(**data)
    db.session.add(history)
    db.session.commit()
    return jsonify({'message': 'Job history added', 'data': data}), 201

# Read
@job_history_bp.route('/<int:job_id>', methods=['GET'])
def get_job_history(job_id):
    history = JobHistory.query.filter_by(job_id=job_id).all()
    return jsonify([{
        'history_id': h.history_id,
        'status': h.status,
        'note': h.note,
        'updated_at': h.updated_at
    } for h in history])
