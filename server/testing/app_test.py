import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'<h1>Python Operations with Flask Routing and Views</h1>' in response.data

def test_print_text(client):
    response = client.get('/print/hello')
    assert response.status_code == 200
    assert b'Printed: hello' in response.data

def test_count_range_10(client):
    response = client.get('/count/10')
    assert response.status_code == 200
    assert b'0\n1\n2\n3\n4\n5\n6\n7\n8\n9' in response.data

def test_math_add(client):
    response = client.get('/math/5%2B5')
    assert response.status_code == 200
    assert b'10.0' in response.data

def test_math_subtract(client):
    response = client.get('/math/5-5')
    assert response.status_code == 200
    assert b'0.0' in response.data

def test_math_multiply(client):
    response = client.get('/math/5%2A5')
    assert response.status_code == 200
    assert b'25.0' in response.data

def test_math_divide(client):
    response = client.get('/math/5div5')
    assert response.status_code == 200
    assert b'1.0' in response.data

def test_math_modulo(client):
    response = client.get('/math/5%255')
    assert response.status_code == 200
    assert b'0.0' in response.data
