# nginx-flask
# Author: Neil Jubinville
# Company:  Orbital Software
# http://www.orbitalsoftware.ca       *** HIRE US FOR DEVOPS ***
# This docker installs a smale base control app to automate AWS using boto3
# A series of examples exist to show automation and how to spin up dockerized VMs on EC2 directly or with ECS / Beanstalk

FROM ubuntu:14.04
# ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update
RUN apt-get install -y python python-pip python-virtualenv python-dev python-crypto nginx supervisor curl locate awscli zip

# Copy the flask 
RUN mkdir -p /orbital/
COPY webapp /orbital/webapp
RUN pip install -r /orbital/webapp/requirements.txt

# Nginx
RUN rm /etc/nginx/sites-enabled/default
COPY orbital-flask.conf /etc/nginx/sites-available/
RUN ln -s /etc/nginx/sites-available/orbital-flask.conf /etc/nginx/sites-enabled/orbital-flask.conf
RUN echo "daemon off;" >> /etc/nginx/nginx.conf

#Supervisor
RUN mkdir -p /var/log/supervisor
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

EXPOSE 80

# Start processes
CMD ["/usr/bin/supervisord"]

