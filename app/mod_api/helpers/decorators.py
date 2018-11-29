from functools import wraps
from flask import request, make_response, abort
from passlib.hash import sha256_crypt

from app.mod_api.models import UserModel

def validate_user(user_id, password):
    user = UserModel.get_one_user(user_id)
    if user:
        return sha256_crypt.verify(password, user.password)
    else:
        abort(401)
        
def authentificate(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not validate_user(auth.username, auth.password):
            abort(401)
        return func(*args, **kwargs)
    return decorated