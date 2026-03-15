#!/usr/bin/env python3
"""
ROM Library Application
"""

from app.core.config import settings
from app.core.database import get_db
from app.models.system import System


def main():
    """Main application entry point."""
    print("ROM Library Application")
    print(f"ROM Library Path: {settings.rom_library_path}")
    print(f"ROM Library Path exists: {settings.rom_library_path.exists()}")
    print(f"ROM Media Path: {settings.rom_library_media_path}")
    print(f"ROM Media Path exists: {settings.rom_library_media_path.exists()}")
    print(f"Log Level: {settings.log_level}")
    print(f"Database URL: {settings.database_url}")

    # Test database connection and show some systems
    db = get_db()
    try:
        system_count = db.query(System).count()
        print(f"Total systems in database: {system_count}")

        # Show first 5 systems as examples
        systems = db.query(System).limit(5).all()
        print("\nExample systems:")
        for system in systems:
            print(f"  {system.system}: {system.system_name}")

    except Exception as e:
        print(f"Database error: {e}")
    finally:
        db.close()

    # TODO: Add your ROM indexing logic here
    # For example:
    # indexer = ROMIndexer(settings.rom_library_path)
    # indexer.scan_and_index()


if __name__ == "__main__":
    main()