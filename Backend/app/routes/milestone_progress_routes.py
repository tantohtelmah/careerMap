from flask import Blueprint, request, jsonify

progress_bp = Blueprint('progress_bp', __name__)

from app.extensions import db
from app.models.milestone_progress import MilestoneProgress

# Create
@progress_bp.route('/', methods=['POST'])
def add_progress():
    data = request.json
    progress = MilestoneProgress(**data)
    db.session.add(progress)
    db.session.commit()
    return jsonify({'message': 'Progress added', 'data': data}), 201

# Read
@progress_bp.route('/<int:milestone_id>', methods=['GET'])
def get_progress(milestone_id):
    progresses = MilestoneProgress.query.filter_by(milestone_id=milestone_id).all()
    return jsonify([{
        'progress_id': p.progress_id,
        'status': p.status,
        'progress_date': p.progress_date,
        'note': p.note
    } for p in progresses])

# Update
@progress_bp.route('/<int:progress_id>', methods=['PUT'])
def update_progress(progress_id):
    progress = MilestoneProgress.query.get_or_404(progress_id)
    data = request.json
    progress.status = data.get('status', progress.status)
    progress.note = data.get('note', progress.note)
    db.session.commit()
    return jsonify({'message': 'Progress updated'})

# Delete
@progress_bp.route('/<int:progress_id>', methods=['DELETE'])
def delete_progress(progress_id):
    progress = MilestoneProgress.query.get_or_404(progress_id)
    db.session.delete(progress)
    db.session.commit()
    return jsonify({'message': 'Progress deleted'})
