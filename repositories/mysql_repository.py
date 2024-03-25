# delete
# update
# select all
from typing import Any

from fastapi import HTTPException, status
from pydantic import BaseModel

from sqlalchemy.orm import Session, Query

from connections.mysql.engine_mysql import Base
from utils.my_logger import eyal_logger


def select_all_records(db: Session, table_model: Base):
    eyal_logger.info("getting all users")
    return db.query(table_model).all()


# select one
def delete_record(db: Session, table_model: Base, id: int) -> bool:
    find_record(db, table_model, id).delete()
    db.commit()
    return True


def find_record(db: Session, table_model: Base, id: int) -> Query[Any]:
    found_record = db.query(table_model).filter(table_model.id == id)
    if not found_record.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"not found {id}")
    return found_record


def add_and_save_record(db: Session, new_record: BaseModel) -> None:
    db.add(new_record)
    db.commit()
    db.refresh(new_record)


def update(db: Session, table_model: Base, new_record: BaseModel) -> Query[Any]:
    record = find_record(table_model=table_model, db=db, id=new_record.id)
    record.update(new_record.dict())
    db.commit()
    db.refresh(record)
    return record
