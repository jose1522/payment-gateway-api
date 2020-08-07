from fastapi import APIRouter
from models import gateway

apiRouter = APIRouter()


@apiRouter.get('/')
async def index():
    return {"hello" : "world"}


@apiRouter.post('/transaction/')
async def index(item: gateway.Transaction):
    verification = gateway.Verification(item)
    response = {}
    if verification.verifyCard():
        authorization = gateway.Authorization(item)
        authorization.processTransaction()
        response = authorization.output
    else:
        response = verification.output
    return response
