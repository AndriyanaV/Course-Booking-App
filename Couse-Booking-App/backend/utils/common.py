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
