from flask import Blueprint, current_app, jsonify, request
from marshmallow import ValidationError
from utils.get_file_url import get_file_url
from database import get_db_connection
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from decoraotrs import role_required
from utils import check_course_availability
from werkzeug.security import generate_password_hash
from datetime import datetime
import pymysql
from schemas.user.update_user_profile_schema import UpdateUserProfileSchema
from utils.file_utils import allowed_file, allowed_file_size
from utils.save_uploaded_file import save_uploaded_file
from utils.common import book_course
import os

users_bp = Blueprint('users', __name__)


@users_bp.route("/user-profile", methods=["GET"])
@jwt_required()
def show_user_profile():

    con, cursor = get_db_connection()

    default_user_image = current_app.config["DEFAULT_USER_IMAGE"]

    claims = get_jwt()
    user_id = claims.get('user_id')

    try:
        query = """
        SELECT id, first_name, last_name,rola, email,phone_number,biography,user_image_url
        FROM user
        WHERE user.id=%s
        """
        cursor.execute(query, (user_id, ))
        data = cursor.fetchone()

        if not data:
            return jsonify({"error": f"User with id {user_id} not found."}), 404
        
        data["user_image_url"] = get_file_url(
            data.get("user_image_url"),
            folder_type="user",
            default=default_user_image)

        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@users_bp.route("/user-courses", methods=["GET"])
@jwt_required()
@role_required(["user"])
def show_user_courses():
    try:
        con, cursor = get_db_connection()

        claims = get_jwt()
        user_id = claims.get('user_id')

        cursor.execute("SELECT id FROM user WHERE id=%s", (user_id,))

        user = cursor.fetchone()

        if not user:
            return jsonify({"message": "User not found"}), 404

        query = """
            SELECT
                course.name,
                course.course_image_url,
                course.id AS course_id,
                current_courses.id,
                current_courses.start_at,
                current_courses.end_at,
                current_courses.price,
                current_courses.level
            FROM course
            JOIN current_courses ON course.id = current_courses.course_id
            JOIN user_course ON user_course.course_id = current_courses.id
            JOIN user ON user.id = user_course.user_id
            WHERE user.id = %s;
        """
        cursor.execute(query, (user_id,))

        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "Error"})
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@users_bp.route("/book-course/<int:id>", methods=["POST"])
@jwt_required()
@role_required(["user"])
def check_course(id):
    try:
        con, cursor = get_db_connection()

        claims = get_jwt()
        user_id = claims.get('user_id')

        cursor.execute("SELECT id FROM user WHERE id=%s", (user_id,))

        user = cursor.fetchone()

        if not user:
            return jsonify({"message": "User not found"}), 404

        course_id = id

        query = """
            SELECT
                current_courses.id,current_courses.start_at,
                current_courses.max_members
            FROM current_courses
            WHERE id=%s
        """
        cursor.execute(query, (course_id, ))
        course = cursor.fetchone()

        if not course:
            return jsonify({"message": "Course not found!"}), 404
        
        aviable = check_course_availability(course)

        if (aviable):
            return book_course(course_id)
        else:
            return jsonify({"message": "All seats are reserved!"})
        
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An unexpected error occurred, please try again later."}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@users_bp.route("/professor-courses", methods=["GET"])
@jwt_required()
@role_required(["professor"])
def show_professor_courses():
    try:
        con, cursor = get_db_connection()

        claims = get_jwt()
        user_id = claims.get('user_id')

        cursor.execute("SELECT id FROM user WHERE id=%s", (user_id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"message": "User not found"}), 404

        query = """
        SELECT course.name,
            course.course_image_url,
            current_courses.id,
            current_courses.price,
            current_courses.start_at,
            current_courses.end_at,
            current_courses.level
        FROM course
        JOIN current_courses ON course.id = current_courses.course_id
        JOIN user ON user.id = current_courses.user_id
        WHERE user.id = %s;
        """

        cursor.execute(query, (user_id,))

        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


#Update user profile route 
@users_bp.route("/update-user/<int:id>", methods=['PUT'])
@jwt_required()
def update_user_info(id):
    try:
        con, cursor = get_db_connection()

        upload_folder_user = current_app.config["UPLOAD_FOLDER_USER"]
        allowed_extensions = current_app.config["ALLOWED_IMAGE_EXTENSIONS"]
        default_user_image = current_app.config["DEFAULT_USER_IMAGE"]

        file = request.files.get('file')
        data = request.form.to_dict()

        remove_image = request.form.get("remove_image")

        query = "SELECT  * FROM user WHERE id=%s"
        cursor.execute(query, (id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": f"User with id {id} not found."}), 404

        schema = UpdateUserProfileSchema()
        schema.context = {"current_user": user}

         # Validation - text fields
        try:
            validated_data = schema.load(
            data,
            unknown="exclude"  
            )
        except ValidationError as err:
            print("Validation errors:", err.messages)
            return jsonify({"errors": err.messages}), 400

        filename = user['user_image_url']

        if file:
            old_filename =  user['user_image_url']
            # Check extension
            if not allowed_file(file.filename):
                allowed_extensions = current_app.config.get("ALLOWED_IMAGE_EXTENSIONS", set())
                return jsonify({
                "message": f"Invalid image format. Allowed: {', '.join(allowed_extensions)}"
                }), 400

            # Check file size (max 2MB)
            if not allowed_file_size(file, max_size_mb=5):
                return jsonify({"message": "File is too large. Max size is 2MB."}), 400

            # Save new image
            filename = save_uploaded_file(file,upload_folder_user)

            # Remove old image
            if old_filename and old_filename != default_user_image:
                old_path = os.path.join(upload_folder_user, old_filename)
                if os.path.exists(old_path):
                    os.remove(old_path)
        else:
            if remove_image == "true":
                filename = default_user_image
            else:
                filename = user['user_image_url']
        

        firstName = validated_data.get('first_name', user['first_name'])
        lastName = validated_data.get('last_name', user['last_name'])
        phoneNumber = validated_data.get('phone_number', user['phone_number'])
        biography = validated_data.get('biography', user['biography'])
        rola = user['rola']  
        email = user['email']  
        hashed_password = user['password_hash']  

        query = """
        UPDATE user
        SET first_name = %s, last_name = %s, email = %s, phone_number = %s, biography = %s, user_image_url = %s, password_hash=%s, rola=%s
        WHERE id = %s
        """

        values = (firstName, lastName, email, phoneNumber,
                  biography, filename, hashed_password, rola, id)

        cursor.execute(query, values)
        con.commit()
        return jsonify({"message": "User info updated successfully."}), 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

