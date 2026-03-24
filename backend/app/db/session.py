from sqlalchemy.orm import sessionmaker
from app.db.engine import engine

Session=sessionmaker(autoflush=False, autocommit=False, bind=engine)

def get_db():
    db=Session()
    try:
        yield db
    finally:
        db.close()