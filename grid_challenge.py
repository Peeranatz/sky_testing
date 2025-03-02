import unittest


# Grid Challenge
def grid_challenge(grid):
    sorted_grid = [sorted(row) for row in grid]
    return (
        "YES"
        if all(
            all(
                sorted_grid[i][j] <= sorted_grid[i + 1][j]
                for i in range(len(sorted_grid) - 1)
            )
            for j in range(len(grid[0]))
        )
        else "NO"
    )
