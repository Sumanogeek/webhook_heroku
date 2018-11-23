import json
import datetime
from flask import Flask, request, Response
import pymongo

app = Flask(__name__)

mongo_URI = "mongodb://pymomo:momo2py@ds033170.mlab.com:33170/try4mongo"
client = pymongo.MongoClient(mongo_URI, connectTimeoutMS=30000)
db = client.get_database("try4mongo")
jiraDB = db.jiralogs

@app.route('/rec', methods=['POST'])
def indata():
    data = json.loads(request.data)
    print ("Data: ", data)
    jiraDB.insert_one(data)
    return Response ("OK")

@app.route('/', methods=['GET'])
def test():
    return Response('It works good!')

if __name__ == '__main__':
    app.run()
