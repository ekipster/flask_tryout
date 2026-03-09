from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return '<p>vandaag is een mooie dag</p>'