from flask import jsonify
from flask_jwt_extended import get_jwt
import pymysql
from database import get_db_connection
from datetime import datetime


con, cursor = get_db_connection()


def check_course_availability(course):
    try:
        # print(course)
        query = """
              SELECT COUNT(*) AS current_number FROM user_course WHERE course_id=%s;"""

        value = course.get('id')
        cursor.execute(query, (value, ))

        result = cursor.fetchone()

        current_number = result.get("current_number")

        start_date = course.get("start_at")
        start_date_ms = int(start_date.timestamp()*1000)

        date = datetime.now()
        date_ms = int(date.timestamp()*1000)

        max_members = course.get('max_members')

        if (current_number == max_members or date_ms > start_date_ms):
            return False
        else:
            return True

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def book_course(course_id):
    try:
        con, cursor = get_db_connection()

        claims = get_jwt()
        user_id = claims.get('user_id')

        # data = request.json

        query = """
        INSERT INTO user_course (user_id,course_id)
        VALUES (%s, %s)
        """
        values = (user_id, course_id)

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