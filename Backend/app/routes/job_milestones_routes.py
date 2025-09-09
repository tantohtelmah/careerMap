from flask import Blueprint, request, jsonify


job_milestones_bp = Blueprint('job_milestones_bp', __name__)

from app.extensions import db
from app.models.jobs import Job
from app.models.milestone import Milestone
from app.models.job_milestones import job_milestones

# Link job to milestone
@job_milestones_bp.route('/link', methods=['POST'])
def link_job_milestone():
    data = request.json  # {"job_id": 1, "milestone_id": 2}
    job = Job.query.get_or_404(data['job_id'])
    milestone = Milestone.query.get_or_404(data['milestone_id'])
    job.milestones.append(milestone)
    db.session.commit()
    return jsonify({'message': f'Milestone {milestone.title} linked to job {job.title}'})

# Unlink job from milestone
@job_milestones_bp.route('/unlink', methods=['POST'])
def unlink_job_milestone():
    data = request.json
    job = Job.query.get_or_404(data['job_id'])
    milestone = Milestone.query.get_or_404(data['milestone_id'])
    if milestone in job.milestones:
        job.milestones.remove(milestone)
        db.session.commit()
    return jsonify({'message': f'Milestone {milestone.title} unlinked from job {job.title}'})
