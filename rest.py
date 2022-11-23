from flask import Flask, request
from flask import jsonify
from flask_httpauth import HTTPBasicAuth, HTTPTokenAuth
import base64

app = Flask(__name__)
auth = HTTPBasicAuth()
bearer_token_auth = HTTPTokenAuth()


@app.route('/test')
def get_test():
    return {"a": 1, "b": 2}


@app.route('/rest-auth', methods=["post"])
# @auth.login_required
def get_response():
    print(request.data)
    headers = request.headers
    print("headers ------------->")
    print(headers)
    return {"g":12}


@bearer_token_auth.verify_token
def authenticate(token):
    if token:
        if token == "qwertyuiop":
            return True
        else:
            return False
    else:
        return False


@auth.verify_password
def authenticate(username, password):
    if username and password:
        if username == 'roy' and password == 'roy':
            return True
        else:
            return False
    return False




if __name__ == "__main__":
    app.run(debug=True)
