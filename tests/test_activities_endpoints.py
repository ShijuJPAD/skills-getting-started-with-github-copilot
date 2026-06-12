from src import app as app_module


def test_get_activities_returns_all_activities(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()

    assert isinstance(payload, dict)
    assert len(payload) == len(app_module.activities)
    assert "Chess Club" in payload
    assert "Math Olympiad" in payload


def test_get_activities_returns_activity_details_and_participants(client):
    response = client.get("/activities")

    assert response.status_code == 200
    payload = response.json()
    chess_club = payload["Chess Club"]

    assert chess_club["description"] == "Learn strategies and compete in chess tournaments"
    assert chess_club["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert chess_club["max_participants"] == 12
    assert chess_club["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]