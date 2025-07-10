from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from .. import schemas, crud, database
import uuid
from ..crud import authenticate_user, generate_token_for_user


router = APIRouter(prefix="/auth", tags=["Auth"])

fake_token_store = {}  # token -> username

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.create_user(db, user.username, user.password)
    return {"id": db_user.id, "username": db_user.username}

@router.post("/login")
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    db_user = authenticate_user(db, user.username, user.password)
    if not db_user:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    
    token = generate_token_for_user(db_user.id)
    return {"token": token}

