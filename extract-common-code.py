from datetime import datetime, timedelta


class Customer:
    """
    Represents a customer with sign-up details, purchase history, and loyalty level.
    """

    def __init__(self, sign_up_date, purchase_history, loyalty_level):
        self.sign_up_date = sign_up_date
        self.purchase_history = purchase_history
        self.loyalty_level = loyalty_level

    def get_sign_up_date(self):
        """Return the date when the customer signed up."""
        return self.sign_up_date

    def get_purchase_history(self):
        """Return a list of the customer's purchase amounts."""
        return self.purchase_history

    def get_loyalty_level(self):
        """Return the customer's loyalty level (integer scale)."""
        return self.loyalty_level


def is_new_customer(customer):
    """
    Determine if the customer is new.
    A customer is considered new if they signed up within the last 90 days.
    """
    return customer.get_sign_up_date() > datetime.now() - timedelta(days=90)


def is_eligible_for_discount(customer):
    """
    Check if the customer is eligible for a discount.
    Must be a new customer with more than 5 purchases.
    """
    return is_new_customer(customer) and len(customer.get_purchase_history()) > 5


def is_eligible_for_loyalty_program(customer):
    """
    Check if the customer qualifies for the loyalty program.
    A customer qualifies if they are new or have a loyalty level greater than 3.
    """
    return is_new_customer(customer) or customer.get_loyalty_level() > 3


def main():
    """Main function to test customer eligibility logic."""
    customer = Customer(
        datetime.now() - timedelta(days=30),  # Customer signed up 30 days ago
        [10, 20, 30, 40, 50, 60],             # Purchase history
        4                                     # Loyalty level
    )
    
    print(f"Eligible for discount: {is_eligible_for_discount(customer)}")
    print(f"Eligible for loyalty program: {is_eligible_for_loyalty_program(customer)}")


if __name__ == "__main__":
    main()
