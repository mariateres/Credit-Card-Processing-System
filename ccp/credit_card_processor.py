import sys
from .user import User


class Ccp:
    def __init__(self):
        self.users = {}

    #   src https://stackoverflow.com/a/21079551/2514799
    def is_luhn_valid(self, card_number):
        def digits_of(n):
            return [int(d) for d in str(n)]
        digits = digits_of(card_number)
        odd_digits = digits[-1::-2]
        even_digits = digits[-2::-2]
        checksum = 0
        checksum += sum(odd_digits)
        for d in even_digits:
            checksum += sum(digits_of(d*2))
        return checksum % 10 == 0

    def add(self, name, cc_number, limit):
        is_luhn_valid = self.is_luhn_valid(cc_number)
        user = User(name, cc_number, limit, is_luhn_valid)
        self.users[name] = user

    def charge(self, user, amount):
        new_balance = user.balance + amount
        if user.is_luhn_valid and new_balance <= user.limit:
            user.balance = new_balance

    def credit(self, user, amount):
        if user.is_luhn_valid:
            user.balance = user.balance - amount

    def print(self):
        sorted_users = sorted(self.users)
        for user in sorted_users:
            print(self.users[user])

    def process(self, command):
        words = command.split()
        if words[0] == 'Add':
            self.add(words[1], int(words[2]), int(words[3].replace('$', '')))
        elif words[0] == 'Charge':
            self.charge(self.users[words[1]], int(words[2].replace('$', '')))
        elif words[0] == 'Credit':
            self.credit(self.users[words[1]], int(words[2].replace('$', '')))
