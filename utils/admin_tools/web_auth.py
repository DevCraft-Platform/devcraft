from flask import Flask, request, render_template, render_template_string
import uuid
import time
import json  # Added import statement
from datetime import datetime, timedelta  # Added import statement
import os
import re
import logging

app = Flask(__name__)

def is_valid_uuid4(uuid_string):
    regex = re.compile(r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}\Z', re.I)
    match = regex.match(uuid_string)
    return bool(match)

@app.route('/webauth', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if username == "admin" and password == "admin":
            token = str(uuid.uuid4())
            with open(f"{os.path.expanduser('~')}/devcraftcli/token.json", "w") as f:
                token_dict = {
                    "token": token,
                    "user": username,
                    "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "expires_at": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")
                }
                f.write(json.dumps(token_dict))
            # Check if the token.json file exists
            if os.path.exists("token.json"):
                # Read the file
                with open(f"{os.path.expanduser('~')}/devcraftcli/token.json", "r") as f:
                    token = json.load(f)
                    # Check if the token is valid
                    if (is_valid_uuid4(token["token"]) == True):
                        # Return a success message
                        print("Token is Valid.")
                        # Kill the server
                        os.system("kill -9 $(lsof -t -i:7070)")
                        
                        
                        
        else:
            # Return an error message and close the window
            return render_template_string('<p>Invalid credentials!</p><script>setTimeout(() => { window.close(); }, 5000);</script>')
    elif request.method == "GET":
        return render_template("auth.html", title="Login to Admin Tools - CLI")

@app.route('/admin', methods=['GET', 'POST'])
def render_admin():
    return render_template("admin.html", title="Admin Tools - CLI")

if __name__ == "__main__":
    log = logging.getLogger('werkzeug')
    log.setLevel(logging.ERROR)
    app.run(port=7070, host="0.0.0.0", use_reloader=False)