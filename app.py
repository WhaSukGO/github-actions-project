from flask import Flask
app = Flask(__name__)s

@app.route('/')
def hello_world():
    return 'Hello, Docker!'
