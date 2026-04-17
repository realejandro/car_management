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
   
    from .routes.car_routes import car_bp
    from .routes.user_routes import user_bp
    from .routes.login_route import login_bp
    app.register_blueprint(car_bp, url_prefix="/cars")
    app.register_blueprint(user_bp, url_prefix = "/users")
    app.register_blueprint(login_bp, url_prefix = "/login")

    return app

