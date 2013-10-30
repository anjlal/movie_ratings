from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker, scoped_session
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

engine = create_engine("sqlite:///ratings2.db", echo=False)
session = scoped_session(sessionmaker(bind=engine, autocommit = False, autoflush = False))

Base = declarative_base()
Base.query = session.query_property()

### Class declarations go here
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key = True)
    age = Column(Integer)
    gender = Column(String(1))
    occupation = Column(String(100))
    zipcode = Column(String(15))
    email = Column(String(64), nullable = True)
    password = Column(String(64), nullable = True)

    
    # def __init__(self, user_id, age, gender, zipcode, email=None, password=None):
    #     self.id = user_id
    #     self.age = age
    #     self.gender = gender
    #     self.zipcode = zipcode
    #     self.email = email
    #     self.password = password
    
class Movie(Base):
    __tablename__ = "movies"
    
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    released_at = Column(Date())
    imdb_url = Column(String(128))
    
    # def __init__(self, movie_id, name, released_at, imdb_url):
    #     self.id = movie_id
    #     self.name = name
    #     self.released_at = released_at
    #     self.imdb_url = imdb_url

class Rating(Base):
    __tablename__ = "ratings"
    
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    movie_id = Column(Integer, ForeignKey('movies.id'))
    rating = Column(Integer)
    timestamp = Column(Integer)
    
    user = relationship("User", backref=backref("ratings", order_by=id))
    movie = relationship("Movie", backref=backref("ratings", order_by=id))
    
    # def __init__(self, rating_id, user_id, movie_id, rating, timestamp):
    #     self.id = rating_id
    #     self.user_id = user_id
    #     self.movie_id = movie_id
    #     self.rating = rating
    #     self.timestamp = timestamp
    # 

### End class declarations
# Not needed because using scoped_session for multithreadedness
# def connect():
#     # global ENGINE
#     # global Session
#     # 
#     # ENGINE = create_engine("sqlite:///ratings2.db", echo=True)
#     # Session = sessionmaker(bind=ENGINE)
#     
#     # return Session()
def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
