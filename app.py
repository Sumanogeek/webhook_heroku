import json
import datetime
from flask import Flask, request, Response
import pymongo
import requests

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
    if data["issue"]["fields"]["priority"]["name"] == "Critical":
        webhook_url = 'https://hooks.slack.com/services/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'
        slmsg = "Update to critical issue: " + data["issue"]["key"]
        slack_data = {'text': slmsg}

        response = requests.post(
            webhook_url, data=json.dumps(slack_data),
            headers={'Content-Type': 'application/json'}
        )
    return Response ("OK")

@app.route('/', methods=['GET'])
def test():
    return Response('It works good!')

if __name__ == '__main__':
    app.run()
