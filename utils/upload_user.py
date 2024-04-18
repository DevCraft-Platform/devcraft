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
import webbrowser
import subprocess
import re

# Load the environment variables
load_dotenv()

def is_valid_uuid4(uuid_string):
    regex = re.compile(r'^[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}\Z', re.I)
    match = regex.match(uuid_string)
    return bool(match)

def checkToken():
    if os.path.exists("admin_tools/token.json"):
        # Load the json
        with open("admin_tools/token.json", "r") as f:
            token = json.load(f)
            # Now pass a regex to check if the token is valid
            if (is_valid_uuid4(token["token"]) == True):
                print("Token found.")
                return True
            return True
    else:
        return False


# Arguments
parser = argparse.ArgumentParser(description="Admin toolset to create/manage the website.")

# Let's add the arguments
parser.add_argument("--push-json", help="Push a user from a JSON file.", type=str)
parser.add_argument("--login", help="Login as a admin to use the CLI.", action="store_true")

# Parse the arguments
args = parser.parse_args()

if all(v is None for v in vars(args).values()):
    os.system("clear" or "cls")
    print("Welcome to Admin Tools CLI.")
    print("===========================")
    print("Please provide an argument to use the CLI.")
    print("Run python3 upload_user.py --help for more information. \n")
    exit()

if args.login:
    os.system("clear" or "cls")
    login_options = ["Token", "WebAuth", "Exit"]

    print("Login to Admin Tools CLI.")
    print("===========================")
    terminal_menu = TerminalMenu(login_options, title="Login Options", menu_cursor="❯ ", menu_cursor_style=("fg_red", "bold"), menu_highlight_style=("bg_red", "bold"))
    menu_entry_index = terminal_menu.show()
    
    if menu_entry_index == 0:
        print("Via Token")
    elif menu_entry_index == 1:
        # Render a simple web server to login
        subprocess.Popen(["python", "utils/admin_tools/web_auth.py"])
        # If it fails, exit the program
        if (subprocess.Popen == False):
            exit()
        webbrowser.open("localhost:7070/webauth")
        # Kill the server
        os.system("kill -9 $(lsof -t -i:7070)")
        # Check if the token exists
        if (checkToken() == True):
            pass
        else:
            print("No token found.")
    elif menu_entry_index == 2:
        exit()

if args.push_json:
    if (checkToken() == True):
        pass
    else:
        print("No token found.")