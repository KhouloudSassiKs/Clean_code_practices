class Car:
    # Class attribute
    number_of_wheels = 4  

    def __init__(self, brand):
        # Instance attribute
        self.brand = brand  

    def display(self):
        print(f"Brand: {self.brand}, Wheels: {self.number_of_wheels}")


if __name__ == "__main__":
    car1 = Car("Tesla")
    car2 = Car("Toyota")

    # Initial display
    car1.display()  # Output: Brand: Tesla, Wheels: 4
    car2.display()  # Output: Brand: Toyota, Wheels: 4

    # TODO: Modify attributes so the expected output is produced
    Car.number_of_wheels = 6
    car1.display()  # Expected Output: Brand: Tesla, Wheels: 6
    car2.display()  # Expected Output: Brand: Toyota, Wheels: 6

    # TODO: Modify attributes so the expected output is produced
    Car.number_of_wheels = 2
    car1.brand = "Ford"
    car1.display()  # Expected Output: Brand: Ford, Wheels: 2

    Car.number_of_wheels = 6
    car2.display()  # Expected Output: Brand: Toyota, Wheels: 6
