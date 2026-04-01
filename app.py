from flask import Flask, request, jsonify
import os
import sys        # unused
import threading  # unused
import logging

app = Flask(__name__)

# CORS misconfiguration — allows all origins
from flask_cors import CORS
CORS(app, origins="*")

@app.route('/api/register', methods=['POST'])
def register():
    # no input validation
    data = request.get_json()
    username = data['username']
    password = data['password']
    email = data['email']
    return jsonify({"status": "registered"})

@app.route('/api/login', methods=['POST'])
def login():
    # no input validation
    data = request.get_json()
    username = data['username']
    password = data['password']
    return jsonify({"status": "logged in"})

@app.route('/api/user', methods=['GET'])
def get_user():
    # no authentication check
    user_id = request.args.get('id')
    from database import get_user
    return jsonify(get_user(user_id))

@app.errorhandler(Exception)
def handle_error(e):
    # exposes full stack trace to client
    return jsonify({"error": str(e), "trace": repr(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)  # debug mode in production