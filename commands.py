import sqlite3
from datetime import datetime

def get_deadline():
    """
    Prompts user for a deadline and validates the format.
    Returns: A formatted string compatible with SQLite DATETIME storage.
    """
    while True:
        user_input = input("Enter deadline (YYYY-MM-DD HH:MM): ")
        try:
            # datetime.strptime ensures the date is mathematically valid (e.g., rejects Feb 30)
            valid_dt = datetime.strptime(user_input, "%Y-%m-%d %H:%M")
            return valid_dt.strftime("%Y-%m-%d %H:%M:%S")
        except ValueError:
            print("Invalid format! Please use YYYY-MM-DD HH:MM (e.g., 2026-02-25 18:00)")


def show(cur):
    """
    Retrieves and displays all tasks from the database.
    Logic: Sorted by status DESC to prioritize 'Pending' over 'Done'.
    """
    cur.execute("SELECT id, title, deadline, priority, duration, status FROM tasks ORDER BY status DESC")
    result = cur.fetchall()

    if not result:
        print("\nYour task list is empty!")
    else:
        # Using string formatting padding (:<x) to ensure clear, tabular output in terminal
        for row in result:
            print(f"id: {row[0]:<4}| task: {row[1]:<20}| deadline: {row[2]:<20}| priority: {row[3]:<8}| duration: {row[4]}| status: {row[5]:<6}")

def add(con, cur):
    """
    Handles user input to create a new task entry.
    Commits changes to the database and provides feedback on success.
    """
    title = input("Enter task title: ")
    subject = input("Enter subject: ")
    deadline = get_deadline()
    priority = input("Enter task priority(low/high): ")
    duration = input("Enter duration(in minutes): ")

    # Use parameterized queries (?) to prevent SQL Injection attacks
    cur.execute("""
    INSERT INTO tasks (title, subject, deadline, priority, duration, status) 
    VALUES (?, ?, ?, ?, ?, "Pending")
    """, (title, subject, deadline, priority, duration))
    con.commit()

    # rowcount checks if the database actually accepted the new record
    if cur.rowcount == 0:
        print("INSERTION FAILED")
    else:
        print("INSERTION SUCCESSFUL!")

def edit(con, cur):
    """
    Modifies specific columns of an existing task identified by ID.
    Validates column names to ensure database integrity.
    """
    valid_columns = ["title", "subject", "deadline", "priority", "duration"]
    
    try:
        row = int(input("Enter row id number to be changed: "))
        column = input("Enter column name: ").lower()
        
        if column in valid_columns:
            # Branching logic to handle different data types (int for duration, str for others)
            if column == "duration":
                value = int(input("Enter new value: "))
            elif column == "deadline":
                value = get_deadline()
            else:
                value = input("Enter new value: ")
        
            # Update the specific record
            cur.execute(f"UPDATE tasks SET {column} = ? WHERE id = ?", (value, row))
            con.commit()

            if cur.rowcount == 0:
                print("NO TASK FOUND WITH THAT ID")
            else:
                print("UPDATE SUCCESSFUL!")
        else:
            print("Invalid column entered")
    except ValueError:
        print("Input Error: IDs and Durations must be numeric.")

def done(con, cur):
    """
    A 'Soft Delete' approach: Updates task status to 'Done' instead of removing the row.
    Useful for historical data tracking/productivity metrics.
    """
    try:
        row = int(input("Enter row id to be marked as done: "))
        cur.execute("UPDATE tasks SET status = ? WHERE id = ?", ("Done", row))
        con.commit()

        if cur.rowcount == 0:
            print("COULD NOT FIND ROW ID")
        else:
            print("MARKED DONE!")
    except ValueError:
        print("Input Error: Row ID must be a number.")

def today(cur):
    """
    Filters tasks due within a 3-day window from the current local time.
    Limits output to the top 5 most urgent items.
    """
    # SQLite date() function handles the time-delta logic internally
    cur.execute("""
                SELECT id, title, deadline, priority 
                FROM tasks 
                WHERE status != 'Done' 
                AND date(deadline) >= date('now', 'localtime') 
                AND date(deadline) <= date('now', 'localtime','+3 days')
                ORDER BY deadline ASC LIMIT 5
                """)
    results = cur.fetchall()

    if not results:
        print("NO PRIORITY TASKS FOR NEXT 3 DAYS")
    else:
        print("\n--- UPCOMING URGENT TASKS ---")
        for row in results:
            print(f"ID: {row[0]} | Task: {row[1]} | Due: {row[2]} | Priority: {row[3]}")

def delete(con, cur):
    """
    Hard Delete: Permanently removes a record from the database.
    """
    try:
        row = int(input("Enter row id to be deleted: "))
        cur.execute("DELETE FROM tasks WHERE id = ?", (row,))
        con.commit()

        if cur.rowcount == 0:
            print("COULD NOT FIND ROW ID")
        else:
            print("DELETED")
    except ValueError:
        print("Input Error: Row ID must be a number.")