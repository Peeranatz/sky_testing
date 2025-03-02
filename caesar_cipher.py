import unittest


def caesar_cipher(s, k):
    result = ""
    k %= 26  # ป้องกันค่า k เกิน 26
    for char in s:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + k) % 26 + shift)
        else:
            result += char
    return result
