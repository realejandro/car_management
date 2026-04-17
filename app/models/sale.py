from app import db
import datetime as dt

class Sale(db.Model):

    __tablename__ = "sales"
    id = db.Column(db.Integer, primary_key= True)
    buyer_name = db.Column(db.String(100), nullable = False)
    sold_price = db.Column(db.Numeric(10, 2), nullable = False)
    commission = db.Column(db.Numeric(10, 2), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    car_id = db.Column(db.Integer, db.ForeignKey('cars.id'))

    created_at = db.Column(
    db.DateTime(timezone=True),
    default=lambda: dt.datetime.now(dt.timezone.utc)
    )

    updated_at = db.Column(
    db.DateTime,
    default=lambda: dt.datetime.now(dt.timezone.utc),
    onupdate=lambda: dt.datetime.now(dt.timezone.utc)
    )

    def to_dict(self):
        return {
            "id": self.id,
            "buyer_name": self.buyer_name,
            "sold_price" : float(self.sold_price),
            "commission": float(self.commission),
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None,
            "user_id": self.user_id,
            "car_id": self.car_id
        }
