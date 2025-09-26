"""
Pseudocode: 
- import Argparse
- define a function to add a task
- define a function to list tasks
- define a function to mark a task as completed
- define a function to edit a task
- define a function to delete a task
- set up argument parsing
- add subcommands for each function
- save tasks to todo.txt
- print results to the console
- start the application

"""



import argparse
from datetime import datetime, timedelta
from todo import TodoManager
from models import TaskStatus


def parse_date(date_string: str) -> datetime:
    try:
        return datetime.strptime(date_string, "%Y-%m-%d")
    except ValueError:
        print(f"Error: Invalid date format '{date_string}'. Use YYYY-MM-DD.")
        exit(1)

def add_task(args):
    todo = TodoManager()
    due_date = parse_date(args.due)

    success = todo.add_task(args.title, due_date, args.priority)
    
    if success:
        print("Task added successfully.")
    else:
        print("Failed to add task.")


def list_tasks(args):   
    todo = TodoManager()
    tasks = todo.list_tasks(show_done=True, sort_by="due")
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        status = "COMPLETED" if task.status == "completed" else "PENDING"
        print(f"ID:{task.id} | {task.title} |(Due: {task.due.strftime('%Y-%m-%d')}) | Priority: {task.priority} | Status: {status}")

def mark_completed(args):
    todo = TodoManager()
    success = todo.mark_completed(args.id)
    if success:
        print(f"Task {args.id} marked as completed.")
    else:
        print(f"Failed to mark task {args.id} as completed.")


def edit_task(args):
    todo = TodoManager()
    
    due_date = None
    if args.due:
        due_date = parse_date(args.due)

    success = todo.edit_task(
        id=args.id,
        title=args.title,
        due=due_date,
        priority=args.priority
    )
    if success:
        print(f"Task {args.id} updated successfully.")
    else:
        print(f"Failed to update task {args.id}.")

def delete_task(args):
    todo = TodoManager()
    success = todo.delete_task(args.id)
    if success:
        print(f"Task {args.id} deleted successfully.")
    else:
        print(f"Failed to delete task {args.id}.")

def main():
    """Main function"""
    parser = argparse.ArgumentParser(description="Todo CLI")
    subparsers = parser.add_subparsers(dest='command')
    
    # Add command
    add_parser = subparsers.add_parser('add')
    add_parser.add_argument('title', help='Task title')
    add_parser.add_argument('--due', required=True, help='Due date (YYYY-MM-DD)')
    add_parser.add_argument('--priority', type=int, default=3, help='Priority 1-5')
    
    # List command
    list_parser = subparsers.add_parser('list')
    
    # Completed command
    completed_parser = subparsers.add_parser('completed')
    completed_parser.add_argument('id', type=int, help='Task ID')
    
    # Edit command
    edit_parser = subparsers.add_parser('edit')
    edit_parser.add_argument('id', type=int, help='Task ID')
    edit_parser.add_argument('--title', help='New task title')
    edit_parser.add_argument('--due', help='New due date (YYYY-MM-DD)')
    edit_parser.add_argument('--priority', type=int, help='New priority 1-5')
    
    # Delete command
    delete_parser = subparsers.add_parser('delete')
    delete_parser.add_argument('id', type=int, help='Task ID')
    
    args = parser.parse_args()
    
    if args.command == 'add':
        add_task(args)
    elif args.command == 'list':
        list_tasks(args)
    elif args.command == 'completed':
        mark_completed(args)
    elif args.command == 'edit':
        edit_task(args)
    elif args.command == 'delete':
        delete_task(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
