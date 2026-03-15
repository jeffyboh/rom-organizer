"""Tests for the root API endpoint."""

def test_root_endpoint(client):
    """Test the root endpoint returns correct information."""
    response = client.get("/")
    assert response.status_code == 200

    data = response.json()
    assert data["message"] == "ROM Library API"
    assert data["version"] == "1.0.0"
    assert "docs" in data
    assert "redoc" in data