"""
A simple FastAPI application.
"""
from fastapi import FastAPI # pylint: disable=import-error

app = FastAPI()

@app.get("/")
async def root():
    """Root endpoint

    Returns:
        dict: message response
    """
    return {"message": "Hello World"}
