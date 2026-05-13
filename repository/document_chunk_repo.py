import logging
from database.models.document_chunk_model import DocumentChunk
from database.connection import session
from logging_config import logger


class EmbeddingsRepository:
    def __init__(self):
        self.model = DocumentChunk

    async def save_chunks(self, filename: str, chunks: list, embeddings: list):
        async with session() as db:
            for chunk, embedding in zip(chunks, embeddings):
                db.add(self.model(text=chunk.page_content, 
                                    embedding=embedding, 
                                    metadata=chunk.metadata, 
                                    source=filename, 
                                    chunk_index=1))
            await db.commit()
            logger.info("Chunks and embeddings saved to the database successfully")

            return True
        return False