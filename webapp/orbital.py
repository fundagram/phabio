from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to the autmated code pipeline and cloud automation tool.  Developed by neil@orbitalsoftware.ca'

if __name__ == '__main__':
    app.debug = True
    app.run(host="0.0.0.0")
    
