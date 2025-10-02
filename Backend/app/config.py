import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://careermap_user:careermap_password@localhost/careermap')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'supersecretkey')
    SYSTEM_USER_ID = int(os.getenv("SYSTEM_USER_ID", 999))
    
    # sudo -u postgres psql -d careermap 
