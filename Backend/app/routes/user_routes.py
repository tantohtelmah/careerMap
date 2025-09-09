from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from app.extensions import db
from app.models.user import User

user_bp = Blueprint('user_bp', __name__)

# Create User
@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.json

    # Ensure password is provided
    if "password" not in data or not data["password"]:
        return jsonify({"error": "Password is required"}), 400

    hashed_password = generate_password_hash(data["password"])

    user = User(
        full_name=data["full_name"],
        email=data["email"],
        password_hash=hashed_password,
        career_goal=data.get("career_goal")
    )

    db.session.add(user)
    db.session.commit()

    return jsonify({
        'message': 'User created',
        'user': {
            'user_id': user.user_id,
            'full_name': user.full_name,
            'email': user.email,
            'career_goal': user.career_goal
        }
    }), 201

# Read Users
@user_bp.route('/', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{
        'user_id': u.user_id,
        'full_name': u.full_name,
        'email': u.email,
        'career_goal': u.career_goal
    } for u in users])

# Update User
@user_bp.route('/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.json
    user.full_name = data.get('full_name', user.full_name)
    user.email = data.get('email', user.email)
    if "password" in data and data["password"]:  # if updating password
        user.password_hash = generate_password_hash(data["password"])
    user.career_goal = data.get('career_goal', user.career_goal)
    db.session.commit()
    return jsonify({'message': 'User updated'})

# Delete User
@user_bp.route('/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted'})
