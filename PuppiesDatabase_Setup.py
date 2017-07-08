import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Shelter(Base):
    __tablename__ = 'shelter'

    id = Column(Integer, primary_key = True)
    name = Column(String(250), nullable=False)
    address = Column(String(300))
    city = Column(String(80))
    state = Column(String(30))
    zipcode = Column(String(10))
    website = Column(String)

class Puppy(Base):
    __tablename__ = 'puppy'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    dateOfBirth = Column(Date)
    gender = Column(String(6), nullable=False)
    weight = Column(Numeric(10))
    shelterId = Column(Integer, ForeignKey('shelter.id'))
    picture = Column(String)
    shelter = relationship(Shelter)


engine = create_engine('sqlite:///puppiesshelter.db')


Base.metadata.create_all(engine)
