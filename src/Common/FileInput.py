from io import BytesIO
from typing import Optional

class FileInput:
    def __init__(self, file_type: str, file_content: BytesIO, mime_type: Optional[str] = None):
        self.file_type = file_type
        self.file_content = file_content
        self.mime_type = mime_type