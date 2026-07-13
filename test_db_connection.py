from app.db.session import SessionLocal
from app.models.user import User

def test_db_connection():
    db = SessionLocal()
    try:
        # Create a test user
        test_user = User(name="Test", email="test@example.com")
        db.add(test_user)
        db.commit()
        print("✅ DB connection working!")
    finally:
        db.close()

if __name__ == "__main__":
    test_db_connection()