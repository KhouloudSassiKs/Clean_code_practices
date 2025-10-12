class Order:
    """
    Order class representing a product purchase.
    Uses the Builder design pattern to simplify object creation
    when multiple optional parameters are involved.
    """

    def __init__(self, builder):
        """
        Constructor takes a Builder instance to initialize all fields.
        """
        self.product_name = builder.product_name
        self.price = builder.price
        self.quantity = builder.quantity
        self.delivery_address = builder.delivery_address
        self.note = builder.note

    def __str__(self):
        """
        Provides a readable string representation of the order.
        """
        return (
            f"Order[product_name={self.product_name}, "
            f"price={self.price}, quantity={self.quantity}, "
            f"delivery_address={self.delivery_address}, note={self.note}]"
        )

    class Builder:
        """
        Inner Builder class to incrementally construct an Order object.
        Allows method chaining for setting optional parameters.
        """

        def __init__(self, product_name, price):
            # Required parameters
            self.product_name = product_name
            self.price = price

            # Optional parameters with default values
            self.quantity = 0
            self.delivery_address = None
            self.note = None

        def set_quantity(self, quantity):
            """
            Set the quantity for the order.
            """
            self.quantity = quantity
            return self

        def set_delivery_address(self, delivery_address):
            """
            Set the delivery address for the order.
            """
            self.delivery_address = delivery_address
            return self

        def set_note(self, note):
            """
            Add an optional note to the order.
            """
            self.note = note
            return self

        def build(self):
            """
            Finalize and create an Order object using current Builder state.
            """
            return Order(self)


def main():
    """
    Demonstrates how to use the Builder to create an Order instance.
    Only required fields are provided initially, while optional ones
    are added using method chaining.
    """
    order = (
        Order.Builder("Laptop", 999.99)
        .set_quantity(2)
        .set_delivery_address("123 Main St, Anytown")
        .build()
    )
    print(order)


if __name__ == "__main__":
    main()
