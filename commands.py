import sqlite3
from datetime import datetime

def get_deadline(): #Accept and format deadline date input
    while True:
        user_input = input("Enter deadline (YYYY-MM-DD HH:MM): ")
        try:
            # Validate format: If it fails, it jumps to 'except'
            valid_dt = datetime.strptime(user_input, "%Y-%m-%d %H:%M")
            return valid_dt.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD HH:MM (e.g., 2026-02-25 18:00)")

con = sqlite3.connect("tasks.db") # Connecting to database
cur = con.cursor() # Creating a cursor to execute SQL commands

def add(cur):
    title = input("Enter task title: ")
    subject = input("Enter subject: ")
    deadline = get_deadline()
    priority = input("Enter task priority(low/high): ")
    duration = input("Enter duration(in minutes): ")

    #Insert values into table
    cur.execute("""
    INSERT INTO tasks (title, subject, deadline, priority, duration, status) 
    VALUES (?, ?, ?, ?, ?, "Pending")
    """, (title, subject, deadline, priority, duration))

