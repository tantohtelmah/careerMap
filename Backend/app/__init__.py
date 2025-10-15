from flask import Flask, request, jsonify
from app.extensions import db, migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

# --- AWS Connection Check ---
aws_bucket = os.getenv("AWS_S3_BUCKET")
aws_region = os.getenv("AWS_REGION")
aws_key = os.getenv("AWS_ACCESS_KEY_ID")

if aws_bucket and aws_region and aws_key:
    print(f"✅ AWS connected — Bucket: {aws_bucket}  |  Region: {aws_region}")
else:
    print("⚠️ AWS credentials missing. Check your .env file or environment variables.")
# --- End AWS Check ---

jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")
    jwt.init_app(app)
    
    db.init_app(app)
    migrate.init_app(app, db)

    # ✅ Apply CORS globally (must be before blueprints)
    CORS(
        app,
        resources={r"/*": {"origins": ["http://localhost:3000", "http://127.0.0.1:3000"]}},
        supports_credentials=True,
        expose_headers="Authorization",
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    )

    # ✅ Always respond 200 OK to any preflight OPTIONS request
    @app.before_request
    def auto_cors_preflight():
        if request.method == "OPTIONS":
            resp = jsonify({"status": "ok"})
            resp.status_code = 200
            return resp

    # ✅ Register blueprints *after* CORS setup
    from app.routes.job_routes import job_bp
    app.register_blueprint(job_bp, url_prefix="/api/jobs")

    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")

    from app.routes.roadmap import roadmap_bp
    app.register_blueprint(roadmap_bp, url_prefix="/api")

    from app.routes.profile_routes import profile_bp
    app.register_blueprint(profile_bp, url_prefix="/api/profile")
    
    from app.routes.certifications import certifications_bp
    app.register_blueprint(certifications_bp, url_prefix="/api/certifications")

    return app  # ✅ must return app!
