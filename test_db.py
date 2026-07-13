from app.db.session import SessionLocal

db = SessionLocal()
print("DB Session created!")
db.close()
