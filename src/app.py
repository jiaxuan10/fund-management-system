
from flask import Flask, jsonify
from src.routes import bp

app = Flask(__name__)
app.register_blueprint(bp)

# Handle 404 errors (Resource Not Found)
@app.errorhandler(404)
def not_found(error):
    """
    Handle 404 errors when the requested resource is not found.
    This can occur if an endpoint is misspelled or if a requested fund ID doesn't exist.
    """
    return jsonify({"error": "Resource not found"}), 404

# Handle 400 errors (Bad Request - Invalid Input)
@app.errorhandler(400)
def bad_request(error):
    """
    Handle 400 errors when the request payload is invalid or missing required fields.
    This can occur if the input is not in the correct format or lacks required parameters.
    """
    return jsonify({"error": "Bad request - Invalid input"}), 400

# Handle 405 errors (Method Not Allowed)
@app.errorhandler(405)
def method_not_allowed(error):
    """
    Handle 405 errors when an HTTP method is not allowed for a specific endpoint.
    For example, sending a POST request to a GET-only endpoint.
    """
    return jsonify({"error": "Method Not Allowed"}), 405

# Handle 500 errors (Internal Server Error)
@app.errorhandler(500)
def server_error(error):
    """
    Handle 500 errors which are unexpected server-side errors.
    This could occur due to issues like database connectivity or coding bugs.
    """
    return jsonify({"error": "Internal Server Error"}), 500

# Custom Error Handling for Missing Data in PUT/POST Requests
@app.before_request
def validate_input():
    """
    This function validates incoming requests to ensure all required fields are present.
    If a required field is missing, it will return a 400 error.
    """
    if request.method == "POST" or request.method == "PUT":
        data = request.json
        required_fields = ['name', 'manager', 'nav']  # These fields must be present
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
