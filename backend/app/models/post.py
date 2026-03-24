from sqlalchemy import Column, String, DateTime,Text
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID as Uuid
from sqlalchemy import ForeignKey
from uuid import uuid4
from app.db.base import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    user_id=Column(Uuid(as_uuid=True),ForeignKey("users.id"), nullable=False)
    content = Column(Text, nullable=False)
    image_url = Column(String(255),nullable=True)
    created_at = Column(DateTime, default=datetime.now,index=True)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)