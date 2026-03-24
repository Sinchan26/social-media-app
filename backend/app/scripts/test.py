from app.db.base import Base
from app.db.engine import engine

import app.models
Base.metadata.create_all(bind=engine)