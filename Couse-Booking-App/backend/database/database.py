import pymysql


def get_db_connection():
    try:
        con = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            password="",
            database="course_management_test",
            cursorclass=pymysql.cursors.DictCursor,
        )

        cursor = con.cursor() 
        return con, cursor  # Vraćamo obe - konekciju i kursor

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None, None
