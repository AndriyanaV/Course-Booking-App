from flask import Blueprint, jsonify, request
from database import get_db_connection
from flask_jwt_extended import jwt_required, get_jwt_identity
from decoraotrs import role_required
from werkzeug.security import generate_password_hash
import os
import uuid

UPLOAD_FOLDER = 'uploads/course'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'svg'}


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
        SET user_id=%s, price = %s,  start_at = %s, end_at = %s, level = %s, location = %s,max_members=%s, lessons=%s
        WHERE id = %s
        """
        values = (
            data['professor'], data['price'], data['start_at'], data['end_at'],
            data['level'], data['location'], data['max_members'], data['lessons'],
            id
        )

        cursor.execute(query, values)
        con.commit()
        return jsonify({"message": "Current course updated successfully."}), 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "Error"}), 500


img_base_url_user = 'http://127.0.0.1:5000/uploads/user/'
UPLOAD_FOLDER_USER = 'uploads/user'


@admin_bp.route("/update-user/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin", "user"])
def update_user_info(id):
    try:
        query = "SELECT  * FROM user WHERE id=%s"
        cursor.execute(query, (id,))
        user = cursor.fetchone()

        file = request.files.get('file')

        if file:
            file_url = str(img_base_url_user+file.filename)
            file.save(os.path.join(UPLOAD_FOLDER_USER, file.filename))

        else:
            file_url = user['user_image_url']

        data = request.form.to_dict()

        firstName = data.get('first_name', user['first_name'])
        lastName = data.get('last_name', user['last_name'])
        phoneNumber = data.get('phone_number', user['phone_number'])
        email = data.get('email', user['email'])
        biography = data.get('biography', user['biography'])
        rola = data.get('rola', user['rola'])
        password = data.get('password')

        if password:
            hashed_password = generate_password_hash(password)
        else:
            hashed_password = user['password_hash']

        query = """
        UPDATE user
        SET first_name = %s, last_name = %s, email = %s, phone_number = %s, biography = %s, user_image_url = %s, password_hash=%s, rola=%s
        WHERE id = %s
        """

        values = (firstName, lastName, email, phoneNumber,
                  biography, file_url, hashed_password, rola, id)

        cursor.execute(query, values)
        con.commit()
        return jsonify({"message": "User info updated successfully."}), 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Internal server error"}), 500


img_base_url_course = 'http://127.0.0.1:5000/uploads/course/'
UPLOAD_FOLDER_COURSE = 'uploads/course'


@admin_bp.route("/update-course/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin"])
def update_course(id):
    try:

        query = "SELECT  * FROM course WHERE id=%s"
        cursor.execute(query, (id,))
        course = cursor.fetchone()

        file = request.files.get('file')

        if file:
            file_url = str(img_base_url_course+file.filename)
            file.save(os.path.join(UPLOAD_FOLDER_COURSE, file.filename))

        else:
            file_url = course['course_image_url']

        data = request.form.to_dict()
        name = data.get('name', course['name'])
        language = data.get('language', course['language'])

        query = """
        UPDATE course
        SET name = %s,course_image_url=%s,  language = %s
        WHERE id = %s
        """

        values = (
            name, file_url, language, id
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
        con, cursor = get_db_connection()
        query = """
        SELECT id,
            first_name,
            last_name,
            email,
            phone_number,
            user_image_url,
            rola
        FROM user;
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@admin_bp.route("/get-user/<int:id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_user(id):
    try:
        query = """
        SELECT id,
            first_name,
            last_name,
            email,
            phone_number,
            biography,
            user_image_url,
            rola
        FROM user WHERE id=%s;
        """
        cursor.execute(query, (id,))
        data = cursor.fetchone()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@admin_bp.route("/get-all-current-courses/<int:id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_all_current_courses(id):
    try:
        level = request.args.get('level', '%')
        if (level == ""):
            level = "%"

        # print("level je"+level)

        query = """
        SELECT course.id AS course_id,course.name,course.course_image_url,course.language,
            current_courses.*
        FROM course
        JOIN current_courses ON course.id = current_courses.course_id
        WHERE course.id=%s AND level LIKE %s;
        """
        values = (id, level)
        cursor.execute(query, values)
        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@admin_bp.route("/get-all-courses", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_all_courses():
    try:
        language = request.args.get('language', '%')

        if (language == ""):
            language = '%'

        print(language)

        query = """
        SELECT * FROM course WHERE language LIKE %s;
        """

        cursor.execute(query, (language,))
        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while fetching courses."}), 500


@admin_bp.route("/get-course/<int:id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_course(id):
    try:

        query = """
        SELECT * FROM course WHERE id=%s;
        """

        cursor.execute(query, (id,))
        data = cursor.fetchone()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while fetching courses."}), 500


@admin_bp.route("/get-professors", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_professors():
    try:

        query = """
        SELECT id,first_name,last_name FROM user WHERE rola LIKE %s;
        """
        rola = 'professor'

        cursor.execute(query, (rola,))
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
        con, cursor = get_db_connection()
        file = request.files.get('file')
        data = request.form.to_dict()

        password = generate_password_hash(data['password'])
        query = """
        INSERT INTO user (first_name, last_name, email, phone_number, biography, password_hash, rola, user_image_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['biography'],
                  password, data['rola'], None)

        cursor.execute(query, values)
        # con.commit()

        cursor.execute("SELECT LAST_INSERT_ID() ")
        last_id = cursor.fetchone()
        last_id = last_id.get('LAST_INSERT_ID()')
        print(last_id)

        # file = request.files['file']
        print(file)

        if file:
            name_without_extension, file_extension = os.path.splitext(
                file.filename)
            img_name = name_without_extension+str(last_id)+file_extension
            file.save(os.path.join(UPLOAD_FOLDER_USER, img_name))

        else:
            img_name = 'anonymous'+'.png'

        file_url = str(img_base_url_user+img_name)

        query = "UPDATE user SET user_image_url=%s WHERE id=%s"

        values = (file_url, last_id)

        cursor.execute(query, values)
        con.commit()

        return jsonify({"message": "You've added new user sucessfully!"}, 200)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "Error!"})


@admin_bp.route("/add-current-course", methods=["POST"])
@jwt_required()
@role_required(["admin"])
def add_current_course():
    try:
        # Dobijanje podataka iz zahteva
        data = request.json

        query = """
            INSERT INTO current_courses (course_id, user_id, price, start_at, end_at, max_members, level,location,lessons)
            VALUES (%s,  %s, %s, %s, %s, %s, %s,%s, %s)
            """
        values = (data['course_id'], data['user_id'], data['price'],  data['start_at'],
                  data['end_at'], data['max_members'], data['level'], data['location'], data['lessons'])

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
        file = request.files['file']
        file_url = str(img_base_url_course+file.filename)

        if file:
            file.save(os.path.join(UPLOAD_FOLDER_COURSE, file.filename))

        else:
            return jsonify({"message": "Image is required!"})

        data = request.form.to_dict()

        if 'name' not in data or 'language' not in data:
            return jsonify({"message": "Name and language fields are required!"})

        query = """
        INSERT INTO course (name, course_image_url,language)
        VALUES (%s, %s, %s)
        """
        values = (data['name'], file_url,
                  data['language'])

        cursor.execute(query, values)
        con.commit()
        return jsonify({"message": "You've added new course sucessfully!"})

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return ("Error")


@admin_bp.route("/delete-course/<int:id>", methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_course(id):
    try:
        print(id)

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
