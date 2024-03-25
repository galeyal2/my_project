from pydantic import BaseModel


class BlogSchema(BaseModel):
    title: str
    body: str


class ShowBlog(BaseModel):
    title: str
    body: str

    class Config():
        from_attributes = True
