from pydantic import BaseModel
from typing import List

class TaskStep(BaseModel):
    id: int
    description: str

class AgentPlan(BaseModel):
    task_name: str
    steps: List[TaskStep]
    status: str = "planned"

class CriticReview(BaseModel):
    approved: bool
    feedback: str
    score: float