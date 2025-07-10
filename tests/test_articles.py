from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_article():
    login = client.post("/auth/login", json={"username": "testuser2", "password": "pass2"})
    token = login.json()["token"]
    print("DEBUG token:", token)
    response = client.post(
        "/articles/",
        headers={"Authorization": f"Bearer {token}"},
        json={"title": "Test Title", "content": "Test content"}
    )
    
    print("DEBUG response:", response.status_code, response.json())
    assert response.status_code == 200
