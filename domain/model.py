# coding: utf-8

# model.py


class User:
    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

        self.addresses


class Mail:
    def __init__(self, email: str):
        self.email = email
        self.user_id


class Customer:
    def __init__(self, firstname: str, lastname: str, city_id=None, city=None):
        self.firstname = firstname
        self.lastname = lastname
        self.city_id = city_id
        self.city = city


class City:
    def __init__(self, name: str):
        self.name = name


class Employee:
    def __init__(self, firstname: str, lastname: str, pay=None):
        self.firstname = firstname
        self.lastname = lastname
        self.pay = pay


class Pay:
    def __init__(self, hourly_rate: int, employee_id=None, employee=None):
        self.hourly_rate = hourly_rate
        self.employee_id = employee_id
        self.employee = employee


class Post:
    def __init__(self, title: str, tag=None):
        self.title = title
        self.tag = tag


class Tag:
    def __init__(self, name: str):
        self.name = name
