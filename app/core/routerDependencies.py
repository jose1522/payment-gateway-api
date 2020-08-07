from fastapi import Header, HTTPException

async def get_token_header(x_token: str = Header(...)):
    if x_token != 'my-secret-token':
        raise HTTPException(status_code=400, detail='X-Token header invalid')