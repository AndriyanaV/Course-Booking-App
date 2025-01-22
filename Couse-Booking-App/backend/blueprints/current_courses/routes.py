from flask import Blueprint, jsonify, request
from database import get_db_connection
from utils import check_course_availability

current_courses_bp = Blueprint('current_courses', __name__)

con, cursor = get_db_connection()


@current_courses_bp.route("/get-courses", methods=["GET"])
def get_courses():
    try:
        # Ako nije prosleđen, koristi "%" kao default
        language = request.args.get("language", default="%")
        # Ako nije prosleđen, koristi "%" kao default
        level = request.args.get("level", default="%")

        if (language == ""):
            language = "%"

        if (level == ""):
            level = "%"

        print(f"Language: {language}, Level: {level}")

        query = """
            SELECT 
    course.id AS course_id, 
    course.name, 
    course.course_image_url,
    current_courses.id, 
    current_courses.start_at,
    current_courses.level, 
    current_courses.price, 
    CEIL(DATEDIFF(end_at, start_at) / 7) AS weeks_duration,
    current_courses.max_members, 
    current_courses.lessons
    FROM 
        course
    JOIN 
        current_courses 
    ON 
        course.id = current_courses.course_id
    WHERE  
        language LIKE %s 
        AND level LIKE %s;
    """

        values = (language, level)
        cursor.execute(query, values)
        data = cursor.fetchall()

        # return jsonify(data)
        aviable_courses = []

        for course in data:

            aviability = check_course_availability(course)

            if (aviability):

                aviable_courses.append(course)
                print("i spot avilable course")

        query = "SELECT DATE(start_at) AS samo_datum FROM current_courses;"

        cursor.execute(query)
        date = cursor.fetchall()
        print(date)

        return jsonify(aviable_courses)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"message": "We don't have course to offer!"})


@current_courses_bp.route("/course-info/<int:id>", methods=["GET"])
def show_clicked_course(id):
    try:

        query = """
            SELECT course.*,
                current_courses.*,
                CEIL(DATEDIFF(end_at, start_at) / 7) AS weeks_duration,
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
