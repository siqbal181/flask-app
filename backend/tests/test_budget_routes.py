import pytest
from src.main import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_budgets(client):
    response = client.get('/get_budgets')
    assert response.status_code == 200
    assert b'This is a placeholder response for get_budgets' in response.data

def test_save_budget(client):
    response = client.post('/save_budget')
    assert response.status_code == 200
    assert b'This is a placeholder response for save_budget' in response.data
