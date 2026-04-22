from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    
    data = response.json()
    assert data["message1"] == "Welcome to the DevOps world"
    assert data["message2"] == "Happy to learn coding"
    assert data["message3"] == "Excellent decision"