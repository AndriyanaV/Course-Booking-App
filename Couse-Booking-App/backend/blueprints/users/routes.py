from flask import Blueprint, jsonify, request
from database import get_db_connection
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from decoraotrs import role_required
from utils import check_course_availability
from datetime import datetime
import pymysql

users_bp = Blueprint('users', __name__)

con, cursor = get_db_connection()


@users_bp.route("/user-profile", methods=["GET"])
@jwt_required()
def show_user_profile():

    claims = get_jwt()
    user_id = claims.get('user_id')

    try:
        query = """
        SELECT *
        FROM user
        WHERE user.id=%s
        """
        cursor.execute(query, (user_id, ))
        data = cursor.fetchone()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@users_bp.route("/user-courses", methods=["GET"])
@jwt_required()
def show_user_courses():
    try:

        claims = get_jwt()
        user_id = claims.get('user_id')

        query = """
            SELECT  
                course.name AS course_name, 
                course.id AS course_id, 
                current_courses.id AS current_course_id, 
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

    # finally:
    #     cursor.close()  # Zatvori kursor
    #     con.close()  # Zatvori konekciju


@users_bp.route("/book-course", methods=["POST"])
@jwt_required()
def count_members():
    try:
        data = request.json
        aviable = check_course_availability(data['current_course_id'])

        if (aviable):
            return book_course()
        else:
            return jsonify({"message": "All seats are reserved!"})
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "You need to register or login to book a course!"})


def book_course():
    try:
        claims = get_jwt()
        user_id = claims.get('user_id')

        data = request.json

        query = """
        INSERT INTO user_course (user_id,course_id)
        VALUES (%s, %s)
        """
        values = (user_id, data['course_id'])

        cursor.execute(query, values)
        con.commit()
        return jsonify({"message": "You've registered course sucessfully!"})

    except pymysql.IntegrityError as e:
        if e.args[0] == 1062:
            return jsonify({"message": "You have already booked this course!"}), 400
        else:
            return jsonify({"message": "Database error occurred!"}), 500

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "You need to register or login to book a course!"})


@users_bp.route("/professor-courses", methods=["GET"])
@jwt_required()
@role_required(["professor"])
def show_professor_courses():
    try:

        claims = get_jwt()
        user_id = claims.get('user_id')

        query = """
        SELECT course.name,
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
