from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from database_setup import Base, Users, Country, Post

engine = create_engine('sqlite:///project.db')
Base.metadata.create_all(engine)
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# You can add some starter data for your database here.
"""
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

<<<<<<< HEAD
print(user.posts)
=======
print user.posts
"""

Italy = Country(name="Italy", image="http://rickzullo.com/wp-content/uploads/2013/09/Italiagiochi.jpg", lon=41.8719, lat=12.5674)
Mexico=Country(name="Mexico", image="http://culturewhiz.org/sites/default/files/images/articles/Mexico.png", lon=23.6345, lat=102.5528)
Palestine=Country(name="Palestine", image="https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/UN_Partition_Plan_For_Palestine_1947.svg/2000px-UN_Partition_Plan_For_Palestine_1947.svg.png", lon=31.9522, lat=35.2332)
Israel = Country(name="Israel", image="http://www.asianinfo.org/asianinfo/israel/is-map.gif", lon=31.0461, lat=34.8516)
session.add(Italy)
session.add(Mexico)
session.add(Israel)
session.add(Palestine)
session.commit()

