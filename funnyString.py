import unittest


def funny_string(s):
    # Compute the ASCII difference for original string
    original_diff = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    # Compute the ASCII difference for reversed string
    reversed_diff = original_diff[::-1]
    # Check if they are equal
    return "Funny" if original_diff == reversed_diff else "Not Funny"
