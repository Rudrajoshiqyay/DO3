import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_hello(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Hello, World!" in response.data

def test_square(client):
    response = client.get('/square/5')
    assert response.status_code == 200
    assert b"25" in response.data

def test_factorial(client):
    response = client.get('/factorial/5')
    assert response.status_code == 200
    assert b"120" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data
