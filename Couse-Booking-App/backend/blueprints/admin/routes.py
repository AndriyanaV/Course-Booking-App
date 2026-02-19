from flask import Blueprint, app, current_app, jsonify, request
from database import get_db_connection
from flask_jwt_extended import jwt_required, get_jwt_identity
from decoraotrs import role_required
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
import os
from marshmallow import ValidationError
import uuid
from schemas.course.add_course_schema import AddCourseSchema
from schemas.course.add_current_course_schema import AddCurrentCourseSchema
from schemas.user.add_user_schema import AddUserSchema
from utils.file_utils import allowed_file, allowed_file_size
from utils.save_uploaded_file import save_uploaded_file


admin_bp = Blueprint('admin', __name__)


# UPDATE
@admin_bp.route("/update-current-course/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin"])
def update_current_course(id):
    try:
        con, cursor = get_db_connection()

        data = request.json

        cursor.execute("SELECT * FROM current_courses WHERE id = %s", (id,))
        current_course = cursor.fetchone()

        professor = data.get('professor', current_course['user_id'])
        price = data.get('price', current_course['price'])
        start_at = data.get('start_at', current_course['start_at'])
        end_at = data.get('end_at', current_course['end_at'])
        level = data.get('level', current_course['level'])
        location = data.get('location', current_course['location'])
        max_members = data.get('max_members', current_course['max_members'])
        lessons = data.get('lessons', current_course['lessons'])

        query = """
        UPDATE current_courses
        SET user_id=%s, price = %s,  start_at = %s, end_at = %s, level = %s, location = %s,max_members=%s, lessons=%s
        WHERE id = %s
        """
        values = (
            professor, price, start_at, end_at, level, location, max_members, lessons, id
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
@role_required(["admin"])
def update_user_info(id):
    try:
        con, cursor = get_db_connection()

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


@admin_bp.route("/update-course/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin"])
def update_course(id):
    try:
        con, cursor = get_db_connection()

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
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@admin_bp.route("/get-user/<int:id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_user(id):
    try:
        con, cursor = get_db_connection()

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

        if not data:
            return jsonify({"message": "User not found"}), 404
        
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@admin_bp.route("/get-all-current-courses/<int:id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_all_current_courses(id):
    try:
        con, cursor = get_db_connection()
        print('RUtaa')

        # level = request.args.get('level', '%')
        # if (level == ""):
        #     level = "%"
        level = request.args.get('level') or '%'

        query = """
        SELECT course.id AS course_id,
        course.name,
        course.course_image_url,
        course.language,
        current_courses.*
        FROM course
        JOIN current_courses ON course.id = current_courses.course_id
        WHERE course.id = %s
        AND current_courses.level LIKE %s;
        """
        values = (id, level)
        cursor.execute(query, values)
        data = cursor.fetchall()
        print(data)
        return jsonify(data)
    

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@admin_bp.route("/get-all-courses", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_all_courses():
    try:
        con, cursor = get_db_connection()

        # language = request.args.get('language', "%")

        # if (language == ""):
        #     language = '%'
        language = request.args.get('language') or '%'

        query = """
        SELECT * FROM course WHERE language LIKE %s;
        """

        cursor.execute(query, (language,))
        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while fetching courses."}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@admin_bp.route("/get-course/<int:id>", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_course(id):
    try:
        con, cursor = get_db_connection()

        query = """
        SELECT * FROM course WHERE id=%s;
        """

        cursor.execute(query, (id,))
        data = cursor.fetchone()

        # if no course
        if not data:
            return jsonify({"message": "Course not found"}), 404
        
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while fetching courses."}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@admin_bp.route("/get-professors", methods=["GET"])
@jwt_required()
@role_required(["admin"])
def get_professors():
    try:
        con, cursor = get_db_connection()

        query = """
        SELECT id, first_name, last_name FROM user WHERE rola = %s;
        """
        rola = 'professor'

        cursor.execute(query, (rola,))
        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while fetching courses."}), 500
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


# CREATE
# User Schema for Validation
add_user_schema = AddUserSchema()

@admin_bp.route("/add-user", methods=["POST"])
@jwt_required()
@role_required(["admin"])
def add_user():
    try:

        con, cursor = get_db_connection()

        upload_folder_user = current_app.config["UPLOAD_FOLDER_USER"]
        img_base_url_user = current_app.config["USER_IMAGE_BASE_URL"]
        allowed_extensions = current_app.config["ALLOWED_IMAGE_EXTENSIONS"]

        file = request.files.get('file')
        data = request.form.to_dict()

        # Validating text fields with Marshmallow
        try:
            data = add_user_schema.load(request.form)
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        
        # Provera da li email postoji
        cursor.execute("SELECT id FROM user WHERE email = %s", (data["email"],))
        if cursor.fetchone():
            return jsonify({"message": "User with this email already exists!"}), 409

        password_hash = generate_password_hash(data['password'])

        # Image is required only for professors
        if data['rola'] == 'professor' and (not file or file.filename == ""):
            return jsonify({"message": "Image is required!"}), 400

        # Ako fajl postoji → sačuvaj ga
        if file and file.filename != "":
            # Check exte.
            if not allowed_file(file.filename):
                allowed_extensions = current_app.config.get("ALLOWED_IMAGE_EXTENSIONS", set())
                return jsonify({
                "message": f"Invalid image format. Allowed: {', '.join(allowed_extensions)}"
                }), 400

        # Provera veličine fajla (max 2MB)
            if not allowed_file_size(file, max_size_mb=2):
                return jsonify({"message": "File is too large. Max size is 2MB."}), 400
        
            file_url = save_uploaded_file(file, upload_folder_user,
                              img_base_url_user)

        # Ako nema fajla i nije professor → stavlja default
        else:
            filename = current_app.config["DEFAULT_USER_IMAGE"]
            file_url = f"{img_base_url_user.rstrip('/')}/{filename}"

        query = """
        INSERT INTO user 
        (first_name, last_name, email, phone_number, biography, password_hash, rola, user_image_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data['first_name'],
            data['last_name'],
            data['email'],
            data.get('phone_number'),
            data.get('biography'),
            password_hash,
            data['rola'],
            file_url
        )

        cursor.execute(query, values)
        con.commit()

        return jsonify({"message": "You've added new user!"}), 201

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "Error!"})
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

# Current Course Schema for Validation
current_course_schema = AddCurrentCourseSchema()

@admin_bp.route("/add-current-course", methods=["POST"])
@jwt_required()
@role_required(["admin"])
def add_current_course():
    try:
        con, cursor = get_db_connection()

        # Validating text fields with Marshmallow
        try:
            data = current_course_schema.load(request.json)
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        
        # Checking whether the course (language) for which we are adding a current course exists
        cursor.execute("SELECT id FROM course WHERE id = %s", (data['course_id'],))
        course = cursor.fetchone()
        if not course:
            return jsonify({"error": f"Course with id {data['course_id']} does not exist"}), 400
        
        # Checking if the professor exists
        cursor.execute(
            "SELECT id FROM user WHERE id = %s AND rola = %s",
            (data['user_id'], "professor")
        )
        if not cursor.fetchone():
            return jsonify({"error": f"User (professor) with id {data['user_id']} does not exist"}), 400

        #check if the course with the same term and professor has already been added 
        cursor.execute("""
            SELECT id FROM current_courses 
            WHERE course_id = %s 
            AND user_id = %s 
            AND NOT (%s > end_at OR %s < start_at)
            """, (data['course_id'], data['user_id'], data['start_at'], data['end_at']))

        if cursor.fetchone():
            return jsonify({"error": "This course is already scheduled for this professor in the given period."}), 400
        
        query = """
            INSERT INTO current_courses (course_id, user_id, price, start_at, end_at, max_members, level,location,lessons)
            VALUES (%s,  %s, %s, %s, %s, %s, %s,%s, %s)
            """
        values = (data['course_id'], data['user_id'], data['price'],  data['start_at'],
                  data['end_at'], data['max_members'], data['level'], data['location'], data['lessons'])

        cursor.execute(query, values)
        con.commit()

        return jsonify({"message": "Course has been successfully added to current courses."}), 201

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

# Course Schema for Validation
course_schema = AddCourseSchema()

@admin_bp.route("/add-course", methods=["POST"])
@jwt_required()
@role_required(["admin"])
def add_course():

    con = cursor = None

    try:
        con, cursor = get_db_connection()

        upload_folder_course = current_app.config["UPLOAD_FOLDER_COURSE"]
        img_base_url_course = current_app.config["COURSE_IMAGE_BASE_URL"]
        allowed_extensions = current_app.config["ALLOWED_IMAGE_EXTENSIONS"]

        file = request.files.get("file")
        data = request.form.to_dict()

        # Validating text fields with Marshmallow
        try:
            data = course_schema.load(request.form)
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        
        data["language"] = data["language"].strip().lower()
        data["name"] = data["name"].strip().lower()
        
        query_check = "SELECT id FROM course WHERE name = %s OR language = %s"
        cursor.execute(query_check, (data["name"], data["language"]))
        existing_course = cursor.fetchone()

        if existing_course:
            return jsonify({"message": "Course with this name or language already exists!"}), 400
        
        if not file or file.filename == "":
            return jsonify({"message": "Image is required!"}), 400

        # Provera ekstenzije
        if not allowed_file(file.filename):
            allowed_extensions = current_app.config.get("ALLOWED_IMAGE_EXTENSIONS", set())
            return jsonify({
            "message": f"Invalid image format. Allowed: {', '.join(allowed_extensions)}"
            }), 400

        # Provera veličine fajla (max 2MB)
        if not allowed_file_size(file, max_size_mb=2):
            return jsonify({"message": "File is too large. Max size is 2MB."}), 400

        # generisati UUID i sačuvati fajl
        original_filename = secure_filename(file.filename)
        ext = original_filename.rsplit(".", 1)[-1].lower()
        filename = f"{uuid.uuid4()}.{ext}"
        file_url = f"{img_base_url_course.rstrip('/')}/{filename}"
        file.save(os.path.join(upload_folder_course, filename))
        # file_url = save_uploaded_file(file, upload_folder_course,
        #                       img_base_url_course)

        query = """
            INSERT INTO course (name, course_image_url, language)
            VALUES (%s, %s, %s)
        """
        values = (data["name"], file_url, data["language"])

        cursor.execute(query, values)
        con.commit()

        return jsonify({"message": "You've added new course successfully!"}), 201

    except Exception as e:
        print(f"[add_course] {e}")
        if con:
            con.rollback()
        return jsonify({"message": "Internal server error"}), 500

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


# Instead of a real delete, it is better to use a soft delete
@admin_bp.route("/delete-course/<int:id>", methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_course(id):
    try:

        con, cursor = get_db_connection()

        query = """
        DELETE FROM course WHERE id = %s;
        """

        cursor.execute(query, (id,))
        con.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Course not found."}), 404

        return jsonify({"message": "Course deleted successfully."}), 200


    except Exception as e:

        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while deleting the course."}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@admin_bp.route("/delete-current-course/<int:id>", methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_current_course(id):
    try:
        con, cursor = get_db_connection()

        query = """
            DELETE FROM current_courses WHERE id = %s;
            """

        cursor.execute(query, (id,))
        con.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "Course not found."}), 404

        return jsonify({"message": "Course deleted successfully."}), 200


    except Exception as e:

        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while deleting the course."}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


@admin_bp.route("/delete-user/<int:id>", methods=['DELETE'])
@jwt_required()
@role_required(["admin"])
def delete_user(id):
    try:

        con, cursor = get_db_connection()

        query = """
        DELETE FROM user WHERE id = %s;
        """

        cursor.execute(query, (id, ))

        con.commit()

        if cursor.rowcount == 0:
            return jsonify({"message": "User not found."}), 404

        return jsonify({"message": "User deleted sucessfully."}), 200

    except Exception as e:

        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while deleting the user."}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()

#to do on delete delete images