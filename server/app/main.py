from flask_app import flask_app

def register_blueprint():
    from sessions import sessions_bp
    from balances import balances_bp
    flask_app.register_blueprint(sessions_bp)
    flask_app.register_blueprint(balances_bp)

register_blueprint()
if __name__ == '__main__':
    flask_app.run(host ='0.0.0.0',debug=True)