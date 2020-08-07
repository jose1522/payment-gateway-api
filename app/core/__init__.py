from fastapi import FastAPI, Depends
from api.routes import apiRouter
from .routerDependencies import *


def create_app():
    app = FastAPI()
    app.include_router(apiRouter, dependencies=[Depends(get_token_header)])
    return app