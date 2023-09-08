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
            return compose_response(data=sheet)
    except BaseException as err:
        msg = f'exception occured in fetch_baalace API. {err}'
        print(msg)
        return compose_response(data=msg,status='failed')
    
@balances_bp.route('/summit_sheet',methods=['POST'])
def summit_sheet():
    try:
        request_data = request.get_json()
        sheet = request_data.get('sheet')
        loanamount = request_data.get('loanamount')
        account = Accounting()
        approved_loan,preAssesment = account.summarise_outcome(sheet=sheet,requested_loan=int(loanamount))
        response = {
            'ApprovedLoan' : approved_loan,
            "preAssesment" : preAssesment
            
        }
        if approved_loan:
            return compose_response(data=response)
    except BaseException as err:
        msg = f'exception occured in summit_sheet API. {err}'
        print(msg)
        return compose_response(data=msg,status='failed')