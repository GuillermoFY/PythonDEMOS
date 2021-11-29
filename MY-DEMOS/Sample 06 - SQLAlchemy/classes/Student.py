from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from . import dataToBD

class Student(dataToBD.Base):
    #Now, we put the table name for introducing the data to the bd
    __tablename__ = "students"
    
    id = Column(Integer,primary_key=True)
    name =  Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __init__(self,name,year):
        self.name = name
        self.year = year
