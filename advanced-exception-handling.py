from random import random


# --- Custom Exceptions ---
class AccountException(Exception):
    def __init__(self, exception_msg: str, cause: Exception = None, account_id: str = None):
        """Base class for account-related exceptions."""
        super().__init__(exception_msg)
        self.exception_msg = exception_msg
        self.account_id = account_id
        self.cause = cause


class AccountNotFoundException(AccountException):
    """Raised when an account cannot be found."""
    pass


class InsufficientFundsException(AccountException):
    """Raised when an account does not have sufficient funds."""
    pass


class TransferFailedException(AccountException):
    """Raised when a transfer between accounts fails."""
    pass


# --- Repository simulating account operations ---
class AccountRepository:
    def withdraw(self, account_id: str, amount: float):
        """Simulate withdrawing money from an account."""
        if account_id == "11111":
            raise AccountNotFoundException("Account not found", account_id=account_id)
        if random() < 0.5:
            raise InsufficientFundsException("Insufficient funds", account_id=account_id)

    def deposit(self, account_id: str, amount: float):
        """Simulate depositing money to an account."""
        if account_id == "11111":
            raise AccountNotFoundException("Account not found", account_id=account_id)


# --- Service handling business logic ---
class AccountService:
    def __init__(self):
        self.account_repository = AccountRepository()

    def transfer_funds(self, from_account_id: str, to_account_id: str, amount: float):
        """Transfer funds between two accounts, handling exceptions."""
        try:
            self.account_repository.withdraw(from_account_id, amount)
            self.account_repository.deposit(to_account_id, amount)
        except AccountException as e:
            # Wrap any account-related exceptions in a TransferFailedException
            raise TransferFailedException(f"Transfer failed: {e}", cause=e) from e


# --- Main Program ---
def main():
    account_service = AccountService()

    # Test case 1: Successful transfer (randomized simulation)
    try:
        print("Attempting transfer...")
        account_service.transfer_funds("20000", "30000", 100.00)
        print("Transfer completed successfully.")
    except TransferFailedException as e:
        print(f"Transaction failed: {e}")

    # Test case 2: Account not found
    try:
        print("\nAttempting transfer with non-existent account...")
        account_service.transfer_funds("11111", "67890", 150.00)
    except TransferFailedException as e:
        print(f"Transaction failed: {e}")


if __name__ == "__main__":
    main()
