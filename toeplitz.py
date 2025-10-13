def is_toeplitz(matrix: List[List[int]]) -> bool:
    """
    Check if a given matrix is a Toeplitz matrix.
    A Toeplitz matrix has all left to right diagonals containing the same value (per diagonal).
    """

    rows = len(matrix)
    cols = len(matrix[0])

    # Check lower diagonals starting from each row (first column)
    for row in range(rows):
        i, j = row, 0
        element = matrix[i][j]
        while i < rows and j < cols:
            if matrix[i][j] != element:
                return False
            i += 1
            j += 1

    # Check upper diagonals starting from each column (first row)
    for col in range(cols):
        i, j = 0, col
        element = matrix[i][j]
        while i < rows and j < cols:
            if matrix[i][j] != element:
                return False
            i += 1
            j += 1

    return True


# Example usage
if __name__ == "__main__":
    matrix1 = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [9, 5, 1, 2]
    ]
    matrix2 = [
        [1, 2],
        [2, 2]
    ]

    print(is_toeplitz(matrix1))  # True
    print(is_toeplitz(matrix2))  # False
