from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.sale import Sale
from models.car import Car
from app import db

sales_bp = Blueprint("sales", __name__)

@sales_bp.route("/create", methods=["POST"])
@jwt_required()
def create_sale():
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        user_id = get_jwt_identity()
        car_id = data["car_id"]
        sold_price = data["sold_price"]

        car = Car.query.get(car_id)

        if not car:
            return jsonify({"error": "Car not found"}), 404

        if car.status == "sold":
            return jsonify({"error": "Car already sold"}), 400

        
        # 🔥 Business logic
        commission = sold_price * 0.05  # 5%

        new_sale = Sale(
            buyer_name=data["buyer_name"],
            sold_price=sold_price,
            commission=commission,
            user_id=user_id,
            car_id=car_id,
            
        )

        # update car status
        car.status = "sold"

        db.session.add(new_sale)
        db.session.commit()

        return jsonify({
            "message": "Sale created successfully",
            "sale": {
                "id": new_sale.id,
                "buyer_name": new_sale.buyer_name,
                "sold_price": float(new_sale.sold_price),
                "commission": float(new_sale.commission),
                "car_id": new_sale.car_id,
                "user_id": new_sale.user_id
            }
        }), 201

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400

    except Exception as e:
        return jsonify({"error": str(e)}), 500