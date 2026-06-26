"""
[[main.py
Entry point for the RTM FastAPI backend application.]]
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database.db import Base, engine
from app.routers import dashboard, equipment, charts

# Create all tables automatically on startup if they don't already exist
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="RTM Dashboard API",
    description="Real Time Monitoring API for Aquila Digital Energy Solutions",
    version="1.0.0"
)

# Allow the Angular dev server to call this backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dashboard.router, tags=["Dashboard"])
app.include_router(equipment.router, tags=["Equipment"])


@app.get("/")
def root():
    """Health check endpoint."""
    return {"message": "RTM API is running. Visit /docs for Swagger UI."}
