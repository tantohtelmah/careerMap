# app/routes/auth_routes.py
from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.user import User
import jwt
import datetime
from flask import current_app

auth_bp = Blueprint("auth", __name__)

# ✅ Register
@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    if not data or not data.get("username") or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing required fields"}), 400

    # Check if email/username already exists
    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"error": "Email already registered"}), 400
    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"error": "Username already taken"}), 400

    new_user = User(
        username=data["username"],
        email=data["email"]
    )
    new_user.set_password(data["password"])

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


# ✅ Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data or not data.get("email") or not data.get("password"):
        return jsonify({"error": "Missing email or password"}), 400

    user = User.query.filter_by(email=data["email"]).first()
    if user and user.check_password(data["password"]):
        # Generate JWT token
        token = jwt.encode({
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }, current_app.config["SECRET_KEY"], algorithm="HS256")

        return jsonify({"token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401
