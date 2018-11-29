from flask import request, Blueprint, jsonify, abort

from app import db

from app.mod_api.models import UserModel, AssetModel

mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route('/users', methods=['POST'])
def create_user():
    """
    Create User Function
    """

    data = request.get_json()

    if not 'name' in data or not 'surname' in data:
        abort(400)
    
    user = UserModel(data)
    user.create()

    return jsonify(user.serialize)
