from flask import Blueprint, jsonify, request
from database import get_db_connection
from flask_jwt_extended import jwt_required, get_jwt_identity
from decoraotrs import role_required
from werkzeug.security import generate_password_hash
import os
import uuid

UPLOAD_FOLDER = 'uploads/course'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}


def generate_unique_filename(filename):
    # Generiši jedinstveni ID
    unique_id = str(uuid.uuid4())
    # Ekstraktuj ekstenziju fajla
    extension = os.path.splitext(filename)[1]
    # Kreiraj jedinstveno ime fajla
    unique_filename = f"{unique_id}{extension}"
    return unique_filename


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


admin_bp = Blueprint('admin', __name__)

con, cursor = get_db_connection()

# UPDATE


@admin_bp.route("/update-current-course/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin"])
def update_current_course(id):
    try:
        data = request.json

        query = """
        UPDATE current_courses
        SET price = %s, duration = %s, start_at = %s, end_at = %s, level = %s, location = %s
        WHERE id = %s
        """
        values = (
            data['price'], data['duration'], data['start_at'], data['end_at'],
            data['level'], data['location'],
            id
        )

        cursor.execute(query, values)
        con.commit()
        return jsonify({"message": "Current course updated successfully."}), 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # finally:
    #     cursor.close()  # Zatvori kursor
    #     con.close()  # Zatvori konekciju


@admin_bp.route("/update-user-info/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin"])
def update_user_info(id):
    try:
        data = request.json

        query = """
        UPDATE user
        SET first_name = %s, last_name = %s, email = %s, phone_number = %s, biography = %s, user_image_url = %s, password_hash=%s, rola=%s
        WHERE id = %s
        """
        password = generate_password_hash(data['password'])
        values = (
            data['first_name'], data['last_name'], data['email'], data['phone_number'],
            data['biography'], None, password, data['rola'],
            id
        )

        cursor.execute(query, values)
        con.commit()
        return jsonify({"message": "User info updated successfully."}), 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500


img_base_url = 'http://127.0.0.1:5000/uploads/course/'
UPLOAD_FOLDER = 'uploads/course'


@admin_bp.route("/update-course/<int:id>", methods=['PUT'])
# @jwt_required()
# @role_required(["admin"])
def update_course(id):
    try:

        file = request.files['file']
        file_url = str(img_base_url+file.filename)
        print(file.filename)

        if file:
            file.save(os.path.join(UPLOAD_FOLDER, file.filename))

        data = request.form.to_dict()

        query = """
        UPDATE course
        SET name = %s,course_image_url=%s,  language = %s
        WHERE id = %s
        """

        values = (
            data['name'], file_url, data['language'], id
        )

        cursor.execute(query, values)

        con.commit()

        return jsonify({"message": "Course details updated successfully."}), 200

    except Exception as e:

        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while updating the course."}), 500


# READ

@admin_bp.route("/get-users", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_all_users():
    try:
        query = """
        SELECT id,
            first_name,
            last_name,
            email,
            rola
        FROM user;
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@admin_bp.route("/get-all-current-courses/<int:id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_all_current_courses(id):
    try:
        query = """
        SELECT course.*,
            current_courses.*
        FROM course
        JOIN current_courses ON course.id = current_courses.course_id
        WHERE course.id=%s;
        """
        cursor.execute(query, (id, ))
        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@admin_bp.route("/get-courses", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_all_courses():
    try:
        query = """
        SELECT * FROM course
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while fetching courses."}), 500


# CREATE


@admin_bp.route("/add-user", methods=["POST"])
@jwt_required()
@role_required(["admin"])
def add_user():
    try:
        data = request.json

        # file = data['file']
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #     file.save(file_path)
        #     file_url = f'/uploads/{filename}'

        password = generate_password_hash(data['password'])
        query = """
        INSERT INTO user (first_name, last_name, email, phone_number, biography, user_image_url, password_hash, rola)
        VALUES (%s, %s, %s, %s, %s,  %s, %s, %s)
        """
        values = (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['biography'], 'null',
                  password, data['rola'])

        cursor.execute(query, values)
        con.commit()
        return jsonify({"message": "You've added new user sucessfully!"})

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@admin_bp.route("/add-current-course", methods=["POST"])
@jwt_required()
@role_required(["admin"])
def add_current_course():
    try:
        # Dobijanje podataka iz zahteva
        data = request.json

        query = """
            INSERT INTO current_courses (course_id, user_id, price, duration, start_at, end_at, max_members, level,location)
            VALUES (%s,  %s, %s, %s, %s, %s, %s,%s,%s)
            """
        values = (data['course_id'], data['user_id'], data['price'], data['duration'], data['start_at'],
                  data['end_at'], data['max_members'], data['level'], data['location'])

        cursor.execute(query, values)
        con.commit()

        return jsonify({"message": "Course has been successfully added to current courses."}), 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@admin_bp.route("/add-course", methods=["POST"])
@jwt_required()
@role_required(["admin"])
def add_course():
    try:
        data = request.json

        # file = data['file']
        # if file and allowed_file(file.filename):
        #     filename = secure_filename(file.filename)
        #     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        #     file.save(file_path)
        #     file_url = f'/uploads/{filename}'

        query = """
        INSERT INTO course (name, course_image_url,language)
        VALUES (%s, %s, %s, %s)
        """
        values = (data['name'], "null",
                  data['language'])

        cursor.execute(query, values)
        con.commit()
        return jsonify({"message": "You've added new course sucessfully!"})

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@admin_bp.route("/delete-course/<int:id>", methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_course():
    try:

        data = request.json

        query = """
        DELETE FROM course WHERE id = %s;
        """

        cursor.execute(query, (id, ))

        con.commit()

        return jsonify({"message": "Course deleted sucessfully."}), 200

    except Exception as e:

        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while deleting the course."}), 500


@admin_bp.route("/delete-current-course/<int:id>", methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_current_course(id):
    try:

        query = """
        DELETE FROM current_courses WHERE id = %s;
        """

        # values = (
        #     data['id']
        # )

        cursor.execute(query, (id,))

        con.commit()

        return jsonify({"message": "Course deleted sucessfully."}), 200

    except Exception as e:

        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while deleting the course."}), 500


@admin_bp.route("/delete-user/<int:id>", methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_user(id):
    try:

        query = """
        DELETE FROM user WHERE id = %s;
        """

        cursor.execute(query, (id, ))

        con.commit()

        return jsonify({"message": "User deleted sucessfully."}), 200

    except Exception as e:

        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while deleting the user."}), 500
