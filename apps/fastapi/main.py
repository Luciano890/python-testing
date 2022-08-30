"""
A simple FastAPI application.
"""
# pylint: disable=import-error
import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Spartan(BaseModel):
    name: str
    age: int

@app.get("/")
async def root():
    """Root endpoint

    Returns:
        dict: message response
    """
    return {"message": "Hello World"}

@app.get("/spartans")
async def get_spartans():
    """Get all spartans

    Returns:
        list: list of spartans
    """
    return [
        {"name": "John", "age": 30},
        {"name": "Doe", "age": 25},
    ]

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
