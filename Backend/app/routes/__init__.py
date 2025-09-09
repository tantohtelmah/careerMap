from flask import Flask
from app.routes.job_routes import job_bp
from app.routes.user_routes import user_bp
from app.routes.job_history_routes import job_history_bp
from app.routes.notification_routes import notification_bp
from app.routes.tag_routes import tag_bp
from app.routes.job_tags_routes import job_tags_bp
from app.routes.career_goal_routes import career_goal_bp
from app.routes.milestone_routes import milestone_bp
from app.routes.milestone_progress_routes import progress_bp
from app.routes.job_milestones_routes import job_milestones_bp

def register_blueprints(app: Flask):
    app.register_blueprint(job_bp, url_prefix='/api/jobs')
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(job_history_bp, url_prefix='/api/job_history')
    app.register_blueprint(notification_bp, url_prefix='/api/notifications')
    app.register_blueprint(tag_bp, url_prefix='/api/tags')
    app.register_blueprint(job_tags_bp, url_prefix='/api/job_tags')
    app.register_blueprint(career_goal_bp, url_prefix='/api/career_goals')
    app.register_blueprint(milestone_bp, url_prefix='/api/milestones')
    app.register_blueprint(progress_bp, url_prefix='/api/milestone_progress')
    app.register_blueprint(job_milestones_bp, url_prefix='/api/job_milestones')
