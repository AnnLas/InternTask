import unittest
from unittest import TestCase

from main import calculate


class TestCalculator(TestCase):

    def test_calculate1(self):
        usb_size = 1
        memes = [
            ('rollsafe.jpg', 205, 6),
            ('sad_pepe_compilation.gif', 410, 10),
            ('yodeling_kid.avi', 605, 12)
        ]

        self.assertEqual((22, {'sad_pepe_compilation.gif', 'yodeling_kid.avi'}), calculate(usb_size, memes))

    def test_calculate2(self):
        usb_size = 165 / 1024.
        memes = [
            ('a', 23, 92),
            ('b', 31, 57),
            ('c', 29, 49),
            ('d', 44, 68),
            ('e', 53, 60),
            ('f', 38, 43),
            ('g', 63, 67),
            ('h', 85, 84),
            ('i', 89, 87),
            ('j', 82, 72)

        ]

        self.assertEqual((309, {'a', 'b', 'c', 'd', 'f'}), calculate(usb_size, memes))

    def test_calculate_one_meme(self):
        usb_size = 165 / 1024.
        memes = [
            ('a', 23, 92)

        ]

        self.assertEqual((92, {'a'}), calculate(usb_size, memes))

    def test_calculate_two_meme(self):
        usb_size = 165 / 1024.
        memes = [
            ('a', 33, 92),
            ('b', 33, 92)

        ]

        self.assertEqual((184, {'a', 'b'}), calculate(usb_size, memes))

    def test_calculate_two_same_meme(self):
        usb_size = 165 / 1024.
        memes = [
            ('a', 23, 92),
            ('a', 23, 92)

        ]

        self.assertEqual((92, {'a'}), calculate(usb_size, memes))


if __name__ == '__main__':
    unittest.main()
