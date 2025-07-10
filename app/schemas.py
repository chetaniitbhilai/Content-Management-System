from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ArticleBase(BaseModel):
    title: str
    content: str

class ArticleCreate(ArticleBase):
    title: str
    content: str

class ArticleUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

class ArticleResponse(ArticleBase):
    id: int
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(from_attributes=True)


class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(BaseModel):
    username: str
    password: str

class TokenResponse(BaseModel):
    token: str

