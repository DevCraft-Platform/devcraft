import cryptography.fernet
import cryptography.utils
from flask import Flask, render_template, request, testing, jsonify
from utils import db_connect, password_encrypt as pe
import bcrypt
import datetime
import json
import requests

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html", title="MainPage")

# App Routes
@app.route("/app/auth/signup")
def render_signup():
    return render_template("app/auth/signup.html", title="Signup")

@app.route("/app/auth/signin")
def render_login():
    return render_template("app/auth/signin.html", title="Login")

@app.route("/app/")
def render_app():
    return render_template("app/home/index.html", title="App")

@app.route("/api")
def render_api():
    return {
        "message": "Welcome to the API",
        "Auth": "None"
    }

@app.route("/api/v1/random/quotes/")
def render_random_quote():
    try:
        res = requests.get("https://api.quotable.io/random", timeout=10)
        res.raise_for_status()
    except requests.exceptions.RequestException as e:
        return jsonify(error=str(e)), 500

    return res.json()

@app.route("/app/profile/<username>", methods=["GET"])
def render_profile(username):
    return render_template("app/profile/index.html", title="Profile", username=username)