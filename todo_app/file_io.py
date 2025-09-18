# file_io.py
"""
Handles saving and loading tasks from todo.txt

Format:
- Each line in todo.txt is one JSON object (representing a Task).
- Use Task.to_dict() when writing
- Use Task.from_dict() when reading

Public API:

def load_tasks(path: str) -> list[Task]
    - If file does not exist:
        return empty list
    - Open file in read mode
    - For each line:
        - strip newline
        - if line not empty:
            - parse JSON → dict
            - convert dict to Task with Task.from_dict()
            - add Task to list
    - Return list of Task objects

def save_tasks(path: str, tasks: list[Task]) -> None
    - Open file in write mode
    - For each Task in tasks:
        - convert to dict with to_dict()
        - convert dict to JSON string
        - write JSON string + newline
    - Close file
    - (Overwrites existing file completely each time)
"""

import json
import os
from typing import List
from todo_app.models import Task

class TaskFileManager:
    def __init__(self, filename: str = "todo.txt"):
        self.filename = filename

    def load_tasks(self) -> List[Task]:
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                content = file.read().strip()
                if not content:
                    return []
                
                data = json.loads(content)
                return [Task.from_dict(item) for item in data]
        except (json.JSONDecodeError, FileNotFoundError, KeyError) as e:
            print(f"Error loading tasks: {e}")
            return []
        
    def save_tasks(self, tasks: List[Task]) -> bool:
        try:
            task_dicts = [task.to_dict() for task in tasks]
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(task_dicts, file, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error saving tasks: {e}")
            return False

    