from flask import Flask, render_template, flash, request, jsonify
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
import json
import logging
import sqlite3
import requests_toolbelt.adapters.appengine

requests_toolbelt.adapters.appengine.monkeypatch()

try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib2 import HTTPError
    from urllib import quote
    from urllib import urlencode

# App config.
# DEBUG = True
app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/view_image', methods=['GET', 'POST'])
def view_image():
    if request.method == 'POST':
        data = {}
        data['submit'] = request.form['submit']
        return render_template('view_image.html', data = data)
    else:
        return render_template('view_image.html')


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)


@app.route('/list',methods = ['POST', 'GET'])
def list():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    sql = "SELECT * FROM users"
    cur.execute(sql)
    rows = cur.fetchall()
    for line in rows:
        print ' '.join(map(str, line))

    print(rows)
    return render_template("result.html",results = rows)

if __name__ == '__main__':
    app.run(debug=True)

