from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_root():
    """Test the root endpoint returns correct status"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["message"] == "Sprint Review AI Backend"


def test_health():
    """Test the health endpoint returns healthy status"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"


def test_analyze_missing_fields():
    """Test that /analyze rejects requests with missing fields"""
    response = client.post("/analyze", json={})
    assert response.status_code == 422  # Validation error
    