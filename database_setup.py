from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'
    fullname = Column(String)
    email = Column(String, primary_key=True)
    gender = Column(String)
    country = Column(String)
    interest = Column(String)
    dob = Column(Date)
    password = Column(String)
