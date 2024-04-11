import cryptography.fernet
import cryptography.utils
from flask import Flask, render_template, request, testing, jsonify
from utils import db_connect, password_encrypt as pe
import bcrypt

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

@app.route("/api/v1/", methods=["GET"])
def render_users():
    # Check if the API Token (Barrer Token) is valid.
    token = request.headers.get("Authorization")
    database = db_connect.db_connect()
    cursor = database.cursor()
    # Now we stract the token from the database and compare it with the token provided by the user.
    query = "SELECT * FROM api_tokens WHERE token = ?"
    values = (token,)
    cursor.execute(query, values)
    api_token = cursor.fetchall()
    if api_token:
        # now we can return the users
        q = "SELECT * FROM users"
        cursor.execute(q)
        users = cursor.fetchall()
        cursor.close()

        return jsonify(users)
    else:
        cursor.close()
        return jsonify({"message": "Unauthorized"}), 401

@app.route("/api/v1/signin", methods=["POST"])
def signin_process():
    try:
        username = request.get_json()["username"]
        password = request.get_json()["password"].encode()
        print(f"Username: {username} \n Password: {password}")
        database = db_connect.db_connect()
        cursor = database.cursor()
        query = "SELECT * FROM users WHERE username = ?"
        values = (username.strip(),)
        cursor.execute(query, values)
        user = cursor.fetchone()
        # Now we can check if the user password is correct
        if user:
            encrypted_password = user[2].encode()
            print(encrypted_password)
            is_valid = bcrypt.checkpw(password, encrypted_password)
            print(is_valid)
            if is_valid:
                cursor.close()
                return jsonify({"message": "User Authenticated"})
            else:
                cursor.close()
                return jsonify({"message": "Invalid Credentials"}), 401
        else:
            cursor.close()
            print("User not found")
            return jsonify({"message": "Invalid Credentials"}), 401
    except KeyError:
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
        database = db_connect.db_connect()
        cursor = database.cursor()
        query = "INSERT INTO users (username, password) VALUES (?, ?)"
        values = (username.strip(), encrypted_password)
        cursor.execute(query, values)
        database.commit()
        cursor.close()
        return jsonify({"message": "User Created"})
    except KeyError:
        return jsonify({"message": "Invalid Request"}), 400
    except Exception as e:
        return jsonify({"message": str(e)}), 500