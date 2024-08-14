import simpleapi  # Importing the simpleapi library
import json

BASE_URL = 'http://127.0.0.1:5000'

def test_login_success():
    response = simpleapi.post(f'{BASE_URL}/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    response_data = response.json()
    assert 'userId' in response_data, "Response should contain 'userId'"
    print('Login success test passed:', response_data)

def test_login_invalid_credentials():
    response = simpleapi.post(f'{BASE_URL}/login', json={'username': 'testuser', 'password': 'wrongpassword'})
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    response_data = response.json()
    assert 'error' in response_data, "Response should contain 'error'"
    print('Login invalid credentials test passed:', response_data)

def test_login_missing_credentials():
    response = simpleapi.post(f'{BASE_URL}/login', json={})
    assert response.status_code == 400, f"Expected 400, got {response.status_code}"
    response_data = response.json()
    assert 'error' in response_data, "Response should contain 'error'"
    print('Login missing credentials test passed:', response_data)

def test_logout_success():
    # First, login to get a session or token
    login_response = simpleapi.post(f'{BASE_URL}/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert login_response.status_code == 200, f"Expected 200, got {login_response.status_code}"
    login_data = login_response.json()
    token = login_data.get('userId')  # Assuming userId is used as token for simplicity
    
    # Perform logout
    logout_response = simpleapi.post(f'{BASE_URL}/logout', headers={'Authorization': f'Bearer {token}'})
    assert logout_response.status_code == 200, f"Expected 200, got {logout_response.status_code}"
    print('Logout success test passed:', logout_response.json())

def test_logout_no_auth():
    response = simpleapi.post(f'{BASE_URL}/logout')
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    response_data = response.json()
    assert 'error' in response_data, "Response should contain 'error'"
    print('Logout no auth test passed:', response_data)

def test_get_user_details_success():
    # First, login to get a session or token
    login_response = simpleapi.post(f'{BASE_URL}/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert login_response.status_code == 200, f"Expected 200, got {login_response.status_code}"
    login_data = login_response.json()
    token = login_data.get('userId')  # Assuming userId is used as token for simplicity
    
    # Fetch user details
    user_id = '12345'  # Should match the ID used in the server setup
    user_response = simpleapi.get(f'{BASE_URL}/user/{user_id}', headers={'Authorization': f'Bearer {token}'})
    assert user_response.status_code == 200, f"Expected 200, got {user_response.status_code}"
    user_data = user_response.json()
    assert user_data['username'] == 'testuser', "User details do not match"
    print('Get user details success test passed:', user_data)

def test_get_user_details_unauthorized():
    # Fetch user details without authentication
    user_id = '12345'
    user_response = simpleapi.get(f'{BASE_URL}/user/{user_id}')
    assert user_response.status_code == 401, f"Expected 401, got {user_response.status_code}"
    response_data = user_response.json()
    assert 'error' in response_data, "Response should contain 'error'"
    print('Get user details unauthorized test passed:', response_data)

def test_get_user_details_not_found():
    # First, login to get a session or token
    login_response = simpleapi.post(f'{BASE_URL}/login', json={'username': 'testuser', 'password': 'testpassword'})
    assert login_response.status_code == 200, f"Expected 200, got {login_response.status_code}"
    login_data = login_response.json()
    token = login_data.get('userId')  # Assuming userId is used as token for simplicity
    
    # Fetch user details with an invalid user ID
    user_id = 'invalid_id'
    user_response = simpleapi.get(f'{BASE_URL}/user/{user_id}', headers={'Authorization': f'Bearer {token}'})
    assert user_response.status_code == 404, f"Expected 404, got {user_response.status_code}"
    response_data = user_response.json()
    assert 'error' in response_data, "Response should contain 'error'"
    print('Get user details not found test passed:', response_data)

if __name__ == '__main__':
    test_login_success()
    test_login_invalid_credentials()
    test_login_missing_credentials()
    test_logout_success()
    test_logout_no_auth()
    test_get_user_details_success()
    test_get_user_details_unauthorized()
    test_get_user_details_not_found()
