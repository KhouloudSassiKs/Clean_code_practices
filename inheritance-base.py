class BankAccount:
    """
    Base class representing a general bank account.
    Provides common functionality for all account types such as deposits.
    """

    def __init__(self):
        # Initialize account with a zero balance
        self.balance = 0

    def deposit(self, amount):
        """
        Deposit money into the account if the amount is positive.
        """
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}, New balance: {self.balance}")
        else:
            print("Deposit failed. Amount must be positive.")


class CheckingAccount(BankAccount):
    """
    Represents a checking account.
    Inherits from BankAccount and adds withdrawal functionality.
    """

    def __init__(self):
        # Call base class constructor to initialize balance
        super().__init__()

    def withdraw(self, amount):
        """
        Withdraw money from the account if funds are sufficient.
        """
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New balance: {self.balance}")
        else:
            print("Withdrawal failed. Insufficient balance or invalid amount.")


class SavingsAccount(BankAccount):
    """
    Represents a savings account.
    Inherits from BankAccount and adds interest calculation functionality.
    """

    def __init__(self):
        # Initialize base class
        super().__init__()

    def add_interest(self):
        """
        Add 5% interest to the current balance.
        """
        interest = self.balance * 0.05
        self.balance += interest
        print(f"Interest added: {interest}, New balance: {self.balance}")


class LoanAccount(BankAccount):
    """
    Represents a loan account.
    Inherits from BankAccount and includes loan repayment functionality.
    """

    def __init__(self):
        # Initialize base class
        super().__init__()

    def withdraw(self, amount):
        """
        Withdraw from the loan account (simulating taking more loan funds)
        only if balance is sufficient.
        """
        if amount > 0 and self.balance >= amount:
            self.balance -= amount
            print(f"Withdrawn: {amount}, New balance: {self.balance}")
        else:
            print("Withdrawal failed. Insufficient balance or invalid amount.")

    def repay_loan(self, amount):
        """
        Repay part of the loan by adding to the balance.
        """
        if amount > 0:
            self.balance += amount
            print(f"Loan repayment of {amount} made. New balance: {self.balance}")
        else:
            print("Repayment failed. Amount must be positive.")


def main():
    """
    Demonstrates inheritance and polymorphism among account types.
    Each subclass customizes or extends base class behavior.
    """
    # Checking account demo
    checking_account = CheckingAccount()
    checking_account.deposit(100)
    checking_account.withdraw(50)

    # Savings account demo
    savings_account = SavingsAccount()
    savings_account.deposit(200)
    savings_account.add_interest()

    # Loan account demo
    loan_account = LoanAccount()
    loan_account.repay_loan(100)
    loan_account.withdraw(50)


if __name__ == "__main__":
    main()
