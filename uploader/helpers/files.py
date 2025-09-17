import mimetypes
import os

try:
    import magic
    MAGIC_AVAILABLE = True
except ImportError:
    MAGIC_AVAILABLE = False

CONTENT_TYPE_ICO = "image/x-icon"
CONTENT_TYPE_JPG = "image/jpeg"
CONTENT_TYPE_PNG = "image/png"

CONTENT_TYPE_PDF = "application/pdf"


def get_content_type(file):
    if MAGIC_AVAILABLE:
        if hasattr(file, "temporary_file_path"):
            content_type = magic.from_file(file.temporary_file_path(), mime=True)
        else:
            content_type = magic.from_buffer(file.read(), mime=True)
    else:
        # Fallback to mimetypes
        if hasattr(file, "name"):
            content_type, _ = mimetypes.guess_type(file.name)
        else:
            content_type = "application/octet-stream"

    if hasattr(file, "seek") and callable(file.seek):
        file.seek(0)

    return content_type or "application/octet-stream"
