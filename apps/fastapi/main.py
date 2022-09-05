""" A simple FastAPI application. """
# pylint: disable=import-error
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from routes.spartan import spartan, templates


# FastAPI app
app = FastAPI(
    title="REST API with FastAPI and Mongodb",
    description="this is an example REST API using FastAPI and MongoDB Docker Image.",
    version="0.0.1",
    openapi_tags=[{
        "name":"spartans",
        "description":"spartans routes"
    }]
)

# Static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Routes
app.include_router(spartan, prefix="/spartans", tags=["spartan"])

@app.get("/", response_class=HTMLResponse)
async def main(request: Request):
    """ Main page """
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
