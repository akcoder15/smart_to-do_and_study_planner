# To-do and study planner

## 🚀 Pro-Academic CLI: A Study in Data Integrity

Data integrity is the foundation of Machine Learning. I developed this  to comprehend the 'Data Lifecycle'- from sanitizing user inputs and managing relational schemas to executing complex SQL filters. This project is a demonstration of my first CRUD utility tool that can capture, store, and retrieve information with 100% accuracy.

## 🛠 Engineering Core

This is a keyboard-centric utility built for efficiency. While most beginners build simple "list" apps, this project focuses on Backend Robustness and Environment Isolation.

- Relational Database: Implements a persistent SQLite3 backend.

- Modular Architecture: Uses a "Decoupled Design" where main.py (UI/Loop) and commands.py (Data Logic) operate independently.

- Bulletproof Inputs: Implements .strip().lower() normalization and try-except blocks to handle malformed user data without crashing.

- Professional Git Workflow: Managed via feature branches and a strict .gitignore policy to ensure environment-specific files (like tasks.db) stay off the public cloud.

## 📂 Project Structure

```text
├── main.py          # Entry point & Command Dispatcher
├── commands.py      # SQL Logic & Database CRUD Operations
├── .gitignore       # Prevents .db and __pycache__ from tracking
└── README.md        # Technical Documentation
```

## 🚀 Getting Started

1. Clone the repository:
```text
git clone https://github.com/akcoder15/smart_to-do_and_study_planner.git
```
3. Execute the utility:
```text
python main.py
```

## 📊 Feature Architecture

| Feature | Technical Implementation | Impact |
| :--- | :--- | :--- |
| **Smart Fetch** | Uses `DATETIME` arithmetic to filter tasks due in the next 72 hours. | Optimizes UX by surfacing urgent data first. |
| **Atomic Updates** | Specific column targeting in SQL to avoid overwriting clean data. | Ensures data integrity and reduces database overhead. |
| **Soft Delete** | Status-based toggling for "Done" vs "Pending" states. | Maintains historical records for future data analysis. |
| **Error Handling** | Integer validation for row selection to prevent `ValueErrors`. | Prevents application crashes from malformed user input. |

## 🔮 Future Roadmap (The ML Vision)
To evolve this from a CLI utility into a Data Science tool, I plan to:

- Predictive Scheduling: Implement a basic linear regression model to predict how long a task will take based on past "Duration" data.

- NLP Integration: Allow "Natural Language" input (e.g., "Add math homework due Friday") using a basic parsing library.

- Data Export: Add a feature to export task history to .csv for visualization in Matplotlib or Tableau.
