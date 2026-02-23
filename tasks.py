import sqlite3 # Importing sqlite for database management

con = sqlite3.connect("tasks.db") # Connecting to database
cur = con.cursor() # Creating a cursor to execute SQL commands


# Aesthetics
print("________________________")
print("What do you want to do?")
print("________________________")
print("Enter \"add\" to add a new task")
print("Enter \"edit\" to edit a task")
print("Enter \"delete\" to mark it as complete")
print("Enter \"today\" to check today's priority tasks")
print("________________________")
print("________________________")

command = input("Enter command: ")

if command.lower() == "add":
    