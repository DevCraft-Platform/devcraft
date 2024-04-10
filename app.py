from flask import Flask, render_template

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