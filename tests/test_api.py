
import pytest
from src.app import app

@pytest.fixture
def client():
    """
    This fixture provides a test client for the Flask application. It allows us to simulate requests to the API
    without needing to run the server manually.
    """
    app.config['TESTING'] = True  # Enable testing mode
    return app.test_client()  # Returns a test client

def test_get_funds(client):
    """
    Test GET /funds endpoint to ensure it retrieves all funds.
    """
    response = client.get('/funds')
    assert response.status_code == 200  # Expecting a 200 OK response
    assert isinstance(response.json, list)  # The response should be a list

def test_create_fund(client):
    """
    Test POST /funds endpoint to create a new fund.
    """
    data = {
        "name": "New Fund",
        "manager": "Jane Smith",
        "nav": 1500.0,
        "description": "A new fund for tech investments",
        "performance": 6.0
    }
    response = client.post('/funds', json=data)
    assert response.status_code == 201  # Expecting a 201 Created response
    assert response.json['name'] == data['name']  # Verify that the fund name is correct
    assert response.json['manager'] == data['manager']  # Verify manager name

def test_get_fund(client):
    """
    Test GET /funds/<id> endpoint to retrieve a specific fund by its ID.
    """
    # First, create a fund
    data = {
        "name": "Global Fund",
        "manager": "John Doe",
        "nav": 1000.0,
        "description": "A diversified fund",
        "performance": 5.5
    }
    create_response = client.post('/funds', json=data)
    fund_id = create_response.json['id']  # Get the ID of the newly created fund
    
    # Now, retrieve the created fund by its ID
    response = client.get(f'/funds/{fund_id}')
    assert response.status_code == 200  # Expecting a 200 OK response
    assert response.json['id'] == fund_id  # Verify the fund ID matches
    assert response.json['name'] == data['name']  # Verify the fund name is correct

def test_update_performance(client):
    """
    Test PUT /funds/<id>/performance endpoint to update the performance of a fund.
    """
    # Create a fund
    data = {
        "name": "Tech Fund",
        "manager": "Alice Cooper",
        "nav": 2000.0,
        "performance": 7.0
    }
    create_response = client.post('/funds', json=data)
    fund_id = create_response.json['id']  # Get the ID of the newly created fund
    
    # Update performance
    updated_data = {"performance": 8.5}
    response = client.put(f'/funds/{fund_id}/performance', json=updated_data)
    assert response.status_code == 200  # Expecting a 200 OK response
    assert response.json['performance'] == updated_data['performance']  # Verify performance is updated

def test_delete_fund(client):
    """
    Test DELETE /funds/<id> endpoint to delete a specific fund by its ID.
    """
    # Create a fund
    data = {
        "name": "Retirement Fund",
        "manager": "Bob Martin",
        "nav": 5000.0,
        "performance": 4.0
    }
    create_response = client.post('/funds', json=data)
    fund_id = create_response.json['id']  # Get the ID of the newly created fund
    
    # Delete the fund
    response = client.delete(f'/funds/{fund_id}')
    assert response.status_code == 204  # Expecting a 204 No Content response
    # Try to get the deleted fund (should return 404)
    response = client.get(f'/funds/{fund_id}')
    assert response.status_code == 404  # Fund should no longer exist
