import pytest
import sys
import os

# Ensure project root (Backend/) is in sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import create_app
from app.extensions import db
from app.models.user import User

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"  # in-memory DB
    app.config["SECRET_KEY"] = "testsecret"

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.session.remove()
        db.drop_all()


def test_register_user(client):
    response = client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    })

    assert response.status_code == 201
    assert b"User registered successfully" in response.data


def test_register_existing_email(client):
    # First registration
    client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    })

    # Second registration (same email)
    response = client.post("/api/auth/register", json={
        "username": "anotheruser",
        "email": "test@example.com",
        "password": "password123"
    })

    assert response.status_code == 400
    assert b"Email already registered" in response.data


def test_login_success(client):
    # Register first
    client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    })

    # Then login
    response = client.post("/api/auth/login", json={
        "email": "test@example.com",
        "password": "password123"
    })

    assert response.status_code == 200
    data = response.get_json()
    assert "token" in data


def test_login_wrong_password(client):
    # Register first
    client.post("/api/auth/register", json={
        "username": "testuser",
        "email": "test@example.com",
        "password": "password123"
    })

    # Wrong password
    response = client.post("/api/auth/login", json={
        "email": "test@example.com",
        "password": "wrongpassword"
    })

    assert response.status_code == 401
    assert b"Invalid credentials" in response.data
