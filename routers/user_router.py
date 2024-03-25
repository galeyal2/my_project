from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from connections.mysql.engine_mysql import get_db
from models import user_model
from models.user_model import User
from repositories.mysql_repository import select_all_records, find_record, delete_record, update, add_and_save_record
from schemas.user_schema import ShowUser, UserSchema, UpdateUser
from utils.hashing import Hash

user_router = APIRouter(
    prefix='/user',
    tags=['users']
)


@user_router.post(path='', response_model=ShowUser)
async def create(request: UserSchema, db: Session = Depends(get_db)):
    new_user = user_model.User(
        user=request.user,
        email=request.email,
        password=Hash.bcrypt(request.password)
    )
    add_and_save_record(db, new_user)
    return new_user


@user_router.get(path='', response_model=List[ShowUser])
async def select_all_users(db: Session = Depends(get_db)):
    return select_all_records(db, User)


@user_router.get(path="/{id}", response_model=ShowUser)
async def select_user(id: int, db: Session = Depends(get_db)):
    return find_record(db=db, id=id, table_model=User).first()


@user_router.delete(path='/{id}')
async def delete_user(id: int, db: Session = Depends(get_db)) -> bool:
    return delete_record(id=id, db=db, table_model=User)


@user_router.put(path='', response_model=ShowUser)
async def update_user(request: UpdateUser, db: Session = Depends(get_db)):
    update(table_model=User, db=db, new_record=request)
