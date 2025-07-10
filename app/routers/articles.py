from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, database
from collections import defaultdict

recently_viewed = defaultdict(list)

router = APIRouter(prefix="/articles", tags=["Articles"])

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ArticleResponse)
def create(article: schemas.ArticleCreate, db: Session = Depends(get_db)):
    return crud.create_article(db, article)

@router.get("/{article_id}", response_model=schemas.ArticleResponse)
def read(article_id: int, user_id: int = 1, db: Session = Depends(get_db)):
    article = crud.get_article(db, article_id)
    if not article:
        raise HTTPException(status_code=404, detail="Article not found")

    views = recently_viewed[user_id]
    if article_id in views:
        views.remove(article_id)
    views.insert(0, article_id)
    if len(views) > 5:
        views.pop()

    return article

@router.get("/", response_model=list[schemas.ArticleResponse])
def list_articles(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_articles(db, skip=skip, limit=limit)

@router.put("/{article_id}", response_model=schemas.ArticleResponse)
def update(article_id: int, article: schemas.ArticleUpdate, db: Session = Depends(get_db)):
    updated = crud.update_article(db, article_id, article)
    if not updated:
        raise HTTPException(status_code=404, detail="Article not found")
    return updated

@router.delete("/{article_id}", response_model=schemas.ArticleResponse)
def delete(article_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_article(db, article_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Article not found")
    return deleted

