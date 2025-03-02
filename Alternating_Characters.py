import unittest


def alternating_characters(s):
    # นับจำนวนครั้งที่ต้องลบตัวอักษรซ้ำ
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions


class TestAlternatingCharacters(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(alternating_characters("AABAAB"), 2)

    def test_no_deletions(self):
        self.assertEqual(alternating_characters("ABABABAB"), 0)

    def test_all_same(self):
        self.assertEqual(alternating_characters("AAAA"), 3)

    def test_empty_string(self):
        self.assertEqual(alternating_characters(""), 0)  # กรณีสตริงว่าง

    def test_single_character(self):
        self.assertEqual(alternating_characters("A"), 0)  # กรณีมีตัวอักษรเดียว
