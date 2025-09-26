# DEVELOPMENT PROCESS DOCUMENTATION
This file documents the development processes, decisions, challenges and lessons learned while building this app.

---

## 1. Project Overview
- **App Name**: ToDo CLI
- **Goal**: This app will enable the user create, edit, view, delete todo tasks. 
- **Tech Stack**: Python, Argparse, CLI

---

## 2. Project Scope
- CLI only
- Store tasks in a text file "todo.txt"
- Each task has ID, Title, due date, priority, status(completed/pending), timestamp
- Commands include add new, edit, list, completed, delete
- Sort by due date or priority

---

## Data Model
class Task:
- id: int
- title: str
- description: str
- due: datetime
- priority: int (1-5 where 1 is the highest)
- status: ENUM["pending", "completed"]
- created_at: datetime

---

## System Architecture
This file outlines the system design for the Todo App project.
1. Structure
    - todo_app/
      - README.md
      - main.py # Entry point, sets up argparse and CLI interface
      - todo.py # Core business logic (add, list, completed, delete, etc.)
      - file_io.py # File handling (load/save tasks to todo.txt)
      - models.py # Class definitions
      - todo.txt # File to store tasks
