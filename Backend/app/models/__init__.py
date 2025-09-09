# app/models/__init__.py
from app.models.jobs import Job
from app.models.user import User
from app.models.job_history import JobHistory
from app.models.notification import Notification
from app.models.tag import Tag, job_tags
from app.models.career_goal import CareerGoal
from app.models.milestone import Milestone
from app.models.milestone_progress import MilestoneProgress
from app.models.job_milestones import job_milestones
# from .user import User  # add other models later
