def solution(grid):
    # Checks if the grid is empty
    if not grid:
        return [None, None]
    
    cols = len(grid[0]) - 1
    rows = len(grid) - 1
    i = 0
    j = cols

    # Initialize minimum and maximum with the first element in the anti-diagonal
    minimum = maximum = grid[i][j]

    # Traverse the anti-diagonal (top-right to bottom-left)
    while j >= 0 and i <= rows:
        if grid[i][j] <= minimum:
            minimum = grid[i][j]
        elif grid[i][j] >= maximum:
            maximum = grid[i][j]
        i += 1
        j -= 1

    return [minimum, maximum]


if __name__ == "__main__":
    grid1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Grid 1:", solution(grid1))  # Expected: [3, 7]

    grid2 = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]
    ]
    print("Grid 2:", solution(grid2))  # Expected: [40, 32]
