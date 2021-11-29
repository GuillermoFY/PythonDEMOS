from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Here, we create the db and the session to work with the tables
engine = create_engine('sqlite:///school.sqlite')
#And now, we start the session
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
