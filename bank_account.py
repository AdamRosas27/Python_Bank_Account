# Base class for other exceptions
class Error(Exception):
    pass

# ValueTooSmall exception raised when deposit value is too small


class ValueTooSmallError(Error):
    pass

# ValueTooLargeError exception raised when withdraw value too large


class ValueTooLargeError(Error):
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
            else:
                print("Amount To Deposit: $%.2f" % (amount))
                self.balance += amount
                self.show_balance()
        except:
            print("Cannot Deposit Amount Less Than Or Equal To Zero.")

    # Withdraw method lets user withdraw an amount from bank account
    def withdraw(self, amount):
        try:
            if amount > self.balance:
                raise ValueTooLargeError
            else:
                print("Amount To Withdraw: $%.2f" % (amount))
                self.balance -= amount
                self.show_balance()
        except:
            print("Cannot Withdraw Amount Greater Than The Current Balance.")

    # Method that takes in an amount and returns the value allocated for each expense
    def savings(self):
        monthly_income = int(
            input("50/30/20 Budget Calculator. Enter Monthly Income As Whole: "))
        if monthly_income <= 0:
            return "Monthly Income Cannot Be Less Than Or Equal To Zero."
        else:
            necessities = monthly_income * (.5)
            wants = monthly_income * (.3)
            savings = monthly_income * (.2)
            print("Monthly Necessity Allowance: $%.2f, Monthly Wants Allowance: $%.2f, Monthly Savings Allowance: $%.2f" % (
                (necessities, wants, savings)))


"""Tester Code"""
my_account = BankAccount("Adam")
my_account.deposit(100)
my_account.savings()
