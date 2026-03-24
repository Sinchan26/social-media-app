from datetime import datetime

from sqlalchemy import Column, DateTime, UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID as Uuid
from sqlalchemy import ForeignKey
from uuid import uuid4
from app.db.base import Base

class Follow(Base):
    __tablename__ = "follows"
    id = Column(Uuid(as_uuid=True), primary_key=True, default=uuid4)
    follower_id = Column(Uuid(as_uuid=True), ForeignKey("users.id"), nullable=False)
    following_id = Column(Uuid(as_uuid=True), ForeignKey("users.id"), nullable=False)
    created_at = Column(DateTime, default=datetime.now,index=True)
    __table_args__=(
        UniqueConstraint('follower_id', 'following_id', name='unique_follow'),
    )