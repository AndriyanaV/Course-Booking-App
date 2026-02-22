import os, uuid
from werkzeug.utils import secure_filename
from flask import current_app

def save_uploaded_file(file, folder):
    """
    Save uploaded file in given folder with a UUID filename.
    Returns the filename (not full URL).
    """
    if not file:
        return None
    
    original_filename = secure_filename(file.filename)
    ext = original_filename.rsplit(".", 1)[-1].lower()
    filename = f"{uuid.uuid4()}.{ext}"
    
    path = os.path.join(folder, filename)
    file.save(path)
    
    return filename