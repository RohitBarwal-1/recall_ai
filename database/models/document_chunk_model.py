from database.connection import Base
from sqlalchemy  import Column, Integer, Text
from sqlalchemy.dialects.postgresql import JSONB
from pgvector.sqlalchemy import Vector


class DocumentChunk(Base):
    __tablename__ = 'document_chunks'
    
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    embedding = Column(Vector, nullable=False)
    source = Column(Text)
    chunk_index = Column(Integer)
    chunk_metadata = Column(JSONB, column_name="metadata")
