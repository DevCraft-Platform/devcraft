import cryptography.fernet
import cryptography.utils
from flask import Flask, render_template, request, testing, jsonify
from utils import db_connect, password_encrypt as pe
import bcrypt
import datetime

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html", title="MainPage")

# App Routes
@app.route("/app")
def render_app():
    return render_template("app/home/index.html", title="App")

@app.route("/app/auth/signup")
def render_signup():
    return render_template("app/auth/signup.html", title="Signup")

@app.route("/app/auth/signin")
def render_login():
    return render_template("app/auth/signin.html", title="Login")

@app.route("/api")
def render_api():
    return {
        "message": "Welcome to the API",
        "Auth": "None"
    }


@app.route("/api/v1/signin", methods=["POST"])
def signin_process():
    try:
        username = request.get_json()["username"]
        password = request.get_json()["password"].encode()
        user = db_connect.db_select_user(dict(username=username))
        if bcrypt.checkpw(password, user["password"].encode()):
            return jsonify({"message": "User Authenticated"})
        else:
            return jsonify({"message": "Invalid Credentials"}), 401
    except KeyError as e:
        print(f"Key Error: {e}")
        return jsonify({"message": "Invalid Request"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500
    
@app.route("/api/v1/signup", methods=["POST"])
def signup_process():
    try:
        username = request.get_json()["username"]
        password = request.get_json()["password"].encode()
        encrypted_password = bcrypt.hashpw(password, bcrypt.gensalt())
        print(f"Username: {username} \n Password: {password}")
        db_connect.db_insert_user(dict(
            username=username,
            password=encrypted_password.decode(),
            email=request.get_json()["email"]
        ))
        return jsonify({"message": "User Created"})
    except KeyError as e:
        print(f"Key Error: {e}")
        return jsonify({"message": "Invalid Request"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500