from flask import Flask
from app.extensions import db, migrate
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    # Register job blueprint with prefix
    from app.routes.job_routes import job_bp
    app.register_blueprint(job_bp, url_prefix="/api/jobs")
        
    from app.routes.auth_routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix="/api/auth")


    CORS(app)  # <-- allow frontend requests

    return app
