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
 
    if not set(['name', 'surname']).issubset(list(data.keys())):
        abort(400)
    
    user = UserModel(data)
    user.create()

    return jsonify(user.serialize)

@mod_api.route('/users/<int:user_id>', methods=['PUT'])
def update(user_id):
  """
  Update user
  """
  data = request.get_json()

  user = UserModel.get_one_user(user_id)
  user.update(data)
  
  return jsonify({'user': user.serialize}), 200

@mod_api.route('/users', methods=['GET'])
def get_all():
    """
    Return all users
    """
    users = UserModel.get_all_users()
    return jsonify({'users':[user.serialize for user in users]}), 200

@mod_api.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """
    Delete the user selected by user_id
    """
    user = UserModel.get_one_user(user_id)
    if user:
        user.delete() 
        return jsonify({'success': 'User {} deleted'.format(user_id)}), 200
    else:
        return jsonify({'error': 'UserID {} not in the database'.format(user_id)}), 404

@mod_api.route('/assets', methods=['GET'])
def get_all_assets():
    """
    Return all assets
    """
    assets = AssetModel.get_all_assets()
    return jsonify({'assets':[asset.serialize for asset in assets]}), 200

@mod_api.route('/assets', methods=['POST'])
def create_asset():
    """
    Create Asset Function
    """

    data = request.get_json()

    if not set(['name', 'type', 'city', 'rooms', 'details', 'owner']).issubset(list(data.keys())):
        abort(400)
    
    asset = AssetModel(data)
    asset.create()

    return jsonify(asset.serialize)
