from flask import Blueprint, request, jsonify

career_goal_bp = Blueprint('career_goal_bp', __name__)

from app.extensions import db
from app.models.career_goal import CareerGoal

# Create
@career_goal_bp.route('/', methods=['POST'])
def create_goal():
    data = request.json
    goal = CareerGoal(**data)
    db.session.add(goal)
    db.session.commit()
    return jsonify({'message': 'Career goal created', 'data': data}), 201

# Read
@career_goal_bp.route('/<int:user_id>', methods=['GET'])
def get_goals(user_id):
    goals = CareerGoal.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'goal_id': g.goal_id,
        'title': g.title,
        'description': g.description
    } for g in goals])

# Update
@career_goal_bp.route('/<int:goal_id>', methods=['PUT'])
def update_goal(goal_id):
    goal = CareerGoal.query.get_or_404(goal_id)
    data = request.json
    goal.title = data.get('title', goal.title)
    goal.description = data.get('description', goal.description)
    db.session.commit()
    return jsonify({'message': 'Career goal updated'})

# Delete
@career_goal_bp.route('/<int:goal_id>', methods=['DELETE'])
def delete_goal(goal_id):
    goal = CareerGoal.query.get_or_404(goal_id)
    db.session.delete(goal)
    db.session.commit()
    return jsonify({'message': 'Career goal deleted'})
