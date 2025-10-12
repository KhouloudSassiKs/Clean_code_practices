class BankAccount:
    def __init__(self, initial_balance):
        """
        Initialize the bank account with a positive balance.
        Raises ValueError if initial balance is not positive.
        """
        if initial_balance > 0:
            # Private attribute: name-mangled to prevent direct external access
            self.__balance = initial_balance
        else:
            raise ValueError("Initial balance must be positive")

    @property
    def balance(self):
        """
        Property to provide read-only access to the private balance.
        Allows external code to get the balance as 'account.balance' 
        without using a traditional getter method.
        """
        return self.__balance
    
    def deposit(self, amount):
        """
        Deposit a positive amount into the account.
        Raises ValueError if the amount is not positive.
        """
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Deposited amount must be positive")
    
    def withdraw(self, amount):
        """
        Withdraw an amount from the account if sufficient funds exist.
        Raises ValueError if the amount is negative or exceeds current balance.
        """
        if amount > 0 and self.balance >= amount:
            self.__balance -= amount
        else:
            raise ValueError("Insufficient funds")


def main():
    # Create a BankAccount object with an initial balance
    account = BankAccount(500.00)
    print("Initial Balance:", account.balance)

    # Deposit funds and show updated balance
    account.deposit(150.00)
    print("After Deposit:", account.balance)

    # Withdraw funds and show updated balance
    account.withdraw(100.00)
    print("After Withdrawal:", account.balance)


if __name__ == "__main__":
    main()
