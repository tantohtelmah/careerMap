from flask import Blueprint, request, jsonify

job_tags_bp = Blueprint('job_tags_bp', __name__)

from app.extensions import db
from app.models.jobs import Job
from app.models.tag import Tag, job_tags

# Assign tag to job
@job_tags_bp.route('/assign', methods=['POST'])
def assign_tag_to_job():
    data = request.json  # Expect {"job_id": 1, "tag_id": 2}
    job = Job.query.get_or_404(data['job_id'])
    tag = Tag.query.get_or_404(data['tag_id'])
    job.tags.append(tag)
    db.session.commit()
    return jsonify({'message': f'Tag {tag.name} assigned to job {job.title}'})

# Remove tag from job
@job_tags_bp.route('/remove', methods=['POST'])
def remove_tag_from_job():
    data = request.json
    job = Job.query.get_or_404(data['job_id'])
    tag = Tag.query.get_or_404(data['tag_id'])
    if tag in job.tags:
        job.tags.remove(tag)
        db.session.commit()
    return jsonify({'message': f'Tag {tag.name} removed from job {job.title}'})
