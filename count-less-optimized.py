def count_less_than(matrix, target):
    """
    This is the optimized version of the existing count_less algo
    This approach runs in O(m + n) time.
    """
    rows = len(matrix) - 1
    cols = len(matrix[0]) - 1
    i = rows         # start from bottom-left corner
    j = 0
    element_count = 0

    while i >= 0 and j <= cols:
        if matrix[i][j] < target:
            # All elements above this (0..i) in the same column are smaller
            element_count += i + 1
            j += 1
        else:
            i -= 1

    return element_count


if __name__ == "__main__":
    # Example 1
    matrix = [
        [1, 3, 5],
        [6, 7, 12],
        [11, 14, 14]
    ]
    target = 10
    print(f"Count of elements less than {target}: {count_less_than(matrix, target)}")
    # Expected output: 5

    # Example 2
    matrix2 = [
        [2, 4, 6, 8],
        [5, 7, 9, 10],
        [11, 13, 15, 17]
    ]
    target2 = 9
    print(f"Count of elements less than {target2}: {count_less_than(matrix2, target2)}")
    # Expected output: 5
