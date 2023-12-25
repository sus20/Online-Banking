import json
from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

# Add a counter to generate unique account numbers
account_number_counter = 1


def test_ping():
    response = client.get("/ping")
    assert response.status_code == 200
    assert response.json() == {"status": "active"}


@pytest.fixture
def generate_unique_account_number():
    global account_number_counter
    account_number_counter += 1
    return account_number_counter


def test_create_account(generate_unique_account_number):
    # Test creating an account with a unique account number
    data = {
        "firstName": "John",
        "lastName": "Doe",
        "accountNumber": generate_unique_account_number,
    }
    response = client.post("/accounts", json=data)
    assert response.status_code == 200


def test_create_duplicate_account():
    # Test attempting to create an account with a duplicate accountNumber
    data = {"firstName": "Jane", "lastName": "Doe", "accountNumber": 123}
    response = client.post("/accounts", json=data)
    assert response.status_code == 400
    assert "AccountNumber already in use" in response.json()["detail"]
