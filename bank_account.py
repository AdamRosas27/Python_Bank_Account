# Base class for other exceptions
class Error(Exception):
    pass

# ValueTooSmall exception raised when input value is too small


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

    # Prints out the current balance of bank account
    def show_balance(self):
        print("Current Balance: $%.2f" % (self.balance))

    # Takes in an amount to deposit and displays it for the user. If amount is less than or equal to 0, ValueTooSmallError exception will be raised.
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueTooSmallError
                return
            else:
                print("Amount To Deposit: $%.2f" % (amount))
                self.balance += amount
                self.show_balance()
        except:
            print("Cannot Deposit Value Less Than Or Equal To Zero.")
