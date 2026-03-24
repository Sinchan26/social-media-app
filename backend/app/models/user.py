from sqlalchemy import Column, Boolean, String
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.dialects.postgresql import UUID as Uuid
from uuid import uuid4
from app.db.base import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String(255), unique=True, index=True,nullable=False)
    email = Column(String(255), unique=True, index=True,nullable=False)
    password_hash = Column(String(255),nullable=False)
    created_at = Column(DateTime,default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, default=True)