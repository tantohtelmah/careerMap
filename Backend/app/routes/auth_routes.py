# app/routes/auth_routes.py
from flask import Blueprint, request, jsonify, current_app
from app.extensions import db
from app.models.user import User
import jwt
import datetime
from functools import wraps
from werkzeug.utils import secure_filename
import os


auth_bp = Blueprint("auth", __name__, url_prefix="/api/auth")

# ✅ Signup
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "All fields are required"}), 400

    # Check if user already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400
    if User.query.filter_by(username=username).first():
        return jsonify({"error": "Username already taken"}), 400

    # Create user and hash password
    user = User(username=username, email=email)
    user.set_password(password)

    # Add to DB
    db.session.add(user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 201


# ✅ Login
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Missing email or password"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT token
    token = jwt.encode(
        {
            "user_id": user.id,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        },
        current_app.config["SECRET_KEY"],
        algorithm="HS256"
    )

    return jsonify({
        "message": "Login successful",
        "token": token,
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }
    }), 200

# ✅ Auth decorator
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]  # Bearer <token>

        if not token:
            return jsonify({"error": "Token is missing"}), 401

        try:
            data = jwt.decode(token, current_app.config["SECRET_KEY"], algorithms=["HS256"])
            current_user = User.query.get(data["user_id"])
        except:
            return jsonify({"error": "Token is invalid"}), 401

        return f(current_user, *args, **kwargs)

    return decorated


# ✅ Profile route
@auth_bp.route("/profile", methods=["GET"])
@token_required
def profile(current_user):
    return jsonify({
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "profile_image": current_user.profile_image,
        "skills": current_user.skills,
        "education": current_user.education,
        "experience": current_user.experience,
        "preferences": current_user.preferences
    }), 200
    
@auth_bp.route("/upload-profile-image", methods=["POST", "OPTIONS"])
@token_required
def upload_profile_image(current_user):
    if request.method == "OPTIONS":
        return '', 200

    if "file" not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "No selected file"}), 400

    # Allowed extensions
    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "gif"}
    def allowed_file(filename):
        return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

    if allowed_file(file.filename):
        filename = secure_filename(file.filename)
        upload_folder = os.path.join(current_app.root_path, "static", "uploads")
        os.makedirs(upload_folder, exist_ok=True)

        file_path = os.path.join(upload_folder, f"user_{current_user.id}_{filename}")
        file.save(file_path)

        current_user.profile_image = f"/static/uploads/user_{current_user.id}_{filename}"
        db.session.commit()

        return jsonify({
            "message": "Profile image uploaded successfully",
            "profile_image": current_user.profile_image
        }), 200

    return jsonify({"error": "File type not allowed"}), 400


@auth_bp.route("/update-profile", methods=["PUT"])
@token_required
def update_profile(current_user):
    data = request.get_json()

    # Basic fields
    if "username" in data:
        current_user.username = data["username"]
    if "email" in data:
        current_user.email = data["email"]

    # JSON fields
    if "skills" in data:
        current_user.skills = data["skills"]
    if "education" in data:
        current_user.education = data["education"]
    if "experience" in data:
        current_user.experience = data["experience"]
    if "preferences" in data:
        current_user.preferences = data["preferences"]

    db.session.commit()

    return jsonify({
        "message": "Profile updated successfully",
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email,
            "skills": current_user.skills,
            "education": current_user.education,
            "experience": current_user.experience,
            "preferences": current_user.preferences,
            "profile_image": current_user.profile_image
        }
    }), 200
