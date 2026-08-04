import json
from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert data["message"] == "Hello from GitHub Actions demo app!"

def test_add():
    client = app.test_client()
    response = client.get("/add/2/3")
    assert response.status_code == 200
    data = json.loads(response.data.decode("utf-8"))
    assert data["result"] == 5
