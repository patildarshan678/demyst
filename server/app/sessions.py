from flask import Blueprint,jsonify, request
import jwt
from flask_app import flask_app
import datetime

sessions_bp  = Blueprint('sessions',__name__,url_prefix='/session')


@sessions_bp.route('/start',methods =['POST'])
def start_session():
    try:
        payload = {
        'user_id': 1,
        'username': 'example_user',
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # Token expiration time
    }
        print(flask_app.config['SECRET_KEY'])
        token = jwt.encode(payload, flask_app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})


    except BaseException as err:
        msg = f"Exception occured in start_session API.{err}"
        print(msg)
        return msg