from sqlalchemy import Column, Integer, String

from connections.mysql.engine_mysql import Base


class Blog(Base):
    __tablename__ = 'blogs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    body = Column(String(1000))

