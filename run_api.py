#!/usr/bin/env python3
"""
Script to run the FastAPI server for the ROM Library API.
"""

import uvicorn
from app.core.config import settings


def main():
    """Run the FastAPI server."""
    print("Starting ROM Library API server...")
    print(f"API will be available at: http://localhost:8000")
    print(f"Swagger UI: http://localhost:8000/docs")
    print(f"ReDoc: http://localhost:8000/redoc")

    uvicorn.run(
        "app.api.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True,  # Enable auto-reload during development
        log_level=settings.log_level.lower()
    )


if __name__ == "__main__":
    main()