import pytest
from .user import User
from .test import name, name_invalid_card, limit, valid_card, invalid_card

def test_valid_user(capsys, name, valid_card, limit):
    user = User(name, valid_card, limit, True)
    assert isinstance(user, User)
    assert user.name == name
    assert user.number == valid_card
    assert user.limit == limit
    assert user.balance == 0
    assert user.is_luhn_valid 
    print(user)
    captured = capsys.readouterr()
    assert captured.out == name + ': $0\n' 

def test_invalid_user(capsys, name, invalid_card, limit):
    user = User(name, invalid_card, limit, False)
    assert isinstance(user, User)
    assert user.name == name
    assert user.number == invalid_card
    assert user.limit == limit
    assert user.balance == 0
    assert not user.is_luhn_valid 
    print(user)
    captured = capsys.readouterr()
    assert captured.out == name + ': error\n' 
