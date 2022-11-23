import xmltodict
from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello"


@app.route("/testapp", methods=['POST', 'GET'], strict_slashes=False)
def parseRequest():
    print(request.data)
    print(request.headers)
    return request.data


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
