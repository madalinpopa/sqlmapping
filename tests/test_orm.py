# coding: utf-8

from domain.model import User, Mail



def test_can_insert_new_line_user_table(session):
    session.execute(
        'INSERT INTO user (username, password) VALUES'
        '("User1", "Pass1")'
    )

    expected = [User("User1", "Pass1")]
    
    assert session.query(User).all() == expected