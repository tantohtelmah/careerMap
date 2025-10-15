from flask import Blueprint, request, jsonify
from app.models.notification import Notification
from app.extensions import db

notification_bp = Blueprint("notification_bp", __name__)

# Get notifications for a user
@notification_bp.route("/notifications/<int:user_id>", methods=["GET"])
def get_notifications(user_id):
    notifications = Notification.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "id": n.id,
        "type": n.type,
        "message": n.message,
        "read_status": n.read_status,
        "created_at": n.created_at
    } for n in notifications])

# Create a notification
@notification_bp.route("/notifications", methods=["POST"])
def create_notification():
    data = request.get_json()
    notification = Notification(
        user_id=data.get("user_id"),
        type=data.get("type"),
        message=data.get("message"),
        read_status=data.get("read_status", False)
    )
    db.session.add(notification)
    db.session.commit()
    return jsonify({"id": notification.id, "message": notification.message}), 201

# Mark notification as read
@notification_bp.route("/notifications/<int:notification_id>/read", methods=["PUT"])
def mark_as_read(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    notification.read_status = True
    db.session.commit()
    return jsonify({"message": "Notification marked as read"})
