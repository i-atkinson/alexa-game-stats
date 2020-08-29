from flask import Flask, render_template, jsonify
import os
import requests

app = Flask(__name__)
data_url = os.environ['data_url']

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/data')
def data():
    return requests.get(data_url).json()

app.run()
