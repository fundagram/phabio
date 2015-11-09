from flask import Flask, Response
import traceback
import orbitalaws as aws 
import simplejson as json
from flask import render_template as render
from flask import request, url_for
from threading import Timer
import uuid

app = Flask(__name__)
nodeList = []


@app.route('/')
def home():
    return render("base.html")


@app.route('/guage')
def guage():
    return render("guage.html")

@app.route('/infrastructure')
def infrastructure():
    return render("infrastructure.html")

@app.route('/nuke')
def nuke():
    return render("nuke.html")

@app.route('/elastic')
def elastic():
    return render("elastic.html")



@app.route('/kafkadeploy')
def kafkadeploy():
    # here we want to deploy an instance then launch the appropriate fabric script 
    instance = aws.launchEC2Image("KafkaServer");
    return "Deploy Kafka VM ID = " +instance[0].id     

@app.route('/elasticdeploy')
def elasticdeploy():
    # here we want to deploy an instance then launch the appropriate fabric script 
    instance = aws.launchEC2Image("ElasticServer");
    return "Deploy elastic fabric... VM ID = " +instance[0].id    

@app.route('/consumerdeploy')
def consumerdeploy():
    # here we want to deploy an instance then launch the appropriate fabric script 
    instance = aws.launchEC2Image("ConsumerServer");
    return "Deploy consumer ... VM ID = " +instance[0].id    

@app.route('/producerdeploy')
def producerdeploy():
    # here we want to deploy an instance then launch the appropriate fabric script 
    instance = aws.launchEC2Image("ProducerServer");
    return "Deploy producer... VM ID= " +instance[0].id    


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
        print instanceList[0].id        
        nodeList.append(instanceList[0].id)
        return Response('{ "instanceid":"'+instanceList[0].id+'"}', 200, mimetype='application/json')
    except:
        traceback.print_exc()
        return Response('{ "message":"Unable to launchEC2Image" }', 400, mimetype='application/json')


@app.route('/nodes')
def nodes():    
    try:
        instanceList = aws.getAllNodes("t2.micro","running")
        #print instanceList
        ilist = instanceList['Reservations']
        print ilist
        
        return render("nodes.html", instances=ilist)
    except:
        traceback.print_exc()
        return Response('{ "message":"Unable to get Node List" }', 400, mimetype='application/json')


if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
    
