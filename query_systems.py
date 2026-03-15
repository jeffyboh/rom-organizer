#!/usr/bin/env python3
"""
Utility script to query systems from the database.
"""

import sys
from pathlib import Path

# Add the app directory to the Python path
sys.path.insert(0, str(Path(__file__).parent / "app"))

from app.core.database import get_db
from app.models.system import SystemConfig


def list_all_systems():
    """List all systems in the database."""
    db = get_db()
    try:
        systems = db.query(SystemConfig).order_by(SystemConfig.system).all()
        print(f"Total systems: {len(systems)}\n")
        for system in systems:
            print(f"{system.system}: {system.system_name}")
    finally:
        db.close()


def find_system(system_id: str):
    """Find a specific system by ID."""
    db = get_db()
    try:
        system = db.query(SystemConfig).filter(SystemConfig.system == system_id).first()
        if system:
            print(f"System: {system.system}")
            print(f"Name: {system.system_name}")
        else:
            print(f"System '{system_id}' not found.")
    finally:
        db.close()


def search_systems(search_term: str):
    """Search systems by name."""
    db = get_db()
    try:
        systems = db.query(SystemConfig).filter(
            SystemConfig.system_name.ilike(f"%{search_term}%")
        ).all()

        if systems:
            print(f"Found {len(systems)} systems matching '{search_term}':")
            for system in systems:
                print(f"  {system.system}: {system.system_name}")
        else:
            print(f"No systems found matching '{search_term}'.")
    finally:
        db.close()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python query_systems.py list                    # List all systems")
        print("  python query_systems.py find <system_id>        # Find specific system")
        print("  python query_systems.py search <search_term>    # Search by name")
        sys.exit(1)

    command = sys.argv[1]

    if command == "list":
        list_all_systems()
    elif command == "find" and len(sys.argv) == 3:
        find_system(sys.argv[2])
    elif command == "search" and len(sys.argv) == 3:
        search_systems(sys.argv[2])
    else:
        print("Invalid command or arguments.")
        sys.exit(1)