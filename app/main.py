from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import profile, applications, filters, agents
from app.db import Base, engine
import os

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="BountyHunter API",
    description="Agentic Career Application Tracker & Automator",
    version="0.1.0"
)

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files for evidence capture
app.mount("/static", StaticFiles(directory="static"), name="static")

# Include routers
app.include_router(profile.router)
app.include_router(applications.router)
app.include_router(filters.router)
app.include_router(agents.router)


# Mount the frontend as the root. This must come AFTER all API routers:
# a mount at "/" matches every path, so anything registered after it is unreachable.
app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
