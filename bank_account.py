class Error(Exception):
    pass


class ValueTooSmallError(Error):
    pass


class BankAccount:
    # Represents starting balance of a new bank account
    balance = 0

    # Name user types will be assigned to bank account object that will be created
    def __init__(self, name):
        self.name = name

    # Returns bank account info if user prints bank account object
    def __repr__(self):
        return "%s's Account. Current Balance: $%.2f" % (self.name, self.balance)

    def show_balance(self):
        print("Current Balance: $%.2f" % (self.balance))
