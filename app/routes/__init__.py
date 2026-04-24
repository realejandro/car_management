from .car_routes import car_bp
from .sale_routes import sales_bp
from .user_routes import user_bp


def register_routes(app):
    app.register_blueprint(car_bp, url_prefix="/cars")
    app.register_blueprint(user_bp, url_prefix="/users")
    app.register_blueprint(sales_bp, url_prefix="/sales")
    