from flask import Blueprint, jsonify, request
from database import get_db_connection

current_courses_bp = Blueprint('current_courses', __name__)

con, cursor = get_db_connection()


@current_courses_bp.route("/get-courses", methods=["GET"])
def get_courses():
    try:

        query = """
            SELECT course.id, course.name,course.max_members, course.course_image_url,
                current_courses.id, user.user_image_url,current_courses.duration,
                current_courses.level, current_courses.price
            FROM course
            JOIN current_courses ON course.id = current_courses.course_id
            JOIN user ON user.id = current_courses.user_id
            WHERE status != 'inactive';
        """

        cursor.execute(query)
        data = cursor.fetchall()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


@current_courses_bp.route("/course-info/<int:id>", methods=["GET"])
def show_clicked_course(id):
    try:
        query = """
            SELECT course.*,
                current_courses.*,
                user.biography,
                user.first_name,
                user.last_name,
                user.user_image_url
            FROM course
            JOIN current_courses ON course.id = current_courses.course_id
            JOIN user ON user.id = current_courses.user_id
            WHERE current_courses.id = %s;
        """
        cursor.execute(query, (id,))
        data = cursor.fetchone()
        return jsonify(data)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
