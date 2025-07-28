# Task model using pydantic
from pydantic import BaseModel

class Task(BaseModel):
    id: int
    description: str
    assigned_driver: int
    assigned_vehicle: int
    status: str