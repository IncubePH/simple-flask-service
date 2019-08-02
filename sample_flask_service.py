from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is a Flask'

#app.run('0.0.0.0', debug=True)
app.run()