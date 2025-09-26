"""
Todo application logic


"""
from datetime import datetime
from typing import List, Optional
from file_io import TaskFileManager
from models import Task, TaskStatus

class TodoManager:
    def __init__(self, filename: str = "todo.txt"):
        self.file_manager = TaskFileManager(filename)
        self.tasks: List[Task] = self.file_manager.load_tasks()
        self.next_id = self._get_next_id()

    def _get_next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1
    
    def _save_tasks(self) -> bool:
        return self.file_manager.save_tasks(self.tasks)

    def add_task(self, title: str, due_date: datetime, priority: int = 3) -> bool:
        if not 1 <= priority <= 5:
            print(f"Error: Invalid priority {priority}. It must be between 1 and 5.")
            return False

        task = Task(
            id=self.next_id,
            title=title,
            due=due_date,
            priority=priority,
            status=TaskStatus.PENDING,
            created_at=datetime.now()
        )
        self.tasks.append(task)
        return self._save_tasks()


    def edit_task(self, task_id: int, title: Optional[str] = None,due_date: Optional[datetime] = None, priority: Optional[int] = None) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        if title:
            task.title = title
        if due_date:
            task.due = due_date
        if priority:
            if not 1 <= priority <= 5:
                print("Priority must be between 1 and 5")
                return False
            task.priority = priority
        
        return self._save_tasks()
    
    def mark_completed(self, task_id: int) -> bool:
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        task.status = TaskStatus.COMPLETED
        return self._save_tasks()

    def delete_task(self, task_id: int) -> bool:
        """Delete a task"""
        task = self.get_task_by_id(task_id)
        if not task:
            return False
        
        self.tasks.remove(task)
        return self._save_tasks()
    
    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its ID"""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None
    
    def list_tasks(self, show_done: bool = True, sort_by: str = "due") -> List[Task]:
        tasks = self.tasks.copy()
        tasks.sort(key=lambda t: t.due)
        return tasks