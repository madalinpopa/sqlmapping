# coding: utf-8

# orm.py

from sqlalchemy import MetaData, Table, Column, String, Integer, ForeignKey
from sqlalchemy.orm import mapper, relationship

from domain.model import User, Mail, Customer, City, Employee, Pay, Tag, Post


metadata = MetaData()


# One to Many - One user can have multiple addresses
#
# A one to many relationship places a foreign key on the child table referencing
# the parent. relationship() is then specified on the parent, as referencing a
# collection of items represented by the child:
user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(50), nullable=False, unique=True),
    Column("password", String(250), nullable=False),
)

mail = Table(
    "mail",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("city", String(50)),
    Column("user_id", Integer, ForeignKey("user.id")),
)


def map_one_to_many():
    mapper(User, user, properties={"mails": relationship(Mail)})
    mapper(Mail, mail)


# Many to One - on city can be assigned to many customers
#
# Many to one places a foreign key in the parent table referencing the child.
# relationship() is declared on the parent, where a new scalar-holding attribute
# will be created:
customer = Table(
    "customer",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("firstname", String(30), nullable=False),
    Column("lastname", String(30), nullable=False),
    Column("city_id", Integer, ForeignKey("city.id")),
)

city = Table(
    "city",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(30), nullable=False),
)


def map_many_to_one():
    mapper(City, city)
    mapper(
        Customer, customer, properties={"city": relationship(City)}
    )


# One to One - one employee is assigned to one pay
#
# One To One is essentially a bidirectional relationship with a scalar attribute
# on both sides. To achieve this, the uselist flag indicates the placement of a
# scalar attribute instead of a collection on the “many” side of the relationship.
# To convert one-to-many into one-to-one:
employee = Table(
    "employee",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("firstname", String(30), nullable=False),
    Column("lastname", String(30), nullable=False),
)

pay = Table(
    "pay",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("hourly_rate", Integer, nullable=False),
    Column("employee_id", Integer, ForeignKey("employee.id")),
)


def map_one_to_one():
    mapper(
        Employee,
        employee,
        properties={"pay": relationship(Pay, uselist=False, back_populates="employee")},
    )
    mapper(
        Pay, pay, properties={"employee": relationship(Employee, back_populates="pay")}
    )


# Many to Many
#
# Many to Many adds an association table between two classes. The association
# table is indicated by the secondary argument to relationship(). Usually, the
# Table uses the MetaData object associated with the declarative base class, so
# that the ForeignKey directives can locate the remote tables with which to link:
post = Table(
    "post",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(100), nullable=False),
)

tag = Table(
    "tag",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(30), nullable=False),
)

post_tag = Table(
    "post_tag",
    metadata,
    Column("post_id", Integer, ForeignKey("post.id")),
    Column("tag_id", Integer, ForeignKey("tag.id")),
)


def map_many_to_many():
    tag_mappers = mapper(Tag, tag)
    mapper(
        Post,
        post,
        properties={
            "tag": relationship(tag_mappers, uselist=False, secondary=post_tag)
        },
    )
