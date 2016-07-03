# /usr/bin/env python
from flask import Flask
from flask import request
from flask import make_response
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>' + request.headers.get('user-agent')

@app.route('/response')
def testResponse():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

@app.route('/redirect')
def testRedirect():
    return redirect('http://cn.bing.com')

if __name__ == '__main__':
    app.run(debug=True)