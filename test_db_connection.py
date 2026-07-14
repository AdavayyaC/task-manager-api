from app.core.config import settings
from app.db.session import SessionLocal, engine
from app.db.base import Base
from app.models.user import User

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

def test_db_connection():
    db = SessionLocal()
    try:
        test_user = User(name="Test", email="test@example.com")
        db.add(test_user)
        db.commit()
        print("✅ DB connection working!")
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()