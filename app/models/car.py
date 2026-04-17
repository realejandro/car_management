from app import db
from app.models.user import User

class Car(db.Model):
    __tablename__ = "cars"

    id = db.Column(db.Integer, primary_key=True)
    brand = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    mileage = db.Column(db.Integer, nullable=False)
    vin = db.Column(db.String(17), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    status = db.Column(db.String(20), default="available")


    def to_dict(self):
        return {
            "id": self.id,
            "brand": self.brand,
            "model": self.model,
            "year": self.year,
            "price": float(self.price),
            "status": self.status,
            "mileage": self.mileage,
            "vin": self.vin, 
            "user_id": self.user_id
        }