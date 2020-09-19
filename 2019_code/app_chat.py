#!/usr/local/bin/python

from flask import Flask, request, jsonify
app = Flask(__name__)
app.config["DEBUG"] = True

books = [
    { 'id':0,
    'title': 'Testing',
    'author': 'Paing',
    },
    {'id':1,
    'title': 'Test1',
    'author': 'Gniap',
    }
    ]

@app.route('/', methods=['GET'])
def index():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''

@app.route('/api/books/all', methods=['GET'])
def api_all():
    return jsonify(books)

@app.route('/api/books', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No ID"

    result = []
    for a in books:
        if a['id'] == id:
            result.append(a)
    return jsonify(result)

app.run()

@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/user/<name>')
def hello(name=None):
    return render_template('user-profile.html', name=name)
