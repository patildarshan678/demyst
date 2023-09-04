from flask import Flask
from flask_cors import CORS
flask_app = Flask(__name__)
CORS(flask_app)

flask_app.config.from_object ( 'config.Developement')