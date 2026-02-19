import os

class Config:
    # Course images
    UPLOAD_FOLDER_COURSE = os.getenv("UPLOAD_FOLDER_COURSE", "uploads/course")
    COURSE_IMAGE_BASE_URL = os.getenv("COURSE_IMAGE_BASE_URL", "http://127.0.0.1:5000/uploads/course/")

    # User images
    UPLOAD_FOLDER_USER = os.getenv("UPLOAD_FOLDER_USER", "uploads/user")
    USER_IMAGE_BASE_URL = os.getenv("USER_IMAGE_BASE_URL", "http://127.0.0.1:5000/uploads/user/")

    # Allowed extensions
    ALLOWED_IMAGE_EXTENSIONS = set(
        e.lower() for e in os.getenv("ALLOWED_IMAGE_EXTENSIONS", "jpg,jpeg,png,webp").split(",")
    )

    DEFAULT_USER_IMAGE = "anonymous.png"
