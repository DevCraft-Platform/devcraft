"""
    Upload User - Admin tool to create a new user in the database.

    Usage:
        python3 upload_user.py
"""

import os
import json
from dotenv import load_dotenv
import db_connect
from schemas import user
import argparse
from simple_term_menu import TerminalMenu
import flask
import threading
import webbrowser

# Load the environment variables
load_dotenv()

def openLogin():
    app = flask.Flask(__name__)

    @app.route("/login-cli")
    def login():
        return "Login Page"

    # Start the server
    server = threading.Thread(target=app.run, kwargs={"port": 7070})
    server.start()

    # Open the browser
    webbrowser.open("http://localhost:7070/login-cli")

    # Show the user a message of "Waiting for token..."
    print("Waiting for token...")
    # Now we need to wait for the token to be generated
    # We can use a while loop to check if the token.key file exists
    


# Arguments
parser = argparse.ArgumentParser(description="Upload User - Admin tool to create/manage a new user in the database.")

# Let's add the arguments
parser.add_argument("--push-json", help="Push a user from a JSON file.", type=str)
parser.add_argument("--login", help="Login as a admin to use the CLI.", action="store_true")

# Parse the arguments
args = parser.parse_args()

if args.login:

    login_options = ["Via Token", "Via Web", "Exit"]

    print("Welcome to Admin Tools CLI.")
    print("===========================")
    print("What method would you like to use?")
    terminal_menu = TerminalMenu(login_options)
    menu_entry_index = terminal_menu.show()
    
    if menu_entry_index == 0:
        print("Via Token")
    elif menu_entry_index == 1:
        # Render a simple web server to login
        openLogin()
    elif menu_entry_index == 2:
        exit()
    
    


# Connect to the database
# We need to check if a token.key file exists
if os.path.exists("admin_tools/token.key"):
    pass
else:
    print("No token.key file found. Please login to use the CLI.")
    exit()