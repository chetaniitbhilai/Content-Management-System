from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_register_and_login():
    # register = client.post("/auth/register", json={"username": "testuser2", "password": "pass2"})
    # assert register.status_code == 200

    login = client.post("/auth/login", json={"username": "testuser21", "password": "pass21"})
    assert login.status_code == 200
    assert "token" in login.json()
