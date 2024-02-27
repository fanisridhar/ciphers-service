from django.test import TestCase
from .ciphers import caesar_encode

class CiphersTest(TestCase):
    def test_caesar_encoding_1(self):
        plain_text = "hello"
        shift = 1
        expected = "ifmmp"
        output = caesar_encode(plain_text, shift)
        self.assertEqual(output, expected)

    def test_caesar_encoding_2(self):
        plain_text = "winter"
        shift = 3
        excepted = "zlqwhu"
        output = caesar_encode(plain_text, shift)
        self.assertEqual(output, excepted) 