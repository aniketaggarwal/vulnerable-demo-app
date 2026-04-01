import sqlite3
import os
import sys        # unused
import subprocess # unused

conn = sqlite3.connect("app.db")
cursor = conn.cursor()

def get_user(user_id):
    # SQL injection vulnerability
    query = "SELECT * FROM users WHERE id = " + user_id
    return cursor.execute(query)

def get_orders(customer_name):
    # Another SQL injection
    query = "SELECT * FROM orders WHERE name = '" + customer_name + "'"
    return cursor.execute(query)

def delete_user(user_id):
    # SQL injection + no auth check
    query = "DELETE FROM users WHERE id = " + user_id
    cursor.execute(query)
    conn.commit()