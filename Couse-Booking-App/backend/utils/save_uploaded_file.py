import os
import uuid
from werkzeug.utils import secure_filename

def save_uploaded_file(file, upload_folder, base_url):
    """
    Save uploaded file safely with UUID name and return its URL.
    Works exactly like your original snippet.
    
    Args:
        file: Werkzeug FileStorage object
        upload_folder: folder gde se čuva fajl (string)
        base_url: base URL za fajlove

    Returns:
        file_url (str)
    """
    if not file or file.filename == "":
        return None

    # Secure filename i UUID
    original_filename = secure_filename(file.filename)
    ext = original_filename.rsplit(".", 1)[-1].lower()
    filename = f"{uuid.uuid4()}.{ext}"

    # Kreiraj folder ako ne postoji
    os.makedirs(upload_folder, exist_ok=True)

    # Sačuvaj fajl
    file.save(os.path.join(upload_folder, filename))

    # Vrati URL fajla
    return f"{base_url.rstrip('/')}/{filename}"
