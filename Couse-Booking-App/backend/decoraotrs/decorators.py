from functools import wraps
from flask import jsonify
from flask_jwt_extended import get_jwt


def role_required(roles):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            claims = get_jwt()  # Dobijanje podataka iz JWT tokena
            if claims.get("role") not in roles:
                return jsonify({"message": "Nemate dozvolu za pristup ovoj ruti."}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper
