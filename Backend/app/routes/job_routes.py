import os
import re
import json
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from openai import OpenAI

# --------------------------------------------------------------------------
#  🔹 Blueprint Setup
# --------------------------------------------------------------------------
job_bp = Blueprint("job", __name__, url_prefix="/api/jobs")

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


# --------------------------------------------------------------------------
#  🧠 AI-Powered Job Recommendations
# --------------------------------------------------------------------------
@job_bp.route("/recommended", methods=["GET"])
@jwt_required(optional=True)
def recommended_jobs():
    """
    Generate AI-powered job recommendations for the current user
    (JWT required, or fallback to demo user if JWT is missing).
    """
    try:
        # ------------------------------------------------------------------
        #  1️⃣ Identify user (JWT or fallback)
        # ------------------------------------------------------------------
        user_id = get_jwt_identity() or 1
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        # ------------------------------------------------------------------
        #  2️⃣ Build prompt for OpenAI
        # ------------------------------------------------------------------
        skills = user.skills or "None"
        education = user.education or "None"
        experience = user.experience or "None"
        preferences = getattr(user, "preferences", "None")

        prompt = f"""
        You are an expert career advisor. Recommend 5 IT or software-related jobs 
        that best fit this user's background.

        Skills: {skills}
        Education: {education}
        Experience: {experience}
        Career goals or preferences: {preferences}

        For each job, include these exact lowercase keys:
        title, company, description, required_skills (list), 
        experience_level (beginner, intermediate, advanced), link.

        Respond strictly as a JSON array only.
        """

        # ------------------------------------------------------------------
        #  3️⃣ Query OpenAI model
        # ------------------------------------------------------------------
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI job recommendation assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )

        # ------------------------------------------------------------------
        #  4️⃣ Clean and parse model output
        # ------------------------------------------------------------------
        content = response.choices[0].message.content.strip()

        # Remove markdown code fences (```json ... ```)
        content = re.sub(r"^```(?:json)?", "", content.strip())
        content = re.sub(r"```$", "", content.strip())
        content = content.strip()

        try:
            recommendations = json.loads(content)
        except json.JSONDecodeError:
            print("⚠️ Invalid AI JSON output:\n", content)
            recommendations = [{"error": "Invalid JSON response", "raw": content}]

        # ------------------------------------------------------------------
        #  5️⃣ Normalize keys to ensure consistent frontend fields
        # ------------------------------------------------------------------
        normalized = []
        for job in recommendations:
            normalized.append({
                "title": job.get("title") or job.get("Title") or "Untitled Role",
                "company": job.get("company") or job.get("Company") or "N/A",
                "description": job.get("description") or job.get("Description") or "",
                "required_skills": job.get("required_skills") or job.get("Required Skills") or [],
                "experience_level": job.get("experience_level") or job.get("Experience Level") or "Intermediate",
                "link": job.get("link") or job.get("Link") or "#"
            })

        # ------------------------------------------------------------------
        #  6️⃣ Return final JSON response
        # ------------------------------------------------------------------
        return jsonify({
            "user": {
                "id": user.id,
                "username": getattr(user, "username", "Guest"),
                "skills": skills,
                "education": education,
                "experience": experience,
            },
            "recommendations": normalized,
        }), 200

    # ----------------------------------------------------------------------
    #  7️⃣ Global error handling
    # ----------------------------------------------------------------------
    except Exception as e:
        print("AI Recommendation Error:", str(e))
        return jsonify({"error": "Failed to generate job recommendations"}), 500
