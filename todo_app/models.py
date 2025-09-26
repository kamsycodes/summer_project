"""
Task model for the todo app.

All fields are required:
- id: int
- title: str
- due: str        (YYYY-MM-DD)
- priority: int   (1 = highest, 5 = lowest)
- status: str     ("PENDING" or "COMPLETED")
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
    due: datetime
    priority: int 
    status: TaskStatus
    created_at: datetime

    def __post_init__(self):
            if not isinstance(self.status, TaskStatus):
                raise ValueError("status must be a TaskStatus enum")
            if not 1 <= self.priority <= 5:
                raise ValueError("priority must be between 1 and 5")
            if not isinstance(self.due, datetime):
                raise ValueError("due must be a datetime")
            if not isinstance(self.created_at, datetime):
                raise ValueError("created_at must be a datetime")
        
    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'title': self.title,
            'due': self.due.isoformat(),
            'priority': self.priority,
            'status': self.status.value,
            'created_at': self.created_at.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        # Enforce presence of required fields
        required = ["id", "title", "due", "priority", "status", "created_at"]
        missing = [k for k in required if k not in data]
        if missing:
            raise ValueError(f"Missing required fields: {missing}")

        return cls(
            id=int(data["id"]),
            title=str(data["title"]),
            due=datetime.fromisoformat(data["due"]),
            priority=int(data["priority"]),
            status=TaskStatus(data["status"]),              # string -> Enum
            created_at=datetime.fromisoformat(data["created_at"]),
        )
    
    def __str__(self) -> str:
        return (
                f"Task(id={self.id}, title='{self.title}', "
                f"due={self.due.date()}, priority={self.priority}, status='{self.status.value}', "
                f"created_at={self.created_at.isoformat()})"
                )
