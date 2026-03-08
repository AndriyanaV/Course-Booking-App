import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    BASE_URL = os.getenv(
        "BASE_URL",
        "http://127.0.0.1:5000"
    )

    
    # Upload folders
    UPLOAD_FOLDER_COURSE = os.path.join(BASE_DIR, "uploads", "course")
    UPLOAD_FOLDER_USER = os.path.join(BASE_DIR, "uploads", "user")

    # Base URL for images
    COURSE_IMAGE_BASE_URL = f"{BASE_URL}/uploads/course/"
    USER_IMAGE_BASE_URL = f"{BASE_URL}/uploads/user/"

    
    # Allowed extensions
    ALLOWED_IMAGE_EXTENSIONS = set(
        e.strip().lower()
        for e in os.getenv(
            "ALLOWED_IMAGE_EXTENSIONS",
            "jpg,jpeg,png,webp"
        ).split(",")
    )

    DEFAULT_USER_IMAGE = "default_user.png"
    DEFAULT_COURSE_IMAGE = "default_course.png"