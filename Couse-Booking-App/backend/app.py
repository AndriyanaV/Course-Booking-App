
from blueprints.current_courses.routes import current_courses_bp
from blueprints.auth.routes import auth_bp
from blueprints.users.routes import users_bp
from blueprints.admin.routes import admin_bp
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt
from flask import Flask, jsonify, request
import mysql.connector
from datetime import datetime
import pymysql
from flask import Blueprint

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = 'e2b6fc2a9bfb5d70d4d5c7ad67e2a6f5016a82c49e9bc0af3a1c7e879bb10f6a'
jwt = JWTManager(app)


app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(users_bp, url_prefix='/users')
app.register_blueprint(current_courses_bp, url_prefix='/current-courses')
app.register_blueprint(auth_bp, url_prefix='/')


if __name__ == "__main__":
    app.run(debug=True)


# UPLOAD_FOLDER = 'uploads/'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}


# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# try:
#     con = pymysql.connect(
#         host="localhost",
#         port=3306,
#         user="root",
#         passwd="",
#         database="course_management_test",
#         cursorclass=pymysql.cursors.DictCursor,
#     )

#     cursor = con.cursor()


# except Exception as e:
#     print(f"An unexpected error occurred: {e}")


# @app.route("/get-courses", methods=["GET"])
# def get_courses():
#     try:

#         query = """
#             SELECT course.id, course.name, course.course_image_url,
#                 current_courses.id, user.user_image_url,
#                 current_courses.level, current_courses.price
#             FROM course
#             JOIN current_courses ON course.id = current_courses.course_id
#             JOIN user ON user.id = current_courses.user_id
#             WHERE status != 'inactive';
#         """

#         cursor.execute(query)
#         data = cursor.fetchall()
#         return jsonify(data)

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/course-info/<int:id>", methods=["GET"])
# def show_clicked_course(id):
#     try:
#         query = """
#             SELECT course.*,
#                 current_courses.*,
#                 user.biography,
#                 user.first_name,
#                 user.last_name,
#                 user.user_image_url
#             FROM course
#             JOIN current_courses ON course.id = current_courses.course_id
#             JOIN user ON user.id = current_courses.user_id
#             WHERE current_courses.id = %s;
#         """
#         cursor.execute(query, (id,))
#         data = cursor.fetchone()
#         return jsonify(data)

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/my-profile/<int:id>", methods=["GET"])
# def show_user_profile(id):
#     try:
#         query = """
#         SELECT id,
#              first_name,
#              last_name,
#              email,
#              user_image_url AS image,
#              phone_number,
#              biography,
#              rola
#         FROM user
#         WHERE user.id=%s
#         """
#         cursor.execute(query, (id,))
#         data = cursor.fetchone()
#         return jsonify(data)

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/professor-courses/<int:id>", methods=["GET"])
# def show_professor_courses(id):
#     try:
#         query = """
#         SELECT course.name,
#             current_courses.start_at,
#             current_courses.end_at,
#             current_courses.level
#         FROM course
#         JOIN current_courses ON course.id = current_courses.course_id
#         JOIN user ON user.id = current_courses.user_id
#         WHERE user.id = %s;
#         """

#         cursor.execute(query, (id,))

#         data = cursor.fetchall()
#         return jsonify(data)

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/user-courses/<int:id>", methods=["GET"])
# def show_user_courses(id):
#     try:
#         query = """
#         SELECT user.id,
#              course.name,
#              course.id,
#              current_courses.id,
#              current_courses.start_at,
#              current_courses.end_at,
#              current_courses.price,
#              current_courses.level
#         FROM course
#         JOIN current_courses ON course.id = current_courses.course_id
#         JOIN user_course ON user_course.course_id = current_courses.id
#         JOIN user ON user.id = user_course.user_id
#         WHERE user.id = %s;
#         """
#         cursor.execute(query, (id,))

#         data = cursor.fetchall()
#         return jsonify(data)

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/admin-users", methods=["GET"])
# def get_all_users():
#     try:
#         query = """
#         SELECT id,
#             first_name,
#             last_name,
#             email,
#             rola
#         FROM user;
#         """
#         cursor.execute(query)
#         data = cursor.fetchall()
#         return jsonify(data)

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/admin-current-courses", methods=["GET"])
# def get_all_current_courses():
#     try:
#         query = """
#         SELECT course.*,
#             current_courses.*
#         FROM course
#         JOIN current_courses ON course.id = current_courses.course_id;
#         """
#         cursor.execute(query)
#         data = cursor.fetchall()
#         return jsonify(data)

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/admin-courses", methods=["GET"])
# def get_all_courses():
#     try:
#         query = """
#         SELECT * FROM course
#         """
#         cursor.execute(query)
#         data = cursor.fetchall()
#         return jsonify(data)

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#         return jsonify({"message": "An error occurred while fetching courses."}), 500


# @app.route("/add-user", methods=["POST"])
# def add_user():
#     try:
#         data = request.json

#         # file = data['file']
#         # if file and allowed_file(file.filename):
#         #     filename = secure_filename(file.filename)
#         #     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         #     file.save(file_path)
#         #     file_url = f'/uploads/{filename}'

#         query = """
#         INSERT INTO user (first_name, last_name, email, phone_number, biography, user_image_url, password_hash, rola)
#         VALUES (%s, %s, %s, %s, %s,  %s, %s, %s)
#         """
#         values = (data['first_name'], data['last_name'], data['email'], data['phone_number'], data['biography'], 'null',
#                   data['password_hash'], data['rola'])

#         cursor.execute(query, values)
#         con.commit()
#         return jsonify({"message": "You've added new user sucessfully!"})

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/add-current-course", methods=["POST"])
# def add_current_course():
#     try:
#         # Dobijanje podataka iz zahteva
#         data = request.json

#         query = """
#             INSERT INTO current_courses (course_id, user_id, price, duration, start_at, end_at, status, level,location)
#             VALUES (%s,  %s, %s, %s, %s, %s, %s,%s,%s)
#             """
#         values = (data['course_id'], data['user_id'], data['price'], data['duration'], data['start_at'],
#                   data['end_at'], data['status'], data['level'], data['location'])

#         cursor.execute(query, values)
#         con.commit()

#         return jsonify({"message": "Course has been successfully added to current courses."}), 200

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/add-course", methods=["POST"])
# def add_course():
#     try:
#         data = request.json

#         # file = data['file']
#         # if file and allowed_file(file.filename):
#         #     filename = secure_filename(file.filename)
#         #     file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         #     file.save(file_path)
#         #     file_url = f'/uploads/{filename}'

#         query = """
#         INSERT INTO course (name, course_image_url, max_members, language)
#         VALUES (%s, %s, %s, %s)
#         """
#         values = (data['name'], "null",
#                   data['max_members'], data['language'])

#         cursor.execute(query, values)
#         con.commit()
#         return jsonify({"message": "You've added new course sucessfully!"})

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")

# rezervacija kursa


# @app.route("/add-user-course", methods=["POST"])
# def add_user_course():
#     try:
#         data = request.json

#         query = """
#         INSERT INTO user_course (user_id,course_id)
#         VALUES (%s, %s)
#         """
#         values = (data['user_id'], data['course_id'])

#         cursor.execute(query, values)
#         con.commit()
#         return jsonify({"message": "You've registered course sucessfully!"})

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/update-current-course/<int:id>", methods=['PUT'])
# def update_current_course(id):
#     try:
#         data = request.json

#         query = """
#         UPDATE current_courses
#         SET price = %s, duration = %s, start_at = %s, end_at = %s, status = %s, level = %s, location = %s
#         WHERE id = %s
#         """
#         values = (
#             data['price'], data['duration'], data['start_at'], data['end_at'],
#             data['status'], data['level'], data['location'],
#             id
#         )

#         cursor.execute(query, values)
#         con.commit()
#         return jsonify({"message": "Current course updated successfully."}), 200

#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")


# @app.route("/update-course/<int:id>", methods=['PUT'])
# def update_course():
#     try:

#         data = request.json

#         query = """
#         UPDATE course
#         SET name = %s, max_members = %s, language = %s
#         WHERE id = %s
#         """

#         values = (
#             data['name'], data['max_members'], data['language'], id
#         )

#         cursor.execute(query, values)

#         con.commit()

#         return jsonify({"message": "Course details updated successfully."}), 200

#     except Exception as e:

#         print(f"An unexpected error occurred: {e}")
#         return jsonify({"message": "An error occurred while updating the course."}), 500


# @app.route("/delete-course/<int:id>", methods=['DELETE'])
# def delete_course():
#     try:

#         data = request.json

#         query = """
#         DELETE FROM course WHERE id = %s;
#         """

#         cursor.execute(query, (id, ))

#         con.commit()

#         return jsonify({"message": "Course deleted sucessfully."}), 200

#     except Exception as e:

#         print(f"An unexpected error occurred: {e}")
#         return jsonify({"message": "An error occurred while deleting the course."}), 500


# @app.route("/delete-current-course/<int:id>", methods=['DELETE'])
# def delete_current_course():
#     try:

#         data = request.json

#         query = """
#         DELETE FROM current_courses WHERE id = %s;
#         """

#         # values = (
#         #     data['id']
#         # )

#         cursor.execute(query, (id,))

#         con.commit()

#         return jsonify({"message": "Course deleted sucessfully."}), 200

#     except Exception as e:

#         print(f"An unexpected error occurred: {e}")
#         return jsonify({"message": "An error occurred while deleting the course."}), 500


# @app.route("/delete-user/<int:id>", methods=['DELETE'])
# def delete_current_course():
#     try:

#         data = request.json

#         query = """
#         DELETE FROM user WHERE id = %s;
#         """

#         # values = (
#         #     data['id']
#         # )

#         cursor.execute(query, )

#         con.commit()

#         return jsonify({"message": "User deleted sucessfully."}), 200

#     except Exception as e:

#         print(f"An unexpected error occurred: {e}")
#         return jsonify({"message": "An error occurred while deleting the user."}), 500


# if __name__ == "__main__":
#     app.run(debug="True")
