from urllib.parse import quote
from flask import current_app

def get_file_url(filename: str, folder_type: str, default=None) -> str:
    """
    Vrati puni URL za dati fajl koristeći konfiguraciju.
    
    folder_type: 'course' ili 'user' 
    default: filename default slike ako ne postoji
    """
    if not filename and folder_type == "course":
        return f"{current_app.config['COURSE_IMAGE_BASE_URL']}{default}" if default else None
    
    if not filename and folder_type == "user":
        return f"{current_app.config['USER_IMAGE_BASE_URL']}{default}" if default else None

    if folder_type == "course":
        base_url = current_app.config['COURSE_IMAGE_BASE_URL']
    elif folder_type == "user":
        base_url = current_app.config['USER_IMAGE_BASE_URL']
    else:
        raise ValueError("Unknown folder type")

    return f"{base_url.rstrip('/')}/{quote(filename)}"