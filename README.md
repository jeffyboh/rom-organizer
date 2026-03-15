# ROM Library

This repository contains a Python application for indexing ROM files and their corresponding images.

## Configuration

The application uses a `config.yaml` file to define the location of your ROM library and other settings.

### Setting up your ROM library path

1. Edit the `config.yaml` file in the root directory
2. Set the `rom_library_path` to the absolute path of your ROM directory
3. Example:
   ```yaml
   rom_library_path: "/home/user/Games/ROMs"
   ```

### Alternative configuration methods

You can also configure the ROM library path using:
- Environment variable: `ROM_LIBRARY_ROM_LIBRARY_PATH=/path/to/roms`
- `.env` file: Copy `.env.example` to `.env` and set `ROM_LIBRARY_ROM_LIBRARY_PATH=/path/to/roms`
- The `config.yaml` file (recommended for most users)

Configuration sources are loaded in this priority order:
1. Environment variables (highest priority)
2. `.env` file
3. `config.yaml` file
4. Default values (lowest priority)

## Installation

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application:
```bash
python -m app.main
```

## Database Setup

The application uses SQLite for data storage. The database file will be created automatically when you first run the population script.

### Populating Systems Data

The application includes a comprehensive list of gaming systems. To populate the database with system information:

```bash
python populate_systems.py
```

This will create the `systems` table and populate it with 190+ gaming systems including consoles, computers, and arcade systems.

### Database Schema

- **systems** table:
  - `system` (string, primary key): Unique system identifier (e.g., "nes", "snes")
  - `system_name` (string): Human-readable system name (e.g., "Nintendo Entertainment System")

### Querying Systems

Use the query script to search and find systems:

```bash
# List all systems
python query_systems.py list

# Find a specific system by ID
python query_systems.py find nes

# Search systems by name
python query_systems.py search "PlayStation"
```

## API

The ROM Library includes a FastAPI-based REST API that follows OpenAPI specifications.

### Running the API

Start the API server:
```bash
python run_api.py
```

The API will be available at:
- **Base URL**: http://localhost:8000
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### API Endpoints

#### GET /
Returns basic API information.

**Response:**
```json
{
  "message": "ROM Library API",
  "version": "1.0.0",
  "docs": "/docs",
  "redoc": "/redoc"
}
```

#### GET /systems
Returns all gaming systems.

**Response:** Array of system objects
```json
[
  {
    "system": "nes",
    "system_name": "Nintendo Entertainment System"
  },
  {
    "system": "snes",
    "system_name": "Nintendo SNES (Super Nintendo)"
  }
]
```

#### GET /systems/search
Search systems by name (case-insensitive).

**Parameters:**
- `q` (required): Search query (minimum 2 characters)
- `limit` (optional): Maximum number of results (default: 50)

**Example:** `/systems/search?q=Nintendo&limit=10`

**Response:** Array of matching system objects

#### GET /systems/{system_id}
Get a specific system by its ID.

**Parameters:**
- `system_id`: The system identifier (e.g., "nes", "snes")

**Response:** Single system object
```json
{
  "system": "nes",
  "system_name": "Nintendo Entertainment System"
}
```

**Error Response (404):**
```json
{
  "detail": "System not found"
}
```

### Error Handling

The API uses standard HTTP status codes:
- `200`: Success
- `400`: Bad Request (e.g., search query too short)
- `404`: Not Found (e.g., system doesn't exist)
- `500`: Internal Server Error

### OpenAPI Specification

The API automatically generates OpenAPI 3.0 specifications accessible at `/docs` (Swagger UI) and `/redoc` (ReDoc).

## Testing

The project includes a comprehensive test suite using pytest for Test-Driven Development (TDD).

### Running Tests

**Run all tests:**
```bash
python run_tests.py
```

**Run tests with pytest directly:**
```bash
pytest tests/ -v
```

**Run tests with coverage:**
```bash
pytest tests/ --cov=app --cov-report=html
```

**Run specific test file:**
```bash
pytest tests/test_systems.py -v
```

**Run specific test:**
```bash
pytest tests/test_systems.py::test_get_all_systems -v
```

### Test Structure

```
tests/
├── __init__.py
├── conftest.py          # Shared fixtures and configuration
├── test_root.py         # Tests for root API endpoint
└── test_systems.py      # Tests for systems API endpoints
```

### Test Fixtures

- **`test_engine`**: Creates an in-memory SQLite database for testing
- **`test_db`**: Provides a database session for each test function
- **`client`**: FastAPI TestClient for making API requests
- **`sample_systems`**: Pre-populated test data with sample gaming systems

### Writing New Tests

When adding new API endpoints, follow this TDD pattern:

1. **Write the test first** (Red)
2. **Run the test** to see it fail
3. **Implement the code** to make the test pass (Green)
4. **Refactor** if needed (Refactor)

Example test structure:
```python
def test_new_endpoint(client):
    """Test description."""
    response = client.get("/new-endpoint")
    assert response.status_code == 200
    # Add more assertions...
```

### Test Coverage

The test suite covers:
- ✅ API endpoint responses
- ✅ Error handling (400, 404 errors)
- ✅ Database operations
- ✅ Input validation
- ✅ Search functionality
- ✅ Case-insensitive operations

## Usage

Run the application:
```bash
python -m app.main
```

This will display your current configuration and show example systems from the database.
