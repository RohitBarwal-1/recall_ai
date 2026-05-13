from typing import Optional

from fastapi import Form


class FileUploadRequest:
    def __init__(
        self,
        user_id: Optional[str] = Form(None),
        document_type: Optional[str] = Form(None),
        tags: Optional[str] = Form(None)
    ):
        self.user_id = user_id
        self.document_type = document_type
        self.tags = tags