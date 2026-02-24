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


def add(con, cur):

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
    con.commit()


def edit(con, cur):

    valid_columns = ["title", "subject", "deadline", "priority", "duration"]
    row = int(input("Enter row id number to be changed: "))
    column = input("Enter column name: ")
    
    if column.lower() in valid_columns: #Checking if column name entered is valid
        if column.lower() == "duration":
            value = int(input("Enter new value: "))
        elif column.lower() == "deadline":
            value = get_deadline()
        else:
            value = input("Enter new value: ")
    
        cur.execute(f"UPDATE tasks SET {column.lower()} = ? WHERE id = ?", (value, row))
        con.commit()

        if cur.rowcount == 0: # Checks if any row was modified
            print("Update failed: No task found with that ID.")
        else:
            print("Update successful!")
    
    else:
        print("Invalid column entered")
