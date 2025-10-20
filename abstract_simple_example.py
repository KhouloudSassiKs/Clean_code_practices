from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self):
        """Perform a payment action"""
        pass


class CashPayment(Payment):
    def pay(self):
        print("Paying with cash")


class CreditCardPayment(Payment):
    def pay(self):
        print("Paying with credit card")


def main():
    cash_payment = CashPayment()
    credit_card_payment = CreditCardPayment()

    cash_payment.pay()
    credit_card_payment.pay()


if __name__ == "__main__":
    main()
