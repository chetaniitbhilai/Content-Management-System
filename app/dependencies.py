from fastapi import Header, HTTPException, Depends
from .routers.auth import fake_token_store

def get_current_user(token: str = Header(...)):
    user_id = fake_token_store.get(token)
    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid or missing token")
    return user_id
