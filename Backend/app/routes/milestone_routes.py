from flask import Blueprint, request, jsonify


milestone_bp = Blueprint('milestone_bp', __name__)

from app.extensions import db
from app.models.milestone import Milestone

# Create
@milestone_bp.route('/', methods=['POST'])
def create_milestone():
    data = request.json
    milestone = Milestone(**data)
    db.session.add(milestone)
    db.session.commit()
    return jsonify({'message': 'Milestone created', 'data': data}), 201

# Read
@milestone_bp.route('/<int:goal_id>', methods=['GET'])
def get_milestones(goal_id):
    milestones = Milestone.query.filter_by(goal_id=goal_id).all()
    return jsonify([{
        'milestone_id': m.milestone_id,
        'title': m.title,
        'description': m.description,
        'target_date': m.target_date
    } for m in milestones])

# Update
@milestone_bp.route('/<int:milestone_id>', methods=['PUT'])
def update_milestone(milestone_id):
    milestone = Milestone.query.get_or_404(milestone_id)
    data = request.json
    milestone.title = data.get('title', milestone.title)
    milestone.description = data.get('description', milestone.description)
    milestone.target_date = data.get('target_date', milestone.target_date)
    db.session.commit()
    return jsonify({'message': 'Milestone updated'})

# Delete
@milestone_bp.route('/<int:milestone_id>', methods=['DELETE'])
def delete_milestone(milestone_id):
    milestone = Milestone.query.get_or_404(milestone_id)
    db.session.delete(milestone)
    db.session.commit()
    return jsonify({'message': 'Milestone deleted'})
