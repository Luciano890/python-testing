""" Spartan routes. """
from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Request,
    Response,
)
from fastapi.encoders import jsonable_encoder
from fastapi.templating import Jinja2Templates
from starlette.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_404_NOT_FOUND,
)

import common.helper as helper
from config.db import client
from models.spartan import Spartan

# Spartan router
spartan = APIRouter()

# MongoDB collection
db = client.local.spartans

# Jinja2 templates
templates = Jinja2Templates(directory="templates")


@spartan.get(
    path="/",
    response_model=list[Spartan],
    status_code=HTTP_200_OK,
)
async def get_spartans(request: Request):
    """ Get all spartans. """
    cursor = db.find({})
    response = [await helper.remove_id_field(document)
                async for document in cursor]
    return templates.TemplateResponse(
        "spartans.html",
        {
            "request": request,
            "spartans": response
        }
    )


@spartan.get(
    path="/{uuid}",
    response_model=Spartan,
    status_code=HTTP_200_OK,
)
async def get_spartan(uuid: str):
    """ Get a spartan by uuid. """
    response = await db.find_one({"uuid": uuid})
    if response:
        await helper.remove_id_field(response)
        return response
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Spartan not found.")


@spartan.post(
    path="/",
    response_model=Spartan,
    status_code=HTTP_201_CREATED,
)
async def create_spartan(spartan: Spartan):
    """ Create a new spartan. """
    spartan = jsonable_encoder(spartan)
    new_spartan = await db.insert_one(spartan)
    response = await db.find_one({"_id": new_spartan.inserted_id})
    await helper.remove_id_field(response)
    return response


@spartan.put(
    path="/{uuid}",
    response_model=Spartan,
    status_code=HTTP_200_OK,
)
async def update_spartan(uuid: str, spartan: Spartan):
    """ Update a spartan by uuid. """
    updated_spartan = jsonable_encoder(spartan)
    updated_spartan.pop("uuid")
    await db.find_one_and_update({"uuid": uuid}, {"$set": updated_spartan})
    response = await db.find_one({"uuid": uuid})
    await helper.remove_id_field(response)
    return response


@spartan.delete(
    path="/{uuid}",
    status_code=HTTP_204_NO_CONTENT,
)
async def delete_spartan(uuid: str):
    """ Delete a spartan by uuid. """
    await db.find_one_and_delete({"uuid": uuid})
    return Response(status_code=HTTP_204_NO_CONTENT)
