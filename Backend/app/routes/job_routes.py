from flask import Blueprint, request, jsonify
from app.models.job import Job
from app.extensions import db
from app.services.ai_service import get_recommended_jobs

# job_bp = Blueprint("job_bp", __name__)

# # Get all jobs
# @job_bp.route("/jobs", methods=["GET"])
# def get_jobs():
#     jobs = Job.query.all()
#     return jsonify([{
#         "id": j.id,
#         "title": j.title,
#         "company": j.company,
#         "description": j.description,
#         "requirements": j.requirements,
#         "location": j.location,
#         "link": j.link
#     } for j in jobs])

# # Create a job
# @job_bp.route("/jobs", methods=["POST"])
# def create_job():
#     data = request.get_json()
#     job = Job(
#         title=data.get("title"),
#         company=data.get("company"),
#         description=data.get("description"),
#         requirements=data.get("requirements", []),
#         location=data.get("location"),
#         link=data.get("link")
#     )
#     db.session.add(job)
#     db.session.commit()
#     return jsonify({"id": job.id, "title": job.title}), 201

# # Show AI-recommended jobs for a user
# @job_bp.route("/jobs/recommended", methods=["GET"])
# def recommended_jobs():
#     user_id = request.args.get("user_id")
#     if not user_id:
#         return jsonify({"error": "user_id is required"}), 400

#     jobs = get_recommended_jobs(user_id)
#     return jsonify(jobs)

# from flask import Blueprint, request, jsonify

job_bp = Blueprint("job", __name__)

@job_bp.route("/recommended", methods=["POST"])
def recommended_jobs():
    """
    Recommend jobs based on user's skills, experience, and career goal.
    """
    data = request.get_json()

    # Extract inputs
    skills = data.get("skills", [])
    experience = data.get("experience", 0)
    career_goal = data.get("career_goal", "")

    # For now → return dummy jobs using inputs
    recommendations = [
        {
            "title": f"{career_goal} (Python Focus)",
            "match": 90 if "python" in skills else 70,
            "required_experience": 2
        },
        {
            "title": "Data Engineer",
            "match": 80 if "sql" in skills else 65,
            "required_experience": 3
        },
        {
            "title": "Fullstack Developer",
            "match": 75 if experience >= 2 else 55,
            "required_experience": 2
        }
    ]

    return jsonify({
        "input_received": {
            "skills": skills,
            "experience": experience,
            "career_goal": career_goal
        },
        "recommended_jobs": recommendations
    })
