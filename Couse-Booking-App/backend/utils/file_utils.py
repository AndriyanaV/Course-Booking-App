from flask import current_app

def allowed_file(filename):
    # Checks if the file has an allowed extension.
    if "." not in filename:
        return False
    ext = filename.rsplit(".", 1)[-1].lower()
    allowed_extensions = current_app.config.get("ALLOWED_IMAGE_EXTENSIONS", set())
    return ext in allowed_extensions

def allowed_file_size(file, max_size_mb=2):
    # Checks that the file does not exceed the maximum size in MB.
    file.seek(0, 2)  # pomeri na kraj da izmeriš veličinu
    size = file.tell()
    file.seek(0)  # vrati na početak za save()
    return size <= max_size_mb * 1024 * 1024
