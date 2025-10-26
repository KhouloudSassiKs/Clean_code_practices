"""
This code impliments a simple delivery system using OOP principles.

Update note:
Refactored the code to prevent `DeliveryService` from directly accessing
`Customer` and `Order` attributes. Instead, interaction now occurs
through defined methods, promoting encapsulation.
"""

class Customer:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name
    
    def process_received_order(self, order):
        """Handle the receipt of an order."""
        print(f"{self._name} received order: {order.received_total_order()}")


class Order:
    def __init__(self, item, quantity):
        self._item = item
        self._quantity = quantity

    def received_total_order(self):
        """Return a string describing the total order."""
        return f"{self._item} * {self._quantity}"


class DeliveryService:
    def process_order(self, order, customer):
        """Process delivery without directly accessing customer or order data."""
        customer.process_received_order(order)


def main():
    customer = Customer("Alice")
    order = Order("Pizza", 2)
    delivery_service = DeliveryService()
    delivery_service.process_order(order, customer)


if __name__ == "__main__":
    main()
