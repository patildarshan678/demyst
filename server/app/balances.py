from flask import Blueprint,jsonify, request
from flask_app import flask_app
from utility import compose_response
from accounting.accounting import Accounting
balances_bp = Blueprint('balances',__name__,url_prefix='/balances')

@balances_bp.route('/fetch_balance_sheet',methods=['GET'])
def fetch_balance():
    try:
        account = Accounting()
        sheet = account.fetch_balance_sheet()
        if sheet:
            compose_response(data=sheet)
    except BaseException as err:
        msg = f'exception occured in fetch_baalace API. {err}'
        print(msg)
        return compose_response(data=msg,status='failed')