from database.models.document_chunk_model import DocumentChunk
from database.connection import session
from logging_config import logger
from sqlalchemy import select

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
    
    async def retrieve_chunks(self, user_query: str, top_k: int = 5) -> list:
        async with session() as db:
            query_embedding = user_query
            stmt = (
                select(
                    self.model.id,
                    self.model.text.label("content"),
                    (1 - self.model.embedding.cosine_distance(query_embedding)).label("similarity")
                )
                .order_by(self.model.embedding.cosine_distance(query_embedding))
                .limit(top_k)
            )

            result = await db.execute(stmt)
            rows = result.all()

            return [
                {
                    "id": row.id,
                    "content": row.content,
                    "similarity": row.similarity
                }
                for row in rows
            ]
        return []