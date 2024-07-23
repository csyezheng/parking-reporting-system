from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from pydantic_settings import BaseSettings

# Load configuration from environment variables or a .env file
class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"  # Default to SQLite

    class Config:
        env_file = ".env"

settings = Settings()

# Create the SQLAlchemy engine
engine = create_engine(settings.database_url, echo=True)

# Create a configured "Session" class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a scoped session to handle thread safety
db_session = scoped_session(SessionLocal)

# Create a base class for our models
Base: DeclarativeMeta = declarative_base()

# Dependency for FastAPI to get the database session
def get_db():
    db = db_session()
    try:
        yield db
    finally:
        db.close()
