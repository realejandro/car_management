from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt 
from .config import Config

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
   
    from .routes import register_routes
    from .auth.auth_routes import auth_bp

    register_routes(app)
    app.register_blueprint(auth_bp, url_prefix="/auth")
    

    return app
