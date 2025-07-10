from sqlalchemy.orm import Session
from . import models, schemas

def create_article(db: Session, article: schemas.ArticleCreate):
    db_article = models.Article(**article.dict())
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article

def get_article(db: Session, article_id: int):
    return db.query(models.Article).filter(models.Article.id == article_id).first()

def get_articles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Article).offset(skip).limit(limit).all()

def update_article(db: Session, article_id: int, article_data: schemas.ArticleUpdate):
    article = get_article(db, article_id)
    if article:
        for key, value in article_data.dict(exclude_unset=True).items():
            setattr(article, key, value)
        db.commit()
        db.refresh(article)
    return article

def delete_article(db: Session, article_id: int):
    article = get_article(db, article_id)
    if article:
        db.delete(article)
        db.commit()
    return article
