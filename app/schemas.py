from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional

class IssueStatus(str, Enum):
    OPEN = "open"
    IN_PROGRESS = "in_progress"
    CLOSED = "closed"


class IssuePriority(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"



class IssueCreate(BaseModel):
    title: str = Field(min_length=3, max_length=100, example="Issue title")
    description: str = Field(min_length=10, max_length=500, example="Issue description")
    priority: IssuePriority = Field(IssuePriority.MEDIUM, example=IssuePriority.MEDIUM)



class IssueUpdate(BaseModel):
    title: Optional[str] = Field(default=None, min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, min_length=10, max_length=500, example="Updated issue description")
    status: Optional[IssueStatus] = None
    priority: Optional[IssuePriority] = None


class IssueOut(IssueCreate):
    id: int
    title: str
    description: str
    status: IssueStatus
    priority: IssuePriority