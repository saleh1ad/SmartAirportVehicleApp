# Driver model using pydantic
from pydantic import BaseModel

class Driver(BaseModel):
    id: int
    name: str
    status: str