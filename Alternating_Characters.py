import unittest


def alternating_characters(s):
    # นับจำนวนครั้งที่ต้องลบตัวอักษรซ้ำ
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions
