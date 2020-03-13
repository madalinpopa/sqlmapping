# coding: utf-8

# tests/test_repository.py

from adapters.repository import FakeUserRepository
from domain.model import User


def test_add_and_get_an_user():
    user = User("username", "password")
    repository = FakeUserRepository()
    repository.add(user)
    saved_user = repository.get("username")
    assert user == saved_user
