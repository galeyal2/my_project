from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from utils.my_logger import eyal_logger

username = 'user'
password = 'password'
host = 'localhost'
port = '3306'
database_name = 'db'
connection_string = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database_name}'
engine = create_engine(connection_string)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

eyal_logger.info("sdfsdf")
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
