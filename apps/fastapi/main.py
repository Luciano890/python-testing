""" A simple FastAPI application. """
# pylint: disable=import-error
# import uuid

import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from config.db import client
from models.spartan import Spartan

app = FastAPI()

db = client.spartans

@app.get("/spartans")
async def get_spartans():
    """ Get all spartans. """
    response = jsonable_encoder(db.find())
    return response


@app.post("/spartans")
async def post_spartan(spartan: Spartan):
    """ Post a spartan. """
    await db.insert_one(spartan.dict())
    return spartan

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
