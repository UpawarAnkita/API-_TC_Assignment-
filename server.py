from flask import Flask, request, jsonify, session
from flask_session import Session
import uuid

app = Flask(__name__)

# Secret key for session management
app.config['SECRET_KEY'] = 'your_secret_key'  # Change this to a real secret key
app.config['SESSION_TYPE'] = 'filesystem'  # Store session data in the filesystem

# Initialize Flask-Session
Session(app)

# In-memory storage for users (for demo purposes)
users = {
    'testuser': 'testpassword'  # username: password
}

# Dummy data for user details
user_details = {
    'testuser': {
        'userId': '12345',
        'username': 'testuser',
        'email': 'testuser@example.com'
    }
}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'error': 'Missing credentials'}), 400

    if username in users and users[username] == password:
        # Create a token (for simplicity, using userId as token)
        token = user_details[username]['userId']
        return jsonify({'userId': token}), 200

    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    # Clear session
    if 'Authorization' in request.headers:
        # Simulate logout by clearing session
        session.pop('username', None)
        return jsonify({'message': 'Logged out successfully'}), 200

    return jsonify({'error': 'Unauthorized'}), 401

@app.route('/user/<user_id>', methods=['GET'])
def get_user_details(user_id):
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'Unauthorized'}), 401

    # Find the username by userId (token)
    username = next((user for user, details in user_details.items() if details['userId'] == user_id), None)
    
    if username and username in user_details:
        return jsonify(user_details[username]), 200

    return jsonify({'error': 'User not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)