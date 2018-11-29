# Handle errors to return restful response

from app import app
from flask import make_response, jsonify

@app.errorhandler(400)
def unauthorized(error):
    return make_response(jsonify({'error': 'Bad request'}), 401)

@app.errorhandler(401)
def unauthorized(error):
    return make_response(jsonify({'error': 'Unauthorized'}), 401)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)
