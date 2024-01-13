from flask import Flask, request
from errors import AuthenticationError

app = Flask(__name__)

def auth(fn):
    def wrapper(*args, **kwargs):
        app.logger.info(request.headers)
        if 'Authorization' in request.headers:
            return fn(*args, **kwargs)
        raise AuthenticationError('Authorization failed')
    return wrapper

@app.get('/hello')
def hello():
    return {'message': 'Bismillah-hirrahman-nirraheem'}, 200

@app.get('/dashboard')
@auth
def authenticated_route():
    return {'message': 'Authenticated'}, 200

@app.errorhandler(Exception)
def error_handler(error):
    if isinstance(error, AuthenticationError):
        return {'error':'Unauthorized'}, 401
    return {'error': 'Unknown error'}, 500