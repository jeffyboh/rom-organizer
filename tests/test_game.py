"""Tests for the systems API endpoints."""

import pytest


def test_get_all_games_empty(client):
    """Test getting all games when database is empty."""
    response = client.get("/games")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 0

def test_get_all_games_with_data(client, sample_games):
    """Test getting all games when database has data."""
    response = client.get("/games")
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) == 4
    game_names = [game["game_name"] for game in data]
    assert "Super Mario Bros." in game_names
    assert "The Legend of Zelda" in game_names
    assert "Super Mario World" in game_names
    assert "Sonic the Hedgehog" in game_names
