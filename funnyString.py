import unittest


def funny_string(s):
    # Compute the ASCII difference for original string
    original_diff = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    # Compute the ASCII difference for reversed string
    reversed_diff = original_diff[::-1]
    # Check if they are equal
    return "Funny" if original_diff == reversed_diff else "Not Funny"


class TestFunnyString(unittest.TestCase):
    def test_funny(self):
        self.assertEqual(funny_string("acxz"), "Funny")

    def test_not_funny(self):
        self.assertEqual(funny_string("bcxz"), "Not Funny")

    def test_single_char(self):
        self.assertEqual(funny_string("a"), "Funny")  # Edge case with one character

    def test_palindrome(self):
        self.assertEqual(funny_string("abccba"), "Funny")  # Palindrome case

    def test_all_same(self):
        self.assertEqual(funny_string("aaaa"), "Funny")  # All characters same
