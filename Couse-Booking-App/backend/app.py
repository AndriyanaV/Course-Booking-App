import os
from pathlib import Path
from blueprints.current_courses.routes import current_courses_bp
from blueprints.auth.routes import auth_bp
from blueprints.users.routes import users_bp
from blueprints.admin.routes import admin_bp
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask import Flask, abort, jsonify, request, send_file, send_from_directory
from config import Config
import mysql.connector
from datetime import datetime
import pymysql
from datetime import timedelta
from flask import Blueprint
from werkzeug.utils import safe_join

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = 'e2b6fc2a9bfb5d70d4d5c7ad67e2a6f5016a82c49e9bc0af3a1c7e879bb10f6a'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=3)
jwt = JWTManager(app)

app.config.from_object(Config)

app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(current_courses_bp, url_prefix='/current-courses')
app.register_blueprint(auth_bp, url_prefix='/')

@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({"message": "You need to log in first!"}), 401


@app.route("/uploads/<folder_name>/<file_name>")
def return_file(folder_name, file_name):

    print(f"Request for file: {folder_name}/{file_name}")

    # Pronađi odgovarajući folder na osnovu folder_name
    if folder_name == "course":
        folder = Path(app.config["UPLOAD_FOLDER_COURSE"]).resolve()
        default_file = "default_course.png"
    elif folder_name == "user":
        folder = Path(app.config["UPLOAD_FOLDER_USER"]).resolve()
        default_file = app.config["DEFAULT_USER_IMAGE"]
    else:
        abort(400, description="Invalid folder")

    # Logovanje foldera i default fajla
    print(f"Folder resolved to: {folder}")
    print(f"Default file: {default_file}")

    # Proveri koji je pun put do fajla
    file_path = folder / file_name
    print(f"Looking for file at path: {file_path}")

    # Ako fajl postoji → vrati ga
    if file_path.exists():
        print(f"File found: {file_path}")
        return send_from_directory(folder, file_name)

    # Ako ne postoji → vrati default
    default_file_path = folder / default_file
    print(f"Looking for default file at: {default_file_path}")
    
    if default_file_path.exists():
        print(f"Default file found: {default_file_path}")
        return send_from_directory(folder, default_file)

    # Ako nema ni fajla ni default fajla → 404
    print(f"Neither file nor default file found.")
    abort(404, description="File not found")

# @app.route("/uploads/user/<file_name>", methods=['GET'])
# def return_user_img(file_name):
#     try:
#         return send_from_directory('uploads/user', file_name)
#     except FileNotFoundError:
#         return ('error')


if __name__ == "__main__":
    app.run(debug=True)
