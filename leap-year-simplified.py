"""
This code determines whether a given year is a leap year.

Update note:
Simplified the leap year logic for better readability.
"""

def main():
    year = 2024
    leap = check_leap(year)
    print(f"{year} is a leap year: {leap}")


def check_leap(year):
    """
    Check whether a given year is a leap year.

    A leap year is:
      - divisible by 400, or
      - divisible by 4 but not by 100
    """
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    return False


if __name__ == "__main__":
    main()
