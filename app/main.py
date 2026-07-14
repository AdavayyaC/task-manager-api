from fastapi import FastAPI
from app.api.users import router as users_router

# Create the FastAPI app instance (THIS WAS MISSING!)
app = FastAPI(title="Task Manager API", version="1.0.0")

# Now include your router
app.include_router(users_router, prefix="/api/v1", tags=["users"])