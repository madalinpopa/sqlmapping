# coding: utf-8

# adapters/repository.py

import abc
from domain import model
from sqlalchemy.orm import Session
from typing import List



class AbstracRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, model: object):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, id: int) -> object:
        raise NotImplementedError

class UserRepository(abstractmethod):

    def __init__(self, session: Session):
        self._session = session

    def add(self, user: model.User):
        self._session.add(user)

    def get(self, id: int) -> model.User:
        return self._session.query(model.User).get(id)

    def allUser(self) -> List[model.User]:
        return self._session.query(model.User).all()

class FakeUserRepository(AbstracRepository):

    def __init__(self):
        self._session = list()

    def add(self, user: model.User):
        self._session.append(user)

    def get(self, username: str) -> model.User:
        try:
            return next(user for user in self._session if user.username == username)
        except StopIteration:
            return None
