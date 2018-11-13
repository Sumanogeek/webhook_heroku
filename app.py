import json
from flask import Flask, request, Response

app = Flask(__name__)

@app.route('/rec', methods=['POST'])
def indata():
    data = json.loads(request.data)
    print ("Data: ", data)
    return "OK"

@app.route('/', methods=['GET'])
def test():
    return Response('It works good!')

if __name__ == '__main__':
    app.run()
