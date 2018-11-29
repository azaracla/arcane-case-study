from flask import Flask, make_response, jsonify
from flask_sqlalchemy import SQLAlchemy

# Define the application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

from app.mod_api.controllers import mod_api as api_module

app.register_blueprint(api_module)

db.create_all()

@app.route('/', methods=['GET'])
def index():
    return 'It works'