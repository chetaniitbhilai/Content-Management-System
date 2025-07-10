from sqlalchemy.orm import Session
from . import models, schemas

def create_article(db: Session, article: schemas.ArticleCreate, user_id: int):
    db_article = models.Article(
        title=article.title,
        content=article.content,
        author_id=user_id  # or author_id, match your model
    )
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


fake_token_store = {} 

def create_user(db: Session, username: str, password: str):
    user = models.User(username=username, password=password)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(models.User).filter(models.User.username == username).first()
    if user and user.password == password:
        return user
    return None

def generate_token_for_user(user_id: int):
    import uuid
    token = str(uuid.uuid4())
    fake_token_store[token] = user_id
    return token
