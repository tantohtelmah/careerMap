from flask import Flask
from app.routes.job_routes import job_bp
from app.routes.user_routes import user_bp
from app.routes.notification_routes import notification_bp
from app.routes.career_goal_routes import career_goal_bp
from app.routes.auth_routes import auth_bp

def register_blueprints(app: Flask):
    app.register_blueprint(job_bp, url_prefix='/api/jobs')
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(notification_bp, url_prefix='/api/notifications')
    app.register_blueprint(career_goal_bp, url_prefix='/api/career_goals')
    app.register_blueprint(auth_bp, url_prefix='/api/auth')
