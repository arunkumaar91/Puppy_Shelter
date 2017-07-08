"""Script to perform queries using SQLAlchemy"""
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker

from PuppiesDatabase_Setup import Base, Shelter, Puppy
import datetime
from datetime import date

engine = create_engine('sqlite:///puppiesshelter.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

print("\n")
print("*** Uda County District of Animal Shelters Reports ***" "\n")

# 1. Query all of the puppies and return the results in ascending alphabetical order

def pup_names():
    print("*** 1. All the Puppies name in ascending alphabetical order ***" "\n")
    allPupp = session.query(Puppy.name)
    result_1 = allPupp.order_by(Puppy.name.asc())
    for item in result_1:
        print item.name
    print("\n")

# 2. Query all of the puppies that are less than 6 months old organized by the youngest first

def pup_sixmonths():
    print("*** 2. Puppies which are less than 6 months old sorted by the youngest first ***" "\n")
    date_today = date.today()
    sixMonthsAgo = date_today - datetime.timedelta(days = 183)
    sixOldPupp = session.query(Puppy.name, Puppy.dateOfBirth).filter(Puppy.dateOfBirth > sixMonthsAgo)
    result_2 = sixOldPupp.order_by(Puppy.dateOfBirth.desc())
    for item in result_2:
        print item.name, "--->", item.dateOfBirth
    print("\n")


# 3. Query all puppies by ascending weight

def pup_weights():
    print("*** 3. Puppies based on the weight sorted in the ascending order ***" "\n")
    pup_weight = session.query(Puppy.name,Puppy.weight)
    result_3 = pup_weight.order_by(Puppy.weight.asc())
    for item in result_3:
        print item.name, "--->", item.weight
    print("\n")


# 4. Query all puppies grouped by the shelter in which they are staying

def pup_shelterGroups():
    print("*** 4. Puppies grouped by the shelter in which they are staying ***" "\n")
    for thispup_shelter in session.query(Shelter).\
                                   join(Puppy).\
                                   filter(Shelter.id == Puppy.id).\
                                   group_by(Shelter.id):
        print("\n" + str(thispup_shelter.name)) + ":"
    for thispup_puppy in session.query(Puppy).\
                                 filter(Puppy.shelterId == thispup_shelter.id).\
                                 order_by(Puppy.name):
        print thispup_puppy.name
    print("\n")

pup_names()
pup_sixmonths()
pup_weights()
pup_shelterGroups()
