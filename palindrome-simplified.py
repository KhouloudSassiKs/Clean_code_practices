"""
This script checks whether a given word is a palindrome.

Update note:
Simplified the palindrome check by converting each character to uppercase 
inside the loop instead of transforming the entire string before processing.
We want to avoid unnecessary string allocation.
"""

def main():
    word = "radar"
    result = is_palindrome(word)
    print(f"{word} is a palindrome: {result}")


def is_palindrome(word):
    """
    Check if a word is a palindrome (case-insensitive).
    """
    length = len(word)
    for i in range(length // 2):
        if word[i].upper() != word[length - i - 1].upper():
            return False
    return True


if __name__ == "__main__":
    main()
