from flask import Flask, jsonify, request

# Initialize the Flask application
app = Flask(__name__)

# In-memory data store for users
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"},
]
next_user_id = 3

# --- API Endpoints ---

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    """Returns a list of all users."""
    return jsonify(users)

# GET a single user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Returns a single user if found, otherwise returns a 404 error."""
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

# POST a new user
@app.route('/users', methods=['POST'])
def create_user():
    """Creates a new user."""
    global next_user_id
    if not request.json or not 'name' in request.json or not 'email' in request.json:
        return jsonify({"error": "Missing name or email in request body"}), 400
    
    new_user = {
        'id': next_user_id,
        'name': request.json['name'],
        'email': request.json['email']
    }
    users.append(new_user)
    next_user_id += 1
    return jsonify(new_user), 201

# PUT (update) an existing user
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Updates an existing user."""
    user = next((user for user in users if user['id'] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    if 'name' in request.json:
        user['name'] = request.json['name']
    if 'email' in request.json:
        user['email'] = request.json['email']
        
    return jsonify(user)

# DELETE a user
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Deletes a user."""
    global users
    user_to_delete = next((user for user in users if user['id'] == user_id), None)
    if not user_to_delete:
        return jsonify({"error": "User not found"}), 404

    users = [user for user in users if user['id'] != user_id]
    return jsonify({"result": f"User with ID {user_id} deleted successfully"})

# --- Main execution ---
if __name__ == '__main__':
    # Runs the app on port 5000 and makes it accessible from any IP address on the network
    app.run(host='0.0.0.0', port=5000, debug=True)

