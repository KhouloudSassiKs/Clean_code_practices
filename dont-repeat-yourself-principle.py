def calculate_avg(scores):
    """Calculate and return the average of a list of scores."""
    if not scores:
        raise ValueError("Score list cannot be empty.")
    total = sum(scores)
    return total / len(scores)


def main():
    """Main function to calculate and display class averages."""
    class_a_scores = [85.5, 90.0, 78.5, 88.0]
    class_b_scores = [92.0, 81.5, 79.0, 85.5]

    print("Average score for Class A:", calculate_avg(class_a_scores))
    print("Average score for Class B:", calculate_avg(class_b_scores))


if __name__ == "__main__":
    main()
