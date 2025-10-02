from flask import Blueprint, request, jsonify
from app.models.career_goal import CareerGoal
from app.extensions import db
from app.services.ai_service import get_career_path_suggestions

career_goal_bp = Blueprint("career_goal_bp", __name__)

# Get all career goals for a user
@career_goal_bp.route("/career_goals/<int:user_id>", methods=["GET"])
def get_career_goals(user_id):
    goals = CareerGoal.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "id": g.id,
        "goal": g.goal,
        "ai_recommendations": g.ai_recommendations,
        "created_at": g.created_at
    } for g in goals])

# Create a career goal
@career_goal_bp.route("/career_goals", methods=["POST"])
def create_career_goal():
    data = request.get_json()
    user_id = data.get("user_id")
    goal_text = data.get("goal")

    if not user_id or not goal_text:
        return jsonify({"error": "user_id and goal are required"}), 400

    # Optionally get AI suggestions
    ai_suggestions = get_career_path_suggestions(user_id, goal_text)

    career_goal = CareerGoal(
        user_id=user_id,
        goal=goal_text,
        ai_recommendations=ai_suggestions
    )
    db.session.add(career_goal)
    db.session.commit()
    return jsonify({
        "id": career_goal.id,
        "goal": career_goal.goal,
        "ai_recommendations": career_goal.ai_recommendations
    }), 201
