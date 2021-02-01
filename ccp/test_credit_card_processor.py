import pytest, sys, os
from .credit_card_processor import Ccp
from .test import name, name_invalid_card, limit, valid_card, invalid_card

@pytest.fixture
def ccp():
    return Ccp()

def test_ccp_constructor():
    ccp = Ccp()
    assert isinstance(ccp, Ccp)
    assert isinstance(ccp.users, dict)
    assert len(ccp.users) == 0

def test_is_luhn_valid(ccp, valid_card, invalid_card):
    assert ccp.is_luhn_valid(valid_card)
    assert not ccp.is_luhn_valid(invalid_card)

def test_add_users(ccp, name, name_invalid_card, valid_card, invalid_card, limit):
    ccp.add(name, valid_card, limit)
    user = ccp.users[name]
    assert len(ccp.users) == 1

    ccp.add(name_invalid_card, invalid_card, limit)
    user = ccp.users[name_invalid_card]
    assert len(ccp.users) == 2

def test_charge_valid_card(ccp, name, valid_card, limit):
    ccp.add(name, valid_card, limit)
    user = ccp.users[name]
    assert user.balance == 0
    ccp.charge(user, 1000)
    assert user.balance == 1000

def test_charge_invalid_card(ccp, name_invalid_card, invalid_card, limit):
    ccp.add(name_invalid_card, invalid_card, limit)
    user = ccp.users[name_invalid_card]
    assert user.balance == 0
    ccp.charge(user, 1000)
    assert user.balance == 0

def test_credit_valid_card(ccp, name, valid_card, limit):
    ccp.add(name, valid_card, limit)
    user = ccp.users[name]
    assert user.balance == 0
    ccp.credit(user, 1000)
    assert user.balance == -1000

def test_credit_invalid_card(ccp, name_invalid_card, invalid_card, limit):
    ccp.add(name_invalid_card, invalid_card, limit)
    user = ccp.users[name_invalid_card]
    assert user.balance == 0
    ccp.credit(user, 1000)
    assert user.balance == 0

def test_print_valid_user(ccp, name, valid_card, limit, capsys):
    ccp.add(name, valid_card, limit)
    user = ccp.users[name]
    print(user)
    captured = capsys.readouterr()
    assert captured.out == name + ': $0\n' 

    ccp.charge(user, 1000)
    print(user)
    captured = capsys.readouterr()
    assert captured.out == name + ': $1000\n'

    ccp.credit(user, 100)
    print(user)
    captured = capsys.readouterr()
    assert captured.out == name + ': $900\n' 

def test_print_invalid_user(ccp, name_invalid_card, invalid_card, limit, capsys):
    error_value = ': error\n'
    ccp.add(name_invalid_card, invalid_card, 2000)
    user = ccp.users[name_invalid_card]
    print(user)
    captured = capsys.readouterr()
    assert captured.out == name_invalid_card + error_value

    ccp.charge(user, 1000)
    print(user)
    captured = capsys.readouterr()
    assert captured.out == name_invalid_card + error_value

    ccp.credit(user, 100)
    print(user)
    captured = capsys.readouterr()
    assert captured.out == name_invalid_card + error_value

def test_command_add(ccp, name, valid_card):
    ccp.process("Add " + name + " " + valid_card + " $1000")
    assert len(ccp.users) == 1
    
def test_command_charge(ccp, name, valid_card):
    ccp.add(name, valid_card, 1000)
    user = ccp.users[name]
    old_balance = user.balance
    ccp.process("Charge " + name + " $1000")
    assert old_balance != user.balance
    
def test_command_credit(ccp, name, valid_card):
    ccp.add(name, valid_card, 1000)
    user = ccp.users[name]
    old_balance = user.balance
    ccp.process("Credit " + name + " $100")
    assert old_balance != user.balance