from fastapi import FastAPI, HTTPException, Query, Depends
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional, Generator
from sqlalchemy.orm import Session
from pydantic import BaseModel, ConfigDict
from datetime import datetime

from app.core.database import SessionLocal
from app.models.game import Game
from app.models.system import System

# Create FastAPI app
app = FastAPI(
    title="ROM Library API",
    description="API for managing ROM library systems and games",
    version="1.0.0",
    docs_url="/docs",  # Swagger UI
    redoc_url="/redoc"  # ReDoc
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for API responses
class SystemResponse(BaseModel):
    system: str
    system_name: str

    model_config = ConfigDict(from_attributes=True)

class GameResponse(BaseModel):
    game_id: int
    system: str
    game_name: str
    game_path: str
    date_added: Optional[datetime]

    model_config = ConfigDict(from_attributes=True)

# Dependency to get database session
def get_db() -> Generator[Session, None, None]:
    """Database dependency for FastAPI."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def root():
    """Root endpoint with API information."""
    return {
        "message": "ROM Library API",
        "version": "1.0.0",
        "docs": "/docs",
        "redoc": "/redoc"
    }


@app.get("/systems", response_model=List[SystemResponse])
async def get_all_systems(db: Session = Depends(get_db)):
    """
    Get all gaming systems.

    Returns a list of all systems with their IDs and names.
    """
    systems = db.query(System).order_by(System.system).all()
    return systems


@app.get("/systems/search", response_model=List[SystemResponse])
async def search_systems(
    q: str = Query(..., description="Search query for system name"),
    limit: Optional[int] = Query(50, description="Maximum number of results to return"),
    db: Session = Depends(get_db)
):
    """
    Search systems by name.

    Performs a case-insensitive search on system names.
    """
    if not q or len(q.strip()) < 2:
        raise HTTPException(
            status_code=400,
            detail="Search query must be at least 2 characters long"
        )

    systems = db.query(System).filter(
        System.system_name.ilike(f"%{q}%")
    ).limit(limit).all()

    return systems


@app.get("/systems/{system_id}", response_model=SystemResponse)
async def get_system(system_id: str, db: Session = Depends(get_db)):
    """
    Get a specific system by its ID.

    Returns detailed information about a single system.
    """
    system = db.query(System).filter(System.system == system_id).first()
    if not system:
        raise HTTPException(status_code=404, detail="System not found")
    return system

# TODO: Move game endpoints to a separate router for better organization

# Games endpoints
@app.get("/games", response_model=List[GameResponse])
async def get_all_games(db: Session = Depends(get_db)):
    """
    Get all gaming games.

    Returns a list of all games.
    """
    games = db.query(Game).all()
    return games


