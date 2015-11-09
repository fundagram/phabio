from fabric.api import *

#env.hosts = []

env.user = "ubuntu"


def test(who="key"):
    print "Jinja Style! {who}!".format(who=who)


def installDocker():
    output = run("wget https://get.docker.com/ -O dockerinstall.sh")    
    print output
    output = run("chmod 777 dockerinstall.sh")
    print output
    output = sudo("./dockerinstall.sh") 
    print output
    output = sudo("docker -d &")       
    print output

def deployControllerNode():  
    output = sudo("docker run -d -p 80:80 fed007/nginx-flask")
    print output

def deployKafkaNode():  
    output = sudo("docker run -d -p 9092:9092 spotify/docker-kafka")
    print output

def deployProducerNode():  
    output = sudo("docker run -d -p 80:80 fed007/nginx-flask")
    print output

def deployConsumerNode():  
    output = sudo("docker run -d -p 80:80 fed007/nginx-flask")
    print output



