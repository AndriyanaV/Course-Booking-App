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
from schemas.user.update_user_schema import UpdateUserSchema
from schemas.user.add_user_schema import AddUserSchema
from utils.file_utils import allowed_file, allowed_file_size
from utils.get_file_url import get_file_url
from utils.save_uploaded_file import save_uploaded_file


admin_bp = Blueprint('admin', __name__)

# Update current course schema
update_current_course_schema = UpdateCurrentCourseSchema()

# UPDATE
@admin_bp.route("/update-current-course/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin"])
def update_current_course(id):
    try:
        con, cursor= None, None
        con, cursor = get_db_connection()

        #JSON podaci
        data = request.json 

        cursor.execute("SELECT * FROM current_courses WHERE id=%s", (id,))
        current_course = cursor.fetchone()
        if not current_course:
            return jsonify({"message": "Current course not found"}), 404

        try:
            validated_data = update_current_course_schema.load(data)
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400

        # Combine old and new values
        professor = validated_data.get('user_id', current_course['user_id'])
        price = validated_data.get('price', current_course['price'])
        start_at = validated_data.get('start_at', current_course['start_at'])
        end_at = validated_data.get('end_at', current_course['end_at'])
        level = validated_data.get('level', current_course['level'])
        location = validated_data.get('location', current_course['location'])
        max_members = validated_data.get('max_members', current_course['max_members'])
        lessons = validated_data.get('lessons', current_course['lessons'])
        course_id =  current_course['course_id']

        # checking if the professor and the course exist
        if 'user_id' in validated_data:
            cursor.execute("SELECT id FROM user WHERE id=%s AND rola='professor'", (professor,))
            if not cursor.fetchone():
                return jsonify({"message": f"Professor with id {professor} does not exist"}), 400

        if 'course_id' in validated_data:
            cursor.execute("SELECT id FROM course WHERE id=%s", (course_id,))
            if not cursor.fetchone():
                return jsonify({"message": f"Course with id {course_id} does not exist"}), 400

        # Check for appointment overlap if start_at, end_at or professor is sent
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

# update_user_schema = UpdateUserSchema()

@admin_bp.route("/update-user/<int:id>", methods=['PUT'])
@jwt_required()
@role_required(["admin"])
def update_user_info(id):
    try:
        con, cursor = get_db_connection()

        upload_folder_user = current_app.config["UPLOAD_FOLDER_USER"]
        allowed_extensions = current_app.config["ALLOWED_IMAGE_EXTENSIONS"]
        default_user_image = current_app.config["DEFAULT_USER_IMAGE"]

        file = request.files.get('file')
        data = request.form.to_dict()

        remove_image = request.form.get("remove_image")

        print("Received data:", data)

        query = "SELECT  * FROM user WHERE id=%s"
        cursor.execute(query, (id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"error": "User not found"}), 404
        print(type(user))

        schema = UpdateUserSchema()
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
            
       
        password = validated_data.get("password")

        if password:
            password_hashed = generate_password_hash(password)
        else:
            password_hashed = user['password_hash']
    
        first_name = validated_data.get('first_name', user['first_name'])
        last_name = validated_data.get('last_name', user['last_name'])
        phone_number = validated_data.get('phone_number', user['phone_number'])
        email = validated_data.get('email', user['email'])
        biography = validated_data.get('biography', user['biography'])
        rola = validated_data.get('rola', user['rola'])
        password = password_hashed

        query = """
        UPDATE user
        SET first_name = %s, last_name = %s, email = %s, phone_number = %s, biography = %s, user_image_url = %s, password_hash=%s, rola=%s
        WHERE id = %s
        """

        values = (first_name, last_name, email, phone_number,
                  biography, filename, password_hashed, rola, id)

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
        default_course_image = current_app.config["DEFAULT_COURSE_IMAGE"]

        cursor.execute("SELECT * FROM course WHERE id=%s", (id,))
        course = cursor.fetchone()
        if not course:
            return jsonify({"message": "Course not found"}), 404

        file = request.files.get('file')
        data = request.form.to_dict()

        try:
            validated_data = update_course_schema.load(
            data,
            unknown="exclude"  
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
            if not allowed_file_size(file, max_size_mb=5):
                return jsonify({"message": "File is too large. Max size is 2MB."}), 400

            # Save new image
            filename = save_uploaded_file(file,upload_folder_course)

            # Remove old image
            if old_filename and old_filename != default_course_image:
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

        default_user_image = current_app.config["DEFAULT_USER_IMAGE"]

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

        # generate img url
        for user in data:
            user["user_image_url"] = get_file_url(
            user.get("user_image_url"),
            folder_type="user",
            default=default_user_image
        )
            
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

        default_user_image = current_app.config["DEFAULT_USER_IMAGE"]

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
        
        data["user_image_url"] = get_file_url(
            data.get("user_image_url"),
            folder_type="user",
            default=default_user_image)
        
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

        # generate img url
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
    con, cursor = None, None  
    try:
        con, cursor = get_db_connection()

        default_course_image = current_app.config["DEFAULT_COURSE_IMAGE"]

        language = request.args.get('language') or '%'

        query = "SELECT id, name, course_image_url, language FROM course WHERE language LIKE %s;"
        cursor.execute(query, (language,))
        data = cursor.fetchall()

        # Generate url for course image
        for course in data:
            course["course_image_url"] = get_file_url(
            course.get("course_image_url"),
            folder_type="course",
            default=default_course_image
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

        default_course_image = current_app.config["DEFAULT_COURSE_IMAGE"]

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
            default=default_course_image)
        
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
        return jsonify({"message": "An error occurred while fetching professors."}), 500
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
        allowed_extensions = current_app.config["ALLOWED_IMAGE_EXTENSIONS"]

        file = request.files.get('file')  # optional image
        data = request.form.to_dict()      # svi ostali Field-ovi

        # Marshmallow validacija
        try:
            validated_data = add_user_schema.load(data)
        except ValidationError as err:
            return jsonify({"errors": err.messages}), 400

        # Check if email exists
        cursor.execute("SELECT id FROM user WHERE email = %s", (validated_data["email"],))
        if cursor.fetchone():
            return jsonify({"message": "User with this email already exists!"}), 409

        password_hash = generate_password_hash(validated_data['password'])

        # Image required only for professors
        if validated_data['rola'] == 'professor' and (not file or file.filename == ""):
            return jsonify({"message": "Image is required for professors"}), 400

        # Ako file postoji, sačuvaj
        if file and file.filename != "":
            if not allowed_file(file.filename):
                return jsonify({
                    "message": f"Invalid image format. Allowed: {', '.join(allowed_extensions)}"
                }), 400

            if not allowed_file_size(file, max_size_mb=5):
                return jsonify({"message": "File is too large. Max 2MB."}), 400

            filename = save_uploaded_file(file, upload_folder_user)
        else:
            filename = current_app.config["DEFAULT_USER_IMAGE"]

        # Insert u DB
        query = """
        INSERT INTO user 
        (first_name, last_name, email, phone_number, biography, password_hash, rola, user_image_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            validated_data['first_name'],
            validated_data['last_name'],
            validated_data['email'],
            validated_data.get('phone_number'),
            validated_data.get('biography'),
            password_hash,
            validated_data['rola'],
            filename
        )

        cursor.execute(query, values)
        con.commit()

        return jsonify({"message": "You've added new user!"}), 201

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "Error!"}), 500
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

        # Validating text fields with Marshmallow
        try:
            validated_data = current_course_schema.load(request.json)
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
        default_course_image = current_app.config["DEFAULT_COURSE_IMAGE"]

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
        if not allowed_file_size(file, max_size_mb=5):
            return jsonify({"message": "File is too large. Max size is 5MB."}), 400

       
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

        upload_folder_course = current_app.config["UPLOAD_FOLDER_COURSE"]
        default_course_image = current_app.config["DEFAULT_COURSE_IMAGE"]

        cursor.execute("SELECT course_image_url FROM course WHERE id = %s", (id,))
        course = cursor.fetchone()

        if not course:
            return jsonify({"message": "Course not found."}), 404
        
        filename = course['course_image_url']

        if filename and filename != default_course_image:
                old_path = os.path.join(upload_folder_course, filename)
                if os.path.exists(old_path):
                    os.remove(old_path)
                    
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

        upload_folder_user = current_app.config["UPLOAD_FOLDER_USER"]
        default_user_image = current_app.config["DEFAULT_USER_IMAGE"]

        cursor.execute("SELECT user_image_url FROM user WHERE id = %s", (id,))
        user = cursor.fetchone()

        if not user:
            return jsonify({"message": "User not found."}), 404
        
        filename = user['user_image_url']

        if filename and filename != default_user_image:
                old_path = os.path.join(upload_folder_user, filename)
                if os.path.exists(old_path):
                    os.remove(old_path)

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

