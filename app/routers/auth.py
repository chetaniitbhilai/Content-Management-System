from fastapi import APIRouter, Depends, HTTPException, Header
from sqlalchemy.orm import Session
from .. import schemas, crud, database
import uuid

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

@router.post("/login", response_model=schemas.TokenResponse)
def login(user: schemas.UserLogin, db: Session = Depends(get_db)):
    valid_user = crud.authenticate_user(db, user.username, user.password)
    if not valid_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    token = str(uuid.uuid4())
    fake_token_store[token] = valid_user.id
    return {"token": token}
