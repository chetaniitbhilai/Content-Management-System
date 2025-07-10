from fastapi import Header, HTTPException

def get_current_user(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid auth header format")

    token = authorization.split(" ")[1]

    # For simplicity (mock auth), extract user_id from in-memory token store
    from .crud import fake_token_store
    user_id = fake_token_store.get(token)

    if not user_id:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

    return user_id
