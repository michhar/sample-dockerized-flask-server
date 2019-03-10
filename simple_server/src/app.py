import flask
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def hello_world():
    return 'Flask Dockerized'

# @_flask.route('/', methods = ['POST'])
# def flask_main():
#     s = str(request.form['abc'])
#     ind = global_fn_main(param1,param2,param3)
#     return ind

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')