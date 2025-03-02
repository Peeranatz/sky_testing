import unittest


# Two Characters
def two_characters(s):
    unique_chars = set(s)
    max_length = 0
    for c1 in unique_chars:
        for c2 in unique_chars:
            if c1 != c2:
                filtered = [c for c in s if c in (c1, c2)]
                if all(
                    filtered[i] != filtered[i + 1] for i in range(len(filtered) - 1)
                ):
                    max_length = max(max_length, len(filtered))
    return max_length


class TestTwoCharacters(unittest.TestCase):
    def test_two_characters(self):
        self.assertEqual(two_characters("beabeefeab"), 5)
        self.assertEqual(two_characters("aaaa"), 0)
        self.assertEqual(two_characters("abcabc"), 4)
        self.assertEqual(two_characters("ababab"), 6)
        self.assertEqual(two_characters("a"), 0)  # กรณีสั้นสุด
        self.assertEqual(two_characters("abababa"), 7)  # กรณีที่ผลลัพธ์เป็น s เอง
        self.assertEqual(two_characters("aabbcc"), 0)  # ไม่มีตัวอักษร 2 ตัวที่สลับกัน
        self.assertEqual(two_characters("xyxyxy"), 6)  # ผลลัพธ์ควรเป็นทั้งสตริง
        self.assertEqual(two_characters("acacacbcbcbc"), 0)  # มีหลายชุดที่เป็นไปได้
