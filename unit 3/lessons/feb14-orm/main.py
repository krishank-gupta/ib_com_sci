from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class user(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key = True)
    username = Column(String(250), unique=True, nullable=False)
    email = Column(String(250), unique=True, nullable=False)
    password = Column(String(300))

# connect to file
engine = create_engine('sqlite:///orm_login_db.db')
# Create tables the first time
Base.metadata.create_all(engine)

# Configuration
Base.metadata.bind = engine
session = sessionmaker(bing=engine)
my_session = session()

# Create user
bob = user(username="bob", email="bob@bob", password="bob")
my_session.add(bob)
my_session.commit()


