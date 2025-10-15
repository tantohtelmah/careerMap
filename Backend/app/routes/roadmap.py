from flask import Blueprint, request, jsonify
import os, json, re
import openai
from dotenv import load_dotenv
# from flask_jwt_extended import jwt_required

# --- Load environment variables and initialize OpenAI ---
load_dotenv()

roadmap_bp = Blueprint("roadmap_bp", __name__)

@roadmap_bp.route("/roadmap", methods=["POST", "OPTIONS"])
# Uncomment the next line if you want JWT protection later
# @jwt_required(optional=True)
def generate_roadmap():
    try:
        # --- Handle CORS preflight request ---
        if request.method == "OPTIONS":
            return jsonify({"msg": "CORS preflight OK"}), 200

        # --- Get request data ---
        data = request.get_json()
        print("Received data:", data)

        if not data:
            return jsonify({"error": "No data provided"}), 400

        career_goal = data.get("career_goal", "").strip()
        education = data.get("education", "").strip()
        skills = data.get("skills", "").strip()

        if not career_goal or not education or not skills:
            return jsonify({"error": "All fields are required"}), 400

        # --- Build the prompt for OpenAI ---
        prompt = (
            f"You are a career mentor AI. Generate a step-by-step roadmap to help "
            f"the user become a {career_goal}. They have education: {education}, "
            f"and skills: {skills}. Include 5–8 milestones in JSON format. "
            f"Each milestone should include 'milestone', 'description', 'resources', and 'target_date'."
        )

        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
        )

        text_output = response.choices[0].message.content.strip()
        print("Raw model output:", text_output[:300], "...")  # debug

        import re

        try:
            json_match = re.search(r"```json\s*(\{.*?\}|\[.*?\])\s*```", text_output, re.DOTALL)
            if json_match:
                clean_json = json_match.group(1).strip()
            else:
                fallback_match = re.search(r"(\{.*\}|\[.*\])", text_output, re.DOTALL)
                clean_json = fallback_match.group(1).strip() if fallback_match else None

            if clean_json:
                roadmap_data = json.loads(clean_json)
            else:
                raise ValueError("No JSON structure found in text output.")

            if isinstance(roadmap_data, dict):
                if "roadmap" in roadmap_data:
                    roadmap = roadmap_data["roadmap"]
                elif "milestones" in roadmap_data:
                    roadmap = roadmap_data["milestones"]
                else:
                    roadmap = [roadmap_data]
            elif isinstance(roadmap_data, list):
                roadmap = roadmap_data
            else:
                roadmap = [{"step": 1, "milestone": "AI Output", "details": roadmap_data}]

        except Exception as e:
            print("JSON parse failed:", e)
            roadmap = [{"step": 1, "milestone": "AI Output", "details": text_output}]


        # --- Return structured JSON response ---
        return jsonify({"roadmap": roadmap}), 200

    except Exception as e:
        print("Error:", e)
        return jsonify({"error": f"Server error: {str(e)}"}), 500
