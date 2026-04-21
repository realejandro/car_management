from app import create_app, db
from app.models.car import Car
from app.models.user import User
from app.models.sale import Sale


app = create_app()

with app.app_context():
    db.drop_all()
    db.create_all()
    print("Database tables created successfully!")