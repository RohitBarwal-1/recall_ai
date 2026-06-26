from database.models.document_model import Document
from database.connection import async_session

class DocumentRepository:
    def __init__(self):
        self.model = Document

    async def add_document(self, data, file):
        async with async_session() as session:
            return   
        return