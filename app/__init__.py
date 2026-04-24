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
    from .routes.sale_routes import sales_bp
    from .auth.auth_routes import auth_bp
    
    app.register_blueprint(car_bp, url_prefix="/cars")
    app.register_blueprint(user_bp, url_prefix = "/users")
    app.register_blueprint(auth_bp, url_prefix = "/auth")
    app.register_blueprint(sales_bp, url_prefix = "/sales")
    

    return app

