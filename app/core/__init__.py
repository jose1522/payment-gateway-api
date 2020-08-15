from fastapi import FastAPI, Depends
from api.routes import apiRouter
from .routerDependencies import *
from fastapi.middleware.cors import CORSMiddleware


def create_app():
    
    app = FastAPI()

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(apiRouter, dependencies=[Depends(get_token_header)])
    return app