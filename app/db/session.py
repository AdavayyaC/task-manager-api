from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

engine = create_engine(
    settings.DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

# ✅ ADD THIS FUNCTION (required for FastAPI dependency injection)
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()