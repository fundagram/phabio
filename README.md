# phabio
### by Neil Jubinville  < neil@orbitalsoftware.ca >

A demo app that automates AWS using boto3.  This app auto deploys into a docker image I built located at docker hub.

https://hub.docker.com/r/fed007/nginx-flask/

More specifically - this docker and github repo contain everything necessary to build and maintain
a continuous integration pipeline with [ Wecker ](http://wercker.com/).  It also contains all the code
necessary to auto deploy to AWS when a github push occurs. 

I'll post a blog a bit later detailing how you need to configure each step.

Stay tuned!

FYI,  webapp/  is where you need to put your code.

If you want to clone down and build a custom docker image for yourself you can by running the below command from the root directory

```bash
docker build -t fed007/nginx-flask .
```
