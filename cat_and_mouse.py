import unittest


def cat_and_mouse(x, y, z):
    dist_a = abs(x - z)
    dist_b = abs(y - z)
    if dist_a < dist_b:
        return "Cat A"
    elif dist_b < dist_a:
        return "Cat B"
    else:
        return "Mouse C"


class TestCatAndMouse(unittest.TestCase):
    def test_cat_a_wins(self):
        self.assertEqual(cat_and_mouse(1, 5, 2), "Cat A")

    def test_cat_b_wins(self):
        self.assertEqual(cat_and_mouse(2, 5, 4), "Cat B")

    def test_mouse_escapes(self):
        self.assertEqual(cat_and_mouse(1, 3, 2), "Mouse C")

    def test_equal_distance(self):
        self.assertEqual(cat_and_mouse(4, 6, 5), "Mouse C")

    def test_large_values(self):
        self.assertEqual(cat_and_mouse(10, 100, 50), "Cat A")
