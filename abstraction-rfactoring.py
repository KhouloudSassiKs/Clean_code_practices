from abc import ABC, abstractmethod

# Abstract base class defining a common printer interface
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        """Print the given document."""
        pass


# Concrete implementation of an Inkjet printer
class InkjetPrinter(Printer):
    def print(self, document):
        print("Inkjet Printer: Printing " + document)


# Concrete implementation of a Laser printer
class LaserPrinter(Printer):
    def print(self, document):
        print("Laser Printer: Printing " + document)


# Manager class that uses any Printer without knowing its type
class PrintManager:
    def print(self, printer, document):
        """Delegate printing to the given printer."""
        printer.print(document)


def main():
    print_manager = PrintManager()
    inkjet_printer = InkjetPrinter()
    laser_printer = LaserPrinter()

    # Demonstrate polymorphic printing
    print_manager.print(inkjet_printer, "Hello World via Inkjet!")
    print_manager.print(laser_printer, "Hello SOLID Principles via Laser!")


if __name__ == "__main__":
    main()
