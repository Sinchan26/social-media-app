from sqlalchemy import create_engine
import os
from dotenv import load_dotenv
from urllib.parse import quote

load_dotenv()

# Read values from .env
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Build database URL dynamically with URL-encoded password
# Use explicit psycopg2 dialect and disable Unix socket fallback
DATABASE_URL = f"postgresql+psycopg2://{DB_USER}:{quote(DB_PASSWORD, safe='')}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create engine (this is the core connection to DB)
try:
    engine = create_engine(DATABASE_URL, echo=True)
    print(f"Database URL: {DATABASE_URL}")  # Debug print to verify URL
    print("Database engine created successfully.")  
except Exception as e:
    print(f"Error creating database engine: {e}")