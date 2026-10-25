import logging
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.app.config import settings
from backend.app.database.db import init_db
from backend.app.api.routes import router as api_router

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)
logger = logging.getLogger("citysoul")

app = FastAPI(
    title=settings.PROJECT_NAME,
    description="CitySoul — Cultural Intelligence Agent that discovers where your taste belongs.",
    version=settings.VERSION
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins for local hackathon demo and testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Startup
@app.on_event("startup")
def on_startup():
    logger.info("Initializing CitySoul SQLite database...")
    init_db()
    logger.info(f"CitySoul ready! Qloo live mode: {bool(settings.QLOO_API_KEY)}")

# Include API Router
app.include_router(api_router, prefix=settings.API_PREFIX)

@app.get("/")
def root():
    return {
        "message": "Welcome to CitySoul — Find the city that feels like you.",
        "documentation": "/docs",
        "api_prefix": settings.API_PREFIX,
        "hackathon": "Qloo Agentic Hackathon"
    }
