from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database
from collections import defaultdict
from ..dependencies import get_current_user

recently_viewed = defaultdict(list)

router = APIRouter(prefix="/articles", tags=["Articles"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create article (optionally, bind it to the logged-in user)
@router.post("/", response_model=schemas.ArticleResponse)
def create(article: schemas.ArticleCreate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    # Optionally attach author_id if you're tracking it
    return crud.create_article(db, article)

# Read article and update "recently viewed" for the current user
@router.get("/{article_id}", response_model=schemas.ArticleResponse)
def read(article_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    article = crud.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    # Update recently viewed for this user
    views = recently_viewed[user_id]
    if article_id in views:
        views.remove(article_id)
    views.insert(0, article_id)
    if len(views) > 5:
        views.pop()

    return article

# List articles (public or you can filter by user_id if needed) for pagination 
@router.get("/", response_model=list[schemas.ArticleResponse])
def list_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_articles(db, skip=skip, limit=limit)

# Update article (can add user ownership check later)
@router.put("/{article_id}", response_model=schemas.ArticleResponse)
def update(article_id: int, article: schemas.ArticleUpdate, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    updated = crud.update_article(db, article_id, article)
    if not updated:
        raise HTTPException(status_code=404, detail="Article not found")
    return updated

# Delete article (can add user ownership check later)
@router.delete("/{article_id}", response_model=schemas.ArticleResponse)
def delete(article_id: int, db: Session = Depends(get_db), user_id: int = Depends(get_current_user)):
    deleted = crud.delete_article(db, article_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Article not found")
    return deleted

# Get recently viewed articles (IDs) for the logged-in user
@router.get("/users/me/recently-viewed", response_model=list[int])
def get_recently_viewed(user_id: int = Depends(get_current_user)):
    return recently_viewed.get(user_id, [])
