import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient

from app.api.main import app, get_db
from app.models.system import System, Base


# Test database URL
TEST_DATABASE_URL = "sqlite:///./test.db"


@pytest.fixture(scope="session")
def test_engine():
    """Create a test database engine."""
    engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
    Base.metadata.create_all(bind=engine)
    yield engine
    Base.metadata.drop_all(bind=engine)
    engine.dispose()


@pytest.fixture(scope="function")
def test_db(test_engine):
    """Create a test database session."""
    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=test_engine)
    db = TestingSessionLocal()
    try:
        # Clear existing data
        db.query(System).delete()
        db.commit()
        yield db
    finally:
        db.rollback()
        db.close()


@pytest.fixture(scope="function")
def client(test_db):
    """Create a test client for the FastAPI app."""
    # Override the database dependency
    def override_get_db():
        try:
            yield test_db
        finally:
            test_db.close()

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client
    app.dependency_overrides.clear()


@pytest.fixture(scope="function")
def sample_systems(test_db):
    """Create sample systems for testing."""
    systems_data = [
        System(system="nes", system_name="Nintendo Entertainment System"),
        System(system="snes", system_name="Super Nintendo Entertainment System"),
        System(system="genesis", system_name="Sega Genesis"),
        System(system="ps1", system_name="Sony PlayStation"),
    ]

    for system in systems_data:
        test_db.add(system)
    test_db.commit()

    return systems_data