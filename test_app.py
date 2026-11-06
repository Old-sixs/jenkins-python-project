import unittest

from app import add_numbers, subtract_numbers, multiply_numbers


class TestApp(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(5, 3), 8)

    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(5, 3), 2)

    def test_multiply_numbers(self):
        self.assertEqual(multiply_numbers(5, 3), 15)


if __name__ == "__main__":
    unittest.main()