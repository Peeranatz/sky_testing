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


class TestGridChallenge(unittest.TestCase):
    def test_grid_challenge(self):
        self.assertEqual(
            grid_challenge(["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]), "YES"
        )
        self.assertEqual(grid_challenge(["abc", "lmn", "xyz"]), "YES")
        self.assertEqual(grid_challenge(["zyx", "wvu", "tsr"]), "NO")
        self.assertEqual(grid_challenge(["a", "z", "m"]), "NO")  # กรณีขนาดเล็กสุด
        self.assertEqual(grid_challenge(["mnop", "abcd", "efgh", "ijkl"]), "NO")
