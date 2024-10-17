from sqlalchemy import Column, Integer, String  , Float , Date
from db import Base, engine


class User(Base):
    __tablename__ = "my_users"
    id = Column(Integer, primary_key = True)
    username = Column(String, unique=True)
    password = Column(String)
    height = Column(Integer)


class Weight(Base):
    __tablename__ = "weight"
    id = Column(Integer , primary_key=True)
    username = Column(String)
    weight = Column(Float)
    date = Column(Date)
              


Base.metadata.create_all(bind=engine)