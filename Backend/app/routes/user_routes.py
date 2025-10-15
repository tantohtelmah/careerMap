from flask import Blueprint, request, jsonify
from app.models.user import User
from app.extensions import db

user_bp = Blueprint('user_bp', __name__)

# Create a new user
@user_bp.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists"}), 400

    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"id": user.id, "name": user.name, "email": user.email}), 201

# Get all users
@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "name": u.name, "email": u.email} for u in users])

# Get single user by ID
@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify({
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "skills": user.skills,
        "education": user.education,
        "experience": user.experience,
        "preferences": user.preferences
    })

# Update user
@user_bp.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    data = request.get_json()
    for key in ["name", "skills", "education", "experience", "preferences"]:
        if key in data:
            setattr(user, key, data[key])
    db.session.commit()
    return jsonify({"message": "User updated successfully"})
