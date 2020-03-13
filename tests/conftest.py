# coding: utf-8

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, clear_mappers


from adapters.orm import (
    metadata,
    map_one_to_many,
    map_many_to_one,
    map_many_to_many,
    map_one_to_one,
)


@pytest.fixture
def in_memory_db():
    engine = create_engine("sqlite:///:memory:")
    metadata.create_all(engine)
    return engine


@pytest.fixture
def session(in_memory_db):
    map_one_to_many()
    map_many_to_one()
    map_many_to_many()
    map_one_to_one()
    yield sessionmaker(bind=in_memory_db)()
    clear_mappers()
