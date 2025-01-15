
from blueprints.current_courses.routes import current_courses_bp
from blueprints.auth.routes import auth_bp
from blueprints.users.routes import users_bp
from blueprints.admin.routes import admin_bp
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask import Flask, jsonify, request, send_from_directory
import mysql.connector
from datetime import datetime
import pymysql
from datetime import timedelta
from flask import Blueprint

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = 'e2b6fc2a9bfb5d70d4d5c7ad67e2a6f5016a82c49e9bc0af3a1c7e879bb10f6a'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(days=1)
jwt = JWTManager(app)


app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(current_courses_bp, url_prefix='/current-courses')
app.register_blueprint(auth_bp, url_prefix='/')


@app.route("/uploads/course/<file_name>", methods=['GET'])
def return_file(file_name):
    try:
        return send_from_directory('uploads/course', file_name)
    except FileNotFoundError:
        return ('no')


if __name__ == "__main__":
    app.run(debug=True)
