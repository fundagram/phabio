from flask import Flask, Response
import traceback
import orbitalaws as aws 
import simplejson as json

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the automated code pipeline and cloud automation tool.  Developed by neil@orbitalsoftware.ca'

@app.route('/listS3')
def listS3():
    try:
        objectList = aws.listS3()
        for obj in objectList:
            print obj
        print objectList
        return Response(json.dumps(objectList), 200, mimetype='application/json')
    except:
        traceback.print_exc()
        return Response("{}", 400, mimetype='application/json')


@app.route('/instance/launch')
def launch():    
    try:
        instanceList = aws.launchEC2Image()
        #print instanceList[0].id
        return Response('{ "instanceid":"'+instanceList[0].id+' ""}', 200, mimetype='application/json')
    except:
        traceback.print_exc()
        return Response('{ "message":"Unable to launchEC2Image" }', 400, mimetype='application/json')


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
    
