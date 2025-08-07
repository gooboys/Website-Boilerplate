from fastapi import FastAPI
from backend.api import health, users, whatever_else

app = FastAPI()

# Include routes
app.include_router(health.router)
app.include_router(users.router)
app.include_router(whatever_else.router)