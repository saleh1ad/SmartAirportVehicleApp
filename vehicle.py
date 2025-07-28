# Vehicle model using pydantic
from pydantic import BaseModel

class Vehicle(BaseModel):
    id: int
    type: str
    status: str
    fuel_level: float