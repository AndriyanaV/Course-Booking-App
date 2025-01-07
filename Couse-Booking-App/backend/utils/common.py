from database import get_db_connection
from datetime import datetime

con, cursor = get_db_connection()


def check_course_availability(course_id):
    try:

        query = """
              SELECT COUNT(*) AS current_number,start_at from user_course JOIN current_courses on user_course.course_id = current_courses.id WHERE current_courses.id=%s;"""

        value = course_id

        cursor.execute(query, (value, ))
        course = cursor.fetchone()

        current_number = course.get("current_number")

        start_date = course.get("start_at")

        date = datetime.now()

        query = "SELECT max_members FROM course where course.id=%s"
        cursor.execute(query, (value, ))
        max_members = cursor.fetchone()
        max_members = max_members.get("max_members")

        if (current_number == max_members or date >= start_date):
            return False
        else:
            return True

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
