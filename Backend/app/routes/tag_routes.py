from flask import Blueprint, request, jsonify

tag_bp = Blueprint('tag_bp', __name__)

from app.extensions import db
from app.models.tag import Tag

# Create
@tag_bp.route('/', methods=['POST'])
def create_tag():
    data = request.json
    tag = Tag(**data)
    db.session.add(tag)
    db.session.commit()
    return jsonify({'message': 'Tag created', 'data': data}), 201

# Read
@tag_bp.route('/', methods=['GET'])
def get_tags():
    tags = Tag.query.all()
    return jsonify([{'tag_id': t.tag_id, 'name': t.name} for t in tags])

# Update
@tag_bp.route('/<int:tag_id>', methods=['PUT'])
def update_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    data = request.json
    tag.name = data.get('name', tag.name)
    db.session.commit()
    return jsonify({'message': 'Tag updated'})

# Delete
@tag_bp.route('/<int:tag_id>', methods=['DELETE'])
def delete_tag(tag_id):
    tag = Tag.query.get_or_404(tag_id)
    db.session.delete(tag)
    db.session.commit()
    return jsonify({'message': 'Tag deleted'})
