import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:admin1234@localhost:5432/cars_management"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key")
    JWT_SECRET_KEY = "super-secret-key-that-is-at-least-32-characters"