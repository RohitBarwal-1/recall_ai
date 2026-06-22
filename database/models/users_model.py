import uuid
from database.connection import Base
from sqlalchemy import Column, Text
from sqlalchemy.dialects.postgresql import UUID


class Users(Base):
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    email = Column(Text, nullable=False, unique=True)
    password = Column(Text, nullable=False)