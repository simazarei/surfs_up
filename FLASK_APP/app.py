from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world'
app.run() 

@app.route('/about')
def about():
    return 'This My About World Page :)'
app.run() 