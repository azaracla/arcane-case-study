from flask import request, Blueprint, jsonify, abort, make_response
from app import db
from app.mod_api.models import UserModel, AssetModel

from app.mod_api.helpers.decorators import authentificate
from app.mod_api.helpers.errors import *

mod_api = Blueprint('api', __name__, url_prefix='/api')

@mod_api.route('/register', methods=['POST'])
def create_user():
    """
    Create User Function
    """

    data = request.get_json()
 
    if not set(['name', 'surname', 'password']).issubset(list(data.keys())):
        abort(400)
    
    user = UserModel(data)
    user.create()

    return make_response(jsonify(user.serialize), 201)

@mod_api.route('/account', methods=['PUT'])
@authentificate
def update_user():
    """
    Update user data
    """

    data = request.get_json()
    user_id = request.authorization.username

    user = UserModel.get_one_user(user_id)

    user.update(data)
    return make_response(jsonify({'user': user.serialize}), 200)

## Accounts administration methods

@mod_api.route('/users', methods=['GET'])
def get_all():
    """
    Return all users
    """
    users = UserModel.get_all_users()
    return make_response(jsonify({'users':[user.serialize for user in users]}), 200)

@mod_api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete the user selected by user_id
    """
    user = UserModel.get_one_user(user_id)
    if user:
        user.delete() 
        return make_response(jsonify({'success': 'User {} deleted'.format(user_id)}), 200)
    else:
        return make_response(jsonify({'error': 'UserID {} not in the database'.format(user_id)}), 404)



@mod_api.route('/assets', methods=['GET'])
def get_all_assets():
    """
    Return all assets
    """
    assets = AssetModel.get_all_assets()
    return jsonify({'assets':[asset.serialize for asset in assets]}), 200

@mod_api.route('/assets', methods=['POST'])
@authentificate
def create_asset():
    """
    Create Asset Function
    """

    data = request.get_json()
    user_id = request.authorization.username

    if not set(['name', 'type', 'city', 'rooms', 'details', 'owner']).issubset(list(data.keys())):
        abort(400)
    
    asset = AssetModel(data, user_id)
    asset.create()

    return make_response(jsonify(asset.serialize), 201)

@mod_api.route('/assets/<int:asset_id>', methods=['PUT'])
@authentificate
def update_asset(asset_id):
    """
    Update Asset Function
    """

    data = request.get_json()
    user_id = request.authorization.username

    asset = AssetModel.get_one_asset(asset_id)

    if asset:
        if user_id == asset.user_id:
            asset.update(data)
            return make_response(jsonify({'asset': asset.serialize}), 200)
        else:
            return make_response(jsonify({'error': 'You are only authorized to edit your own assets'}), 401)
    else:
        return make_response(jsonify({'error': 'AssetID {} not in the database'.format(asset_id)}), 404)

@mod_api.route('/assets/<int:asset_id>', methods=['DELETE'])
@authentificate
def delete_asset(asset_id):
    """
    Delete the asset selected by asset_id
    """
    asset = AssetModel.get_one_asset(asset_id)
    user_id = request.authorization.username

    if asset:
        if user_id == asset.user_id:
            asset.delete() 
            return make_response(jsonify({'success': 'Asset {} deleted'.format(asset_id)}), 200)
        else:
            return make_response(jsonify({'error': 'You are only authorized to delete your own assets'}), 401)

    else:
        return make_response(jsonify({'error': 'AssetID {} not in the database'.format(asset_id)}), 404)