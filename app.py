# coding: utf-8

# model.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from adapters.orm import (
    metadata,
    map_one_to_many,
    map_many_to_one,
    map_one_to_one,
    map_many_to_many,
)
from domain.model import User, Mail, City, Customer, Employee, Pay, Tag, Post

# mapping classes
map_one_to_many()
map_many_to_one()
map_one_to_one()
map_many_to_many()

# create the engine
engine = create_engine("sqlite:///database.db", echo=True)

# create all the database
metadata.create_all(bind=engine)

# create the session
Session = sessionmaker(bind=engine)

# initiate the session
session = Session()
