from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def ensure_user_exists(username: str, password: str):
    # Try logging in
    login = client.post("/auth/login", json={"username": username, "password": password})
    if login.status_code == 200:
        return login.json()["token"]
    
    # If login failed, register
    register = client.post("/auth/register", json={"username": username, "password": password})
    assert register.status_code == 200 or register.status_code == 201

    # Login again to get token
    login = client.post("/auth/login", json={"username": username, "password": password})
    assert login.status_code == 200
    return login.json()["token"]


def test_create_article():

    # First, register a user (if not already registered)
    token = ensure_user_exists("testuser21", "pass21")

    print("DEBUG token:", token)
    response = client.post(
        "/articles/",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Test Title", "content": "Test content"}
    )

    print("DEBUG response:", response.status_code, response.json())
    assert response.status_code == 200
