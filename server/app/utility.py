from flask import jsonify

def compose_response(data,status = 'sucess'):
    return jsonify({
        'data' :data,
        'status' : status
    })