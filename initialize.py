from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Users, Country, Post

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# You can add some starter data for your database here.
user = Users(
	fullname = 'Yermi',
	email = 'yermi@gmail.com')

c = Country(name="a")

p = Post(content = "aaaaaa")
p2 = Post(content = "bbbbb")

p.user = user
p.country = c
p2.user = user
p2.country = c

session.add(user)
session.add(c)
session.add(p)
session.add(p2)

session.commit()

print user.posts
