from flask import Flask, request, render_template, render_template_string
import uuid
import time
import json  # Added import statement
from datetime import datetime, timedelta  # Added import statement
from ..db_connect import db_connect  # Added import statement

app = Flask(__name__)

@app.route('/webauth', methods=['GET', 'POST'])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Connect to the database and check if the user exists
        database = db_connect()
        # Check if the user exists
        if database["cli-user"].find_one({"username": username}):
            # Check if the password is correct
            if database["cli-user"].find_one({"username": username})["password"] == password:
                # Generate a uuid4 token
                token = str(uuid.uuid4())
                # Save the token to a file
                # Create a file for the token
                with open("token.json", "w") as f:
                    # Create a dictionary
                    token_dict = {"token": token, "user": username, "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "expires_at": (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d %H:%M:%S")}
                    # Convert the dictionary to a JSON string
                    json_string = json.dumps(token_dict)
                    # Write the JSON string to the file
                    f.write(json_string)
                # Close window and return a script to close the window in the browser
                time.sleep(5)
                return render_template_string("<script>window.close();</script>")
            else:
                return "Invalid credentials!" and render_template_string("<script>window.close();</script>")
    elif request.method == "GET":
        return render_template("auth.html", title="Login to Admin Tools - CLI", favicon="https://cdn.changelog.com/uploads/icons/topics/rq/icon_large.png?v=63702963062", context="Login to Admin Tools CLI.")

if __name__ == '__main__':
    app.run(port=7070, debug=True)