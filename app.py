import json
import datetime
from flask import Flask, request, Response

app = Flask(__name__)

##global master
master = []
dummy = []

@app.route('/rec', methods=['POST'])
def indata():
    data = json.loads(request.data)
    print ("Data: ", data)
    master.append(data)
    return Response ("OK")

@app.route('/', methods=['GET'])
def test():
    return Response('It works good!')

@app.route('/print')
def wrtfl():
    opFile = "output"+str(datetime.datetime.now())+".json"
    with open(opFile,'w') as op:
        json.dump(master, op)
    master.clear()
    return Response("Written to file!")

if __name__ == '__main__':
    app.run()
