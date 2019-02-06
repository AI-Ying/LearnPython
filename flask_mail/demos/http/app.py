from flask import Flask, request, jsonify, session, make_response, abort, url_for, redirect
app = Flask(__name__)

from urllib.parse import urlparse, urljoin

@app.route('/')
def index():
    return '<h1>Hello</h1>'   


@app.route('/login')
def login():
    session['logged_in'] = True
    return redirect(url_for('hello'))

@app.route('/set/<name>')
def set(name):
    response = make_response(redirect(url_for('hello', name=name)))
    response.set_cookie('name', name)
    return response

@app.route('/json')
def json():
    return jsonify(name='Grey Li', gender='male'), 500


@app.route('/note')
def foo():
    response = make_response('Hello')
    response.mimetype='text/plain'
    return response

@app.route('/hello')
@app.route('/hello/<name>')
def hello():
    name = request.args.get('name')
    if name is None:
        name = request.cookies.get('name')
    return '<h1>Hello {0}</h1>'.format(name)
    
@app.route('/goback/<int:year>')
def goback(year):
    return '<p> Welcome to %d.' %(2019-year)

@app.route('/bar')
def bar():
    return '<h1> Foo Page</h1><a href="{}">Do something and redirect</a>'\
    .format(url_for('hello', next=request.full_path))


