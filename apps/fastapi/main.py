""" A simple FastAPI application. """
# pylint: disable=import-error
import uvicorn
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

import common.helper as helper
from config.db import client
from models.spartan import Spartan

app = FastAPI()

db = client.local.spartans


@app.get("/spartans")
async def get_spartans():
    """ Get all spartans. """
    cursor = db.find({})
    response = [await helper.remove_id_field(document)
                async for document in cursor]
    return response


@app.post("/spartans")
async def create_spartan(spartan: Spartan):
    """ Create a new spartan. """
    spartan = jsonable_encoder(spartan)
    new_spartan = await db.insert_one(spartan)
    response = await db.find_one({"_id": new_spartan.inserted_id})
    await helper.remove_id_field(response)
    return response


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
