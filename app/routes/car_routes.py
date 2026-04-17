from flask import Blueprint, request, jsonify
from app import db
from app.models.car import Car
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt_identity

car_bp = Blueprint("cars", __name__)  

# A Blueprint in Flask is basically a way to organize your routes, views, and related 
# code into reusable modules instead of putting everything in one big file
@car_bp.route("", methods=['GET'])
def all_cars():
    cars = Car.query.all()
    if len(cars) == 0:
        return jsonify({
            "message": "There are no cars"
        }), 404

    return jsonify([ 
    {
        **car.to_dict(),
        "user": User.query.get(car.user_id).to_public_dict()
    }  for car in cars ])


@car_bp.route("/create", methods = ['POST'])
@jwt_required()
def create_car():
    data = request.get_json()
    user_id = get_jwt_identity()

    #Basic Validation
    if not data:
        return jsonify( { "error ": "No input data provided" }), 400
    
    try: 
        new_car = Car(
            brand= data["brand"],
            model = data["model"],
            year = data["year"],
            price = data["price"],
            user_id = user_id,
            vin = data["vin"],
            mileage = data["mileage"]
        )

        db.session.add(new_car)
        db.session.commit()
    
        return jsonify({
            "message": "Car created successfully",
            "car": {
                "id": new_car.id,
                "brand": new_car.brand,
                "model": new_car.model,
                "year": new_car.year,
                "price": new_car.price
                
            }
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@car_bp.route("/delete/<int:car_id>", methods=["DELETE"])
@jwt_required()
def delete_car(car_id):
    car = Car.query.get(car_id)
    user_id = get_jwt_identity()
    user = db.session.get(User, int(user_id))
    if not car:
        return jsonify({"error": "Car not found"}), 404
    
    if car.user_id != user.id:
        return jsonify({"error": "User not Authorized"}), 403

    try:
        db.session.delete(car)
        db.session.commit()
        return jsonify({"message": f"Car {id} deleted"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    
@car_bp.route("/update/<int:car_id>", methods=["PATCH"])
@jwt_required()
def update_car(car_id):
    data = request.get_json()
    user_id = int(get_jwt_identity())
    
    if not data:
        return jsonify({
            "error": "Not input Data provided"
        })
    
    car = db.session.get(Car, car_id)

    if not car:
        return jsonify({
            "error": "Car not found"
        }), 404
    
    if user_id != car.user_id:
        return jsonify({
            "error": "User not authorized"
        }), 403

    # 🔥 Update fields dynamically
    allowed_fields = ["brand", "model", "price", "mileage", "status"]

    for field in allowed_fields:
        if field in data:
            setattr(car, field, data[field])

    # Optional validation
    if "status" in data and data["status"] not in ["available", "sold"]:
        return jsonify({"error": "Invalid status"}), 400

    db.session.commit()

    return jsonify({
        "message": "Car updated successfully",
        "car": car.to_dict()
    }), 200
    