import uuid
from database.connection import Base
from datetime import datetime, UTC
from sqlalchemy import Column, Text, String, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID


class Document(Base):
    __tablename__ = "document"

    document_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    collection_id = Column(UUID(as_uuid=True),ForeignKey("collection.collection_id"),nullable=False,)
    document_name = Column(Text, nullable=False)
    document_path = Column(Text)
    mime_type = Column(String(255))
    status = Column(String(50))
    error_message = Column(Text)
    document_metadata = Column(JSON)
    created_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(UTC))
    updated_at = Column(DateTime(timezone=True), nullable=False, default=lambda: datetime.now(UTC), onupdate=lambda: datetime.now(UTC))
    deleted_at = Column(DateTime(timezone=True), nullable=True)