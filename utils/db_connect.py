"""
    db_connect.py - Route: /utils/db_connect.py
    Author: INovomiast2
    Created: 2024-11-04
    -------------------------------------------
    
    Contents:
        - Database Connection
        - Database Insertion
        - Database Selection
        - Database Update
        - Database Deletion
        - Database Disconnection
        - Database Error Handling

    (C) 2024 DevCraft - All Rights Reserved.
"""

# Module Imports
import os
import libsql_experimental as libsql
import cryptography
import datetime
import time
import random
import dotenv

# Load Environment Variables
dotenv.load_dotenv()

# Auth for the DB:
DB_HOST = os.getenv('DB_HOST')
DB_AUTH_TOKEN = os.getenv('DB_AUTH_TOKEN')
DB_NAME = os.getenv('DB_NAME')

# Database Connection
def db_connect():
    """
    Connect to the Database
    """
    conn = libsql.connect(DB_NAME, sync_url=DB_HOST, auth_token=DB_AUTH_TOKEN)
    return conn

# Database Insertion
def db_insert_user(data):
    """
    Insert Data into the Database
    """
    try:
        conn = db_connect()
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password, email, role, created_at) VALUES (?, ?, ?, ?, ?)"
        values = (data['username'], data['password'], data['email'], data['role'], str(data['created_at']))
        cursor.execute(query, values)
        conn.commit()
        cursor.close()
        return {"status": "success", "message": "Data Inserted Successfully!"}
    except Exception as e:
        return {"status": "error", "message": f"Error: {e}"}


# Database Selection
def db_select_user(data):
    """
    Select User from the Database
    """
    conn = db_connect()
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    values = (data['username'], data['password'])
    cursor.execute(query, values)
    data = cursor.fetchall()
    cursor.close()
    return data



def main():
    conn = db_connect()
    date = datetime.datetime.now()
    # Insert Data
    #data = db_insert_user({"username": "INovomiast2", "password": "password123", "email": "ceo@devcraft.io", "role": "admin", "created_at": str(date)})
    # if (data["status"] == "success"):
    #     print(data["message"])
    # else:
    #     print(data["message"])

    data = db_select_user({"username": "INovomiast2", "password": "password123"})
    if (len(data) > 0):
        print(data)
    else:
        print("No Data Found!")

if __name__ == "__main__":
    main()
    

