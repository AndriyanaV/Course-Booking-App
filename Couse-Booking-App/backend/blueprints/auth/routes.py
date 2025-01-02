
from flask import Blueprint, jsonify, request
from database import get_db_connection
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

auth_bp = Blueprint('auth', __name__)

con, cursor = get_db_connection()


def create_token(email, role, user_id):
    additional_claims = {
        "role": role,
        "user_id": user_id
    }

    return create_access_token(identity={"email": email}, additional_claims=additional_claims)


def role_required(roles):
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            current_user = get_jwt_identity()
            if current_user["role"] not in roles:
                return jsonify({"msg": "You do not have the required role"}), 403
            return fn(*args, **kwargs)
        return wrapper
    return decorator


@auth_bp.route("/register", methods=['POST'])
def register_user():
    try:
        data = request.json

        if not data or not data.get('email') or not data.get('password'):
            return jsonify({"message": "Email and password are required"}), 400

        email = data['email']
        password = data['password']
        rola = 'user'  # Dodeljujemo rolu korisniku, možeš kasnije menjati

        # Proveri da li korisnik već postoji
        query = "SELECT * FROM user WHERE email=%s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if user:
            return jsonify({"message": "User already exists"}), 400

        # Hesiraj lozinku i dodaj korisnika sa rolom
        hashed_password = generate_password_hash(password)
        insert_query = "INSERT INTO user (email, password_hash, rola) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (email, hashed_password, rola))
        con.commit()

        # Kreiraj JWT token
        access_token = create_token(email, rola)
        return jsonify(message="Registration successful.", access_token=access_token), 201

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred during registration"}), 500


@auth_bp.route("/login", methods=['POST'])
def login_user():
    try:
        data = request.json

        if not data or not data.get('email') or not data.get('password'):
            return jsonify({"message": "Email and password are required"}), 400

        email = data['email']
        password = data['password']

        # Proveri da li korisnik postoji
        query = "SELECT * FROM user WHERE email=%s"
        cursor.execute(query, (email,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"message": "Invalid email"}), 401

        # Proveri lozinku
        if not check_password_hash(user['password_hash'], password):
            return jsonify({"message": "Invalid password"}), 401

        # Dohvati rolu korisnika
        role = user['rola']
        user_id = user['id']

        # Kreiraj JWT token sa rolom
        token = create_token(email, role, user_id)
        return jsonify(message="Login successful.", access_token=token), 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred during login"}), 500
