import string
import random

from app import create_app, db, bcrypt
from app.models.user import User
from app.models.car import Car


def generate_vin():
    """
    Generates a fake VIN with 17 characters (uppercase letters + digits).
    """
    chars = string.ascii_uppercase + string.digits

    # VINs typically exclude I, O, Q to avoid confusion
    valid_chars = ''.join(c for c in chars if c not in "IOQ")

    return ''.join(random.choice(valid_chars) for _ in range(17))

app = create_app()

with app.app_context():

    print("🔄 Seeding database...")

    # 🔥 Clear existing data (optional)
    #db.session.query(Car).delete()
    #db.session.query(User).delete()

    # 👤 Users
    admin = User(
        name="Batman",
        username= "batmanW",
        email="admin@test.com",
        password=bcrypt.generate_password_hash("password1234").decode("utf-8"),
        role="admin"
    )

    user1 = User(
        name="John Doe",
        email="john@test.com",
        username="johnD",
        password=bcrypt.generate_password_hash("password1234").decode("utf-8"),
        role="buyer"
    )

    db.session.add_all([admin, user1])
    db.session.commit()

    # 🚗 Cars
    car1 = Car(
        brand="Toyota",
        model="Corolla",
        year=2020,
        price=18000,
        status="available",
        user_id=user1.id,
        mileage = '25000',
        vin = generate_vin()
    )

    car2 = Car(
        brand="Honda",
        model="Civic",
        year=2022,
        price=22000,
        user_id=admin.id, 
        status="available",
        mileage='30000',
        vin = generate_vin()
    )

    db.session.add_all([car1, car2])
    db.session.commit()

    print("✅ Seeding completed successfully!")