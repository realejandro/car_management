from flask import Blueprint, request, jsonify
from app.models.user import User
from flask_jwt_extended import create_access_token
from app import bcrypt
from app import db

auth_bp = Blueprint("login", __name__)


@auth_bp.route("login", methods = ['POST'])
def login():
    data = request.get_json()
    # we are using the flask-sqlAlchemy documentation
    # 1️⃣ Select the user by email
    stmt = db.select(User).filter_by(email=data.get("email"))
    result = db.session.execute(stmt)
    user = result.scalar_one_or_none()  # Returns User or None

    # 2️⃣ Check if user exists and password matches
    if not user or not bcrypt.check_password_hash(user.password, data.get("password")):
        return jsonify({"error": "Invalid email or password"}), 401

    # 3️⃣ Create JWT token
    access_token = create_access_token(identity=str(user.id))

    # 4️⃣ Return token and user info
    return jsonify({
        "access_token": access_token,
        "user": {
            "id": user.id,
            "email": user.email
        }
    })
    