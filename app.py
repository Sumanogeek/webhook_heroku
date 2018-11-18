import json
import datetime
from flask import Flask, request, Response
import pymongo

app = Flask(__name__)

master = []

mongo_URI = "mongodb://pymomo:momo2py@ds033170.mlab.com:33170/try4mongo"
client = pymongo.MongoClient(mongo_URI, connectTimeoutMS=30000)
db = client.get_database("try4mongo")
jiraDB = db.jiralogs

@app.route('/rec', methods=['POST'])
def indata():
    data = json.loads(request.data)
    print ("Data: ", data)
    jiraDB.insert_one(data)
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
