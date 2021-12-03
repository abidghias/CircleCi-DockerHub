"""
waferfault101
4cc93f0c-1189-458c-b93a-fabdce11df4e
abid1
********
"""
from flask import Flask

from wsgiref import simple_server

from flask import Flask, session, request, Response, jsonify
from flask_cors import CORS,cross_origin


import atexit
import uuid
import os
app = Flask(__name__)
CORS(app)


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
    return "Flask app is running with a few changes "

#port = int(os.getenv("PORT", 5001))

if __name__ == "__main__":
    #host = '0.0.0.0'
    #app.run(debug=True)

    app.run(host='0.0.0.0', port=8000, debug=True)

    #httpd = simple_server.make_server(host=host, app=app)
    #httpd = simple_server.make_server(host='127.0.0.1', port=5000, app=app)
    #print("Serving on %s %d" % (host))
    #httpd.serve_forever()