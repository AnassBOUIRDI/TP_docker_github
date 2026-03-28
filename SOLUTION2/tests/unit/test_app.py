import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_hello_route(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {"message": "Hello CI"}

def test_health_route(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.get_json()
    assert data == {"status": "ok"}

def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.is_json
    data = response.get_json()
    assert "status" in data
    assert data["status"] == "ok"

