from abc import ABC, abstractmethod


class PaymentType(ABC):
    """Abstract base class for all payment types."""

    @abstractmethod
    def process(self) -> None:
        """Process the payment."""
        pass


class Cash(PaymentType):
    """Concrete class for cash payments."""

    def process(self) -> None:
        print("Processing cash payment")


class CreditCard(PaymentType):
    """Concrete class for credit card payments."""

    def process(self) -> None:
        print("Processing credit card payment")


class StoreTransaction:
    """Handles store transactions using different payment types."""

    def perform_transaction(self, payment_type: PaymentType) -> None:
        """Perform a transaction with the given payment type."""
        payment_type.process()


def main() -> None:
    """Demonstrate transactions with different payment types."""
    cash_payment = Cash()
    card_payment = CreditCard()

    transaction = StoreTransaction()
    transaction.perform_transaction(cash_payment)
    transaction.perform_transaction(card_payment)


if __name__ == "__main__":
    main()
