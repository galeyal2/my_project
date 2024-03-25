from typing import List

from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from connections.mysql.engine_mysql import get_db
from models.blog_model import Blog
from repositories.mysql_repository import select_all_records, find_record, add_and_save_record, delete_record, update
from schemas.blog_schema import ShowBlog, BlogSchema

blog_router = APIRouter(
    tags=["blog"],
    prefix="/blog"
)


@blog_router.get(path='', response_model=List[ShowBlog])
async def select_all(db: Session = Depends(get_db)):
    return select_all_records(table_model=Blog, db=db)


@blog_router.get(path='', response_model=ShowBlog)
async def select_one_record(id: int, db: Session = Depends(get_db)):
    return find_record(table_model=Blog, id=id, db=db).first()


@blog_router.post(path='', response_model=ShowBlog)
async def create_new_blog(request: BlogSchema, db: Session = Depends(get_db)):
    new_record = Blog(title=request.title, body=request.body)
    add_and_save_record(db, new_record)
    return new_record


@blog_router.put(path='', response_model=ShowBlog)
async def update_record(request: BlogSchema, db: Session = Depends(get_db)):
    update(table_model=Blog, new_record=request, db=db)
    return request


@blog_router.get(path="/{id}")
async def delete_one_record(id: int, db: Session = Depends(get_db)):
    return delete_record(id=id, db=db, table_model=Blog)
