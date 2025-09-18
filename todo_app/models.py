"""
Task model for the todo app.

All fields are required:
- id: int
- title: str
- due: str        (YYYY-MM-DD)
- priority: int   (1 = highest, 5 = lowest)
- status: str     ("open" or "done")
- created_at: str (YYYY-MM-DDTHH:MM:SS)
- completed_at: str (YYYY-MM-DDTHH:MM:SS)

Responsibilities:
1. Represent a task (with @dataclass).
2. Provide to_dict() -> dict for saving.
3. Provide from_dict(d: dict) -> Task for loading.
4. Validate:
   - id: must be int > 0
   - title: must be non-empty str
   - due: must parse with date.fromisoformat()
   - priority: must be between 1 and 5
   - status: must be either "pending" or "completed"
   - created_at: must parse with datetime.fromisoformat()

"""


from datetime import datetime
from typing import Optional
from enum import Enum
from dataclasses import dataclass

class TaskStatus(Enum):
    PENDING = "pending"
    COMPLETED = "completed"

@dataclass
class Task:
    id: int
    title: str
    description: str
    due: datetime
    priority: int 
    status: TaskStatus
    created_at: datetime

    def __post_init__(self):
        if not 1 <= self.priority <= 5:
            raise ValueError("priority must be between 1 and 5")
        
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'due': self.due.isoformat(),
            'priority': self.priority,
            'status': self.status.value,
            'created_at': self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Task':
        return cls(
            id=data['id'],
            title=data['title'],
            description=data['description'],
            due=datetime.fromisoformat(data['due']),
            priority=data['priority'],
            status=TaskStatus(data['status']),
            created_at=datetime.fromisoformat(data['created_at']) if 'created_at' in data else None
        )
    
    def __str__(self) -> str:
        return (
                f"Task(id={self.id}, title='{self.title}', description='{self.description}', "
                f"due={self.due.date()}, priority={self.priority}, status='{self.status.value}', "
                f"created_at={self.created_at.isoformat()})"
                )
