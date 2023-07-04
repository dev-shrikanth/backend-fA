from fastapi import FastAPI
from typing import List, Optional

from pydantic import BaseModel

app = FastAPI()

class Person(BaseModel):
    id: int 
    name: str
    age: int

DB: List[Person] = [
    Person(id=1, name="Jameel", age=22),
    Person(id=2, name="Alex", age=18),
    Person(id=3, name="Scott", age=19),
    Person(id=4, name="Tiger", age=19),
]

@app.get("/api")
def read_root():
    return DB

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}



