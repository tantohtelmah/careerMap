import os
import json
from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import User
from openai import OpenAI

# --- Initialize OpenAI client ---
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

certifications_bp = Blueprint("certifications", __name__)

@certifications_bp.route("/", methods=["GET"])
@jwt_required(optional=True)        # ✅ allows route to run even without a token during local testing
def certifications():
    """
    Generate 5 relevant certification suggestions based on the user's profile.
    """
    try:
        # --- Get current user ---
        user_id = get_jwt_identity() or 1
        user = User.query.get(user_id)

        if not user:
            return jsonify({"error": "User not found"}), 404

        # --- Safe attribute extraction ---
        skills = user.skills or "None"
        education = user.education or "None"
        experience = user.experience or "None"

        # --- AI prompt ---
        prompt = f"""
        Based on this user's data:
        Skills: {skills}
        Education: {education}
        Experience: {experience}

        Suggest 5 relevant IT or software engineering certifications that could advance their career.
        Include: name, provider, description, and difficulty level.
        Respond strictly as a JSON array only.
        """

        # --- OpenAI call ---
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an AI certification advisor."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
        )

        # --- Extract and clean model output ---
        content = response.choices[0].message.content.strip()

        # remove Markdown fences like ```json ... ```
        if content.startswith("```"):
            content = (
                content.replace("```json", "")
                .replace("```", "")
                .strip()
            )

        # --- Parse JSON safely ---
        data = json.loads(content)

        return jsonify({"suggestions": data}), 200

    except json.JSONDecodeError as e:
        print("⚠️ AI returned invalid JSON:", content)
        return jsonify({"error": "Invalid AI JSON output"}), 500

    except Exception as e:
        print("AI Certification Suggestion Error:", str(e))
        return jsonify({"error": "AI generation failed"}), 500
