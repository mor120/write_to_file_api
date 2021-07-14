import flask
from flask import request

from write import write_to_file

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Utility API for Writing Request Data to a File</h1>
    <p>visit /api/write to use API's functionality</p>'''


@app.route('/api/write/', methods=['POST', 'GET'])
def api_in():
    request_body = request.json
    request_headers = request.headers
    request_args = request.args

    write_to_file(body=request_body, headers=request_headers.to_wsgi_list(), args=request_args.to_dict())

    return flask.jsonify(message="Thank you, come again.")


app.run()