from flask import Blueprint, request, jsonify
from app import db, bcrypt
from app.models.user import User
from app.models.car import Car


user_bp = Blueprint("users", __name__)

@user_bp.route("", methods= ['GET'])
def all_users():
    users = User.query.all()
    if len(users) == 0:
        return jsonify({
            "message": "There are no users"
        }), 404

    return jsonify([ user.to_dict() for user in users ])


@user_bp.route("/create", methods = ['POST'])
def create_user():
    data = request.get_json()

    hashed_pw = bcrypt.generate_password_hash(data["password"]).decode("utf-8")

    if not data:
        return jsonify( { "error ": "No input data provided" }), 400

    try:
        new_user = User(
            name = data["name"],
            email= data["email"],
            username = data["username"],
            password = hashed_pw,
        )

        db.session.add(new_user)
        db.session.commit()

        return jsonify({
            "message": "user created successfully",
            "user": {
                "id": new_user.id,
                "name": new_user.name,
                "username": new_user.username,
                "email": new_user.email,
                "password": new_user.password,
                "cars": [car.to_dict() for car in new_user.cars]
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
    