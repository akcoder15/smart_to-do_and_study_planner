import sqlite3 # Importing sqlite for database management
from commands import add, edit, done, today, show, delete


def main():

    con = sqlite3.connect("tasks.db") # Connecting to database
    cur = con.cursor() # Creating a cursor to execute SQL commands

    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            subject TEXT,
            deadline DATETIME,
            priority TEXT,
            duration INTEGER,
            status TEXT
        )
    ''') # Create task table to store tasks


    while True:
        
        # Aesthetics
        print("________________________")
        print("What do you want to do?")
        print("________________________")
        print("Enter \"show\" to view all tasks")
        print("Enter \"add\" to add a new task")
        print("Enter \"edit\" to edit a task")
        print("Enter \"done\" to mark it as complete")
        print("Enter \"today\" to check today's priority tasks")
        print("Enter \"delete\" to delete task")
        print("Enter \"exit\" to quit")
        print("________________________")
        print("________________________")

        # Using .strip().lower() makes the menu 'bulletproof' against spaces or caps
        command = input("Enter command: ").strip().lower()

        if command == "exit": # break loop
            break

        elif command == "show":
            show(cur)

        elif command == "add":
            add(con, cur)
        
        elif command == "edit":
            edit(con, cur)
        
        elif command == "done":
            done(con, cur)

        elif command == "today":
            today(cur)
        
        elif command == "delete":
            delete(con, cur)
        
        else:
            print("ENTER VALID COMMAND")


    cur.close()
    con.close()

if __name__ == "__main__":
    main()