from sqlalchemy import Integer, Column, String

from connections.mysql.engine_mysql import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    user = Column(String(255))
    email = Column(String(255))
    password = Column(String(255))
