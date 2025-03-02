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
