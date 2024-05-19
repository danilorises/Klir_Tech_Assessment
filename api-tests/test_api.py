import pytest
import requests

BASE_URL = "http://localhost:3001"

def test_ok():
    response = requests.post(BASE_URL, json={"name": "Master Yoda"})
    assert response.status_code == 200, "Expected 200 status code for successful request"

def test_missing_contact_info():
    response = requests.post(BASE_URL, json={"name": "Test User"})
    data = response.json()
    customers = data.get("customers", [])
    for customer in customers:
        if "contactInfo" not in customer or not customer["contactInfo"]:
            assert "contactInfo" not in customer, "Expected 'contactInfo' to be missing if no contact information is available"

def test_size_calculation():
    response = requests.post(BASE_URL, json={"name": "Master Yoda"})
    data = response.json()
    customers = data.get("customers", [])
    for customer in customers:
        num_employees = customer.get("employees", 0)
        if num_employees <= 2500:
            expected_size = "Small"
        elif 2501 <= num_employees <= 5000:
            expected_size = "Medium"
        else:
            expected_size = "Big"
        assert customer.get("size") == expected_size, f"Expected size {expected_size} for {num_employees} employees"

if __name__ == "__main__":
    pytest.main()