from pydantic import BaseModel


class Category(BaseModel):
    name: str
    count: int