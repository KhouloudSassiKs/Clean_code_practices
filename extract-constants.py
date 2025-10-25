# Constant for Pi
PI = 3.1415926535


def main():
    # Main function to calculate and display circumference and area
    radius = 5.0  # Radius of the circle
    print("Circumference:", calculate_circumference(radius))  # Print circumference
    print("Area:", calculate_area(radius))  # Print area


def calculate_circumference(radius):
    """
    Calculate the circumference of a circle.
    
    Formula: circumference = 2 * PI * radius
    """
    return 2 * PI * radius


def calculate_area(radius):
    """
    Calculate the area of a circle.
    
    Formula: area = PI * radius^2
    """
    return PI * radius * radius


# Entry point of the program
if __name__ == "__main__":
    main()
