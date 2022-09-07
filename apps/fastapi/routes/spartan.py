""" Spartan routes. """
# pylint: disable=import-error
from uuid import UUID

from fastapi import (
    APIRouter,
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

from config.db import client
from models.spartan import BaseSpartan, CreateSpartan, UpdateSpartan

# Spartan router
spartan_router = APIRouter()

# MongoDB collection
db = client.local.spartans

# Jinja2 templates
templates = Jinja2Templates(directory="templates")


@spartan_router.get(
    path="/",
    response_model=list[BaseSpartan],
    status_code=HTTP_200_OK,
)
async def get_spartans(request: Request):
    """ Get all spartans. """
    cursor = db.find({}, {"_id": False})
    return templates.TemplateResponse(
        "spartans.html",
        {
            "request": request,
            "spartans": [c async for c in cursor],
        }
    )


@spartan_router.get(
    path="/{uuid}",
    response_model=BaseSpartan,
    status_code=HTTP_200_OK,
)
async def get_spartan(uuid: UUID):
    """ Get a spartan by uuid. """
    response = await db.find_one({"uuid": str(uuid)}, {"_id": 0})
    if response:
        return response
    raise HTTPException(status_code=HTTP_404_NOT_FOUND, detail="Spartan not found.")


@spartan_router.post(
    path="/",
    response_model=CreateSpartan,
    status_code=HTTP_201_CREATED,
)
async def create_spartan(spartan: CreateSpartan):
    """ Create a new spartan. """
    spartan = jsonable_encoder(spartan)
    new_spartan = await db.insert_one(spartan)
    response = await db.find_one({"_id": new_spartan.inserted_id}, {"_id": 0})
    return response


@spartan_router.put(
    path="/{uuid}",
    response_model=BaseSpartan,
    status_code=HTTP_200_OK,
)
async def update_spartan(uuid: UUID, spartan: UpdateSpartan):
    """ Update a spartan by uuid. """
    updated_spartan = jsonable_encoder(spartan)
    await db.find_one_and_update({"uuid": str(uuid)}, {"$set": updated_spartan})
    response = await db.find_one({"uuid": str(uuid)}, {"_id": 0})
    return response


@spartan_router.delete(
    path="/{uuid}/delete",
    status_code=HTTP_204_NO_CONTENT,
)
async def delete_spartan(uuid: UUID):
    """ Delete a spartan by uuid. """
    await db.find_one_and_delete({"uuid": str(uuid)}, {"_id": 0})
    return Response(status_code=HTTP_204_NO_CONTENT)
