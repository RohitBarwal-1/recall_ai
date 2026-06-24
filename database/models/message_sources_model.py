import uuid
from database.connection import Base
from datetime import datetime, UTC
from sqlalchemy import Column, Float, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID


class MessageSources(Base):
    __tablename__ = "message_sources"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    message_id = Column(UUID(as_uuid=True),ForeignKey("messages.message_id"),nullable=False,)
    chunk_id = Column(UUID(as_uuid=True),ForeignKey("document_chunks.chunk_id"),nullable=False,)
    relevance_score = Column(Float)
    created_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))
    deleted_at = Column(DateTime(timezone=True), nullable=True)