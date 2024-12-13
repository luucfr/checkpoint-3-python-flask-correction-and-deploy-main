# FILE: test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Inventaire des Serveurs' in response.data

def test_add_server(client):
    response = client.post('/', data={'name': 'Server1', 'ip': '192.168.1.1'})
    assert response.status_code == 302  # Redirect after POST
    response = client.get('/')
    assert b'Server1' in response.data
    assert b'192.168.1.1' in response.data