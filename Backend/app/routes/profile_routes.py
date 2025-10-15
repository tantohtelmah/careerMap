from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, User
from app.utils.s3_uploads import upload_to_s3

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/upload_resume", methods=["POST"])
# @jwt_required()
def upload_resume():
    user_id = 1
    # get_jwt_identity()
    file = request.files.get("resume")

    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    if not file.filename.lower().endswith((".pdf", ".docx")):
        return jsonify({"error": "Invalid file format"}), 400

    file_url = upload_to_s3(file, user_id)

    user = User.query.get(user_id)
    user.resume_url = file_url
    db.session.commit()

    return jsonify({"message": "Resume uploaded successfully", "resume_url": file_url})

# @profile_bp.route("/api/auth/upload_profile_image", methods=["POST", "OPTIONS"])
# def upload_profile_image():
#     # ✅ Let Flask-CORS handle headers; just return 200 for preflight
#     if request.method == "OPTIONS":
#         return '', 200

#     user_id = get_jwt_identity() or 1  # use 1 for local testing
#     file = request.files.get("profile_image")

#     if not file:
#         return jsonify({"error": "No file provided"}), 400

#     filename = secure_filename(file.filename)
#     upload_dir = os.path.join("app", "static", "profile_images")
#     os.makedirs(upload_dir, exist_ok=True)
#     path = os.path.join(upload_dir, f"{user_id}_{filename}")
#     file.save(path)

#     user = User.query.get(user_id)
#     user.profile_image = f"/static/uploads/{user_id}_{filename}"
#     db.session.commit()

#     return jsonify({
#         "message": "Upload successful",
#         "profile_image": user.profile_image,
#     }), 200

@auth_bp.route("/update-profile", methods=["PUT"])
@jwt_required()
def update_profile():
    user_id = get_jwt_identity() or 1
    user = User.query.get(user_id)

    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    user.username = data.get("username", user.username)
    user.email = data.get("email", user.email)
    user.skills = data.get("skills", user.skills)
    user.education = data.get("education", user.education)
    user.experience = data.get("experience", user.experience)
    user.preferences = data.get("preferences", user.preferences)
    db.session.commit()

    return jsonify({
        "message": "Profile updated successfully",
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "skills": user.skills,
            "education": user.education,
            "experience": user.experience,
            "preferences": user.preferences
        }
    }), 200
