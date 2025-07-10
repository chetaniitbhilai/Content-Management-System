from pydantic import BaseModel
from datetime import datetime

class ArticleBase(BaseModel):
    title: str
    content: str
    author_id: int

class ArticleCreate(ArticleBase):
    pass

class ArticleUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

class ArticleResponse(ArticleBase):
    id: int
    created_at: datetime
    updated_at: datetime | None

    class Config:
        orm_mode = True
