def count_less_than(matrix, target):
    """
    Count how many elements in a sorted matrix are less than the target value.
    The matrix is sorted both row and column in a way that moving right or down increases the numbers
    This is the intuitive version
    """
    count = 0
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] < target:
                count += 1
            else:
                # Since the row is sorted, no need to check further in this row
                break
    return count

if __name__ == "__main__":
    # Example 1
    matrix = [
        [1, 3, 5],
        [6, 7, 12],
        [11, 14, 14]
    ]
    target = 10
    print(f"Count of elements less than {target}: {count_less_than(matrix, target)}")
    # Expected: 5

    # Example 2
    matrix2 = [
        [2, 4, 6, 8],
        [5, 7, 9, 10],
        [11, 13, 15, 17]
    ]
    target2 = 9
    print(f"Count of elements less than {target2}: {count_less_than(matrix2, target2)}")
    # Expected: 5
