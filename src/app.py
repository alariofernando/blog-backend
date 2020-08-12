# app.py

from flask import Flask, jsonify


app = Flask(__name__)

headers = {
            'Access-Control-Allow-Headers': 'Content-Type',
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
            }

@app.route("/")
def hello():
    return jsonify({
        "body": "Hello World",
        "headers": headers,
        "statusCode": 200
        })

@app.route("/<name>")
def name(name):
    return jsonify({
        "body": f"Hello {name.capitalize()}",
        "headers": headers,
        "statusCode": 200
        })