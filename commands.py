import sqlite3
from date import get_deadline #Accept and format deadline date input

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

