import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://careermap_user:careermap_password@localhost/careermap')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SYSTEM_USER_ID = int(os.getenv("SYSTEM_USER_ID", 999))
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "super-secret-key")
    JWT_TOKEN_LOCATION = ["headers"]  # 👈 Fixes your KeyError
    JWT_HEADER_NAME = "Authorization"
    JWT_HEADER_TYPE = "Bearer"
    
    # sudo -u postgres psql -d careermap 
