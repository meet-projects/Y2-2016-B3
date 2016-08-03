from sqlalchemy import Column, Date, Float, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()




class Post(Base):
	__tablename__ = 'post'
	id = Column(Integer, primary_key=True)
	country_id = Column(Integer, ForeignKey('country.id'))
	user_id = Column(String, ForeignKey('users.id'))
	content = Column(String)
	user = relationship("Users")
	country = relationship("Country")

class Country(Base):
	__tablename__ = 'country'
	id = Column(Integer, primary_key=True)
	name = Column(String)
	posts = relationship("Post", uselist=True)
	image=Column(String)
	#lat = Column(Float)s
	#long = Column(Float)
		
class Users(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    fullname = Column(String)
    email = Column(String)
    gender = Column(String)
    country = Column(String)
    dob = Column(String)
    password = Column(String)
    posts = relationship("Post", uselist=True)