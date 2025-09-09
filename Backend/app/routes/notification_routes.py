from flask import Blueprint, request, jsonify

notification_bp = Blueprint('notification_bp', __name__)

from app.extensions import db
from app.models.notification import Notification

# Create
@notification_bp.route('/', methods=['POST'])
def create_notification():
    data = request.json
    notif = Notification(**data)
    db.session.add(notif)
    db.session.commit()
    return jsonify({'message': 'Notification created', 'data': data}), 201

# Read
@notification_bp.route('/<int:user_id>', methods=['GET'])
def get_notifications(user_id):
    notifs = Notification.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'notification_id': n.notification_id,
        'message': n.message,
        'read': n.read,
        'created_at': n.created_at
    } for n in notifs])

# Update (mark read)
@notification_bp.route('/<int:notification_id>', methods=['PUT'])
def update_notification(notification_id):
    notif = Notification.query.get_or_404(notification_id)
    data = request.json
    notif.read = data.get('read', notif.read)
    db.session.commit()
    return jsonify({'message': 'Notification updated'})

# Delete
@notification_bp.route('/<int:notification_id>', methods=['DELETE'])
def delete_notification(notification_id):
    notif = Notification.query.get_or_404(notification_id)
    db.session.delete(notif)
    db.session.commit()
    return jsonify({'message': 'Notification deleted'})
