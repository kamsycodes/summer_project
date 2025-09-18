"""
Pseudocode: 
- import Argparse
- define a function to add a task
- define a function to list tasks
- define a function to remove a task
- set up argument parsing
- add subcommands for each function
- save tasks to todo.txt
- print results to the console
- start the application

"""
import argparse
import sys
from datetime import datetime, timedelta
from todo import TodoManager
from models import TaskStatus

DATA_FILE = Path("todo.txt")

def main():
    print("Welcome to the To-Do List Application!")
    
    def add_task(task):