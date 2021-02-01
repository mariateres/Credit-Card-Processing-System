class User: 
    def __init__(self, name, number, limit, is_luhn_valid):
        self.name = name
        self.number = number
        self.limit = limit
        self.balance = 0
        self.is_luhn_valid = is_luhn_valid
        
    def __repr__(self):
        return self.name + ": " + ("$" + str(self.balance) if self.is_luhn_valid else "error")
        
    def __str__(self):
        return self.__repr__()
