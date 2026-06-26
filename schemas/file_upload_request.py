from typing import Optional

from fastapi import Form


class FileUploadRequest:
    def __init__(self,
                    user_id: str = Form(),
                    collection_id: str = Form(),
                    document_type: str = Form(),
                    tags: Optional[str] = Form(None)
                ):  
        self.user_id = user_id
        self.collection_id = collection_id
        self.document_type = document_type
        self.tags = tags