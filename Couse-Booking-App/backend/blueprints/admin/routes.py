from shlex import quote
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
from schemas.course.update_course_schema import UpdateCourseSchema
from schemas.course.update_current_course import UpdateCurrentCourseSchema
from schemas.user.add_user_schema import AddUserSchema
from utils.file_utils import allowed_file, allowed_file_size
from utils.get_file_url import get_file_url
from utils.save_uploaded_file import save_uploaded_file


admin_bp = Blueprint('admin', __name__)


update_current_course_schema = UpdateCurrentCourseSchema()
# UPDATE
@admin_bp.route("/update-current-course/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin"])
def update_current_course(id):
    try:
        con, cursor = get_db_connection()

        # Uzmi JSON podatke
        data = request.json 

        # Uzmi trenutne vrednosti iz baze
        cursor.execute("SELECT * FROM current_courses WHERE id=%s", (id,))
        current_course = cursor.fetchone()
        if not current_course:
            return jsonify({"message": "Current course not found"}), 404

        # Validacija opcionih polja
        try:
            validated_data = update_current_course_schema.load(data)
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400

        # Kombinuj stare i nove vrednosti
        professor = validated_data.get('user_id', current_course['user_id'])
        price = validated_data.get('price', current_course['price'])
        start_at = validated_data.get('start_at', current_course['start_at'])
        end_at = validated_data.get('end_at', current_course['end_at'])
        level = validated_data.get('level', current_course['level'])
        location = validated_data.get('location', current_course['location'])
        max_members = validated_data.get('max_members', current_course['max_members'])
        lessons = validated_data.get('lessons', current_course['lessons'])
        course_id =  current_course['course_id']

        #  provera da li profesor i kurs postoje, ako su poslati
        if 'user_id' in validated_data:
            cursor.execute("SELECT id FROM user WHERE id=%s AND rola='professor'", (professor,))
            if not cursor.fetchone():
                return jsonify({"message": f"Professor with id {professor} does not exist"}), 400

        if 'course_id' in validated_data:
            cursor.execute("SELECT id FROM course WHERE id=%s", (course_id,))
            if not cursor.fetchone():
                return jsonify({"message": f"Course with id {course_id} does not exist"}), 400

        # Provera preklapanja termina ako je start_at, end_at ili profesor poslato
        if any(k in validated_data for k in ['start_at', 'end_at', 'user_id', 'course_id']):
            cursor.execute("""
                SELECT id FROM current_courses
                WHERE course_id=%s AND user_id=%s AND id != %s
                AND NOT (%s > end_at OR %s < start_at)
            """, (course_id, professor, id, start_at, end_at))
            if cursor.fetchone():
                return jsonify({"message": "This course is already scheduled for this professor in the given period."}), 400

        # Update
        query = """
            UPDATE current_courses
            SET user_id=%s, course_id=%s, price=%s, start_at=%s, end_at=%s,
                level=%s, location=%s, max_members=%s, lessons=%s
            WHERE id=%s
        """
        values = (professor, course_id, price, start_at, end_at, level, location, max_members, lessons, id)
        cursor.execute(query, values)
        con.commit()

        return jsonify({"message": "Current course updated successfully."}), 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while updating the course."}), 500

    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


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

# Course update Schema for Validation
update_course_schema = UpdateCourseSchema()

@admin_bp.route("/update-course/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin"])
def update_course(id):
    try:
        con, cursor = get_db_connection()

        upload_folder_course = current_app.config["UPLOAD_FOLDER_COURSE"]
        allowed_extensions = current_app.config["ALLOWED_IMAGE_EXTENSIONS"]

        cursor.execute("SELECT * FROM course WHERE id=%s", (id,))
        course = cursor.fetchone()
        if not course:
            return jsonify({"message": "Course not found"}), 404

        file = request.files.get('file')
        data = request.form.to_dict()

        try:
            validated_data = update_course_schema.load(
            data,
            unknown="exclude"  # ili unknown=EXCLUDE
            )
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400

        if file:
            old_filename = course.get('course_image_url')
            # Check extension
            if not allowed_file(file.filename):
                allowed_extensions = current_app.config.get("ALLOWED_IMAGE_EXTENSIONS", set())
                return jsonify({
                "message": f"Invalid image format. Allowed: {', '.join(allowed_extensions)}"
                }), 400

            # Check file size (max 2MB)
            if not allowed_file_size(file, max_size_mb=2):
                return jsonify({"message": "File is too large. Max size is 2MB."}), 400

       
            filename = save_uploaded_file(file,upload_folder_course)

            # Remove old image
            if old_filename and old_filename != "default_course.png":
                old_path = os.path.join(upload_folder_course, old_filename)
                if os.path.exists(old_path):
                    os.remove(old_path)
            
        else:
            filename = course['course_image_url']

        
        name = validated_data.get('name', course['name']).strip().lower()
        language = validated_data.get('language', course['language']).strip().lower()

        query = """
        UPDATE course
        SET name = %s,course_image_url=%s,  language = %s
        WHERE id = %s
        """

        values = (
            name, filename, language, id
        )

        cursor.execute(query, values)

        con.commit()

        return jsonify({"message": "Course details updated successfully."}), 200

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while updating the course."}), 500
    
    finally:
        if cursor:
            cursor.close()
        if con:
            con.close()


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

        for course in data:
            course["course_image_url"] = get_file_url(
            course.get("course_image_url"),
            folder_type="course",
            default="default_course.png"
        )
        
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
    con, cursor = None, None  # Inicijalizujemo konekciju i cursor
    try:
        con, cursor = get_db_connection()

        language = request.args.get('language') or '%'

        query = "SELECT id, name, course_image_url, language FROM course WHERE language LIKE %s;"
        cursor.execute(query, (language,))
        data = cursor.fetchall()

        # Generate url for course image
        for course in data:
            course["course_image_url"] = get_file_url(
            course.get("course_image_url"),
            folder_type="course",
            default="default_course.png"
        )

        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "An error occurred while fetching courses."}), 500

    finally:
        # Close connection
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
        
        data["course_image_url"] = get_file_url(
            data.get("course_image_url"),
            folder_type="course",
            default="default_course.png")
        
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

        data = request.json

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
        
        # Validating text fields with Marshmallow
        try:
            validated_data = current_course_schema.load(request.json)
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400
        
        
        query = """
            INSERT INTO current_courses (course_id, user_id, price, start_at, end_at, max_members, level,location,lessons)
            VALUES (%s,  %s, %s, %s, %s, %s, %s,%s, %s)
            """
        values = (validated_data['course_id'], validated_data['user_id'], validated_data['price'],  validated_data['start_at'],
                  validated_data['end_at'], validated_data['max_members'], validated_data['level'], validated_data['location'], validated_data['lessons'])

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

        # Check extension
        if not allowed_file(file.filename):
            allowed_extensions = current_app.config.get("ALLOWED_IMAGE_EXTENSIONS", set())
            return jsonify({
            "message": f"Invalid image format. Allowed: {', '.join(allowed_extensions)}"
            }), 400

        # Check file size (max 2MB)
        if not allowed_file_size(file, max_size_mb=2):
            return jsonify({"message": "File is too large. Max size is 2MB."}), 400

       
        filename = save_uploaded_file(file,upload_folder_course)
        query = """
            INSERT INTO course (name, course_image_url, language)
            VALUES (%s, %s, %s)
        """
        values = (data["name"], filename, data["language"])

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